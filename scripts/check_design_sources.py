#!/usr/bin/env python3
"""Dependency-free source sanity checks for the Dual-Auth Cafe Sentry KiCad drafts.

This is deliberately not a replacement for KiCad's parser, ERC, DRC, 3D viewer,
or a physical fit/electrical test. It checks S-expression structure, PCB net
references, duplicate UUID/reference identifiers, and a few project-critical
pad/net contracts so obvious text-edit regressions are caught early.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

TOKEN = re.compile(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+')


class ParseError(ValueError):
    pass


def parse_sexpr(path: Path):
    text = path.read_text(encoding="utf-8")
    tokens = TOKEN.findall(text)
    pos = 0

    def parse_one():
        nonlocal pos
        if pos >= len(tokens):
            raise ParseError("unexpected end of file")
        token = tokens[pos]
        pos += 1
        if token != "(":
            if token == ")":
                raise ParseError("unexpected closing parenthesis")
            return json.loads(token) if token.startswith('"') else token
        result = []
        while True:
            if pos >= len(tokens):
                raise ParseError("unclosed list")
            if tokens[pos] == ")":
                pos += 1
                return result
            result.append(parse_one())

    root = parse_one()
    if pos != len(tokens):
        raise ParseError("trailing tokens after root expression")
    if not isinstance(root, list):
        raise ParseError("root is not a list")
    return root


def walk(node):
    if isinstance(node, list):
        yield node
        for child in node:
            yield from walk(child)


def child(node, name):
    for item in node:
        if isinstance(item, list) and item and item[0] == name:
            return item
    return None


def children(node, name):
    return [item for item in node if isinstance(item, list) and item and item[0] == name]


def property_value(node, key):
    for item in children(node, "property"):
        if len(item) >= 3 and item[1] == key:
            return item[2]
    return None


def fail(message):
    raise RuntimeError(message)


def check_file_structure(files):
    for path in files:
        root = parse_sexpr(path)
        uuids = [n[1] for n in walk(root) if n and n[0] == "uuid" and len(n) > 1]
        duplicates = sorted({u for u in uuids if uuids.count(u) > 1})
        if duplicates:
            fail(f"{path}: duplicate UUID(s): {', '.join(duplicates)}")
        print(f"PASS structure: {path}")


def check_pcb(path):
    root = parse_sexpr(path)
    nets = {}
    for item in children(root, "net"):
        if len(item) >= 3:
            net_id, name = int(item[1]), item[2]
            if net_id in nets:
                fail(f"{path}: duplicate net id {net_id}")
            nets[net_id] = name

    refs = {}
    pad_count = 0
    assigned_count = 0
    footprints = children(root, "footprint")
    for fp in footprints:
        ref = property_value(fp, "Reference")
        if ref:
            if ref in refs:
                fail(f"{path}: duplicate footprint reference {ref}")
            refs[ref] = fp
        for pad in children(fp, "pad"):
            pad_count += 1
            net = child(pad, "net")
            if not net:
                continue
            net_id = int(net[1])
            net_name = net[2]
            if net_id not in nets:
                fail(f"{path}: pad {ref or '?'}:{pad[1]} uses undefined net id {net_id}")
            if nets[net_id] != net_name:
                fail(f"{path}: pad {ref or '?'}:{pad[1]} net name/id mismatch")
            if net_id != 0:
                assigned_count += 1
    print(f"PASS PCB nets: {path} — {len(nets)-1} named nets, {assigned_count}/{pad_count} assigned pads, {len(footprints)} footprints")
    return refs


def pad_net(fp, pad_number):
    for pad in children(fp, "pad"):
        if len(pad) > 1 and pad[1] == str(pad_number):
            net = child(pad, "net")
            return net[2] if net else ""
    return None


def check_project_contracts(repo):
    key_sch = parse_sexpr(repo / "hardware/pocket-keyfob/pocket-keyfob.kicad_sch")
    labels = {n[1] for n in walk(key_sch) if n and n[0] in ("label", "global_label", "hierarchical_label") and len(n) > 1}
    for label in ("K_UART_RX", "K_UART_TX", "K_MOTOR_PWM", "K_MOTOR_GATE", "K_MOTOR_SW"):
        if label not in labels:
            fail(f"Keyfob schematic is missing label {label}")

    key_refs = check_pcb(repo / "hardware/pocket-keyfob/pocket-keyfob.kicad_pcb")
    expected = {
        ("U1", "17"): "K_UART_RX",
        ("U1", "18"): "K_UART_TX",
        ("J1", "1"): "K_3V3_MOTOR_HOLD",
        ("J1", "2"): "K_MOTOR_SW",
        ("Q1", "1"): "K_MOTOR_GATE",
        ("Q1", "2"): "K_GND",
        ("Q1", "3"): "K_MOTOR_SW",
        ("D1", "1"): "K_3V3_MOTOR_HOLD",
        ("D1", "2"): "K_MOTOR_SW",
    }
    for (ref, pad), expected_net in expected.items():
        if ref not in key_refs:
            fail(f"Keyfob PCB is missing footprint {ref}")
        actual = pad_net(key_refs[ref], pad)
        if actual != expected_net:
            fail(f"Keyfob PCB {ref}.{pad}: expected {expected_net}, got {actual}")

    pod_refs = check_pcb(repo / "hardware/sentry-pod/sentry-pod.kicad_pcb")
    pod_expected = {
        ("Q1", "1"): "P_NFC_RESET_BASE",
        ("Q1", "2"): "GND",
        ("Q1", "3"): "P_NFC_RESET_N",
        ("R1", "1"): "P_NFC_RESET_CTL",
        ("R1", "2"): "P_NFC_RESET_BASE",
        ("R2", "1"): "GND",
        ("R2", "2"): "P_NFC_RESET_BASE",
        ("R3", "1"): "P_3V3_PERIPH_HOLD",
        ("R3", "2"): "P_NFC_RESET_N",
    }
    for (ref, pad), expected_net in pod_expected.items():
        if ref not in pod_refs:
            fail(f"Pod PCB is missing footprint {ref}")
        actual = pad_net(pod_refs[ref], pad)
        if actual != expected_net:
            fail(f"Pod PCB {ref}.{pad}: expected {expected_net}, got {actual}")
    print("PASS project contracts: Keyfob UART/motor stage and Pod NFC reset pad mappings")


def main():
    repo = Path(__file__).resolve().parents[1]
    files = sorted((repo / "hardware").rglob("*.kicad_sch"))
    files += sorted((repo / "hardware").rglob("*.kicad_pcb"))
    files += sorted((repo / "hardware").rglob("*.kicad_mod"))
    if not files:
        fail("no KiCad source files found")
    check_file_structure(files)
    check_project_contracts(repo)
    print("\nSource checks passed. This does NOT mean KiCad ERC/DRC or fabrication checks passed.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
