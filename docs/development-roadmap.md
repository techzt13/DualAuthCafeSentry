# Dual-Auth Cafe Sentry - Staged Development Roadmap

Revision: 0.2 | Date: 2026-11-11 | Status: G1 evidence documented; physical freeze incomplete

This roadmap implements the [specification](../PROJECT_SPEC.md) under
[AGENTS.md](../AGENTS.md). Dates, named reviewers, procurement lead times and
stage durations are TBD. Do not infer a delivery schedule from the event name.
**Only the documentation stage is in scope for the current task.**
The [component evidence package](datasheet-index.md) now records verified
documents, unverified assemblies and source-access failures. This completes a
G1 research/register work package, not the G1 exit gate; PCB/CAD remain on hold.

## 1. Stage and dependency overview

| Gate / stage | Prerequisites | Work and persistent deliverables | Exit evidence / owner |
| --- | --- | --- | --- |
| G0 - Design basis | Complete specification and instructions read; existing work inspected | Eight requested documents, source index, component/TBD register, work log | Documentation checks and independent-review-ready package; project lead |
| G1 - Requirements and component freeze | G0; human decisions D-02 through D-20 where applicable | Exact boards/modules/cells/chargers/actuators/connectors; supplier drawings; approved behavior and acceptance criteria; preliminary envelope budget | Safety-critical architecture choices resolved, maximum component envelopes available, source provenance established; EE/ME/FW/lead |
| G2 - Controlled bench feasibility | G1-approved circuits and test procedures; safe test equipment; explicit approval for any procurement | Separate Pod/Keyfob electrical bring-up and power measurements; NFC/IMU/audio/haptic tests; paired radio/state proof; reports in [docs/reports](reports/) | Demonstrated required behavior and known power/timing constraints; no unreviewed battery circuit energized; EE/FW/RF/safety |
| G3 - Authorized schematic and packaging co-design | G1 selections; G2 evidence; explicit authorization to begin PCB/CAD | Native KiCad schematics and footprint review for both units; native parametric FreeCAD packaging/assembly; approved enclosure envelope and tolerance stack | ERC reviewed, every selected part represented, mounting/USB/antenna/thermal/assembly interfaces reconciled; EE/ME |
| G4 - PCB layout and detailed enclosure | G3 interface freeze; remaining layout-critical selections closed | Native KiCad PCBs; editable final base/lid/features; STEP/STL and integration model; assembly drawings; reports | Schematic/PCB consistency, DRC/ERC, verified footprints, fit/clearance and RF/thermal design review; EE/ME/MFG |
| G5 - Human-approved prototype fabrication | G4 review; prototype risks and test limits documented | Reviewed prototype manufacturing package; explicit human approval before any order; received-part inspection | Correct revisions and manufacturing/assembly evidence; MFG/lead |
| G6 - Integrated qualification | Assembled G5 prototypes; approved acceptance matrix and safe fixtures | Functional, RF, power, charging, acoustic, mechanical and service tests; failure analysis and controlled revisions | All applicable criteria pass with reports; no unresolved safety-critical release risk; EE/ME/FW/RF/safety |
| G7 - Release and showcase package | G6 pass; review/approval of all release artifacts | Versioned native sources, manufacturing exports, BOM, firmware/build instructions, test reports, assembly/user/service documentation | Independent engineering sign-off and explicit fabrication authorization; lead/MFG |

The critical path is **selection and power/behavior decisions -> bench evidence
-> authorized co-design -> integration -> prototype -> qualification**.
G3/G4 must not be started solely because component models can be drawn.

Within G1, source verification for unrelated modules and mechanical measurement
can proceed independently. Within G2, individually approved power, sensor,
audio and motor benches can proceed in parallel; integrated timing/RF tests
depend on their results. Closed-case thermal/RF/acoustic validation cannot be
completed before a representative assembled enclosure exists.

## 2. Exact next actions - G1

1. Review the [decision log](design-decisions.md), especially:
   - D-03/D-04/D-05: protected cells, regulation, USB isolation, load sharing,
     temperature supervision and charge-current selection.
   - D-08: whether to include tether, its form factor and misconnection protection.
   - D-10/D-11/D-12/D-19: credential scope, learn/reset authorization,
     force-lock/mute/panic/fault transitions and power-loss policy.
   - D-13/D-18: target envelope interpretation and measurable performance criteria.
2. Identify exact manufacturers and revisions for both Zero boards, GY-521,
   PN532 module/antenna, finished battery packs, chargers, piezo, coin motor,
   transistors/diodes, switches and connectors. Keep all unknown register
   fields TBD until evidence exists.
3. Obtain manufacturer-controlled drawings and inspect actual maximum assembly
   envelopes, including protection PCBs, USB overhang, heights, leads and mating
   plugs. Use the [dimension register](dimension-register.csv); if no drawing
   exists, keep manufacturer dimensions unverified and label any measurements
   separately. Reconcile RGB, PN532 interface and TP4056 tolerance conflicts,
   and the LP401730/charger voltage mismatch before selecting a pairing.
4. Obtain approved human sourcing decisions before purchases; do not order
   cells, boards or fabrication services automatically.
5. Resolve power/source arbitration on paper and with independently reviewed
   bench procedures before battery-powered prototypes. Do not use raw-cell
   wiring from the original abbreviated map as a tested circuit.
6. Re-evaluate both target envelopes with real maximum dimensions, preserving
   the <=1.5 mm NFC window and >=10 mm battery/piezo gaps. If they cannot fit,
   request an explicit requirement/component/size decision before CAD.
7. Freeze test conditions and acceptance values currently marked TBD. Obtain
   authorization for the next implementation stage.

## 3. G2 bench work packages

### A. Power - independent for each unit

- Prove source isolation, regulator headroom/transients, correct polarities and
  safe reset/off states first using suitable controlled supplies.
- Qualify charger voltage/current/termination, temperature sensing/inhibit,
  pack protection and system-load interaction against the exact selected cell.
- Measure complete-board and complete-module currents. Include both possible
  Keyfob boards until one is selected.
- Add the selected siren/motor load only after driver/rail ratings are reviewed.
  Measure startup, stall/switching behavior as appropriate, and USB/charge
  concurrency. Do not short/abuse real cells as an improvised test.

### B. Pod sensor, NFC and alarm

- Probe the shared bus at 7-bit 0x24 and selected 0x68/0x69.
  Verify straps, supply levels, pull-ups, reset direction, IRQ and timeouts.
- Establish IMU calibration, axis convention, sampling/fusion and sustained
  movement metric; test tilt/duration boundaries and sensor faults.
- Verify supported cards and all five credential slots across power cycles.
  Validate card-removal debounce, unsupported UID lengths, full-store errors,
  unauthorized tap and interrupted NVS writes.
- Measure the complete NFC polling cycle and average-current reduction,
  including wake/commands/standby, while IMU acquisition remains responsive.
- Measure the selected piezo waveform and the requested sounds in a safe
  acoustic fixture. Stop treating the 105 dB target as satisfied by a BOM label.

### C. Keyfob and paired firmware

- Verify sleep/button wake and motor safe state for the selected board.
- Implement the approved packet/state/gesture contract, with encrypted
  unicast, current-session checks, application ACKs and bounded retries.
- Measure RSSI distributions rather than inventing a 4 m dBm threshold.
  Characterize orientation, pockets/body shadowing and channel interference.
- Verify two-pulse auto-arm feedback, alarm haptics, cancellation and sleep/RX
  latency. Test loss/reordering/duplicates/reboots and unpaired traffic.

Persist raw captures and concise conclusions in [docs/reports](reports/),
identified by hardware/firmware revisions, test configuration, instruments,
conditions and reviewer. Log failures as failures, not implicit accepted limits.

## 4. G3/G4 editable engineering deliverables

These are **future deliverables**, not files created by this documentation task.

| Area | Required content / existing destination |
| --- | --- |
| Pod electrical | Native KiCad project, full schematic, symbol/footprint provenance, net/connector schedule, PCB and 3D component envelopes in [hardware/sentry-pod](../hardware/sentry-pod/) |
| Keyfob electrical | Separate native KiCad project with selected MCU option, power/motor circuits and matching files in [hardware/keyfob](../hardware/keyfob/) |
| Pod mechanical | Editable FreeCAD base/lid with named parameters, sketches, bosses, fasteners, component envelopes and STEP/STL in [cad/sentry-pod](../cad/sentry-pod/) |
| Keyfob mechanical | Separate editable FreeCAD enclosure, motor/cell mounting and STEP/STL in [cad/keyfob](../cad/keyfob/) |
| Integration | Common coordinates, complete assembled envelopes, PCB/enclosure relationships and service-clearance checks in [cad/assembly](../cad/assembly/) |
| Firmware | Approved state/protocol implementation, reproducible toolchain and hardware-revision configuration in [firmware](../firmware/) |
| Manufacturing | Approved BOM/placement/fabrication/assembly outputs, polarity and inspection notes in [manufacturing](../manufacturing/) |
| Evidence | ERC, DRC, footprint/pin audit, tolerance, interference, thermal, RF and test reports in [docs/reports](reports/) |

Schematic freeze must expand grouped support parts in the register into real
reference designators, values, ratings and footprints. Intentionally unused pins
must be documented; no unresolved power/connector pin may be disguised with
an ERC suppression. Every waiver requires rationale and review.

Before layout freeze, match actual PCB size, hole coordinates, component
heights, antenna keepouts, battery envelope, USB centers, button access,
acoustic vent and wire channels to the FreeCAD assembly. Verify design
recompute and exported STEP/STL dimensions; a rendering alone does not pass.

## 5. Acceptance and validation matrix

Numeric boundary inputs below are test requirements derived from the
specification, not new component ratings. Physical tests need uncertainty and
timing-resolution budgets; exact mathematical boundaries should also be
covered in firmware tests. **TBD criteria must be approved before a pass can
be recorded.**

| Test | Required result / measurable criterion | Stage |
| --- | --- | --- |
| T-01 GPIO / startup | Correct selected-board pin map; no conflicting roles; boot/USB preserved; no unintended piezo/motor actuation during reset, flash, sleep or supply changes | G2/G4/G6 |
| T-02 Bus | PN532 at 7-bit 0x24; MPU at selected 0x68 or 0x69; no 5 V exposure; measured valid rise/low levels, clock stretching and bounded recovery | G2/G6 |
| T-03 Tilt threshold | Logic inputs at/below 12 degrees do not qualify on tilt alone; above 12 do, while armed; validate physical behavior with a calibrated reference | G2/G6 |
| T-04 Movement duration | Continuous movement of exactly 400 ms or less does not qualify on duration alone; greater than 400 ms does; interruptions reset the approved persistence metric | G2/G6 |
| T-05 False-alarm rejection | Representative short table vibrations rejected without hiding sustained motion/tilt; sample/filter/false-event acceptance rates frozen under D-18 | G2/G6 |
| T-06 Warning sequencing | Warning duration 1.5 s with defined timer tolerance; persistent motion follows approved siren transition; cancellation returns to approved original mode | G2/G6 |
| T-07 Tether bypass | If fitted, opening while armed enters SIREN without the warning delay; maximum detection latency TBD; both orientations and approved fault cases tested | G2/G6 |
| T-08 Proximity arm | Authenticated far condition maintained for 3 consecutive seconds; not a guessed packet count. No arm before the interval; near/far/loss rules per approved table. | G2/G6 |
| T-09 Auto-unlock versus force-lock | Near Keyfob unlocks AUTO-ARMED as specified; never removes FORCE-LOCKED, including through warning/siren; approved race cases covered | G2/G6 |
| T-10 Keyfob feedback | Exactly two distinct auto-arm vibrations on one new confirmed arm event; duplicate packets do not repeat them; active-alarm haptics and stop behavior meet approved duty limits | G2/G6 |
| T-11 Link robustness | Unpaired, malformed, stale, replayed and duplicate messages cannot authorize; lost ACKs do not duplicate commands; restart/session changes handled | G2/G6 |
| T-12 Sleep / alert latency | Complete beacon/RX schedule measured; alarm-delivery latency and packet-loss recovery meet an approved numeric bound, currently TBD | G2/G6 |
| T-13 Credential capacity | Five distinct supported credentials persist; sixth rejected without overwriting; duplicate does not consume a slot; full 4-/7-byte comparison and unsupported-length rejection | G2/G6 |
| T-14 Button gestures | 3 s learn, 10 s UID reset and custom four-beat disarm under approved permissions; no accidental enrollment on reset hold; deglitching, attempts and timing tolerance tested | G2/G6 |
| T-15 NVS / reset | Credentials survive power cycles; UID reset clears only approved scope; interrupted writes/corruption produce explicit controlled recovery, not silent authorization | G2/G6 |
| T-16 NFC duty / savings | Poll window 40 ms each 250 ms (4 Hz), within approved timing tolerance; measured full-cycle average-current saving **>80%** versus defined continuous reference; supported-card latency/miss rate TBD | G2/G6 |
| T-17 Acoustic sequence | Requested arm/disarm/enroll/unauthorized sequences and 1.5 s two-tone warning reproduced; siren sweeps 2.8-4.2 kHz; measured alarm SPL must reach >=105 dB at preapproved distance, weighting and drive/mounting conditions, unless the requirement is explicitly revised | G2/G6 |
| T-18 LED / haptics | Correct Pod colors/patterns, adequate final-case visibility and safe current/logic margin; motor voltage/startup/stall/continuous-duty limits satisfied | G2/G6 |
| T-19 Charging / protection | Selected cell's charge-voltage/current/temperature/termination limits met in all approved modes; protection and off/absent-cell behavior verified with safe fixtures | G2/G6 |
| T-20 Sources / brownout | No unsafe VBUS/battery/regulator backfeed; USB orientation/concurrency tested; worst-case radio/actuator peaks do not reset logic above approved battery cutoff | G2/G6 |
| T-21 Runtime / thermal | Measured usable runtime meets approved value (TBD); final-case cell, charger, regulator and driver temperatures remain within selected-part limits | G2/G6 |
| T-22 Mechanical / RF | Actual assembly fits approved envelope, not merely a render; finished NFC wall <=1.5; battery and piezo each >=10 from coil under approved measurement convention; final-case NFC/RF pass | G3/G4/G6 |
| T-23 Assembly / service / strength | Real plug, button, switch, wire and tool access; no cell compression or screw intrusion; safe removal; attachment/drop/retention and any ingress criteria TBD | G3/G6 |
| T-24 Manufacturing consistency | Complete native projects; schematic/PCB/netlist consistency; reviewed ERC/DRC; verified footprints/pinouts; recomputed CAD and checked exports; no undocumented waivers | G3/G4/G7 |

Any changed component, enclosure material/geometry or firmware timing must
trigger the affected matrix tests again. A bench NFC pass does not replace a
closed-case test, and a chip datasheet current does not replace runtime testing.

## 6. Release review and records

Before approving prototype fabrication, review the exact board/CAD revisions,
manufacturing outputs, components, risks and intended test limits. Before
calling a design manufacturing-ready, require the appropriate reports and
independent electrical, physical and manufacturing review; prototype assembly
alone is not qualification.

Keep native sources, source links/revisions, measurements, approvals and
revision history together. Record accepted residual limitations, supported
cards, charge instructions, physical switch behavior, safe siren use and
battery replacement procedure in the eventual user/service documentation.
No unattended ordering or fabrication authorization is granted by this plan.

## 7. Current validation status

G0 produces a documentation package, not a tested product. Manufacturer
documents and conditional envelope arithmetic have been reviewed.
Document consistency/CSV/link checks are recorded in
[LAST-WORKED-ON.md](../LAST-WORKED-ON.md).

ERC: not run. DRC: not run. CAD recompute/interference: not run.
Physical fit, LiPo safety, charging, RF, acoustic, haptic and runtime tests:
not performed. No schematic, PCB, CAD enclosure or firmware was created.
