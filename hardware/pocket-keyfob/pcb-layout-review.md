# Keyfob PCB placement and mechanical layout review

Date: 2026-11-13  
Status: **revised evaluation layout; editable and net-assigned, but unrouted and not fabrication-ready**

## Revised packaging direction

The previous 90-degree module placement put the USB-C access and antenna end into a congested carrier-board region. The current evaluation layout turns the C3-Zero upright so its USB-C connector faces the case's short top wall and the ceramic antenna faces the opposite end.

| Item | Current draft |
|---|---:|
| Keyfob outer enclosure | 44 x 30 x 15.5 mm |
| Internal cavity (1.5 mm walls) | 41 x 27 x 12.5 mm |
| Carrier PCB | 37 x 25 x 1.6 mm |
| C3-Zero module | 18 x 23.5 mm, upright |
| Module footprint centre | (18.5, 13.0) on PCB |
| Antenna relief notch | 8 x 3.5 mm at bottom-centre board edge |
| USB-C case-wall cutout | 10 x 4.8 mm provisional |
| Motor | Vybronics VCLP1020B002L, 10 mm diameter x 2.1 mm, 9 mm x 0.15 mm tape |
| Battery candidate envelope | 27.5 x 20.5 x 4.3 mm |

These dimensions are a proposed mechanical evaluation direction, not a user-approved final size.

## C3-Zero module footprint

Custom footprint:
- File: footprints.pretty/C3Zero_Castellated_2x9.kicad_mod
- Library ID: SentryKeyfob:C3Zero_Castellated_2x9
- Module outline: 18.0 x 23.5 mm.
- 9 contacts on each long edge.
- 2.54 mm contact pitch.
- Contacts 1–9 are on the USB-facing left edge, top-to-bottom; contacts 18–10 are on the right edge, top-to-bottom.
- Row spacing is provisionally 15.24 mm (±7.62 mm); inferred from the official drawing, not explicitly called out as a dimension.
- Carrier pads are provisionally 1.8 x 1.5 mm; the public drawing does not dimension the recommended carrier land shape.

Source: https://docs.waveshare.com/ESP32-C3-Zero

The footprint and board instance now use the official top-view pad order. The module is placed at (18.5,13.0) with zero rotation.

## RF and connector provisions

- A centre-bottom 8 x 3.5 mm Edge.Cuts relief notch is included under the assumed ceramic antenna region. Side rails remain under the castellated pads.
- The battery candidate envelope ends at the antenna-notch boundary; no battery solid is modelled beneath the antenna relief.
- The case CAD macro adds a 10 x 4.8 mm USB-C access cutout through the top wall.
- The antenna's exact dimensions and required clearance are not fully dimensioned in the public drawing. Confirm the actual module revision and RF keepout before releasing copper or plastic.
- The plastic wall near the antenna still requires RF testing; no antenna performance is claimed.

## Draft PCB population and net mapping

- U1: C3-Zero 2x9 module footprint and assigned HOLD/control contacts.
- J1: two motor solder pads.
- Q1: IRLML6344 SOT-23 low-side switch.
- D1: PMEG2010AEB,115 SOD-523 flyback diode.
- R1: 100 Ω gate resistor.
- R2: 100 kΩ gate pull-down.
- C1: 100 nF 0603 and C2: 10 µF 0805.
- All motor-stage components are top-side placements.
- The motor is at PCB local (32,5); J1 is at (32,15.5); Q1/D1/R1/R2/C1/C2 are positioned in the free right-hand board margin.

U1 contact assignments:
- 1 -> K_5V_BOARD_HOLD.
- 2 -> K_GND.
- 3 -> K_3V3_BOARD_HOLD.
- 4 -> K_BAT_ADC.
- 5 -> K_CHARGE_STATUS_N.
- 7 -> K_MOTOR_PWM.
- 8 -> K_BUTTON_N.
- Remaining contacts are intentionally unassigned pending firmware/interface review.

Motor circuit pad assignments are consistent with the schematic: J1 positive to K_3V3_MOTOR_HOLD, J1 negative to K_MOTOR_SW; Q1 gate/source/drain to K_MOTOR_GATE/K_GND/K_MOTOR_SW; D1 cathode/anode to K_3V3_MOTOR_HOLD/K_MOTOR_SW; R1 and R2 implement the gate network; C1/C2 decouple K_3V3_MOTOR_HOLD to K_GND.

## Battery and vertical stack

The current battery candidate is Renata ICP402025PC-01, maximum envelope 27.5 x 20.5 x 4.3 mm. The CAD macro places it below the carrier PCB with 1.2 mm nominal clearance to the board underside. This is a bare geometric envelope only: pack leads, connector, insulation, adhesive, swelling allowance and retention are not fully represented.

The VCLP motor body is 10 x 2.1 mm, with a separate 9 x 0.15 mm adhesive tape reference, above the carrier board. The motor body extends 1 mm beyond the right board edge but remains inside the case envelope. Full lead-exit envelope, adhesive retention, haptic coupling and clearance to the lid must be checked in FreeCAD and against the received motor.

## Remaining layout holds

1. Verify the exact C3-Zero module revision, castellated land dimensions, USB shell position and ceramic antenna area against the physical board.
2. Confirm the antenna relief notch is large enough and that no copper, battery, fastener or enclosure material degrades RF performance.
3. Confirm USB-C plug insertion clearance and the actual case-wall cutout.
4. Verify battery lead/connector location, retention and no-compression clearance.
5. Add the physical SW1 footprint after selecting a real switch.
6. Complete the battery ADC divider and charge-status conditioning; both remain HOLD.
7. Complete copper pours, tracks, vias, return paths and antenna exclusion.
8. Run KiCad ERC/DRC, FreeCAD geometry checks and a physical prototype fit test.

The PCB is not routed and is not fabrication-ready. No ERC/DRC, RF, thermal, electrical or physical fit validation is claimed.
