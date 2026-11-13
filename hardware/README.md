# Hardware design workspace

Status: **implementation in progress**. Both KiCad project skeletons and provisional PCB outlines exist. The Sentry Pod now has its first populated logical schematic draft; the Pocket Keyfob schematic remains a starter sheet. Neither PCB is ready to fabricate.

## Sentry Pod

Files:
- `sentry-pod.kicad_pro`
- `sentry-pod.kicad_sch`
- `sentry-pod.kicad_pcb`
- `sentry-pod.kicad_sym`
- `sym-lib-table`
- `interface-contract.md`

The schematic contains:
- Waveshare ESP32-S3-Zero SKU 25081 P15 contact map.
- Provisional ELECHOUSE PN5321 MINI I2C host interface, with no IRQ connection; polling is used.
- Provisional Adafruit MPU-6050 breakout product 3886 six-pin header interface.
- Active-low failsafe button.
- Provisional MMBT3904 reset inversion stage, 10 kΩ / 100 kΩ / 10 kΩ resistors.
- Optional 4.7 kΩ I2C pull-ups marked DNP.
- Named I2C, sensor, control and reserved power-hold nets.

The controller and module physical footprints remain unset. Exact cable conductor order for the PN5321 MINI is not inferred. The S3 carrier-pad footprint needs final alignment to the exact board drawing and received revision. Battery/charger, power path, tether protection and piezo/audio circuits remain separate unfinished blocks.

## Pocket Keyfob

Files:
- `pocket-keyfob.kicad_pro`
- `pocket-keyfob.kicad_sch`
- `pocket-keyfob.kicad_pcb`
- `interface-contract.md`

The C3-Zero is the evaluation controller option, with S3-Zero alternative; the owner has not frozen this choice. Its schematic and board remain starter-level; motor, power and physical connectors are not yet captured.

## PCB and validation status

- Pod carrier board: provisional 49 x 24 mm outline only; no footprints, board placement, tracks, zones or routed copper yet.
- Keyfob carrier board: provisional 27 x 20 mm outline only.
- No Gerbers or drill files generated.
- The schematic's S-expression structure was checked for balanced parentheses, unique UUIDs and matching embedded symbol IDs. KiCad CLI/Eeschema is unavailable in this execution environment; no KiCad load/parse, ERC or DRC is claimed.
- Neither PCB is ready for ordering or fabrication.


 
## Current native design files (2026-11-13)

### Pod
- sentry-pod/sentry-pod.kicad_sch — main Pod interface and NFC reset schematic.
- sentry-pod/pod-power-stage.kicad_sch — standalone BQ25185 non-energised evaluation block.
- sentry-pod/pod-audio-stage.kicad_sch — standalone PAM8904E 1x-mode evaluation block.
- sentry-pod/power-stage-review.md and sentry-pod/audio-stage-review.md — design basis and open checks.

### Pocket Keyfob
- pocket-keyfob/pocket-keyfob.kicad_sch — C3-Zero interface, button and provisional motor switch.
- pocket-keyfob/pocket-keyfob.kicad_pcb — 37 x 25 mm upright-module placement/net-assignment draft with antenna relief notch; unrouted.
- pocket-keyfob/footprints.pretty/C3Zero_Castellated_2x9.kicad_mod — provisional upright custom 2x9 C3-Zero land pattern.
- pocket-keyfob/footprints.pretty/MotorWirePads_2x.kicad_mod — motor solder-wire pads.
- pocket-keyfob/fp-lib-table — local footprint library registration.
- pocket-keyfob/interface-contract.md and pocket-keyfob/pcb-layout-review.md — interface and layout notes.

All custom footprints and schematic blocks remain draft until opened and checked in the local KiCad version. No fabrication files are released.
