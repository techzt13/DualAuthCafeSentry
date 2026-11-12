# Hackathon Build Plan — Dual-Auth Cafe Sentry

Date: 2026-11-12
Status: IMPLEMENTATION IN PROGRESS — native starter files exist; first Pod electrical interface contract drafted

## Objective

Deliver an actually buildable two-unit hardware project for the hackathon:
Sentry Pod plus Pocket Keyfob, including native KiCad schematics/PCBs,
native FreeCAD parametric enclosures/assembly, firmware, manufacturing
exports, BOM and complete assembly/test instructions.

This is a self-built hackathon prototype. Manufacturer correspondence and
commercial certification are not project gates. Datasheets and engineering
checks remain necessary for safe, credible design decisions.

## Design approach

Use a prototype-first, interface-driven workflow. Keep uncertain circuits
provisional and isolated while continuing with board outlines, connector
placement, component envelopes and mechanical packaging. Do not freeze an
unverified circuit merely to keep moving.

## Deliverables

| Deliverable | Native source | Required output |
| --- | --- | --- |
| Sentry Pod electronics | KiCad project in hardware/sentry-pod/ | Schematic, PCB, BOM, Gerbers, drill files, assembly notes |
| Keyfob electronics | KiCad project in hardware/pocket-keyfob/ | Schematic, PCB, BOM, Gerbers, drill files, assembly notes |
| Sentry Pod enclosure | FreeCAD model in cad/sentry-pod/ | Parametric base/lid, STEP, STL, dimensioned drawing |
| Keyfob enclosure | FreeCAD model in cad/pocket-keyfob/ | Parametric enclosure, STEP, STL, dimensioned drawing |
| Integrated assembly | FreeCAD assembly | PCB, battery, connectors, sensors, actuators and fasteners positioned |
| Firmware | firmware/ | Buildable Pod and Keyfob firmware, configuration and flashing guide |
| Build package | manufacturing/ and docs/ | BOM, fabrication notes, assembly, inspection and test procedures |

## Initial mechanical envelope

- Pod: begin at 55 mm minimum external length, 30 mm width and 16 mm height
  as provisional starting values. Increase any dimension needed for real
  component clearance, walls, connectors, battery removal and acoustic port.
- Preserve 10 mm antenna-to-battery separation as a visible keepout.
- Keyfob: begin at 35 x 25 x 12 mm; enlarge if needed to fit the actual board,
  battery, motor, USB-C and assembly clearances.
- Use measured or datasheet maximum component envelopes, not package names
  as assumed dimensions.

## Electrical design priorities

1. Establish board-to-board interfaces and connector pinouts.
2. Implement MCU, programming/debug and low-voltage sensor interfaces.
3. Add NFC and IMU interfaces with bus pull-ups/voltage domains verified.
4. Develop the power/charging architecture as a separate reviewable block.
5. Develop the piezo driver as a separate provisional block. PAM8904E is a
   candidate, not a selected design; the piezo must not be overdriven.
6. Develop the Keyfob motor switch, flyback path and motor supply.
7. Add buttons, status LED interfaces, test points and assembly connectors.

## Milestone order

1. Repository inspection and native project skeletons — COMPLETE as starter workspace only.
2. Mechanical coordinate system and provisional outlines — STARTED; dimensions are not fit-approved.
3. Pod MCU/sensor logical interface contract — DRAFTED in hardware/sentry-pod/interface-contract.md.
4. Keyfob MCU/actuator logical interface contract — DRAFTED in hardware/pocket-keyfob/interface-contract.md.
5. Native schematic capture from both interface contracts — NEXT; exact physical footprints remain on hold.
6. Power/charger and actuator circuit blocks — provisional design work in parallel, with battery/power holds preserved.
7. PCB footprint mapping, placement and routing — after physical pad/connector geometry is verified.
8. Enclosure iteration against actual board and component envelopes.
9. ERC, DRC, CAD geometry and fit checks.
10. BOM, Gerbers, drill, STEP/STL, drawings, firmware, assembly instructions and bench test plan.
11. Physical build and controlled testing by the owner.

## Status language

- DRAFT: authored but not yet checked.
- CHECKED: tool checks run and results recorded.
- REVIEWED: engineering review completed.
- FABRICATION PACKAGE: exports generated and cross-checked.
- BUILT: physical assembly exists.
- TESTED: test actually performed, with conditions and results recorded.

Never imply a later status from an earlier one.
