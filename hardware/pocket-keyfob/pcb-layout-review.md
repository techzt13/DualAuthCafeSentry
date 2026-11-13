# Keyfob PCB placement and footprint review

Date: 2026-11-13  
Status: **editable placement/netlist draft; unrouted and not fabrication-ready**

## Module footprint

The C3-Zero carrier footprint is stored at:

- footprints.pretty/C3Zero_Castellated_2x9.kicad_mod
- KiCad library ID: SentryKeyfob:C3Zero_Castellated_2x9

The official Waveshare dimension drawing identifies:
- PCB outline: 18.0 x 23.5 mm.
- Castellated contact pitch: 2.54 mm.
- 9 contacts along each long edge, 18 total.

Source: https://docs.waveshare.com/ESP32-C3-Zero

The custom footprint uses a provisional 2x9 layout:
- Pad numbers 1–9 down the USB-facing left edge in the module's documented top view.
- Pad numbers 18–10 down the opposite edge.
- 2.54 mm pitch, 15.24 mm estimated row spacing.
- 1.8 x 1.5 mm carrier lands.
- Row centres provisionally ±7.62 mm (15.24 mm row spacing), inferred from the official dimension drawing; the row datum is not explicitly dimensioned.
- Module outline 18 x 23.5 mm.
- U1 placed at (12.75, 11.5) and rotated 90 degrees on the 33 x 23 mm carrier.

The outline and 2.54 mm pitch are sourced. The 15.24 mm row spacing is inferred from the official drawing, not called out as a numeric dimension; pad size and exact row datum remain estimates. Verify the actual board revision and castellation geometry before ordering a PCB.

## Draft PCB population

The board now contains:
- U1 C3-Zero custom footprint and provisional HOLD/control net assignments.
- J1 motor solder pads.
- Q1 IRLML6344 low-side switch.
- D1 PMEG2010AEB,115 SOD-523 flyback diode.
- R1 100 Ω gate resistor.
- R2 100 kΩ gate pull-down.
- C1 100 nF 0603 and C2 10 µF 0805, bottom-side draft footprints.

Net assignments follow the Keyfob schematic:
- U1 contact 1 -> K_5V_BOARD_HOLD.
- U1 contact 2 -> K_GND.
- U1 contact 3 -> K_3V3_BOARD_HOLD.
- U1 contact 4 -> K_BAT_ADC.
- U1 contact 5 -> K_CHARGE_STATUS_N.
- U1 contact 7 -> K_MOTOR_PWM.
- U1 contact 8 -> K_BUTTON_N.
- J1/Q1/D1/R1/R2/C1/C2 assigned to K_3V3_MOTOR_HOLD, K_MOTOR_SW, K_MOTOR_GATE, K_MOTOR_PWM and K_GND as shown in the schematic.

## Layout holds

1. The module orientation is provisional; confirm USB-C overhang and antenna end against the actual module.
2. Waveshare says the ceramic antenna region must remain clear of carrier PCB, metal and plastic. Its exact keepout dimensions are not given in the drawing.
3. The motor and C1/C2 placement may need to move after antenna keepout is measured.
4. SW1 has no footprint because the physical switch is not selected.
5. Battery/charger, ADC divider, charge-status conditioning and power rails remain HOLD.
6. No copper zones, tracks, vias, mounting holes or enclosure mounting features are released.

A text-level S-expression balance check passed, but no KiCad parser, ERC, DRC, RF check, solder-fit check or physical test has been run.
