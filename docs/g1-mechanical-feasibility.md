# G1 Mechanical Feasibility Comparison

Revision: 0.4 | Date: 2026-11-12 | Status: arithmetic screen with candidate parts; NOT a fit certification; O-01 Option A recorded

All dimensions are in **millimetres**. No CAD model exists and none was
created. This applies the screening method of
[mechanical requirements](mechanical-requirements.md#feasibility) to the G1
candidates in the [component shortlist](g1-component-shortlist.md).
**O-01 has now been decided:** the Pod length direction is enlarged to at least
approximately 55 mm, while 30 mm width and 16 mm height remain provisional.
This is not a fit certification or final envelope. The Keyfob target is
unchanged. See [owner decisions](g1-owner-decisions.md).

## 1. Method and limits

The same screening assumption is kept: 1.5 walls, base and lid, giving an
ideal Pod cavity of 42 x 27 x 13 (14,742 mm3, 1,134 mm2 in plan) and an ideal
Keyfob cavity of 32 x 22 x 9 (6,336 mm3, 704 mm2). These cavities ignore
bosses, radii, lid joints, wires, connectors, solder and all clearances, so
they overstate usable space.

A part is given the largest size its document supports. Where a maker
publishes a size without a dimensioned drawing, the figure is labelled
**published claim**. A screen that fails proves the tested arrangement does
not fit. A screen that passes proves nothing about fit.

## 2. Candidate envelopes

| Part | Envelope used | Evidence class | Source |
| --- | --- | --- | --- |
| Waveshare ESP32-S3-Zero / C3-Zero | 23.5 x 18 PCB outline; **assembled height TBD** | Drawing, outline only | SRC-03, SRC-24 |
| Elechouse PN5321 MINI board | 25 x 16.4 x 4.4; 4.4 is "maximum stated assembly height" | Maker datasheet; DWG not opened | SRC-43 |
| Elechouse 10 x 25 antenna | 10 x 25; **thickness and tolerance TBD**; 100 lead | Maker datasheet | SRC-43 |
| Adafruit 3886 MPU-6050 board | 26.0 x 17.8 x 4.6 | Published claim | SRC-42 |
| Jauch LP502030JH+PCM | 32.0 x 20.5 maximum; 5.0 delivered, 5.4 after cycling | Maker datasheet drawing | SRC-37 |
| Renata ICP521630PM-01 | 31.5 x 17.0 x 5.7 maximum | Maker datasheet | SRC-38 |
| Jauch LP402025JU+PCM | 27.0 x 20.5 maximum; 4.2 delivered, 4.5 after cycling | Maker datasheet drawing | SRC-37 |
| Renata ICP402025PC-01 | 27.5 x 20.5 x 4.3 maximum, measured after 500 cycles | Maker datasheet | SRC-38 |
| PKCELL LP402025 pack (Adafruit 1317) | 25 +/-0.3 x 20 +/-0.3 x 4.0 +/-0.3, so 25.3 x 20.3 x 4.3 | Cell-maker drawing, retailer-hosted, dated 2014 | SRC-40 |
| Adafruit 4410 charger board | 24.0 x 19.0 x 7.2 | Published claim | SRC-42 |
| Same Sky CPT-2475-92T piezo | Diameter 24 +/-0.2 x 7.5 +/-0.2 body; two 0.8 pins, 6 long, on 10 +/-0.2 pitch | Maker drawing, viewed | SRC-44 |
| Precision Microdrives 308-100 motor | Diameter 8 +/-0.1 x 3.4 +/-0.1 body; lead-exit tab 3 +/-1 wide and 7 +/-1 long adds to one side | Maker drawing V0013, viewed | SRC-46 |
| Precision Microdrives 310-103 motor | Diameter 10 +/-0.1 x 2.7 +/-0.1 | Maker datasheet | SRC-46 |
| Vybronics VCLP1020B002L motor | Diameter 10 +/-0.1 x 2.1 +/-0.1 | Maker drawing | SRC-27 |
| GCT USB4125 receptacle | 8.94 wide x 6.80 +/-0.15 deep x 3.16 high above the board | Maker drawing A6 | SRC-52 |
| JST PH header, 2-way | Top entry mounted height 8, width 4.5; side entry about 4.8 high | Maker catalogue, reference dimensions | SRC-51 |
| JST SH header, 2-way | Side entry about 2.95 high | Maker catalogue, reference dimensions | SRC-51 |

## 3. Sentry Pod, original screening target 45 x 30 x 16 (superseded in length by O-01)

### 3.1 Off-the-shelf module set

Modules: S3-Zero, PN5321 MINI with 10 x 25 antenna, Adafruit 3886, Jauch
LP502030JH+PCM, Adafruit 4410, CPT-2475-92T.

```text
box volumes, excluding the processor board and the antenna:
  NFC 25 x 16.4 x 4.4      = 1,804.0
  IMU 26.0 x 17.8 x 4.6    = 2,128.9
  pack 32.0 x 20.5 x 5.4   = 3,542.4
  charger 24.0 x 19.0 x 7.2 = 3,283.2
  piezo 24 x 24 x 7.5      = 4,320.0
  total                    = 15,078.5 mm3 = 102.3 % of the 14,742 mm3 cavity
with the piezo as a cylinder (3,392.9): 14,151.4 mm3 = 96.0 %
plan footprints including the 23.5 x 18 board: 2,983.8 mm2 = 2.63 cavity floors
```

**Result: FAIL.** The parts other than the processor board already fill or
exceed the whole ideal cavity. Even counting the piezo as a cylinder, the
590.6 mm3 left over equals a 23.5 x 18 board only 1.4 thick, before the
antenna, wires, switch, button and connectors. This module set cannot fit
the 45 x 30 x 16 target.

### 3.2 The 10 mm NFC separation with a 502030-class pack

The 10 x 25 antenna is the smallest PN532 antenna found with maker
documentation. It is placed flat under the lid. The pack must keep 10 from
it, measured surface to surface (the convention in mechanical requirements
section 1). Antenna thickness is unknown, so zero is assumed, which favours
fitting.

```text
pack on the floor, 5.4 thick; antenna at the lid:
  vertical gap = 13 - 5.4 = 7.6
  lateral offset needed = sqrt(10^2 - 7.6^2) = 6.5
  along the length: 10 + 6.5 + 32.0 = 48.5  > 42
  across the width: 10 + 6.5 + 20.5 = 37.0  > 27
same plane, no vertical offset:
  along the length: 10 + 10 + 32.0 = 52.0   > 42
  across the width: 10 + 10 + 20.5 = 40.5   > 27
pack turned 90 degrees: its 32.0 length exceeds the 27 width
```

With the narrower Renata ICP521630PM-01 (31.5 x 17.0 x 5.7): vertical gap
7.3, lateral offset 6.83, giving 48.3 along the length and 33.8 across the
width. Both still fail.

**Result: FAIL for every axis-aligned placement tested.** Inside the screened
cavity, a 200 to 250 mAh pack of this class cannot be 10 from even the
smallest documented antenna. The specified battery size, the specified NFC
separation and the specified outside size cannot all be met under the
screening assumptions. Other geometries (a tilted antenna, a non-rectangular
body) were not analysed.

Conditional lower bound, not a recommended size: placing antenna and pack
end to end needs an inside length of `10 + 10 + 32.0 = 52.0`, so about **55
outside**, before any other part. Using the vertical offset it is `48.5 + 3
= 51.5` outside. Both exceed 45.

### 3.3 Piezo

The only externally driven piezo found with a documented level above 90 dB
is 24 in diameter and 7.5 high (section 2). It must also be 10 from the
antenna and sit at a vent. At 24 wide it leaves `27 - 24 = 3` across the
cavity. Smaller documented parts are much quieter; see the shortlist. No
part of 25 diameter or less was found that documents 105 dB at any distance.

### 3.4 What a custom carrier would change

Replacing the IMU and charger breakouts with components on a custom carrier
PCB removes about 5,412 mm3 of module volume. It does not change section 3.2
or 3.3. A carrier is a schematic and layout task, which is outside this
stage and needs separate authorisation.

**Pod conclusion:** the original 45 x 30 x 16 target is not achievable with
the candidates found. O-01 now directs an enlarged Pod with at least about
55 mm external length; this only addresses the identified length/separation
conflict in a lower-bound arrangement. It does **not** establish that a
55 x 30 x 16 enclosure fits the complete candidate set. The piezo, processor,
IMU, NFC board, wiring, connectors, acoustic vent, wall thickness and real
clearances still require a new mechanical screen. The final Pod may need to
be longer, wider or thicker.

## 4. Pocket Keyfob, target 35 x 25 x 12

### 4.1 With a separate charger board

```text
Adafruit 4410, 24.0 x 19.0 x 7.2, with Jauch LP402025JU, 27.0 x 20.5 x 4.5:
  side by side: 24.0 + 27.0 = 51.0 > 32;  19.0 + 20.5 = 39.5 > 22
  stacked:      7.2 + 4.5 = 11.7 > 9
  volumes:      3,283.2 + 2,490.8 = 5,774.0 mm3 = 91.1 % of 6,336 mm3
with the PKCELL pack, 25.3 x 20.3 x 4.3: stacked 11.5 > 9; 86.7 % by volume
```

**Result: FAIL.** The charger board and any listed pack cannot share the
cavity, before the processor board is added.

### 4.2 Without a separate charger board

Assume the charger is on a carrier or on the processor board. Stack the
23.5 x 18 board over the pack.

```text
height: 4.5 (Jauch, after cycling) + board assembly <= 9
        so the board assembly, with insulation, must be <= 4.5
        with a 4.3 pack (Renata or PKCELL) it must be <= 4.7
motor beside the board, along the length: 32 - 23.5 = 8.5
  8 diameter motor, 8.1 maximum: 0.4 total clearance  - marginal
    (its lead-exit tab must point across the width, not along the length)
  10 diameter motor, 10.1 maximum: does not fit
motor height above the pack: 9 - 4.5 = 4.5 >= 3.5 for the 308-100
pack length: 27.0 to 27.5 of the 32 cavity, leaving 4.5 to 5.0 for the
  wire exit, connector and any charge receptacle (6.80 deep)
```

**Result: not excluded, not demonstrated.** It holds only if all of these are
true: no separate charger board; an 8 diameter motor; a processor board
whose assembled height is at most about 4.5; essentially zero clearance; and
a charge receptacle that fits a 5 remainder, which the 6.80 deep USB4125
does not. The Zero boards' assembled height is unknown, so this cannot be
closed on paper. Stacking the pack under the whole board also puts it under
the ceramic antenna, against Waveshare's guidance not to cover the antenna
(SRC-01, SRC-04; risk R-17).

**Keyfob conclusion: the 35 x 25 x 12 target is unproven and high risk.**
It is infeasible with a separate charger module and marginal at best
without one.

## 5. Alternatives for owner approval

None of these is adopted. Each changes a specified value or part.

| ID | Alternative | Effect | Cost or risk |
| --- | --- | --- | --- |
| M-1 | Enlarge the Pod to at least about 55 long, keeping 30 wide and the 10 separation | Removes the section 3.2 conflict for an end-to-end layout | Lower bound only; height and remaining parts still to be studied |
| M-2 | Keep 45 x 30 x 16 and accept a smaller NFC-to-pack separation for the ferrite-backed antenna, proven by read-range tests in the final case | The maker states the ferrite backing improves tolerance near conductive structures (SRC-43) | Changes a specified constraint; no numeric separation is documented; test evidence required first |
| M-3 | Keep the size and separation and use a smaller pack | A 402025-class pack is 27 long | Below the 200 mAh Pod minimum; discharge rating falls further below the transmit peak |
| M-4 | Accept a lower siren level with a smaller piezo | Frees most of the cavity width | Changes the 105 dB target; see shortlist section 5 |
| M-5 | Authorise a custom carrier PCB stage | Removes breakout-board volume in both units | New schematic, layout, RF and manufacturing obligations |
| M-6 | Enlarge the Keyfob | Removes dependence on zero clearance | Size to be derived after the board height is measured |

## 6. Evidence still needed

- Assembled height, USB-C overhang and underside clearance of a received
  Zero board of each type.
- Elechouse antenna thickness, outline tolerance, lead exit and the DWG
  contents; any maker statement on separation from a battery.
- Pack wire exit, connector and bend envelope for the selected pack.
- Piezo cavity and vent requirements for the selected part.
- A parametric layout study, in a later authorised stage, using maximum
  dimensions and real clearances.

## 7. Revision record

| Revision | Date | Change |
| --- | --- | --- |
| 0.3 | 2026-11-12 | First issue: packing screens for G1 candidates; both targets remain unproven; Pod target not achievable with candidates found |
| 0.4 | 2026-11-12 | Recorded O-01 Option A: Pod length direction enlarged to at least about 55 mm; no fit certification; full envelope remains TBD |
