# Hardware design workspace

Status: **native KiCad schematic and placement drafts exist for both devices; neither PCB is routed or fabrication-ready. FreeCAD macro exists but has not been run.**

## Sentry Pod

Files:
- sentry-pod.kicad_pro
- sentry-pod.kicad_sch
- sentry-pod.kicad_pcb
- sentry-pod.kicad_sym
- sym-lib-table
- fp-lib-table
- footprints.pretty/
- interface-contract.md
- packaging-review.md
- pcb-layout-review.md

Current schematic content:
- Waveshare ESP32-S3-Zero SKU 25081 P15 contact map.
- ELECHOUSE PN5321 MINI I2C host interface, active-low reset.
- Adafruit MPU-6050 breakout product 3886 six-pin header interface.
- Active-low failsafe button.
- Provisional MMBT3904 reset sink with 10 kΩ / 100 kΩ / 10 kΩ network.
- Optional 4.7 kΩ I2C pull-ups marked DNP; PN532 module-revision discrepancy documented.

Current PCB placements:
- Provisional S3-Zero 18-contact castellated footprint.
- Adafruit 3886 1x6 2.54 mm daughter-module footprint.
- PN532 host-interface 7-pad solder row.
- Q1 and R1/R2/R3 reset-stage placements.
- 49.5 x 28 mm board outline with S3 antenna relief notch.

Still missing from Pod PCB:
- Charger, battery connector/NTC, USB VBUS isolation and ideal-diode path.
- Piezo driver, transducer connector and acoustic circuitry.
- Button footprint, test points, complete routing, copper/return paths and antenna keepout rules.

Current Pod packaging-study envelope: 72 x 34 x 29 mm.

## Pocket Keyfob

Files:
- pocket-keyfob.kicad_pro
- pocket-keyfob.kicad_sch
- pocket-keyfob.kicad_pcb
- sym-lib-table
- fp-lib-table
- footprints.pretty/
- interface-contract.md
- pcb-layout-review.md
- packaging-review.md

Current schematic content:
- Waveshare ESP32-C3-Zero SKU 25452 evaluation controller.
- Protected battery ADC and conditioned charge-status interfaces (power holds remain unresolved).
- Active-low button interface.
- IRLML6344 N-channel MOSFET low-side motor switch.
- 100 Ω gate resistor, 100 kΩ hardware-off pull-down.
- Nexperia PMEG2010AEB,115 SOD-523 flyback diode.
- 100 nF and 10 µF motor-rail decoupling.
- VCLP1020B002L is the preferred motor evaluation reference only; O-13 remains open and Precision Microdrives 308-100 is an alternate.

Current PCB placements:
- Provisional upright C3-Zero 2x9 castellated footprint.
- Motor-wire solder pads, MOSFET, diode, gate resistors and motor-rail capacitors.
- 37 x 25 mm carrier outline with antenna relief notch and 22 assigned pad nets.

Still missing from Keyfob PCB:
- Battery/charger, USB-C charging path, regulator/source isolation and ADC divider.
- Physical button, battery connector and final motor retention.
- Complete routing, copper/return paths, test points and antenna keepout rules.

Current Keyfob packaging-study envelope: 44 x 30 x 15.5 mm.

## Release status

- Both schematics and PCBs are editable drafts.
- Both PCBs remain unrouted.
- Footprints are provisional and require physical-part/source-drawing checks.
- No KiCad ERC/DRC, FreeCAD run, STEP/STL export, physical fit, RF, acoustic, battery or haptic validation is claimed.
- Keep LAST-WORKED-ON.md current after each meaningful change.
