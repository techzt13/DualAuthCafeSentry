# Sentry Pod PCB placement review

Date: 2026-11-13  
Status: **native KiCad placement draft; unrouted, incomplete and not fabrication-ready**

## Board and outline

- Carrier outline: 49.5 x 28.0 mm.
- Edge.Cuts includes an 8 mm wide centre-bottom relief notch, 7.5 mm deep.
- The notch clears the assumed ESP32-S3-Zero antenna region (8 x 3.5 mm). Its size is deliberately larger than the assumed ceramic antenna zone; verify the received module before changing copper or plastic.
- Board placement in the CAD packaging study: x=10, y=3, z=8 mm inside a proposed 72 x 34 x 29 mm enclosure.

## Current native KiCad footprints

| Ref | Footprint | Board placement | Status |
|---|---|---:|---|
| U1 | SentryPod:S3Zero_Castellated_2x9 | (9,12), F.Cu | Provisional 18-contact footprint |
| Q1 | SentryPod:MMBT3904_SOT23_Draft | (20.5,8.5), F.Cu | Provisional reset transistor land pattern |
| R1 | SentryPod:R_0603_Draft | (20.5,12), F.Cu | Provisional 0603 |
| R2 | SentryPod:R_0603_Draft | (20.5,14.5), F.Cu | Provisional 0603 |
| R3 | SentryPod:R_0603_Draft | (20.5,17), F.Cu | Provisional 0603 |
| J1 | SentryPod:PN5321_MINI_Host_7Pad_Draft | (37,2.5), F.Cu | Generic solder-pad row for module host cable; not a selected connector |
| J2 | SentryPod:Adafruit3886_Module_1x6 | (36.5,14), F.Cu | Daughter-module 1x6, 2.54 mm through-hole interface based on official Eagle board |

### U1 S3-Zero contact order

The custom footprint follows the P15 schematic contact mapping in docs/verified-pinouts.md:
- Pads 1–9 run down the right edge from USB/top.
- Pads 18–10 run down the left edge from USB/top.
- Module outline is 18 x 23.5 mm.
- Pitch is 2.54 mm; row spacing is 15.24 mm.
- Pad size 1.8 x 1.5 mm is provisional; verify the received castellations and recommended carrier land pattern.
- The antenna is at the bottom end; the board notch removes substrate beneath the assumed antenna area.

### J2 Adafruit 3886

The official Adafruit Eagle board source identifies a 25.40 x 17.78 mm module and JP3 1x6 2.54 mm header row. Carrier pad mapping:
1 VIN -> P_3V3_PERIPH_HOLD
2 3Vo -> NC
3 GND -> GND
4 SCL -> P_I2C_SCL
5 SDA -> P_I2C_SDA
6 INT -> P_IMU_INT

The carrier footprint omits the breakout's four 2.5 mm mounting holes. In the current CAD study, the PN532 module is stacked above the IMU breakout, so module support, header pin clearance and service access require a bracket/spacer and physical inspection.

### J1 PN5321 MINI host pads

Rev. 1.5 host order is 1 SCL, 2 SDA, 3 MISO, 4 SCK, 5 RST, 6 VCC, 7 GND. The footprint uses signal-name pad numbers SCL, SDA, MISO, SCK, RST, VCC, GND in that order. The pad row is a generic solder interface for the optional host cable; it is not a selected MX1.25 mating connector. Confirm cable continuity and orientation before soldering.

The module defaults to UART per Rev. 1.5. With power removed, bridge only its I2C solder pad. The Rev. 1.5 and online v1.1 documentation differ on supply range and I2C pull-up population; inspect the received module before finalizing R4/R5.

## NFC reset stage

Q1 and R1/R2/R3 are placed in the 5.5 mm gap between U1 and J2:
- R1: P_NFC_RESET_CTL to Q1 base, 10 kΩ.
- R2: base to GND, 100 kΩ.
- Q1: MMBT3904, pin 1 base / 2 emitter / 3 collector.
- R3: P_3V3_PERIPH_HOLD to P_NFC_RESET_N, 10 kΩ.

This is a low-side NPN reset sink. The peripheral pull-up rail remains unsourced. Footprint pad geometry and orientation are provisional and not checked against the selected package drawing.

## CAD alignment

The current CAD macro uses:
- Pod outer envelope 72 x 34 x 29 mm.
- Carrier 49.5 x 28 x 1.6 mm.
- S3-Zero at x=10, y=3.25, z=9.6 mm.
- Adafruit 3886 at x=33.5, y=8.1, z=9.6 mm.
- PN5321 MINI at x=34.5, y=14, z=15 mm, stacked above the IMU to clear its 1x6 header and STEMMA QT connectors.
- Battery candidate at x=2.5, y=6.5, z=1.5 mm.
- 10 x 25 mm NFC antenna placeholder in the right-hand lid region.
- Piezo reference in the left/centre region.

This is an envelope and placement hypothesis only. It is not a verified assembly.

## Separate evaluation schematics not yet on the Pod PCB

- BQ25185 charger/power-path block exists as [pod-power-stage.kicad_sch](pod-power-stage.kicad_sch), standalone and non-energised.
- PAM8904E 1x audio block exists as [pod-audio-stage.kicad_sch](pod-audio-stage.kicad_sch), standalone and non-energised.
- Neither is yet integrated into the main Pod schematic as a hierarchical sheet or placed on the Pod PCB.

## Not yet on the Pod PCB

- BQ25185 charger and protected battery connection.
- Battery NTC and actual pack connector.
- USB VBUS isolation / ideal-diode path.
- PAM8904E or alternative sounder driver, piezo connector and acoustic circuitry.
- Button footprint and physical switch selection.
- Any routing, copper pours, return paths, vias or antenna keepout rules.
- Complete mounting, test points, programming access, and protection.

## Release holds

1. Verify U1 and module footprints against physical parts and source drawings.
2. Reconcile the Adafruit/PN532 stacked-module clearances and cable access in FreeCAD.
3. Add and review the charger, power-path and audio circuits before placement/routing.
4. Reconcile battery peak-current capability with simultaneous ESP32, PN532 and sounder loads.
5. Add the physical switch, test points, mounting and retention.
6. Run KiCad ERC/DRC and review every unconnected/no-connect pin.
7. Route, inspect return paths and antenna keepouts.
8. Generate fabrication outputs only after the above checks.

No ERC/DRC, routing, RF test, acoustic test, FreeCAD run or physical fit check is claimed.
