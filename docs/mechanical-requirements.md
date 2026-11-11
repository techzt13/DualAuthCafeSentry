# Dual-Auth Cafe Sentry - Mechanical Requirements

Revision: 0.1 | Date: 2026-11-11 | Status: packaging requirements and feasibility screen

All dimensions are in **millimetres**. This is not a CAD model, tolerance
release or fit certification. Future models must be native, parametric FreeCAD
documents with editable sketches/features and named parameters, plus STEP/STL
exports as required by [AGENTS.md](../AGENTS.md).

## 1. Baseline and dimensional status

| Requirement | Sentry Pod | Pocket Keyfob | Status |
| --- | --- | --- | --- |
| Proposed outside size | Approximately 45 x 30 x 16 | Approximately 35 x 25 x 12 | S targets only; fit not demonstrated |
| Body/lid | Two-tone industrial finish, matte dark charcoal or frosted/translucent body, flat NFC-marked lid | Coordinated industrial appearance proposed | Pod aesthetic S; Keyfob implementation P |
| NFC window wall | <=1.5 directly over antenna coil | Not applicable | S; preserve after engraving, finish and manufacturing variation |
| Battery-to-NFC separation | >=10 | Not applicable | S, not a manufacturer-certified RF allowance |
| Piezo-to-NFC separation | >=10 | Not applicable | S, same limitation |
| Acoustic access | Vent directly over piezo | No acoustic transducer specified | S |
| Attachment | Reinforced top carabiner loop | Keyring retention feature proposed | Pod S; Keyfob detail P |

**P screening assumption:** the target dimensions describe the closed main
body. Whether protruding loops, switch actuators and connector plugs are
included in those targets is TBD. Record body and complete assembly envelopes
separately before freezing a size.

The requested NFC separations are provisionally applied to the **nearest
surfaces**, conservatively excluding the entire antenna-loop bounding region,
not just a center-to-center distance. Interpretation and any change require
owner/RF review. Ferrite or a successful isolated bench read is not automatic
permission to remove the 10 mm constraint.

## 2. Verified outlines versus unverified envelopes

| Component / comparison | Verified manufacturer information | Still required |
| --- | --- | --- |
| Waveshare ESP32-S3-Zero | PCB outline 23.50 x 18.00; source drawing SRC-03 | Maximum assembled height above/below board, PCB thickness, USB overhang/centerline, solder envelope, keepout boundary and tolerance |
| Waveshare ESP32-C3-Zero | PCB outline 23.50 x 18.00; source drawing SRC-06 | Same outstanding assembly measurements; C3 is not a smaller PCB in plan view |
| GY-521 assembly | No unique manufacturer/revision identified | Complete outline, height, mounting holes, connector pitch/pin order, regulator/LED and tolerances |
| MPU-6050 IC | Nominal package 4 x 4 x 0.9, SRC-11 | This is **not** the GY-521 assembly envelope |
| Selected PN532 module/antenna | TBD | Board/coil boundaries, component heights, mounting holes, RF keepout and connector envelope |
| PN532 IC | Nominal 6 x 6 x 0.85 HVQFN40 body, SRC-09 | Cannot replace the module, antenna, crystal and matching network envelope |
| Elechouse PN532 V3, **reference only** | Guide states 42.7 x 40.4 x 4 and rounded 43 x 41 x 4, SRC-21 | Actual purchased revision, connectors, tolerances and exact drawing; not selected |
| Pod battery pack | 502030 is only a specification size description | Exact cell/PCM, seal and lead geometry, connector, thermistor, swelling allowance |
| EEMB LP502030 bare cell, **reference only** | Maximum stated cell dimensions 31 x 20.5 x 5.3, SRC-16 | Protection and finished-pack envelope; not selected |
| Keyfob battery pack | 150-200 mAh requirement only | All dimensions and construction TBD |
| Passive piezo | No exact part selected | Diameter/outline, thickness, lead/pad arrangement, support/seal land, acoustic cavity and vent requirements |
| Coin motor | No exact part selected | Diameter/outline, thickness, adhesive/pad, wire exit, vibration and retention requirements |
| Charger, regulators, protection, discrete drivers | Families/functions only | Full assembly/package envelopes, thermal lands, connector positions, footprint verification |
| Buttons, slide switches, connectors and fasteners | No fully qualified mechanical parts | Supplier drawings, tolerances, actuator/mating travel, mounting and service clearance |

The [component register](component-register.csv) is the part-by-part open-item
list. A verified X/Y outline does not mean a part has a verified Z envelope or
approved footprint.

<a id="feasibility"></a>
## 3. Original target size feasibility

### 3.1 Explicit screening assumptions

For arithmetic only, assume 1.5 mm side walls, 1.5 mm base and a 1.5 mm lid.
These are **P screening values**, not selected structural wall thicknesses.
The lid value is at the specification's maximum over the NFC zone; final
nominal thickness must include the manufacturing/finish tolerance budget.

| Calculation | Pod | Keyfob |
| --- | --- | --- |
| External target | 45 x 30 x 16 | 35 x 25 x 12 |
| Ideal rectangular internal space | 42 x 27 x 13 | 32 x 22 x 9 |
| External box volume | 21,600 mm3 | 10,500 mm3 |
| Ideal internal box volume | 14,742 mm3 | 6,336 mm3 |

These internal boxes exclude bosses, corner radii, lid joints, ribs, fasteners,
adhesives, solder, wiring, connector travel and clearances. Their volumes are
upper-bound empty cavities, not usable component packing volumes.

### 3.2 Pod: module width fails for the documented example

The unselected Elechouse V3 module's smaller published in-plane dimension is
40.4 mm. That exceeds both the 30 mm outside target width and the 27 mm
screened inside width. Its larger dimension, 42.7 mm, also exceeds the 42 mm
screened inside length. Rotating it within the lid plane does not solve the
width problem. It cannot be assumed to fit flat under this lid.

This is a rejection of that **reference module / target combination**, not
proof that every possible custom PN532 antenna has the same size. The actual
module has not been selected. Do not scale a breakout drawing or substitute
the 6 mm IC body for the complete NFC assembly.

### 3.3 Pod: battery separation conflicts with conventional stacking

For the EEMB bare-cell reference stacked directly below the antenna region,
using its stated maximum body thickness:

```text
minimum vertical allocation before antenna/PCB/support/wire thickness
    = battery body 5.3 + specified separation 10
    = 15.3
screened internal height = 13
```

Thus this arrangement already exceeds the internal height by 2.3 mm.
With the assumed lid/base alone, the corresponding external-height lower
bound is **18.3 mm**, still excluding other components and clearances.
That is a conditional lower bound, **not a recommended finished enclosure size**.

For simple axis-aligned side-by-side placement of that cell and an NFC region:

```text
remaining length after battery and 10 mm gap = 42 - 31 - 10 = 1
remaining width after battery and 10 mm gap  = 27 - 20.5 - 10 = -3.5
```

These particular layouts leave no credible NFC-module region. Other geometries,
different verified cells or a larger enclosure require a new placement study;
this arithmetic is not a proof about every conceivable three-dimensional
arrangement. The piezo's independent 10 mm NFC separation further constrains
the design.

Even before NFC is included, the reference cell and 23.5 x 18 MCU board need
stacking or a different arrangement in a 42 x 27 cavity: their unrotated
side-by-side spans are 54.5 in length or 38.5 in width. Wiring and component
heights cannot be treated as zero.

**Pod conclusion:** the target is not validated and is incompatible with the
documented reference module; the common antenna-over-battery stack also fails
the specified separation under the stated assumptions. Expect either a
different verified component strategy or an owner-approved size revision.
Do not reduce NFC separation silently to preserve the advertised dimensions.

### 3.4 Keyfob: plausible outline alone does not establish fit

The C3 and S3 Zero boards have the same verified 23.5 x 18 outline. In a
32 x 22 ideal cavity, that leaves only 8.5 mm along the length and 4 mm along
the width for an aligned board before supports and plugs; the remaining
plan-view area is `32*22 - 23.5*18 = 281 mm2`.

The 150-200 mAh battery, motor, charger/protector, regulator, button and switch
are unsized. Any stacked battery/board strategy must meet:

```text
assembled board/carrier height + finished battery thickness
    + insulation + clearances + any overlapping component height <= 9
```

Use an actual layer-by-layer stack, not a sum that omits underside solder or
double-counts/non-counts overlapping regions. A separate USB-C charger module,
the native board USB connector and the motor may dominate the residual
space. The Pod's 250 mAh comparison cell is not a compliant Keyfob battery
selection.

**Keyfob conclusion:** the bare board fits in plan view; the complete
35 x 25 x 12 assembly remains **TBD**, with high risk from Z stack, ports,
motor mounting and battery leads. C3 selection alone does not solve packaging.

### 3.5 Options requiring review, not automatic changes

1. Keep verified modules and increase the body size after an actual envelope
   study; retain all required RF and service clearances.
2. Select a smaller documented reader/antenna and a qualified battery within
   the specified capacity range. Verify RF performance in the assembled case.
3. Consider an integrated custom PCB instead of stacked breakout boards only
   in a later authorized design stage; this adds RF, component sourcing and
   manufacturing obligations.
4. If proposing a smaller cell, reduced sound pressure, altered NFC separation
   or removal/change of the tether, record it as a specification change with
   owner approval. None is adopted by this package.

## 4. Proposed enclosure architecture

### 4.1 Sentry Pod

- Serviceable base with supported electronics and a separate flat removable
  lid. Evaluate screws into suitable bosses/inserts; fastener family, count,
  torque, thread engagement and material are TBD.
- Locate the NFC antenna parallel to the marked tap face. No fasteners, ribs,
  battery, piezo, cable braid or conductive finish may intrude into the approved
  antenna exclusion region. Keep the finished wall <=1.5 mm over the coil.
- Support a custom carrier or actual module mounting features rather than
  drilling arbitrary holes in a Zero board. Castellated pads are electrical
  connections, not automatically structural screw holes.
- Restrain the battery in a smooth, insulated compartment with supplier-approved
  clearance. Do not compress, fold, puncture or use the cell as a spacer under
  PCB screws. Provide removal access and lead strain relief.
- Position the piezo at a dedicated vent/cavity with manufacturer-correct
  mounting. Do not clamp the active diaphragm or put the cell in the acoustic
  path. Vent open area, cavity volume and sealing land are TBD.
- Reinforce the carabiner load path into the base structure rather than relying
  on a thin lid or small cosmetic tab. Attachment load, drop/pull test criteria
  and compatible clip sizes are TBD.
- Provide a guarded side-button interface permitting a 3 s/10 s hold and the
  rhythm gesture without accidental pocket/bag actuation. Single-button travel
  and ergonomic requirements must match the selected switch.
- Charging, programming and tether access must remain distinct and legible.
  Port count is unresolved; reserve actual mating-plug and strain-relief
  volumes rather than just holes the size of the sockets.

### 4.2 Pocket Keyfob

- Removable base/lid with supported board, battery restraint and keyed internal
  wiring; coordinated appearance without assuming identical internal geometry.
- Couple the coin motor to a suitable case surface using its qualified mounting
  method. Avoid loading the cell, rubbing wires or placing the motor against
  the radio antenna.
- Place the user button where deliberate operation is possible but sustained
  accidental pocket presses are unlikely. Define whether/where a visual
  indicator is visible; its enclosure opening is P, not an added requirement.
- Locate USB access so a charging plug does not collide with the keyring,
  button, switch or user's grip. Native service USB and a separate charging
  connector cannot occupy the same physical opening without a designed
  integration.
- Provide a reinforced keyring load path and guarded power-switch access.
  Final ring diameter, loads, fasteners and drop criteria remain TBD.

### 4.3 Material and process

Manufacturing process, resin/thermoplastic grade, wall/rib limits, UV resistance,
drop strength, heat performance, flammability and finish system are TBD.
Do not equate a translucent visual mockup with an adequate enclosure.

Evaluate the specified frosted/translucent appearance without conductive
coatings or pigments that compromise antennas. If an opaque structural base
and separate diffuser are proposed, document the appearance change for approval.
Acoustic vents and open ports preclude assuming an ingress rating. Any claimed
water/dust protection requires a defined target and test.

## 5. Placement and integration constraints

| Area | Placement requirement | Evidence needed before freeze |
| --- | --- | --- |
| 2.4 GHz radio, each unit | At a suitable perimeter region; avoid overlap by carrier copper/metal and nearby cell, braid, motor, piezo or screws | Waveshare advises not covering its ceramic antenna with boards, metal or plastic components; exact keepout dimensions remain TBD. Resolve casing proximity with vendor guidance and final-case RF tests. |
| NFC antenna | Parallel to thin tap window; separate from battery and piezo by specified >=10; no casual ferrite workaround | Antenna outline, plane and keepout drawing; coil tuning/current and supported-card tests |
| IMU | Rigid support, known axes, away from loose wiring and excessive board flex/acoustic coupling | Axis registration and mounted false-alarm measurements |
| Pod piezo | At matching vent/cavity, away from NFC; short driver current loop | Mechanical drawing and acoustic data under the chosen drive |
| Keyfob motor | Secure case coupling, isolated from cell pressure and antenna region | Mounting drawing, haptic strength and retention tests |
| Batteries | Smooth protected compartment; removable without prying against a pouch | Maximum finished dimensions, swelling allowance and replacement procedure |
| Charger/regulators/drivers | Heat spread paths away from cell; no boss over hot components | Closed-case thermal measurements at maximum allowed load/charge |
| USB and tether | Mechanical load carried by case/retention, not only solder joints | Socket/plug drawings, insertion depth, bend radius and retention |
| Buttons/switches | Correct actuator direction, travel and overtravel stop | Tolerance stack and actual component actuation test |
| RGB | Diffuser/light path clear of metal and obstructing components | Brightness, color visibility, current and rail compatibility |
| Bosses/fasteners | Outside components, antenna regions, battery and wire channels | Screw penetration/torque study and assembly clearance |
| Harnesses | Short, secured routes avoiding pinch points, sharp edges and moving controls | Lead lengths, minimum bend radii, connector retention and polarity inspection |

## 6. Required future parametric model inputs

| Parameter group | Current value / status |
| --- | --- |
| `Pod_L_target`, `Pod_W_target`, `Pod_H_target` | 45, 30, 16; S target only |
| `Keyfob_L_target`, `Keyfob_W_target`, `Keyfob_H_target` | 35, 25, 12; S target only |
| `NFC_window_finished_max` | 1.5; S |
| `NFC_battery_gap_min`, `NFC_piezo_gap_min` | 10, 10; S, conservative nearest-surface interpretation pending approval |
| Side/base/lid nominal walls and tolerances | TBD; 1.5 was used only for the feasibility screen |
| PCB X/Y/Z, hole coordinates and component envelopes | TBD from received boards/drawings; no inferred mounting holes |
| Cell, PCM, insulation and expansion envelopes | TBD from exact pack manufacturer |
| Antenna location/keepout and cable routing | TBD jointly with PCB placement |
| USB centers, plug envelopes and insertion clearance | TBD per selected connector/board |
| Button, switch, vent and attachment geometry | TBD from selected parts and user/mechanical requirements |
| Boss, fastener, joint, gasket and service allowances | TBD from process, material and tolerance analysis |

Use explicit origin/axis conventions in future PCB and FreeCAD models. Match
hole coordinates, antenna planes, board tops and USB datums across tools.
Tolerance analysis must include minimum cavity dimensions and maximum component,
solder and hardware dimensions, not only nominal no-interference checks.

## 7. Assembly, removal and verification

Proposed sequence: inspect base and inserts; install mechanically retained
electronics; route/test harnesses; mount piezo or motor; install insulated
protected battery without compression; connect keyed power last; inspect
pinch/clearance points; fit lid; perform control/port/functional checks.
Confirm the real sequence after connectors and mounting features are selected.

Require reversible battery/electronics removal using ordinary service tools.
Do not entrap the battery with permanent adhesive, inaccessible connectors or
a lid that requires destructive prying. Model tool access and screw removal,
not just final solid-body fit.

Future validation must cover:

1. Source-controlled component envelope drawings and actual dimensional inspection.
2. Parametric model recompute, closed solids, interference and worst-case
   clearance reports for both units and the integrated assembly.
3. PCB/module dimensions, heights, mounting features and USB alignment.
4. Finished NFC window thickness and minimum battery/piezo separation.
5. Plug/button/switch access, harness routing, assembly and removal trials.
6. Case strength, attachment, drop/retention, thermal and battery-clearance tests
   against criteria established before testing.
7. Final-case NFC, ESP-NOW, motion, acoustic and haptic tests with the intended
   nearby bag/laptop/keys, not an empty plastic enclosure alone.

Current result: dimensional arithmetic and source review only. No CAD
interference check, tolerance simulation, physical fit test or manufacturing
approval has been performed.
