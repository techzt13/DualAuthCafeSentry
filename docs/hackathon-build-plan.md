# Hackathon Build Plan — Dual-Auth Cafe Sentry

Date: 2026-11-12
Status: IMPLEMENTATION PLAN — PCB/CAD design authorised; no native designs created yet

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

1. Repository inspection and native project skeletons.
2. Mechanical coordinate system, board outlines and interface drawings.
3. Component-envelope library and placement.
4. Schematic capture and pin/net review.
5. PCB placement and routing.
6. Enclosure iteration against the actual PCB.
7. ERC, DRC, CAD geometry and fit checks.
8. BOM, Gerbers, drill, STEP/STL and drawings.
9. Firmware integration, assembly instructions and bench test plan.
10. Physical build and controlled testing by the owner.

## Status language

- DRAFT: authored but not yet checked.
- CHECKED: tool checks run and results recorded.
- REVIEWED: engineering review completed.
- FABRICATION PACKAGE: exports generated and cross-checked.
- BUILT: physical assembly exists.
- TESTED: test actually performed, with conditions and results recorded.

Never imply a later status from an earlier one.
