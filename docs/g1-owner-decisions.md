# G1 Decisions Requiring Owner Approval

Revision: 0.6 | Date: 2026-11-12 | Status: PARTIALLY DECIDED; O-01 and O-02 recorded; O-03/O-05 evaluation direction recorded; O-04 and O-06 to O-15 remain open

Each item is a choice the project owner must make before the component
freeze can proceed. O-01 and O-02 have been decided by the owner as recorded below;
O-03/O-05 have an evaluation direction only; O-04 and O-06 to O-15 remain open. Recommendations are engineering preferences on
the documents in the [datasheet index](datasheet-index.md), not approvals.
Existing decisions D-01 to D-22 are in the
[decision log](design-decisions.md).

Detail: [component shortlist](g1-component-shortlist.md),
[compatibility matrix](g1-battery-charger-compatibility.md),
[power recommendation](g1-power-architecture-recommendation.md),
[mechanical feasibility](g1-mechanical-feasibility.md),
[piezo/driver compatibility investigation](g1-piezo-driver-compatibility.md).

## 1. Decisions that change the specification

| ID | Decision needed | Why it cannot be avoided | Options | Recommendation | Related |
| --- | --- | --- | --- | --- | --- |
| O-01 | Sentry Pod size, NFC separation or battery size | With the smallest documented PN532 antenna (10 x 25) and a 200 to 250 mAh pack, the 10 mm separation does not fit inside 45 x 30 x 16 in any axis-aligned placement tested | (a) Enlarge the Pod to at least about 55 long; (b) keep the size and allow a smaller separation for a ferrite-backed antenna, proven by test first; (c) keep size and separation with a pack below 200 mAh | **OWNER DECISION: Option (a) selected.** Enlarge the Pod; retain the 10 mm separation and 200–250 mAh capacity target. Approximately 55 mm is a lower bound only, not a final dimension or fit approval. | D-13, R-15, R-35 |
| O-02 | Charger IC family | Neither specified family (MCP73831, TP4056) keeps its maximum at or below 4.200 V, and neither has both a power path and a cell-temperature input. Five of seven packs state no tolerance above 4.2 V | (a) Approve a power-path charger such as TI BQ25185 at its 4.1 V setting; (b) keep MCP73831 and obtain each pack maker's written charge-voltage tolerance, with separate temperature and load-disconnect circuits; (c) keep TP4056 after resolving its internal tolerance conflict | **OWNER DECISION: Option (a) selected for further evaluation only.** Evaluate TI BQ25185 at its 4.1 V setting; this does not approve a battery pairing, circuit, purchase, construction or connection to a cell. | D-04, R-02, R-05 |
| O-03 | Sound level target and piezo driver | No externally driven piezo of 25 mm or less was found that documents 105 dB; the 24 mm reference candidate is documented at 92 dB at 10 cm; the specified single-transistor driver does not establish the required drive | (a) Define 105 dB at 10 cm and evaluate a boosted driver with a 24 mm part; (b) lower the target to documented/measured performance; (c) evaluate a self-driven sounder or larger body | **OWNER DIRECTION: Option A for evaluation only.** Use 10 cm as the proposed measurement distance; retain the 24 mm reference piezo and investigate a compatible boosted driver. Weighting, level statistic, duration, waveform and achieved SPL remain open; no component is selected. | D-07, D-18, R-08 |
| O-04 | IMU module and lifecycle | "GY-521" names no maker; the identifiable Adafruit 3886 was out of stock; MPU-6050 is reported obsolete by its maker (unverified lead) | (a) Approve Adafruit 3886 as the MPU-6050 module; (b) accept an unbranded GY-521 and measure every received board; (c) approve evaluation of a current-production IMU, which changes the specified part and firmware | (a) for the prototype, with (c) raised as a supply risk for anything beyond it | D-17, R-30 |
| O-05 | Piezo driver IC | A boosted driver replaces the specified 2N2222 and 1 kohm arrangement; the PAM8904's documented 15 nF load limit is below the CPT-2475-92T's nominal 21 nF capacitance | (a) Evaluate a boosted driver compatible with the selected piezo; (b) retain the transistor driver and accept its measured level | **OWNER DIRECTION: Option A for evaluation only**, jointly with O-03. PAM8904 is not a qualified match (15 nF limit). PAM8904E is the only integrated driver found so far with a documented 47 nF load rating; it remains a research candidate only pending confirmation of output drive, transducer compatibility, current, thermal and EMI behaviour. See [piezo/driver compatibility investigation](g1-piezo-driver-compatibility.md) and [prepared manufacturer questions](g1-piezo-manufacturer-questions.md). | D-07 |
| O-06 | Keyfob size or construction | The 35 x 25 x 12 target fails with any separate charger board and is marginal without one | (a) Authorise a custom carrier PCB stage; (b) enlarge the Keyfob; (c) both | (c), after a Zero board's assembled height has been measured | D-13, R-16 |
| O-07 | Battery capacity ranges | The best-documented Pod pack is 240 mAh minimum, 17 wide (not "502030"); the best-documented Keyfob pack is 150 / 155 mAh; the only pack with an NTC is 205 / 215 mAh and 37 long | Confirm whether the named 502030 size and the 150 to 200 mAh range are requirements or guidance | Treat them as capacity requirements and let the pack shape follow evidence | D-05 |

## 1.1 Owner decision recorded — O-01 (2026-11-12)

The owner selected **Option A: enlarge the Sentry Pod**. The design direction is
to increase external length from 45 mm to **at least approximately 55 mm**,
while retaining the 30 mm width and 16 mm height as provisional targets, the
10 mm antenna-to-pack separation, and the 200–250 mAh battery-capacity target.

This is a specification direction, not a finished enclosure dimension or a
fit certification. The 55 mm figure is a calculated lower bound for one
arrangement before all other parts, clearances, walls, antenna thickness,
wires, connectors and acoustic requirements are accommodated. Width and
height remain provisional and must be re-screened. No component is selected
or frozen; no purchase, CAD, PCB or battery test is authorised by this choice.

**Consequences:** the original 45 mm Pod length is no longer the working
length target; subsequent mechanical screening should start at 55 mm or more.
The 10 mm separation and capacity target are retained rather than relaxed.
The Pod may need to grow further once the piezo, processor, IMU, NFC board,
connectors and real clearances are included.

## 1.2 Owner decision recorded — O-02 (2026-11-12)

The owner selected **Option A for further evaluation**: investigate the TI
BQ25185 configured for its 4.1 V setting as the preferred charger-IC family.
This is an evaluation direction only. It is not approval of a specific battery,
charger implementation, power-path architecture, carrier PCB, charging
current, NTC network or component pairing.

**Explicit limits of this decision:** no purchase or supplier order is
authorised; no schematic, PCB or carrier design is authorised; no circuit may
be built; and no battery may be connected to a charger or test setup under
this decision. Independent electrical review and the evidence listed below
remain mandatory before any battery-powered test.

**Consequences and remaining checks:**

- Obtain the exact BQ25185 datasheet and inspect its package, strap/configuration
details, 4.1 V regulation tolerance, input limits, power-path behaviour,
thermal limits and NTC/fault behaviour.
- Confirm the exact candidate battery's permitted charge voltage and current
in writing; the 4.1205 V figure is a charger-document maximum, not proof of
compatibility with every pack whose datasheet merely says “4.2 V”.
- Establish the correct charge-current setting for the chosen pack and its
temperature restrictions; no battery has yet been paired with this IC.
- Resolve USB-C VBUS backfeed/isolation, the Zero-board regulator and system
load behaviour while charging before any power architecture can be approved.
- Recalculate charger dissipation and closed-case temperatures with actual
currents and enclosure conditions.

O-02 is recorded as an owner direction to evaluate the BQ25185. D-04, the
power architecture, all battery/charger pairings and the physical component
freeze remain OPEN or NOT APPROVED as applicable.

## 1.3 Owner direction recorded — O-03/O-05 (2026-11-12)

The owner chose **Direction A for evaluation only**: retain the 24 mm
Same Sky CPT-2475-92T as the reference piezo candidate and investigate a
boosted driver that is electrically compatible with that transducer and can
produce the required 2.8–4.2 kHz sweep. The proposed SPL measurement distance
is **10 cm**. This is not final approval of the 105 dB target, its measurement
method, the piezo, a driver IC, a circuit or a component pairing.

The CPT-2475-92T is documented at 92 dB at 10 cm, rated at 10 Vp-p and
nominally 21 nF. It is not documented as achieving 105 dB. The Diodes PAM8904
is a research lead only: its manufacturer specifies a maximum 15 nF load,
below the piezo's nominal 21 nF. Do not assume this driver can operate that
piezo; obtain written manufacturer confirmation or investigate a different
driver. No voltage increase may be inferred to produce a predictable SPL
increase.

**Required technical checks before any component selection:**

1. Confirm the piezo's full datasheet conditions, capacitance tolerance,
   voltage limits, frequency response and permitted drive waveform across
   2.8–4.2 kHz; obtain manufacturer clarification on operation away from
   its 4 kHz rated point.
2. Screen boosted-driver candidates against the piezo's capacitance (including
   tolerance), supply range, output topology and peak-to-peak voltage,
   frequency/duty input limits, startup/shutdown behaviour, protection,
   package and external-component requirements. Resolve the PAM8904 load
   mismatch explicitly.
3. Calculate driver input current and battery peak demand at worst-case
   supply and alarm conditions; include boost losses, capacitor ripple,
   startup current and interaction with the processor/radio/NFC loads.
4. Check switching noise and EMI coupling into NFC, IMU, ESP-NOW and audio
   control; define grounding, routing, decoupling and any output clamp or
   protection only after the selected IC's application guidance is reviewed.
5. Define the acoustic acceptance method: dB weighting, peak versus average
   statistic, tone/sweep pattern, duty cycle, measurement tolerance,
   microphone orientation, distance reference point and final enclosure/
   mounting condition. D-18 remains OPEN.
6. Obtain evidence for the 105 dB target from the exact transducer/driver
   combination. Manufacturer-rated SPL or calibrated controlled testing is
   required; extrapolation from voltage or a different sounder is insufficient.
7. Assess piezo, driver and enclosure temperature at the maximum allowed
   alarm duration; define a safe alarm timeout and controlled acoustic test
   procedure before testing.
8. Recheck the 24 mm piezo, driver package, boost capacitors, acoustic port,
   lid and antenna keepouts in the enlarged Pod envelope. No CAD or circuit
   construction is authorised by this evaluation direction.

**Explicitly not authorised:** purchase, supplier order, schematic/PCB design,
circuit construction, battery connection, high-voltage piezo testing or
acoustic exposure testing. Any later physical test requires the relevant
authorisation, independent electrical review and controlled hearing-safety
arrangements. O-03 and O-05 remain OPEN; G1 physical component freeze remains
BLOCKED.

## 2. Decisions within the specification

| ID | Decision needed | Options | Recommendation | Related |
| --- | --- | --- | --- | --- |
| O-08 | NFC module | Elechouse PN5321 MINI (SKU NFC_EX_MINI) with the 10 x 25 antenna, or another PN532 module with evidence | PN5321 MINI. It removes the proposed IRQ connection and requires polling | D-06, R-06 |
| O-09 | Power architecture for the Zero boards | Option A, power-path charger feeding the 5 V pad through an ideal diode; Option B, charge only when switched off; Option C, a different processor board; Option D, board rework | Option A for evaluation. It leaves the native USB-C VBUS pins energised from the battery, so the native port must be service-only or enclosed | D-03, D-04, R-01, R-36 |
| O-10 | Behaviour while charging | Must the Pod be able to alarm while it is charging? | Yes; this is what makes a power path necessary. If no, Option B becomes viable | D-04, D-19 |
| O-11 | Battery supplier | Pod: Renata ICP521630PM-01 or Jauch LP502030JH+PCM. Keyfob: Renata ICP402025PC-01 or Jauch LP402025JU+PCM | Renata for both, subject to the supplier confirming pulse-discharge capability, charge-voltage tolerance and protection thresholds in writing | D-05, R-34 |
| O-12 | Keyfob processor | ESP32-C3-Zero or ESP32-S3-Zero | Keep C3 as the proposed option; decide after measuring both boards' sleep and beacon current | D-02 |
| O-13 | Keyfob motor | 8 mm Precision Microdrives 308-100, or a 10 mm part if the Keyfob is enlarged | 308-100 for the current target | R-09 |
| O-14 | Battery connector | JST PH (2 mm) or JST SH (1 mm), and which side carries the plug | PH for the Pod, SH for the Keyfob; note AWG26 pack wires do not fit SH contacts | R-19 |
| O-15 | Use of datasheets in the public repository | Keep documents local with hashes, or seek written permission to publish specific ones | Keep local. See the [evidence folder](datasheets/README.md) | D-22 |

## 3. Authorisations needed before further work

| ID | Authorisation | Blocks |
| --- | --- | --- |
| A-1 | Purchase of evaluation samples: one of each recommended pack, the NFC module, an IMU module, the piezo, both motors and both Zero boards. Nothing has been ordered | All measurements in section 4 |
| A-2 | Written enquiries to Jauch, Renata, Elechouse, Waveshare and Top Power in the owner's name | Charge-voltage tolerance, pulse discharge, schematics, regulator identity, TP4056 tolerance |
| A-3 | Start of a schematic and carrier-PCB stage | Any charger other than a module; O-06 |
| A-4 | Independent electrical review of the battery, charger and power-path proposal | Any battery-powered test |

## 4. Evidence that would close the open questions

1. Pack makers' written statements of permitted charge voltage tolerance and
   pulse or peak discharge current.
2. Measured battery current during ESP-NOW transmit at the intended power.
3. Measured capacity of each candidate pack charged to 4.1 V.
4. Received Zero board revision, assembled height, and regulator marking.
5. Elechouse schematic or a measured supply and pull-up audit of a received
   module; contents of the maker's DWG drawing; antenna thickness.
6. NFC read distance through a 1.5 lid with the pack at 10, 7 and 5 from the
   ferrite-backed antenna, if option O-01(b) is to be considered.
7. Calibrated sound level of the candidate piezo at a defined distance and
   drive voltage across 2.8 to 4.2 kHz.
8. TDK's current MPU-6050 lifecycle statement from a source the owner can
   access.

## 5. Revision record

| Revision | Date | Change |
| --- | --- | --- |
| 0.3 | 2026-11-12 | First issue: fifteen owner decisions and four authorisations arising from G1 candidate research |
| 0.4 | 2026-11-12 | Recorded owner approval of O-01 Option A only; O-02 to O-15 and A-1 to A-4 remain open |
| 0.5 | 2026-11-12 | Recorded O-02 Option A as BQ25185 4.1 V evaluation direction only; no purchase, design, build or battery connection authorised |
| 0.6 | 2026-11-12 | Recorded O-03/O-05 Direction A for evaluation only and 10 cm as proposed SPL distance; no piezo/driver selection or physical test authorised |
| 0.7 | 2026-11-12 | Added PAM8904E as a promising boosted-driver research candidate; created compatibility report; no component selected or test authorised |
| 0.8 | 2026-11-12 | Expanded driver evaluation after full PAM8904E datasheet and EVB review; PAM8904E remains evaluation-only; no selection or test authorised |
