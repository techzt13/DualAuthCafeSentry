# Sentry Pod packaging feasibility review

Date: 2026-11-13  
Status: **72 x 30 x 29 mm packaging-study direction; not a final owner approval or fit-checked enclosure**

## Why the original 55 x 30 x 19.3 mm envelope was not sufficient

The earlier 19.3 mm figure was only a lower-bound stack for a bare-cell reference, 10 mm battery-to-NFC separation, a 1 mm antenna and 1.5 mm base/lid. It did not include the actual protected Pod battery candidate, carrier PCB, breakout modules or sounder.

The current Pod battery candidate is Renata ICP521630PM-01:
- 31.5 x 17.0 x 5.7 mm maximum envelope.
- 125 mA normal / 250 mA maximum charge current.
- 250 mA continuous / 500 mA non-continuous discharge current.
- Protection thresholds, charge-voltage tolerance, NTC, connector and allowed non-continuous pulse duration remain unresolved.

With the 5.7 mm protected pack, 10 mm vertical battery-to-coil gap, 1 mm coil and 1.5 mm base/lid, the battery/antenna stack alone requires 19.7 mm. That leaves no meaningful space in a 19.7 mm case for the PCB, modules or 7.5 mm piezo.

## Current packaging-study envelope

The CAD macro now uses **72 x 30 x 29 mm** as a working packaging envelope. This is a proposed study size, not a final approval.

| Item | Draft position / envelope |
|---|---|
| Outer case | 72 x 30 x 29 mm |
| Internal cavity | 69 x 27 x 26 mm |
| Carrier PCB | 49.5 x 24 x 1.6 mm at x=10, y=3, z=8 |
| Renata ICP521630PM-01 candidate | 31.5 x 17 x 5.7 mm at x=2.5, y=6.5, z=1.5 |
| Waveshare ESP32-S3-Zero | 23.5 x 18 x 1.2 mm on carrier top |
| Adafruit 3886 IMU breakout | 26 x 17.8 x 4.6 mm on carrier top |
| Elechouse PN5321 MINI | 25 x 16.4 x 4.4 mm on carrier underside |
| NFC antenna | 25 x 10 x 1 mm placeholder at x=44.5, y=10, z=26 |
| CPT-2475-92T piezo | 24 mm diameter x 7.5 mm high at x=20, y=15, z=17 |

### Separation arithmetic

- Battery ends at x=34.0 mm; antenna begins at x=44.5 mm: 10.5 mm horizontal separation.
- Piezo rightmost edge is x=32.0 mm; antenna begins at x=44.5 mm: 12.5 mm horizontal separation.
- Battery top is z=7.2 mm; carrier board bottom is z=8.0 mm: 0.8 mm nominal gap.
- Piezo top is z=24.5 mm; antenna placeholder begins at z=26.0 mm: 1.5 mm vertical gap.
- The coil ends at x=69.5 mm; the internal case boundary is x=70.5 mm: 1.0 mm clearance.

These are envelope arithmetic checks only. They do not establish RF performance, component tolerances, battery restraint, acoustic performance or actual mechanical fit.

## Module arrangement concept

The proposed stack is:
1. Protected battery in the left-hand lower compartment.
2. Carrier PCB above the battery.
3. S3-Zero and IMU breakout arranged end-to-end on the carrier top.
4. PN5321 MINI mounted below the carrier in the right-hand region, where it does not overlap the battery.
5. Separate NFC coil in the right-hand lid region.
6. Piezo mounted above the carrier in the left/centre region, with a sound port still to be designed.

This arrangement is a layout hypothesis. The PN532 module, carrier board and coil still need a proper RF keepout and cable path. The exact PN532 module drawing and antenna construction have not been physically checked.

## Important unresolved conflicts

### Sound target

The CPT-2475-92T publishes 92 dB minimum at 10 cm under its rated 10 Vp-p, 4 kHz, half-duty test condition. That is 13 dB below the proposed 105 dB target. The driver and transducer combination is not proven to meet the target. A different transducer or acoustic design may change the envelope.

### Battery pulse capability

The current Pod load screen is already approximately 493.9 mA before adding the sound driver and other unaccounted transients. The Renata pack's published 500 mA non-continuous discharge rating is too close to treat as approved. The duration allowed for its non-continuous rating is not stated in the reviewed record. The Jauch candidate has a lower published discharge rating and is not an automatic substitute.

### Mechanical details

- The carrier PCB is still outline-only; no module footprints or routed copper are released.
- The PN5321 MINI dimensions are published, but its mechanical drawing archive was downloaded and not opened in the prior review.
- The Adafruit 3886 board dimensions are a product-page claim; its drawing and schematic were not inspected, and it was listed out of stock.
- The antenna coil thickness, cable, mounting and RF keepout are unknown.
- The piezo needs an acoustic cavity, vent and mechanical support.
- No mounting bosses, lid joint, gasket, fasteners, battery restraint, connector access or tolerances are included.

## Next engineering work

1. Use this 72 x 30 x 29 mm envelope as the current packaging study, not a final size.
2. Create a dimensioned module placement in the Pod PCB and verify the underside PN532 module against the top-side IMU breakout.
3. Obtain and inspect the Elechouse PN5321 MINI DWG/STEP archive locally; do not claim its contents are verified until opened.
4. Inspect Adafruit 3886 board files or replace it with a verified, smaller IMU implementation.
5. Design the antenna cable, matching interface, coil mounting and carrier-board keepout.
6. Select a sounder that can credibly approach the 105 dB target, then revise the acoustic cavity.
7. Recalculate the complete Pod peak-current budget against the actual battery pack and driver.
8. Run the CAD macro in FreeCAD, inspect the reference assembly, then adjust the case and mounting geometry.

No manufacturer correspondence is required for the next steps. The current unknowns can be progressed with public drawings, physical inspection and prototype measurements.
