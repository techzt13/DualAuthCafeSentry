# G1 Decisions Requiring Owner Approval

Revision: 0.4 | Date: 2026-11-12 | Status: PARTIALLY DECIDED; O-01 recorded, O-02 to O-15 remain open

Each item is a choice the project owner must make before the component
freeze can proceed. O-01 has been decided by the owner as recorded below;
O-02 to O-15 remain open. Recommendations are engineering preferences on
the documents in the [datasheet index](datasheet-index.md), not approvals.
Existing decisions D-01 to D-22 are in the
[decision log](design-decisions.md).

Detail: [component shortlist](g1-component-shortlist.md),
[compatibility matrix](g1-battery-charger-compatibility.md),
[power recommendation](g1-power-architecture-recommendation.md),
[mechanical feasibility](g1-mechanical-feasibility.md).

## 1. Decisions that change the specification

| ID | Decision needed | Why it cannot be avoided | Options | Recommendation | Related |
| --- | --- | --- | --- | --- | --- |
| O-01 | Sentry Pod size, NFC separation or battery size | With the smallest documented PN532 antenna (10 x 25) and a 200 to 250 mAh pack, the 10 mm separation does not fit inside 45 x 30 x 16 in any axis-aligned placement tested | (a) Enlarge the Pod to at least about 55 long; (b) keep the size and allow a smaller separation for a ferrite-backed antenna, proven by test first; (c) keep size and separation with a pack below 200 mAh | **OWNER DECISION: Option (a) selected.** Enlarge the Pod; retain the 10 mm separation and 200–250 mAh capacity target. Approximately 55 mm is a lower bound only, not a final dimension or fit approval. | D-13, R-15, R-35 |
| O-02 | Charger IC family | Neither specified family (MCP73831, TP4056) keeps its maximum at or below 4.200 V, and neither has both a power path and a cell-temperature input. Five of seven packs state no tolerance above 4.2 V | (a) Approve a power-path charger such as TI BQ25185 at its 4.1 V setting; (b) keep MCP73831 and obtain each pack maker's written charge-voltage tolerance, with separate temperature and load-disconnect circuits; (c) keep TP4056 after resolving its internal tolerance conflict | (a) | D-04, R-02, R-05 |
| O-03 | Sound level target and piezo driver | No externally driven piezo of 25 mm or less was found that documents 105 dB; the loudest verified part is 92 dB at 10 cm and 24 mm in diameter; the specified single-transistor driver cannot reach that part's rated drive voltage | (a) Define the 105 dB distance and accept a boosted driver and a 24 mm part; (b) lower the target to what a smaller part documents; (c) approve a self-driven sounder or a larger body | Define the measuring distance first (D-18), then choose between (a) and (b) with measured data | D-07, D-18, R-08 |
| O-04 | IMU module and lifecycle | "GY-521" names no maker; the identifiable Adafruit 3886 was out of stock; MPU-6050 is reported obsolete by its maker (unverified lead) | (a) Approve Adafruit 3886 as the MPU-6050 module; (b) accept an unbranded GY-521 and measure every received board; (c) approve evaluation of a current-production IMU, which changes the specified part and firmware | (a) for the prototype, with (c) raised as a supply risk for anything beyond it | D-17, R-30 |
| O-05 | Piezo driver IC | A boosted driver such as Diodes PAM8904 replaces the specified 2N2222 and 1 kohm arrangement | (a) Approve evaluation of a boosted driver; (b) keep the transistor driver and accept the resulting level | Decide together with O-03 | D-07 |
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
