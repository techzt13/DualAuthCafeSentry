# Dual-Auth Cafe Sentry

**Hackathon build project — Sentry Pod + Pocket Keyfob**

The project is an access-control demonstrator with two hardware units:

- **Sentry Pod:** NFC credential reader, motion/tamper sensing, alarm output and local controls.
- **Pocket Keyfob:** user-held companion with a button and haptic feedback.

The intended deliverables are editable KiCad electronics projects, editable FreeCAD enclosure models, firmware, build documentation and a repeatable test plan. This repository is an engineering prototype workspace, not a released consumer product.

## Current design workspace

- [Sentry Pod KiCad project](hardware/sentry-pod/sentry-pod.kicad_pro)
- [Pod BQ25185 power-stage evaluation schematic](hardware/sentry-pod/pod-power-stage.kicad_sch)
- [Pod PAM8904E audio-stage evaluation schematic](hardware/sentry-pod/pod-audio-stage.kicad_sch)
- [Pocket Keyfob KiCad project](hardware/pocket-keyfob/pocket-keyfob.kicad_pro)
- [FreeCAD enclosure macro](cad/create_enclosures.FCMacro)
- [Mechanical model instructions](cad/README.md)
- [Hardware workspace guide](hardware/README.md)
- [Latest handoff / last work completed](LAST-WORKED-ON.md)

## Current status

Both devices have native KiCad schematic and PCB placement drafts. The Keyfob has a provisional C3-Zero module interface, motor low-side switch, flyback diode, local bypass capacitors, button interface and service UART nets. The Pod has its controller/NFC/IMU interface and wired NFC reset stage, plus separate standalone charger and audio evaluation schematics.

Both PCBs remain **unrouted**. The Pod power/audio sheets are not yet integrated as hierarchical sheets or placed on its PCB. Battery/charger pairings, processor-board USB power isolation, sounder drive waveform, and several physical component interfaces remain HOLD. The FreeCAD macro has not yet been run, so no generated FCStd/STEP/STL or fit validation is claimed.

## First local checks

From the repository root, run the dependency-free source sanity checker:

    python3 scripts/check_design_sources.py

This checks S-expression structure, PCB pad/net references, selected critical net assignments and duplicate identifiers. It is not a substitute for KiCad's native checks.

Open each KiCad project in KiCad and run:
1. Schematic ERC.
2. Update PCB from schematic and resolve discrepancies.
3. PCB DRC.
4. Inspect 3D view and footprint/connector clearances.

For CAD, follow cad/README.md, run the macro in FreeCAD, inspect the generated editable documents, and verify all component envelopes, USB access, antenna clearances, retention and assembly tolerances.

## Engineering status rules

- **DRAFT** means editable engineering work exists but may contain unresolved assumptions.
- **HOLD** means do not connect or energise that interface until its dependencies are reviewed.
- **VALIDATED** may only be used after the relevant tool/test has actually passed and its evidence is recorded.
- Never treat a paper datasheet screen as proof of acoustic, RF, thermal, battery, haptic or physical performance.
- Do not order boards or parts or initiate fabrication without explicit project-owner approval.

Read PROJECT_SPEC.md, AGENTS.md and LAST-WORKED-ON.md before continuing engineering work.
