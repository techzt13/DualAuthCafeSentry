# Hardware design workspace

Status: DRAFT implementation workspace. Native starter projects and provisional board outlines exist; Pod logical MCU/sensor interface contract drafted 2026-11-12. Nothing is ready to fabricate.

- `sentry-pod/`: KiCad project and provisional 49 x 24 mm carrier-board outline.
- `pocket-keyfob/`: KiCad project and provisional 27 x 20 mm carrier-board outline.

The outlines are initial packaging placeholders. They are not final board sizes.
The `.kicad_sch` sheets are still empty starter sheets. The `.kicad_pcb` files contain outline-only boards. No footprints, copper routing, schematic nets, power circuits or component placements have been released. Do not order these boards.

The Pod logical interface contract is in `sentry-pod/interface-contract.md`. It maps verified S3-Zero P15 contacts to logical nets and records the I2C, PN532, IMU, button, tether, audio-control and battery-monitor boundaries. It intentionally does not invent the physical connector order or footprint for the unresolved modules.

Open each `.kicad_pro` in KiCad. The next step is to translate the interface contract into a native schematic using a custom S3 module interface symbol and explicitly provisional module connectors, then reconcile physical footprints against manufacturer drawings.
