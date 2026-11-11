# Dual-Auth Cafe Sentry - Engineering Risks and Conflicts

Revision: 0.1 | Date: 2026-11-11 | Status: open risk register

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
| R-02 | Both / Critical | Charger current, voltage suffix, termination and cell temperature limits are unselected. Generic 1 A settings greatly exceed plausible small-cell limits; even 0.5 C is not universally permitted. | Exact cell/charger pairing, worst-case tolerance analysis, temperature-inhibit circuit and measured charge/termination. EEMB comparison is not an approval. D-04/D-05. | EE, safety / G1-G2, G6 |
| R-03 | Both / Critical | Neither Zero board nor the bare charger IC provides complete pack discharge/short-circuit protection. Raw B- wiring can bypass low-side PCM FETs. | Qualified finished pack or separately reviewed protector, verified B/P terminals, current/threshold/recovery evidence. | EE / G1-G2 |
| R-04 | Both / Critical | Single-cell voltage can fall below Zero input guidance; unreviewed 3V3 feed can parallel/backfeed the onboard LDO. Brownouts can disable alarms. | Regulation over loaded cell range, approved board interface, startup/reset/off tests and rail transient measurements. D-03. | EE / G1-G2 |
| R-05 | Both / High | Charger BAT tied to a running load can corrupt charge termination; chip thermal regulation does not supervise cell temperature. | Separate charge-current/system-load paths or verified hardware load disconnection; temperature measurement at cell. D-04. | EE / G1-G2, G6 |
| R-06 | Pod / High | Generic PN532/GY-521 VCC, regulators and pull-ups are unknown. 3.3 V into an onboard LDO may undervolt the IC; 5 V pull-ups can damage logic. | Exact module schematics and supply/level-shift audit; effective pull-up/rise-time and power-off injection tests. D-06/D-20. | EE / G1-G2 |
| R-07 | Pod / High | PN532 0x48 address notation, board switch labels and RSTO/RSTPD_N names are easily confused. Wrong reset direction can cause contention. | 7-bit 0x24 host configuration, actual strap mapping/firmware response and pin-direction audit. NXP boot table and internal register encoding must not be interchanged. | EE, FW / G1-G2 |
| R-08 | Pod / High | A passive piezo, unspecified 2N2222 and 1 kohm resistor do not establish controlled AC drive, all musical tones or 105 dB at an undefined distance. | Exact transducer/driver, discharge/clamp network, waveform/thermal data and calibrated closed-case acoustics. Define hearing-safe test setup and actuation limits. D-07/D-18. | EE, ME, safety / G1-G2, G6 |
| R-09 | Keyfob / Critical | Nominal 3 V motor connected to raw LiPo/USB may be overdriven; stall and continuous-alert current can exceed cell/driver/thermal capability. | Rated motor rail, startup/stall and diode/driver sizing, off bias, thermal and maximum-duty qualification. | EE, ME / G1-G2, G6 |
| R-10 | Both / High | Siren/motor/LED/radio pulse currents can disturb I2C, IMU readings and RF or cause supply resets. | Short driver returns/local decoupling and verified routing; concurrent-load power, sensor and RF tests. Avoid arbitrary split grounds. | EE, FW / G2/G4/G6 |
| R-11 | Both / High | Board RGB rails/logic conflict with the Waveshare-linked LED sheet; white-strobe power/brightness and off-state leakage are unknown. | Confirm fitted LED revision/ratings or approved remedy, then measure logic margin, power and final-case visibility. D-16. | EE, supplier / G1-G2, G6 |
| R-12 | Both / High | C3 and S3 pin maps, USB pins and straps differ. A copied fob map could use S3 strap GPIO3 or repurpose native USB. | Freeze board revision and corresponding map; verify reset straps, service pins and safe boot outputs. D-02/D-06. | EE, FW / G1-G2 |
| R-13 | Pod / Critical | A USB-C-form GPIO tether can receive USB power/ESD or wrong contacts in either orientation; a short bypasses static continuity. | Decide inclusion/form factor, complete protected cable/contact map, controlled open/short/charger-misconnection tests; never raw external GPIO. D-08. | EE, ME / G1-G2 |

## 2. Mechanical and cross-domain conflicts

| ID | Unit / priority | Conflict and consequence | Required mitigation / closure evidence | Owner / gate |
| --- | --- | --- | --- | --- |
| R-14 | Pod / High | Documented Elechouse V3 reference is at least 42.7 x 40.4 in plane, exceeding the 45 x 30 target's width before walls. Actual PN532 module is unselected. | Select real module/antenna or approve larger enclosure; use maximum dimensions and actual RF envelope, not the PN532 IC body. D-13. | ME, EE/RF / G1/G3 |
| R-15 | Pod / High | Reference battery 5.3 plus required NFC gap 10 exceeds the screened 13 internal height before NFC/PCB/support material. Lateral placement also has little/no gap-compliant space. | Keep >=10 requirement; redo packing with selected parts or obtain explicit architecture/size change. No silent ferrite exemption. | ME, EE/RF / G1/G3/G6 |
| R-16 | Keyfob / High | C3 is the same 23.5 x 18 PCB outline as S3. Only 9 internal height remains in the screening case; battery/motor/charger stack is unknown. | Full maximum Z stack, port/motor and wire geometry, assembly trial; size remains TBD. | ME, EE / G1/G3/G6 |
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

## 4. Release policy

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
