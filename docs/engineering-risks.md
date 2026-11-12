# Dual-Auth Cafe Sentry - Engineering Risks and Conflicts

Revision: 0.3 | Date: 2026-11-12 | Status: open risk register; physical freeze blocked

This register covers the conflicts identified from the complete
[specification](../PROJECT_SPEC.md), manufacturer evidence and the
[design-basis package](architecture.md). It is not proof that an unbuilt design
has no other hazards.

All risks below are **OPEN**. Likelihood is not scored without evidence.
**Critical** means physical/electrical safety or destructive fault exposure;
**High** means major fit, functional, authentication or reliability impact;
**Medium** means integration/maintainability or incomplete release evidence.
EE = electrical; ME = mechanical; FW = embedded; MFG = manufacturing.
Gates are defined in the [roadmap](development-roadmap.md).

## 1. Electrical and power conflicts

| ID | Unit / priority | Conflict and consequence | Required mitigation / closure evidence | Owner / gate |
| --- | --- | --- | --- | --- |
| R-01 | Both / Critical | Zero USB VBUS is tied to the external 5 V pad. Direct LiPo connection can bypass charging when USB is inserted; external supply can also backfeed a USB port. | Approved complete source/isolation topology; all source combinations tested. Never treat a board's USB connector as a LiPo charger. D-03. | EE / G1-G2 |
| R-02 | Both / Critical | Charger/current/termination/temperature choices remain open. LP401730's 4.220 V charge limit is below cited MCP73831-2 4.232 V and TP4056 4.242 V maxima; TP4056 page 17 tolerance also conflicts with page 4. Generic 1 A or 0.5 C assumptions are unsafe. | Exact pairing and full tolerance/temperature analysis; manufacturer clarification of TP4056 conflict; charge/termination/inhibit measurements. See power architecture section 3. No reference pairing is approved. D-04/D-05/D-21. | EE, safety / G1-G2, G6 |
| R-03 | Both / Critical | Neither Zero board nor the bare charger IC provides complete pack discharge/short-circuit protection. Raw B- wiring can bypass low-side PCM FETs. | Qualified finished pack or separately reviewed protector, verified B/P terminals, current/threshold/recovery evidence. | EE / G1-G2 |
| R-04 | Both / Critical | Single-cell voltage can fall below Zero input guidance; unreviewed 3V3 feed can parallel/backfeed the onboard LDO. Brownouts can disable alarms. | Regulation over loaded cell range, approved board interface, startup/reset/off tests and rail transient measurements. D-03. | EE / G1-G2 |
| R-05 | Both / High | Charger BAT tied to a running load can corrupt charge termination; chip thermal regulation does not supervise cell temperature. | Separate charge-current/system-load paths or verified hardware load disconnection; temperature measurement at cell. D-04. | EE / G1-G2, G6 |
| R-06 | Pod / High | Generic PN532/GY-521 VCC, regulators and pull-ups are unknown. 3.3 V into an onboard LDO may undervolt the IC; 5 V pull-ups can damage logic. | Exact module schematics and supply/level-shift audit; effective pull-up/rise-time and power-off injection tests. D-06/D-20. | EE / G1-G2 |
| R-07 | Pod / High | PN532 0x48 address notation, board switch labels and RSTO/RSTPD_N names are easily confused. Wrong reset direction can cause contention. | 7-bit 0x24 host configuration, actual strap mapping/firmware response and pin-direction audit. NXP boot table and internal register encoding must not be interchanged. | EE, FW / G1-G2 |
| R-08 | Pod / High | A passive piezo, unspecified 2N2222 and 1 kohm resistor do not establish controlled AC drive, all musical tones or 105 dB at an undefined distance. | Exact transducer/driver, discharge/clamp network, waveform/thermal data and calibrated closed-case acoustics. Define hearing-safe test setup and actuation limits. D-07/D-18. | EE, ME, safety / G1-G2, G6 |
| R-09 | Keyfob / Critical | Raw LiPo/USB can overdrive a nominal 3 V motor. The Vybronics reference's specified start-current test is not a universal stall limit, and 1 s on/off life testing does not qualify continuous alert. | Select actual motor and rated rail; startup/stall, diode/driver, off-bias, thermal and continuous-duty qualification against the selected cell. | EE, ME / G1-G2, G6 |
| R-10 | Both / High | Siren/motor/LED/radio pulse currents can disturb I2C, IMU readings and RF or cause supply resets. | Short driver returns/local decoupling and verified routing; concurrent-load power, sensor and RF tests. Avoid arbitrary split grounds. | EE, FW / G2/G4/G6 |
| R-11 | Both / High | Board RGB rails/logic conflict with the Waveshare-linked LED sheet; white-strobe power/brightness and off-state leakage are unknown. | Confirm fitted LED revision/ratings or approved remedy, then measure logic margin, power and final-case visibility. D-16. | EE, supplier / G1-G2, G6 |
| R-12 | Both / High | C3 and S3 pin maps/straps differ. The revision 0.1 C3 USB pad pair was reversed and is corrected in revision 0.2; copies of the old table could miswire USB. | Use verified pinouts: C3 GPIO18/D- at contact 15, GPIO19/D+ at 16. Confirm received revision, reset/service pins and safe boot outputs. D-02/D-06/D-21. | EE, FW / G1-G2 |
| R-13 | Pod / Critical | A USB-C-form GPIO tether can receive USB power/ESD or wrong contacts in either orientation; a short bypasses static continuity. | Decide inclusion/form factor, complete protected cable/contact map, controlled open/short/charger-misconnection tests; never raw external GPIO. D-08. | EE, ME / G1-G2 |

## 2. Mechanical and cross-domain conflicts

| ID | Unit / priority | Conflict and consequence | Required mitigation / closure evidence | Owner / gate |
| --- | --- | --- | --- | --- |
| R-14 | Pod / High | Elechouse V3 publishes 42.7 x 40.4 and rounded 43 x 41 in plane, exceeding the Pod target width. No mechanical drawing was located, so these claims are drawing-unverified; actual module remains unselected. | Obtain exact module/antenna drawing or approve larger enclosure; use maximum assembly/RF dimensions, not IC size or marketing claims as fit certification. D-13/D-21. | ME, EE/RF / G1/G3 |
| R-15 | Pod / High | Reference battery 5.3 plus required NFC gap 10 exceeds the screened 13 internal height before NFC/PCB/support material. Lateral placement also has little/no gap-compliant space. | Keep >=10 requirement; redo packing with selected parts or obtain explicit architecture/size change. No silent ferrite exemption. | ME, EE/RF / G1/G3/G6 |
| R-16 | Keyfob / High | Both boards are 23.5 x 18; ideal cavity is 32 x 22 x 9. LP401730 L1 max 32 leaves no length margin; a 10.1 diameter reference motor beside the board needs 33.6 length or 28.1 width. These are conditional screens, not universal no-fit proofs. | Select real pack/motor; include adhesive, lead exit, ports, supports and full maximum Z stack; alternative placement and assembly trial required. Size remains TBD. | ME, EE / G1/G3/G6 |
| R-17 | Both / High | Ceramic antennas compete with battery, metal fasteners, keys/carabiner, piezo/motor, steel braid, carrier copper and enclosure material. | Vendor-compatible keepout/placement and final-case radio tests near real carried/attached objects; no assumed generic keepout number. | EE/RF, ME / G1/G3-G6 |
| R-18 | Pod / High | NFC RF field and acoustic/structural layout compete: metal piezo, battery, bosses or an overly thick lid detune/block reading. | Measured finished <=1.5 window, both >=10 separations, antenna/case/card matrix; include pigments, adhesive and engraving effects. | EE/RF, ME / G3/G6 |
| R-19 | Both / Critical | Unknown pouch seals, PCM, wiring, swelling or screw penetration can cause compression/puncture or service damage. | Finished-pack drawing and clearance requirements, smooth insulated restraint, no battery-as-spacer, safe removal and worst-case tolerances. | ME, EE / G1/G3/G6 |
| R-20 | Both / High | Native USB, charging USB and optional tether need different roles/possibly multiple openings. Socket-only cutouts omit plug shells, insertion travel and wire bends. | Freeze port count and power topology together; use mating-part drawings, retention/strain relief and access checks in both orientations. | ME, EE / G1/G3/G6 |
| R-21 | Both / High | Small bosses/loops, brittle or heat-sensitive unselected material, and PCB-only connector support may fail under drops/pulls. | Material/process qualification, structural load path and defined attachment/drop/retention tests; do not load thin NFC lid or cell. | ME, MFG / G1/G3/G6 |
| R-22 | Both / Critical | Linear-charger/driver heat in a small closed body can heat the cell or soften the enclosure. Vents do not establish cooling or ingress protection. | Final-case thermal budget and tests at allowed charge/alarm loads; material temperature limits and cell spacing. Define any ingress claim separately. | EE, ME, safety / G2/G3/G6 |
| R-23 | Both / Medium | Insufficient wire, fastener and tool clearance can make a visually fitting enclosure unassemblable or battery replacement destructive. | Assembly/removal sequence with actual harnesses, screw/connector access, no pinching and appropriate production tolerances. | ME, MFG / G3/G6 |

## 3. Functional, authentication and evidence conflicts

| ID | Unit / priority | Conflict and consequence | Required mitigation / closure evidence | Owner / gate |
| --- | --- | --- | --- | --- |
| R-24 | Pair / High | RSSI is not distance; body shadowing, orientation, interference and link loss invalidate a universal 4 m threshold or instantaneous return detection. | Final-case calibration, hysteresis/freshness policy, separate loss handling and approved false-event/latency criteria. D-09/D-18. | FW, RF / G1-G2/G6 |
| R-25 | Pair / High | Sleeping Keyfob misses unsolicited alarms; transport success is not application receipt. Continuous motor use conflicts with long runtime. | Coordinated wake/RX windows, retained alerts, application ACKs/retries, power measurement and explicit latency/duty/runtime limits. D-15. | FW, EE / G2/G6 |
| R-26 | Pod / High | 40/250 ms gives 84% ideal inactive time, not >80% measured current savings; PN532 wake/command overhead may miss taps or delay IMU samples. | Actual cycle charge/current and detection-latency measurements against a defined continuous reference; bounded shared-bus scheduling. | FW, EE / G2/G6 |
| R-27 | Pod / High | "Any 13.56 MHz card" overstates compatibility; UID may be unsupported, random, non-unique or cloneable. | Approved card/security scope, full-length comparisons, duplicate/full-store/card-removal behavior and real-card test matrix. D-10. | FW, project lead / G1-G2 |
| R-28 | Pod / High | Unrestricted 3 s learn/10 s reset or guessable/unlimited rhythm attempts can bypass intended authorization; one hold crosses both thresholds. | Approved privileged-operation/recovery policy, mutually controlled gesture parser, attempt limits and recessed-button trials. D-11. | FW, project lead / G1-G2/G6 |
| R-29 | Pair / High | Undefined mute/panic, force-lock warning/siren origin, missing-beacon and reboot transitions can produce unintended disarm or nuisance alarms. | Approved complete state/command/fault table; preserve arm origin; boundary, race, stale-packet and interrupted-power tests. D-12. | FW / G1-G2/G6 |
| R-30 | Pod / High | MPU-6050 has no absolute yaw reference; uncalibrated fusion and unspecified sustained-motion metric can create false alarms. GY-521 identity and MPU lifecycle add sourcing uncertainty. | Gravity-referenced tilt, verified sampling/filtering/calibration and failure handling; genuine module/lifecycle confirmation. D-17. | EE, FW / G1-G2/G6 |
| R-31 | Both / High | Accessible power switch, battery exhaustion or reset can defeat an alarm regardless of radio/NFC checks. | Approved guarded access and armed-state retention/recovery policy; low-battery notification and power-loss tests. D-19. | ME, EE, FW / G1-G2/G6 |
| R-32 | Both / High | Generic component labels, IC-only dimensions, supplier document inconsistencies and missing tolerances can yield wrong footprints or unsafe substitutions. | Exact manufacturer/revision/MPN, schematic-to-footprint audit, physical inspection and review of all register TBDs. D-20. | EE, ME, MFG / G1-G4 |
| R-33 | System / Medium | Unspecified SPL conditions, runtime, latency, environmental loads and acceptance rates prevent objective verification. Documentation may be mistaken for fabrication readiness. | Freeze measurable criteria; maintain reports and sign-offs. No ERC/DRC/CAD or hardware pass claim before those activities occur. D-18/D-01. | Lead, all disciplines / G1-G7 |

## 4. Risks added by G1 candidate research

Evidence is in the [component shortlist](g1-component-shortlist.md),
[compatibility matrix](g1-battery-charger-compatibility.md),
[power recommendation](g1-power-architecture-recommendation.md) and
[mechanical feasibility](g1-mechanical-feasibility.md). Owner decision IDs
(O-nn) are in [owner decisions](g1-owner-decisions.md).

| ID | Unit / priority | Conflict and consequence | Required mitigation / closure evidence | Owner / gate |
| --- | --- | --- | --- | --- |
| R-34 | Both / Critical | Documented radio transmit peaks are 340 mA (S3) and 335 mA (C3). Every 150 to 200 mAh pack examined, and the Jauch 250 mAh pack, states a discharge limit below that peak (150 to 310 mA). Pod worst case from documents is 430 to 494 mA. Consequences: rail sag and reset during an alarm, protector trips, cell stress. | Pack makers' written pulse-discharge ratings; measured cell current during ESP-NOW transmit at the intended power; reviewed transmit-power limit and bulk capacitance, or a higher-rate cell. No battery-powered radio test before review. O-11. | EE, FW, safety / G1-G2 |
| R-35 | Pod / High | With the smallest documented PN532 antenna (10 x 25) and a 200 to 250 mAh pack, the specified 10 mm separation does not fit inside 45 x 30 x 16 in any axis-aligned placement tested. The three requirements cannot all be met as written. | Owner decision O-01. If a smaller separation is considered, in-case read-range evidence with a ferrite-backed antenna comes first. No silent reduction. | ME, EE/RF, lead / G1 |
| R-36 | Both / High | A mirrored data sheet for the regulator named on the Zero schematics forbids VOUT above VIN + 0.3 V, so external 3.3 V into the 3V3 pad is not acceptable on an unmodified board unless the canonical sheet says otherwise. Powering the 5 V pad from the battery instead energises the native USB-C VBUS pins; a USB-C source may refuse to start, and the pins are exposed. | Canonical ME6217 data and received-board leakage measurement; native port made service-only or enclosed; tested source behaviour with a pre-biased VBUS in all source combinations. O-09. | EE / G1-G2 |
| R-37 | Both / Critical | Purchasable charger boards examined default to 1 A and cannot be set below 250 mA (bq25185 board) or 500 mA (bq24074 board) by jumper. Candidate packs allow 125 to 250 mA at most (30 mA below +15 deg C for one). Only the Renata 250 mAh pack's 250 mA maximum equals the lowest setting, with no margin for the charger's +/-10 % current accuracy; every other pack is exceeded. Only one candidate pack includes an NTC. | No charger board connected to a candidate pack as supplied. Charge current, voltage and temperature window set, reviewed and measured on a dummy load before any cell is attached. O-02. | EE, safety / G1-G2 |
| R-38 | Both / Medium | Several candidates have supply or lifecycle exposure: Adafruit 3886 and 6091 out of stock on 2026-11-12; MPU-6050 reported obsolete, Renata packs non-stocked with long lead times, one Murata piezo end-of-life and P2N2222AG obsolete (all unverified leads). | Owner-confirmed sourcing and lifecycle for each part before freeze; second source where practical. O-04, O-11. | Sourcing, lead / G1 |
| R-39 | System / Medium | Research documents cannot be republished, so the repository holds hashes and URLs only. Local copies and the validation script exist on one machine. URLs may change. | Keep [SHA256SUMS](datasheets/SHA256SUMS) current; re-download and compare before relying on a value; owner decision on a backed-up private store. O-15. | Documentation / G1-G7 |

## 5. Release policy

Safety-critical unknowns block battery-powered testing and release of the
affected circuit. Use safe board-level USB/current-limited evaluation only
within applicable manufacturer guidance while those decisions are open.
Geometry-critical unknowns block a dimensional fit commitment.

For each closure, record the exact hardware revision, source/drawing, analysis
or measurement report, responsible reviewer and date. A generic datasheet link,
successful boot, rendered image or single card read is not closure evidence
for an entire subsystem. Retest after changes to cell, charger, actuator,
antenna location, enclosure material or firmware timing.

No PCB, battery assembly or fabrication service may be ordered automatically.
Explicit human approval is required for purchasing/fabrication and for any
specification change.

Revision 0.2 incorporates the [component evidence](datasheet-index.md) and
updates existing risks; none is closed by document inspection alone.

Revision 0.3 adds R-34 to R-39 from G1 candidate research. R-01 to R-33 are
unchanged and remain open. New evidence bearing on them: R-02 and R-05 (see
the compatibility matrix), R-08 (loudest verified piezo of 25 mm or less
documents 92 dB at 10 cm), R-14 and R-15 (a 25 x 16.4 module with a separate
10 x 25 antenna exists, but R-35 applies), R-16 (Keyfob screen), R-26 (the
candidate module's maker measured a 72 % reduction at 4 Hz polling, below the
80 % target, under its own polling scheme).
