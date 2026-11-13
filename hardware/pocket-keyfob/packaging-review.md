# Pocket Keyfob packaging feasibility review

Date: 2026-11-13  
Status: **44 x 30 x 15.5 mm packaging-study direction; not final owner approval or fit-checked enclosure**

## Current packaging-study envelope

The Keyfob case has been increased from 42 mm to **44 x 30 x 15.5 mm** to accommodate the lower-current 10 mm Vybronics motor evaluation reference. The C3-Zero carrier remains 37 x 25 mm.

| Item | Draft position / envelope |
|---|---|
| Outer case | 44 x 30 x 15.5 mm |
| Internal cavity | 41 x 27 x 12.7 mm |
| Carrier PCB | 37 x 25 x 1.6 mm at x=2.5, y=2.5, z=7.0 |
| Waveshare ESP32-C3-Zero | 18 x 23.5 x 1.2 mm at x=12, y=3.75, z=8.6 |
| C3 antenna keepout | 8 x 3.5 mm at x=17, y=24, z=8.6 |
| USB-C access envelope | 10 x 5 x 3.5 mm; case-wall cutout 10 x 4.8 mm |
| Renata ICP402025PC-01 pack candidate | 27.5 x 20.5 x 4.3 mm at x=2.0, y=3.5, z=1.5 |
| Vybronics VCLP1020B002L motor reference | 10 x 2.1 mm at x=35.5, y=7.5, z=8.75 |
| VCLP double-sided tape | 9 x 0.15 mm at x=35.5, y=7.5, z=8.6 |

The dimensions are a working CAD envelope only. The battery, motor, USB plug, antenna, switch and enclosure have not been physically fit-checked.

## Motor evaluation reference

The schematic and CAD use Vybronics VCLP1020B002L as the preferred evaluation reference, not a final selection.

Datasheet A/1 (2020-07-01) specifies:
- Rated voltage 3.0 V; operating range 2.5–3.5 V.
- Rated current 30 mA maximum at 3.0 V.
- Starting voltage 2.3 V maximum.
- Starting current 80 mA maximum under the stated 2.3 V start test. This is not a universal stall-current guarantee.
- Vibration strength 0.75 G minimum in the specified 100 g test jig at 3.0 V.
- Body 10.0 ±0.1 mm diameter x 2.1 ±0.1 mm thick.
- Double-sided tape 9.0 mm diameter x 0.15 mm nominal.
- Leads 25 ±1 mm; red positive and blue negative.
- Life test: 1 s ON / 1 s OFF for 100,000 cycles. Indefinite continuous-alert duty is not qualified.

Precision Microdrives 308-100 remains an alternate: 8 mm diameter x 3.4 mm, 94 mA maximum rated current and 124 mA maximum start current. The existing MOSFET/diode driver stage is provisionally sized for this higher-current alternate, but no battery/power approval follows from that.

## Separation and stack arithmetic

- Battery ends at x=29.5 mm; motor body begins at x=30.5 mm: 1.0 mm nominal horizontal gap.
- C3-Zero body ends at x=30.0 mm; motor begins at x=30.5 mm: 0.5 mm nominal horizontal gap.
- Motor body ends at x=40.5 mm; internal case boundary is x=42.5 mm: 2.0 mm nominal clearance.
- Motor top is z=10.85 mm; lid underside is z=14.0 mm: 3.15 mm nominal vertical clearance.
- Battery top is z=5.8 mm; carrier PCB underside is z=7.0 mm: 1.2 mm nominal vertical gap.
- The motor body extends 1.0 mm beyond the carrier PCB's right edge. It is intended to be retained by adhesive/case support rather than relying on full PCB support.

These are arithmetic checks only. The motor lead exit, tape tolerance, adhesive compression, battery swelling, connector leads and case tolerances are not included.

## Battery and peak-current blocker

The current Keyfob battery candidate is Renata ICP402025PC-01:
- 155 mA continuous discharge.
- 310 mA non-continuous discharge.
- 150 mAh minimum / 155 mAh nominal.
- Charge-voltage tolerance and allowed duration for non-continuous discharge remain unresolved.

The documented ESP32-C3-Zero transmit peak used in the current project screen is 335 mA. The Renata pack's 310 mA non-continuous rating is already 25 mA below that screen, before adding the motor's start current or other loads. The VCLP motor's lower current improves the load case but does not fix the battery mismatch. Do not approve this battery pairing or energise the design until the complete simultaneous-load and pulse-duration budget is reconciled.

## Remaining holds

1. Verify the received VCLP1020B002L body, lead-exit geometry, polarity and tape against the datasheet.
2. Test haptic feel through the actual enclosure; 0.75 G in the 100 g jig is not a case-level guarantee.
3. Determine a qualified alert duty cycle and motor PWM policy.
4. Resolve the battery pulse-current mismatch and select a protected pack with known charge-voltage tolerance, NTC, connector and pulse duration.
5. Complete the Keyfob charger, USB-C charging receptacle, power path and battery-monitor circuits.
6. Confirm C3-Zero USB-C plug access and antenna keepout in the printed case.
7. Add the physical button, keyring retention and motor support features.
8. Route the PCB, complete copper/return paths and antenna exclusion, then run ERC/DRC.
9. Run the FreeCAD macro, inspect the assembly and perform physical fit, haptic and battery tests.

No manufacturer correspondence is required for the next prototype steps. Public datasheets provide enough to continue; actual received-part checks and testing remain necessary.
