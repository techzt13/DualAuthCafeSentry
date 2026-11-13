# Sentry Pod packaging feasibility review

Date: 2026-11-13  
Status: **72 x 34 x 29 mm packaging-study direction; not final owner approval or fit-checked enclosure**

## Why the earlier envelope changed

The earlier 55 x 30 x 19.3 mm estimate was only a lower-bound stack for a bare-cell reference, 10 mm battery-to-NFC separation, a 1 mm antenna and 1.5 mm base/lid. It did not include the protected battery, carrier PCB, breakout modules or piezo.

The current Pod battery candidate is Renata ICP521630PM-01:
- 31.5 x 17.0 x 5.7 mm maximum envelope.
- 250 mA continuous / 500 mA non-continuous discharge current.
- Protection thresholds, permitted pulse duration, charge-voltage tolerance, NTC, connector and restraint remain unresolved.

With the protected pack, a 10 mm vertical battery-to-coil gap, 1 mm coil and 1.5 mm base/lid, the battery/antenna stack alone needs 19.7 mm. That leaves no meaningful space in a 19.7 mm case for the PCB, modules or 7.5 mm piezo.

## Current packaging-study envelope

The CAD macro now uses **72 x 34 x 29 mm**. This is a proposed study size, not a final approval.

| Item | Draft position / envelope |
|---|---|
| Outer case | 72 x 34 x 29 mm |
| Internal cavity | 69 x 31 x 26.2 mm |
| Carrier PCB | 49.5 x 28 x 1.6 mm at x=10, y=3, z=8 |
| Renata ICP521630PM-01 candidate | 31.5 x 17 x 5.7 mm at x=2.5, y=6.5, z=1.5 |
| Waveshare ESP32-S3-Zero | 18 x 23.5 x 1.2 mm, upright, USB at top |
| Adafruit 3886 IMU breakout | 25.4 x 17.78 mm board outline; 26 x 17.8 x 4.6 mm envelope |
| Elechouse PN5321 MINI | 25 x 16.4 x 4.4 mm, stacked above the IMU breakout |
| NFC antenna | 10 x 25 x 1 mm placeholder at x=44.5, y=12, z=26 |
| CPT-2475-92T piezo | 24 mm diameter x 7.5 mm high at x=20, y=15, z=17 |

## PCB placement now represented

The Pod PCB is no longer outline-only. Current native KiCad placement includes:
- U1 S3-Zero 18-contact castellated footprint at board (9,12), with a centre-bottom antenna relief notch.
- Q1 MMBT3904 and R1/R2/R3 NFC reset-stage footprints in the gap between U1 and the IMU module.
- J2 Adafruit 3886 1x6 2.54 mm header footprint at (36.5,14), derived from the official Eagle board.
- J1 PN5321 MINI host-interface solder-pad row at (37,2.5), using datasheet signal names.
- Mechanical reference outlines for the IMU and PN532 modules.

The PN5321 MINI is modelled above the IMU breakout, not underneath the carrier. This avoids the earlier through-hole-header/underside-module collision. It requires a spacer or bracket and physical access to the PN532 host cable.

## Separation arithmetic

- Battery ends at x=34.0 mm; antenna starts at x=44.5 mm: **10.5 mm horizontal separation**.
- Piezo rightmost edge is x=32.0 mm; antenna starts at x=44.5 mm: **12.5 mm horizontal separation**.
- Battery top is z=7.2 mm; carrier PCB bottom is z=8.0 mm: 0.8 mm nominal gap.
- IMU top is z=14.2 mm; PN532 module bottom is z=15.0 mm: 0.8 mm nominal gap.
- PN532 module top is z=19.4 mm; antenna placeholder underside is z=26.0 mm: 6.6 mm vertical gap.
- Piezo top is z=24.5 mm; antenna placeholder underside is z=26.0 mm: 1.5 mm vertical gap, plus 12.5 mm horizontal separation.
- Coil ends at x=69.5 mm; internal case boundary is x=70.5 mm: 1.0 mm nominal clearance.

These are envelope arithmetic checks only. They do not establish RF performance, acoustic output, tolerance stack, battery restraint or physical fit.

## PN5321 MINI revision and interface details

The current Rev. 1.5 datasheet (September 2026) identifies:
- Host connector pin order: 1 SCL, 2 SDA, 3 MISO, 4 SCK, 5 RST, 6 supply (silkscreen “5V”, accepts 3.3–5.0 V), 7 GND.
- Host logic is 3.3 V; the selected carrier VCC net is P_3V3_PERIPH_HOLD.
- Factory interface is UART; for I2C, bridge only the I2C solder pad with power removed and leave SPI open.
- I2C address is 0x24; no host IRQ is exposed, so firmware polling is required.
- The included 10 x 25 mm and 40 x 50 mm ferrite-backed antennas use a 2-pin MX1.0 connector and 10 cm lead. Only one antenna may be connected at a time.

The current v1.1 online documentation differs from the downloaded Rev. 1.5 datasheet on supply range and I2C pull-ups. Rev. 1.5 says optional 0402 pull-up footprints are unpopulated in production; v1.1 says onboard 3.3 V pull-ups are present. Inspect the received hardware revision before deciding whether carrier R4/R5 should be populated. Do not infer cable wire colours or orientation.

The carrier J1 footprint is a generic 7-pad solder row, not a selected mating connector. The optional host cable's bare-wire end must be continuity-checked against the module pinout before soldering.

## Sound and power limits

### Sound target

The CPT-2475-92T publishes 92 dB minimum at 10 cm under its rated 10 Vp-p, 4 kHz, half-duty condition. This is 13 dB below the proposed 105 dB target. The current transducer and driver are not proven to meet the target; the acoustic vent/cavity is not modelled.

### Battery pulse capability

The existing Pod load screen is approximately 493.9 mA before the siren driver, LED and unaccounted transients. The Renata pack's 500 mA non-continuous discharge rating is too close to treat as approved. The duration allowed for the non-continuous rating is not stated in the reviewed record. Recalculate against the actual driver, load simultaneity and battery impedance.

### NFC current and range

The Rev. 1.5 datasheet reports, for the 10 x 25 mm antenna, approximately 23.5 mA mean and 84.6 mA maximum at 100 Hz during 4 Hz polling at 3.3 V; continuous RF averaged 84.4 mA and reached 85.85 mA at 100 Hz. These are measured profiles, not guaranteed maximums or sub-10-ms transient bounds. The 10 x 25 mm antenna's measured stable read distance was 3.2 cm at 3.3 V for the specified card test; the 40 x 50 mm antenna measured farther but does not fit the current envelope. Test with the intended credentials and final enclosure.

## Remaining mechanical and electrical holds

1. Verify actual S3-Zero castellated pad/antenna dimensions and USB-C shell against the received module.
2. Inspect the Adafruit 3886 physical board and header revision; the 6-pin footprint is based on its official Eagle source, but no physical fit has been performed.
3. Inspect the Elechouse PN5321 MINI received revision and host cable; the downloaded DWG archive has not been opened.
4. Confirm the PN532-over-IMU spacer/bracket, host cable route and access to the module's mode solder pads.
5. Confirm the NFC antenna coil mounting, ferrite orientation, lid material and RF clearance.
6. Design the piezo cavity, acoustic vent and retention; validate SPL at 10 cm.
7. Complete the charger, protected-battery interface, ideal-diode/USB isolation and audio-driver blocks.
8. Reconcile the full Pod peak-current budget with the battery pulse capability.
9. Add remaining switch, power/audio footprints and route the board.
10. Run KiCad ERC/DRC, FreeCAD geometry checks and a physical prototype fit test.

No manufacturer correspondence is required for these next steps. Public datasheets and drawings provide enough to continue the prototype; unresolved claims can be isolated and measured on the received parts.
