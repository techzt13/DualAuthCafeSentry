# Last Worked On - Dual-Auth Cafe Sentry

Date: 2026-11-12 (component-evidence task completed; recovery handoff)
Package revision: 0.2
Project stage: G0 design basis complete; G1 component-evidence documentation
complete; G1 exit gate (physical component freeze) OPEN and BLOCKED
Next stage: G1 supplier-controlled selection and evidence closure, not G2/G3

**PCB/schematic creation: not started. CAD enclosure creation: not started.
Firmware and manufacturing exports: not started. Nothing purchased or ordered.
Hardware safety, physical fit and manufacturing readiness: not approved.**

Before the next task, read [PROJECT_SPEC.md](PROJECT_SPEC.md),
[AGENTS.md](AGENTS.md), this file and the relevant `docs/` files. Some session
instructions refer to a parent-level `../AGENTS.md`; that file does not exist,
so the repository [AGENTS.md](AGENTS.md) governs. Neither governing file was
changed by any task recorded here.

## 1. Current status

The requested component-evidence documentation task is **complete**. The
**physical component freeze is BLOCKED** (decision D-21). No project assembly
is marked FROZEN, no reference part was substituted into the specification,
and every unverified identity, dimension, pinout or rating remains TBD or on
HOLD. Each row's `freeze_blocker` column states the missing evidence.

| Item | Current value |
| --- | --- |
| [docs/component-register.csv](docs/component-register.csv) | 111 rows, 30 columns, 111 unique `part_id` values |
| [docs/dimension-register.csv](docs/dimension-register.csv) | 111 rows, 24 columns; the same 111 IDs in the same order |
| Classification | 54 Pod, 43 Keyfob, 14 reference-only |
| Original IDs | All 75 IDs from G0 commit `13863c9` retained with unchanged unit and function; 36 IDs added |
| `freeze_status` | HOLD_CIRCUIT 44, HOLD_IDENTITY 40, REFERENCE_NOT_SELECTED 14, NOT_DESIGNED 8, HOLD_SELECTION 4, HOLD_REVISION_ENVELOPE 1, FROZEN 0 |
| `dimension_status` | TBD 87; numeric drawing-scoped rows 14; TARGET_ONLY 3, UNVERIFIED_FITTED_PART 2, TBD_SELECTION 2, UNVERIFIED_NO_MECHANICAL_DRAWING 2, UNVERIFIED_SOURCE_BLOCKED 1 |
| Controlled IDs | SRC-01..29, D-01..21, R-01..33 (all open), T-01..24 |

The 14 numeric rows are partial and drawing-scoped (board outline, IC body,
bare cell or reference part), never complete installed envelopes:
P-MCU, K-MCU-C3, K-MCU-S3 (board drawings); P-IMU-IC, P-NFC-IC (IC packages);
REF-EEMB-LP502030, REF-EEMB-LP401730 (bare cells); REF-P2N2222A,
REF-MCP73831-SOT23, REF-MCP73831-DFN, REF-TP4056-ESOP8, REF-TP4056-EMSOP8,
REF-VYBRONICS-VCLP1020B002L and REF-SHOUHAN-MSK12C02 (reference parts).
Only the first five belong to project rows, and none of them is a complete
assembly envelope.

## 2. Repository and Git state

Repository: `techzt13/DualAuthCafeSentry` on GitHub (public), branch `master`.

| Commit | Date | Content |
| --- | --- | --- |
| `13863c9` | 2026-11-11 | G0 eight-document design basis, revision 0.1, 75-ID register; fixed baseline for validation |
| `13eb171` | 2026-11-12 | Revision 0.2 deliverables (111-row registers, datasheet index, verified pinouts and related revisions); committed by the repository owner during recovery and preserved unchanged |
| Commit containing this file | 2026-11-12 | Completion handoff, recovery records and whitespace-only readability corrections |

Empty local directories (`cad/`, `hardware/`, `firmware/`, `manufacturing/`,
`scripts/`, `docs/datasheets/`, `docs/reports/`) contain no files and are not
tracked by Git. Nothing was placed in them.

## 3. Files created or modified by the component-evidence task

| File | Actual completed work |
| --- | --- |
| [docs/component-register.csv](docs/component-register.csv) | Extended to 111 entries and 30 columns; retained all 75 original IDs and original 16 fields; added evidence, parentage, pinout, drawing, mounting, keepout and freeze controls |
| [docs/datasheet-index.md](docs/datasheet-index.md) | SRC-01..29 evidence ledger, document revisions/access limits, 14 inspected PDF fingerprints, freeze conflicts, recovery diagnosis (section 7) |
| [docs/dimension-register.csv](docs/dimension-register.csv) | 111 matching entries and 24 columns; nominal/maximum values only within a stated drawing scope; everything else TBD |
| [docs/verified-pinouts.md](docs/verified-pinouts.md) | Package-specific S3/C3, PN532, MPU-6050 and charger maps; manufacturer facts separated from project proposals and unknown connector maps |
| [docs/pinout.md](docs/pinout.md) | Corrected C3 V2 USB contacts; preserved all application allocations |
| [docs/architecture.md](docs/architecture.md) | Navigation/evidence controls; system behavior and G0 sources retained |
| [docs/mechanical-requirements.md](docs/mechanical-requirements.md) | Drawing versus published-claim evidence, battery/tab envelopes, reference-motor packing limits |
| [docs/power-architecture.md](docs/power-architecture.md) | LP401730/charger voltage-tolerance conflict, TP4056 source discrepancy, actuator/switch qualification holds |
| [docs/design-decisions.md](docs/design-decisions.md) | D-21 evidence/freeze controls; 2026-11-12 completion note |
| [docs/engineering-risks.md](docs/engineering-risks.md) | Directly affected risks updated; none closed by documentation alone |
| [docs/development-roadmap.md](docs/development-roadmap.md) | Completed G1 evidence work distinguished from the still-open G1 exit gate; all 24 acceptance tests retained |
| [LAST-WORKED-ON.md](LAST-WORKED-ON.md) | This handoff |

Changes made in the final 2026-11-12 session (after `13eb171`):

- [LAST-WORKED-ON.md](LAST-WORKED-ON.md): rewritten as this complete handoff.
- [docs/datasheet-index.md](docs/datasheet-index.md): completion-review line,
  resume wording clarified, new section 7 (failure and validator diagnosis).
- [docs/design-decisions.md](docs/design-decisions.md): completion-review note
  after the revision table. No decision content or status changed.
- [docs/component-register.csv](docs/component-register.csv),
  [docs/dimension-register.csv](docs/dimension-register.csv) and
  [docs/engineering-risks.md](docs/engineering-risks.md): whitespace-only
  readability fix (section 5.3). No value changed.

## 4. Why the earlier run reported "Main pass failed"

The saved execution record shows the last `refine_registers.py` run succeeded:
exit code **0**, output **"Applied inspected PN532/DFN package bounds and
clarified register scopes; 111 IDs preserved."** Both CSVs contain those
refinements, so the script was not rerun.

The subsequent failure was a **connection timeout requesting a response from
Copilot's AI model**, reported as `ETIMEDOUT` after **five retries** with
23 seconds of total retry waiting (session event log, 2026-11-11T13:10:05Z).
That is the recorded immediate cause; it was not a Python exception, missing
source file or CSV validation failure. The log does not establish whether the
fault was in local Wi-Fi, another network segment or the upstream service,
and it does not account for how the reported overall run time was spent.
The validation script had been saved but not yet run when the timeout
occurred. Earlier manufacturer retrieval failures (section 9.5) are separate
evidence-access holds.

## 5. Validation performed and actual results

### 5.1 Validator history

| Run | Validator state | Result |
| --- | --- | --- |
| First run (recovery) | As first written | FAIL: 2 of 7565 checks (roadmap "Duplicate/missing IDs" and "Wrong ID set") |
| Second run | Roadmap pattern fixed, baseline pinned, GPIO matching strengthened | PASS: 7590 checks |
| With `--sources --handoff` | Same | PASS: 7779 checks |
| Final run, after readability fix and this handoff | Same | PASS: 8005 checks, exit 0 (count rises with the longer handoff's extra lines and links) |

Validator corrections and their justification:

1. **Genuine checker bug, roadmap IDs.** The pattern required a table cell
   containing only `T-01`; the valid roadmap cells read `T-01 GPIO / startup`.
   The pattern became `^\| T-(\d+)\b[^|]*\|`. It still requires the unique,
   complete T-01..24 set. The roadmap was not changed.
2. **Latent checker defect, moving baseline.** Original-ID and scope checks
   compared against `HEAD`. After `13eb171`, `HEAD` contains 111 rows, so the
   75-row baseline check would fail for reasons unrelated to data quality.
   This was established by counting rows at `HEAD`; the unpinned checker was
   not rerun in that state. The baseline is now pinned to
   `13863c939cae64e06590eb81724b75ade7a83eb5`.
3. **Strengthening, not loosening.** S3/C3 GPIO checks changed from substring
   to word-boundary matching, so `GPIO1` can no longer be satisfied by
   `GPIO13`.

No check was deleted or relaxed to obtain a pass. The validator is
session-local, not part of the repository:

```sh
S=/Users/zacktudor/.copilot/session-state/2c446fbc-cda8-45b4-9d42-75911398d217/files
$S/component-freeze-review/pdf-tools/bin/python \
  $S/validate-component-registers.py --sources --handoff
```

It uses the Python standard library for CSV/document checks. `--sources` adds
the session-local PDF reader (pypdf 7.0.1), and `--handoff` checks this file.
It will not exist on another machine or in another session. No repository
tooling or dependency was added.

### 5.2 Documentation checks covered by the validator

| Check | Result |
| --- | --- |
| Actual deliverable contents | PASS: all four files inspected; valid refinements preserved, not inferred from file existence |
| CSV parsing/schema | PASS: 111 unique rows each; component 30 columns, dimension 24; no empty or ragged fields |
| Baseline preservation | PASS: all 75 original IDs, units and functions retained versus `13863c9`; original 16 component fields retained |
| Classification/parentage | PASS: 54 Pod, 43 Keyfob, 14 reference-only; no cross-unit parents or cycles; C3/S3 alternatives exclusive; no reference promoted to selected hardware |
| Cross-register equality | PASS: shared identity/source/status/drawing fields identical in both CSVs |
| Dimensions/evidence | PASS at document level: exactly the 14 expected numeric rows; all other numeric fields TBD; scope and protrusion caveats retained |
| Sources | PASS: every CSV source ID/URL exists in the SRC-01..29 ledger |
| Cached PDFs | PASS: 14 primary PDFs pass signature, parsing, page-count and SHA-256 comparison with the ledger |
| Pinouts | PASS at document level: S3/C3 contact maps, C3 USB pair in both `pinout.md` and the CSV, original Pod GPIO4-9 roles, PN532 40-pin and MPU-6050 24-pin coverage, I2C address notation |
| Links/structure | PASS: 276 local Markdown/CSV links and anchors resolve; tables, code fences, ASCII, final newlines, no CR or trailing whitespace |
| Controlled IDs | PASS: SRC-01..29, D-01..21, R-01..33, T-01..24 complete and unique |
| Arithmetic | PASS: 12/22 mV charger-limit exceedances; 33.6/28.1 mm motor/board screens; 15.3 mm Pod stack; cavity volumes and cell derating recomputed |
| Git scope | PASS: changes since `13863c9` limited to the 12 allowed files; specification/instructions unchanged; `git diff --check` clean |

### 5.3 Additional checks in the final session

- **Independent GPIO cross-check (ad hoc, separate from the validator): PASS.**
  Pod GPIO1 and GPIO4-13 match S3 contacts by the rule contact 3..15 =
  GPIO13..GPIO1. Keyfob C3 GPIO0/1/3/4 match contacts 4/5/7/8. The S3 Keyfob
  alternative GPIO1/13/6/7 matches P15-15/3/10/9. No application net uses a
  strap, native-USB, RGB or UART0 pin.
- **Power consistency spot check: PASS (consistency only).** Register rows and
  [power-architecture.md](docs/power-architecture.md) agree on LP401730
  4.200 +/- 0.020 V (4.220 V limit), MCP73831-2 4.232 V maximum (+12 mV),
  TP4056 4.242 V maximum (+22 mV) and the TP4056 page 4 versus page 17
  tolerance conflict.
- **CSV round-trip: PASS.** Both CSVs round-trip byte-identically through
  Python `csv` with `QUOTE_ALL` and LF line endings, before and after the fix.
- **Whitespace-only readability fix: applied and verified.** 48 CSV cells had
  words fused to numbers, for example `charge4.200` became `charge 4.200`,
  `page213` became `page 213`, and `catalog403` became `catalog 403`. In
  [engineering-risks.md](docs/engineering-risks.md), `max32` became `max 32`.
  With all whitespace removed, each file is identical to `13eb171`. No value,
  unit, ID, URL, source or status changed. Dimension symbols such as `D/E1`
  and labels such as `switch1 ON/switch2 OFF` were deliberately left unchanged.
  `last_reviewed` stays `2026-11-11` because the evidence was not re-reviewed.
  The fix script is `files/normalize_fused_text.py` in session storage.
- `git diff --check`: clean. `git status` and the full diff were reviewed.

### 5.4 Design verification not performed

No ERC, DRC, CAD fit, assembly trial, battery, charging, protection, RF,
NFC read-range, acoustic, haptic, thermal or runtime test has been performed
or is claimed. All PASS results above are documentation-consistency checks
against recorded sources, not hardware qualification.

## 6. Research PDFs: local cache versus GitHub

**In the repository and on GitHub: 0 PDFs.** `git ls-files '*.pdf'` is empty.
They were deliberately not committed: the repository is public, manufacturer
datasheets are copyrighted, and the package policy
([architecture.md](docs/architecture.md) section 9) is to link to, not
republish, manufacturer documents.

**Local only, on this Mac in this Copilot session's storage (not backed up or
synchronized):**
`/Users/zacktudor/.copilot/session-state/2c446fbc-cda8-45b4-9d42-75911398d217/files/component-freeze-review/`

There are 14 cached primary PDFs. Their page counts and SHA-256 hashes are in
[docs/datasheet-index.md](docs/datasheet-index.md) section 5, "Inspected PDF
fingerprints".

| Cached file | Source |
| --- | --- |
| `s3-schematic.pdf` | SRC-02 Waveshare ESP32-S3-Zero schematic |
| `c3-v2-schematic.pdf` | SRC-05 Waveshare ESP32-C3-Zero V2 schematic |
| `pn532-ic.pdf` | SRC-09 NXP PN532 (222 pages) |
| `mpu6050-manufacturer-mirror.pdf` | SRC-11 TDK InvenSense MPU-6050, manufacturer-authored mirror |
| `mcp73831.pdf` | SRC-13 Microchip MCP73831/2 |
| `tp4056.pdf` | SRC-14 TP4056 |
| `eemb-lp502030.pdf` | SRC-16 EEMB LP502030 |
| `elechouse-v3.pdf` | SRC-21 Elechouse PN532 V3 |
| `p2n2222a.pdf` | SRC-22 onsemi P2N2222A |
| `joyit-mpu6050-datasheet.pdf` | SRC-25 Joy-IT SEN-MPU6050 datasheet |
| `joyit-mpu6050-manual.pdf` | SRC-25 Joy-IT SEN-MPU6050 manual |
| `eemb-lp401730.pdf` | SRC-26 EEMB LP401730 |
| `vybronics-vclp1020b002l.pdf` | SRC-27 Vybronics VCLP1020B002L |
| `shouhan-msk12c02-mirror.pdf` | SRC-28 SHOUHAN MSK12C02, manufacturer-authored mirror |

There are 8 derived single-page or drawing extracts, not separately
fingerprinted: `mcp73831-page-20`, `mcp73831-page-23`, `pn532-ic-page-213`,
`tp4056-page-13`, `tp4056-page-14`, `shouhan-msk12c02-mirror-page-10`,
`eemb-lp502030-drawing` and `vybronics-vclp1020b002l-drawing`, all `.pdf`.

The same directory also holds text extractions, PNG renders, `s3-drawing.jpg`,
`c3-drawing.jpg`, the `pdf-tools/` environment, `build_registers.py` and
`refine_registers.py`. **Do not rerun either register script.** The generator
would overwrite the refined registers, and the refinement has already been
applied.

If the cache is unavailable, re-download from the ledger URLs and compare
SHA-256 hashes. A different hash means a different document revision, which
must be re-inspected before use. The G0 handoff recorded that its own temporary
downloads were removed; this cache was created later, by the
component-evidence task.

## 7. Pinout corrections and current allocations

**Correction (SRC-05):** on the ESP32-C3-Zero V2, **pad 15 = GPIO18 / USB D-**
and **pad 16 = GPIO19 / USB D+**. Revision 0.1 had the pair reversed. This is
corrected in [pinout.md](docs/pinout.md) and
[verified-pinouts.md](docs/verified-pinouts.md#c3-zero), and recorded in R-12.
Application allocations were unaffected.

Board contact maps ([verified-pinouts.md](docs/verified-pinouts.md#s3-zero)):

- **S3-Zero P15:** 1 = GPIO43 UART0 TX through board R6 (499 ohm); 2 = GPIO44
  RX; 3..15 = GPIO13..GPIO1; 16 = 3V3 (onboard LDO); 17 = GND; 18 = VBUS /
  external 5 V pad. Reserved: GPIO0/3/45/46 straps, GPIO19/20 USB,
  GPIO21 RGB.
- **C3-Zero V2:** 1 = 5 V / VBUS; 2 = GND; 3 = 3V3; 4..14 = GPIO0..GPIO10;
  15 = GPIO18 D-; 16 = GPIO19 D+; 17 = GPIO20 RX; 18 = GPIO21 TX. Reserved:
  GPIO2/8/9 straps, GPIO10 RGB (LED on the 5 V net), GPIO18/19 USB.

| Unit / board | Baseline (specification) | Proposed (not approved) |
| --- | --- | --- |
| Pod, S3-Zero | GPIO4 SDA, GPIO5 SCL, GPIO6 piezo PWM, GPIO7 button, GPIO8/9 tether drive/sense | GPIO1 battery ADC, GPIO10 NFC IRQ, GPIO11 NFC RSTPD_N, GPIO12 IMU INT, GPIO13 charge status |
| Keyfob, C3-Zero option | None fixed by the specification | GPIO0 battery ADC, GPIO1 charge status, GPIO3 motor PWM, GPIO4 button (contacts 4/5/7/8) |
| Keyfob, S3-Zero alternative | None fixed by the specification | GPIO1 battery ADC, GPIO13 charge status, GPIO6 motor PWM, GPIO7 button (P15-15/3/10/9) |

I2C (Pod): PN532 7-bit **0x24** (0x48 write byte, 0x49 read byte);
MPU-6050 **0x68** with AD0 low or 0x69 with AD0 high (bytes 0xD0/0xD1 or
0xD2/0xD3). There is no address conflict. Module straps, pull-ups and supply
levels are TBD until the actual modules are identified. These allocations are
document-level only; they are not a wiring release.

## 8. Engineering decisions already made

Full text: [docs/design-decisions.md](docs/design-decisions.md).

| Decision | Status |
| --- | --- |
| D-01 Documentation before PCB/CAD | APPLIED-DOC |
| D-02 Keyfob processor selection | OPEN; C3 evaluation PROPOSED |
| D-03 Battery regulation and Zero-board USB isolation | OPEN, safety-critical |
| D-04 Charger, temperature supervision and load sharing | OPEN |
| D-05 Finished battery assemblies | OPEN |
| D-06 Shared I2C and additional GPIO | GPIO4/5 BASELINE; supporting connections PROPOSED |
| D-07 Piezo driver and acoustic specification | OPEN; GPIO6 and 1 kohm base resistor BASELINE |
| D-08 Optional USB-C-form tether | OPEN |
| D-09 Paired encrypted ESP-NOW and freshness | PROPOSED |
| D-10 NFC compatibility and security claim | OPEN; five stored 4-/7-byte credentials BASELINE |
| D-11 Button recovery, learning and reset | OPEN; authorization-gated parser PROPOSED |
| D-12 Alarm origin, priority and fault states | OPEN; `arm_origin` PROPOSED |
| D-13 Target dimensions are not a fit commitment | OPEN; 45 x 30 x 16 and 35 x 25 x 12 remain BASELINE targets |
| D-14 Serviceable parametric enclosure construction | PROPOSED |
| D-15 NFC duty cycle versus radio sleep and alert latency | OPEN |
| D-16 Onboard RGB source inconsistency | OPEN |
| D-17 GY-521/MPU-6050 identity and lifecycle | OPEN |
| D-18 Quantified acceptance criteria | OPEN |
| D-19 Power-switch accessibility and armed-state retention | OPEN |
| D-20 Component identity and release provenance | PROPOSED verification rule |
| D-21 Evidence register is not a physical freeze | APPLIED-DOC for evidence controls; hardware selections OPEN |

Rules applied throughout this task:

- EEMB LP502030/LP401730, Elechouse PN532 V3, Joy-IT SEN-MPU6050, onsemi
  P2N2222A, Microchip MCP73831, TP4056, Vybronics VCLP1020B002L,
  SHOUHAN MSK12C02 and TDK PS1240P02BT are reference-only comparisons, not
  selections or substitutions.
- No enclosure target, clearance, capacity or performance requirement was
  changed.
- Datasheet PDFs are linked and fingerprinted, not committed (section 6).
- Validation compares against fixed baseline `13863c9`, not a moving `HEAD`.

## 9. Unresolved questions (HOLD/TBD)

### 9.1 Component identity

- **P-NFC, P-NFC-IC, P-NFC-ANT:** exact PN532 module maker, MPN, revision,
  schematic, mechanical drawing, antenna and ROM suffix (PN5321A3HN/C1xx),
  plus voltage interface and RF evidence. Elechouse V3 is reference only.
- **P-IMU, P-IMU-IC:** GY-521 maker, MPN, revision, drawing, regulator and
  pull-ups; received MPU-6050 marking, genuine sourcing and TDK lifecycle
  status (direct TDK access returned HTTP 403).
- **P-PIEZO and P-AUDIO-Q/RB/BIAS:** no transducer is qualified for the
  105 dB target. The TDK PS1240P02BT lead is blocked (HTTP 403; distributor
  mirrors failed). Driver topology and ratings are TBD.
- **K-MOTOR and K-MOTOR-Q/DIODE/SUPPLY/CONTROL/RSERIES/RBIAS/MOUNT:** motor not
  selected; start, stall and continuous-alert duty are unqualified.
- **P-BUTTON, K-BUTTON, P-SWITCH, K-SWITCH:** exact parts TBD. The MSK-12C02
  supplier variant and a canonical SHOUHAN drawing are missing.
- **Connectors:** P/K-USB-CHARGE, P/K-BAT-PLUG, P/K-BAT-RECEPTACLE and
  P/K-USB-SERVICE are TBD.
- **K-MCU-C3 versus K-MCU-S3:** Keyfob board choice is OPEN (D-02).
- **P-MCU and fitted board parts:** received revision and full envelope
  (HOLD_REVISION_ENVELOPE); fitted RGB, LDO and ceramic-antenna MPNs.

### 9.2 Dimensions

- 87 rows have no numeric dimensions. The 14 numeric rows exclude installed
  envelopes (connectors, leads, tabs, adhesive, swelling, moving parts).
- Zero boards: 23.5 x 18 mm PCB outline only. Assembled height, USB-C
  protrusion and component heights on the received revision are TBD.
- Numeric antenna keepouts (2.4 GHz ceramic antennas, NFC antenna) are TBD.
- Finished pack envelopes including PCM, tabs, leads and swelling are TBD.

### 9.3 Power

- Protected packs (P-BATTERY, K-BATTERY), PCM and temperature sensing (P-NTC,
  K-NTC) are unselected. An NTC cannot be assumed to be inside a pack.
- Charger module, IC suffix and programming resistor are unselected. LP401730
  allows at most 4.220 V; the cited MCP73831-2 maximum (4.232 V) and TP4056
  maximum (4.242 V) exceed it by 12 mV and 22 mV. TP4056 states +/-1% on
  page 4 and +/-1.5% on page 17. Manufacturer clarification is required
  before any battery/charger pairing is approved.
- Power path and source isolation (D-03/D-04): neither Zero board has
  charging or protection, and VBUS shares a net with the external 5 V pad.
  Combined USB, charger and battery operation is unresolved.
- Peak loads (motor start/stall, piezo drive, radio bursts) and runtime
  budgets are unmeasured.

### 9.4 Mechanical

- **Pod (45 x 30 x 16 target):** the Elechouse V3 published size of
  42.7 x 40.4 mm is wider than the 30 mm target. Under the 1.5 mm wall
  screen, a 5.3 mm maximum cell plus the required 10 mm NFC gap needs
  15.3 mm, but only 13 mm of interior height is available.
- **Keyfob (35 x 25 x 12 target):** LP401730 L1 maximum 32 mm uses the full
  32 mm cavity length. Board plus reference motor side by side needs 33.6 mm
  (more than 32) or 28.1 mm (more than 22). The full Z stack is unknown.
- Neither target is proven feasible or infeasible. Any change needs an owner
  decision under D-13 once real parts are known.
- Antenna clearance, button/USB access, tether form and service removal
  depend on the selections above.

### 9.5 Research access blockers

- TDK MPU-6050 direct PDF/page: HTTP 403; the manufacturer-authored mirror
  was used and is identified as a mirror.
- TDK PS1240P02BT product/catalog: HTTP 403; Mouser mirrors failed at
  transport level.
- SHOUHAN MSK12C02: only a manufacturer-authored mirror was inspected.
- Supplier drawings for the actual PN532, GY-521, charger modules and
  finished packs are missing because the parts are unselected, not because
  of a network failure.

## 10. Exact next step

Start a **supplier-controlled assembly selection and evidence-closure review**
for G1, driven by each register row's `freeze_blocker`. In order:

1. Obtain exact order code, revision, schematic and mechanical drawing for
   P-NFC/P-NFC-ANT and P-IMU from the intended supplier.
2. Select finished protected packs and charger modules as pairs
   (P-BATTERY/P-CHARGER, K-BATTERY/K-CHARGER), including PCM, NTC and
   connectors. Obtain written resolution of the charge-voltage tolerance
   conflict before approving any pairing.
3. Decide D-02 (Keyfob C3 versus S3) and select piezo, motor, switches and
   connectors through the existing decision gates.
4. Update only the affected register rows when evidence is obtained; keep
   reference status and TBDs otherwise. Rerun the validator.
5. Re-screen maximum installed envelopes against the unchanged targets and
   NFC clearances. Record any required target change as a proposal for owner
   decision.

Do not rerun the register generator or repeat successful research. Do not
start KiCad, FreeCAD, firmware or manufacturing work, and do not purchase
anything, without independent electrical/physical review and explicit human
authorization.

## 11. History

- **2026-11-11, G0 (commit `13863c9`, revision 0.1):** eight-document design
  basis with SRC-01..22, D-01..20, R-01..33 and T-01..24, plus the original
  75-row register. Superseded in detail by revision 0.2. The original handoff
  is in Git history: `git show 13863c9:LAST-WORKED-ON.md`.
- **2026-11-11, component-evidence task:** registers extended to 111 rows;
  SRC-23..29 and D-21 added. A Wi-Fi interruption was resumed without
  restarting work, and TDK 403 and mirror failures were recorded.
- **2026-11-11:** "Main pass failed" (model `ETIMEDOUT`) after
  `refine_registers.py` had already succeeded.
- **2026-11-12:** `13eb171` recorded the deliverables. Final validation, the
  validator corrections, the whitespace-only readability fix and this handoff
  completed the documentation task. The physical freeze remains BLOCKED.
