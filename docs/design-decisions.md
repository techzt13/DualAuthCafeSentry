# Dual-Auth Cafe Sentry - Design Decision Log

Revision: 0.2 | Date: 2026-11-11 | Status: design basis; physical freeze blocked

The [project specification](../PROJECT_SPEC.md) remains unchanged.
**No human engineering approval is implied by this log.**
Sources are indexed in the [current datasheet ledger](datasheet-index.md) and
the retained [architecture index](architecture.md#9-manufacturer-source-index);
unselected items remain in the [component register](component-register.csv).

## 1. Decision control

- **APPLIED-DOC:** documentation/scope action completed, not hardware approval.
- **BASELINE:** retain a stated project requirement.
- **PROPOSED:** recommendation requiring owner and discipline review.
- **OPEN:** an unresolved selection or behavior that must not be silently chosen.

Record each future approval with date, reviewer, selected alternative, supporting
report and any specification revision. Keep superseded decisions in the history.
The owners below are required engineering disciplines; named reviewers are TBD.
Gate identifiers refer to the [development roadmap](development-roadmap.md).

## 2. Scope, components and electrical design

<a id="d-01"></a>
### D-01 - Documentation before PCB/CAD

**Status:** APPLIED-DOC. **Owner:** project lead. **Gate:** G0.

Create the eight requested design-basis documents and update the work log.
Do not create or edit PCB, schematic, CAD, firmware or manufacturing artifacts
in this task. Existing source requirements are retained, and incomplete
physical/electrical information is explicitly TBD. Future engineering stages
need their own authorization and validation.

<a id="d-02"></a>
### D-02 - Keyfob processor selection

**Status:** OPEN; C3 evaluation is PROPOSED. **Owners:** embedded, electrical,
mechanical. **Gate:** G1, confirmed at G2.

Evaluate Waveshare ESP32-C3-Zero first; preserve the specification's S3-Zero
alternative. Both boards have a documented 23.5 x 18 mm outline, so C3 is not
assumed to save board area. Measure whole-board beacon/RX/motor power and verify
software support. Select exactly one GPIO map and board revision.
**Approval required:** board, supplier, received revision and measured tradeoff.

<a id="d-03"></a>
### D-03 - Battery regulation and Zero-board USB isolation

**Status:** OPEN. **Owner:** electrical. **Gates:** G1/G2; safety-critical.

Reject direct raw-cell connection to the Zero's 5 V/VBUS net as an unqualified
architecture. The reviewed board schematics share that net with native USB.
Propose regulated logic power across the selected cell's usable range, but do
not approve 3V3-pad injection until onboard-LDO isolation/reverse behavior and
native USB coexistence are resolved. Alternatives include a verified isolated
board-input strategy or approved board/component changes.
**Closure:** annotated power-source circuit, worst-case analysis and bench
tests covering every allowed source combination.

<a id="d-04"></a>
### D-04 - Charger, temperature supervision and system load sharing

**Status:** OPEN. **Owners:** electrical, embedded, safety reviewer.
**Gates:** G1/G2.

MCP73831 and TP4056 are candidates, not complete approved modules. Choose the
exact regulated-voltage/termination variant and battery-matched current.
MCP73831 has no cell-temperature input; TP4056 TEMP is ineffective when tied
to ground. Neither candidate provides a separate system power-path output.

Owner must choose:

1. Verified simultaneous operation/charging with an additional qualified
   power-path circuit or an approved alternative charger; or
2. A verified hardware-enforced load-disconnect charging mode.

An integrated alternative charger would be a specification/BOM decision,
not an automatic substitution. Specify charge timeout, temperature inhibit,
source-current allocation, status logic and off-state behavior.
**Closure:** selected cell/charger/protector data and measured charge/termination,
temperature and system-load behavior.

<a id="d-05"></a>
### D-05 - Finished battery assemblies

**Status:** OPEN. **Owners:** electrical, mechanical, manufacturing.
**Gate:** G1, qualified at G2/G6.

Select Pod 200-250 mAh and Keyfob 150-200 mAh protected assemblies independently.
`502030` does not specify manufacturer, protection, thermistor, leads, connector
or maximum dimensions. EEMB LP502030 is an unselected **bare-cell comparison**,
not an approved pack or Keyfob substitution.
**Closure:** exact cell/pack drawings, charging/discharge/temperature limits,
protection evidence, connector polarity and physical samples.

<a id="d-06"></a>
### D-06 - Shared I2C and additional GPIO

**Status:** BASELINE GPIO4/5; PROPOSED supporting connections.
**Owners:** electrical, embedded. **Gates:** G1/G2.

Keep PN532 and MPU-6050 on GPIO4 SDA / GPIO5 SCL. Proposed initial bus speed is
100 kHz and MPU AD0 low gives 0x68; PN532 uses 7-bit 0x24. Reserve GPIO10/11
for PN532 IRQ/reset and GPIO12 for IMU INT; battery/status pins are proposals.
Verify actual module supplies, effective pull-ups, reset direction, straps and
power-down behavior before wiring. Do not confuse RSTOUT_N with RSTPD_N.
**Closure:** exact module schematics, pin audit, bus traces and bounded driver
timing while motion acquisition runs.

<a id="d-07"></a>
### D-07 - Piezo driver and acoustic specification

**Status:** OPEN; GPIO6/1 kohm nominal base resistor remain BASELINE.
**Owners:** electrical, acoustic/mechanical, safety reviewer. **Gates:** G1/G2/G6.

The unspecified 2N2222 and passive piezo cannot establish voltage, current,
105 dB performance or reproduction of all requested tones. Define SPL
distance/weighting/mounting/duty before selecting a transducer. Determine a
controlled charge/discharge waveform, clamp network and safe supply. Evaluate
a different driver only as an approved design change if the baseline cannot
meet requirements. Maximum siren duration and safe testing method are TBD.
**Closure:** identified parts, electrical waveforms, thermal results and
calibrated acoustic measurements in the final case.

<a id="d-08"></a>
### D-08 - Optional USB-C-form tether

**Status:** OPEN. **Owners:** electrical, mechanical, embedded, project lead.
**Gates:** G1/G2.

Retain GPIO8/9 and armed-open immediate-alarm intent if the optional feature
is included. Native programming USB cannot also be this GPIO loop.
Actual cable topology, port count, contacts, reversibility, ESD/fault-voltage
protection and initial-open arming behavior are TBD.

Recommend evaluating a mechanically keyed non-USB interface to reduce
misconnection risk; that changes the requested form factor and needs owner
approval. A static loop is bypassable by a short. A coded/challenged loop is
a separate enhancement, not assumed functionality.
**Closure:** inclusion decision, complete cable/connector drawings, protected
interface circuit and controlled misconnection/open/short tests.

## 3. Authentication, behavior and power management

<a id="d-09"></a>
### D-09 - Paired encrypted ESP-NOW and freshness

**Status:** PROPOSED. **Owners:** embedded, electrical/RF. **Gates:** G1/G2.

Use one Pod/Keyfob pair initially, explicit legal channel configuration,
encrypted unicast with unique provisioned keys, application ACKs, session
freshness and sequence-based deduplication. Do not use a MAC address or
unauthenticated RSSI as authorization. Pairing/revocation, key storage,
recovery, packet encoding and retry/deadline policies remain TBD.
**Closure:** approved protocol and threat assumptions, test vectors, paired
hardware traces and power/latency measurements.

<a id="d-10"></a>
### D-10 - NFC compatibility and security claim

**Status:** OPEN; five stored 4-/7-byte credentials remain BASELINE.
**Owners:** embedded, project lead. **Gates:** G1/G2.

"Any 13.56 MHz card" is not a valid interoperability guarantee. Proposed
initial support is compatible ISO/IEC 14443A cards with stable supported UIDs,
explicit rejection of unsupported types/lengths, duplicate handling and
card-removal debouncing. UID comparison is not cryptographic authentication.
Owner must accept a documented convenience-security limitation or approve
specific cryptographic credentials/protocols and revised compatibility wording.
**Closure:** supported-card matrix, enrollment/reset/power-loss tests and
approved claim wording.

<a id="d-11"></a>
### D-11 - One button, rhythm recovery, learning and reset

**Status:** OPEN; authorization-gated parser is PROPOSED.
**Owners:** embedded, human factors, project lead. **Gates:** G1/G2.

Use the single specified Pod button without quietly adding another switch.
Resolve 3 s learn versus 10 s reset overlap, rhythm timing tolerances,
attempt limits, code setup and lost-credential recovery.

Recommended policy: privileged learn/reset actions require an authorized
state/procedure; a 10 s hold must not enroll at the 3 s threshold. This adds
restrictions not specified in the original text and requires approval.
Reset currently means clearing NFC UIDs, not automatically deleting radio keys
or the rhythm code.
**Closure:** explicit gesture/state table, security/recovery review and
ergonomic tests with the recessed final-case control.

<a id="d-12"></a>
### D-12 - Alarm origin, priority and fault-state transitions

**Status:** OPEN; retaining `arm_origin` is PROPOSED.
**Owners:** embedded, project lead. **Gates:** G1/G2.

Preserve force-lock through warning and siren so proximity does not bypass it.
Freeze the following transitions before firmware implementation:

- Authorized NFC tap while AUTO-ARMED.
- Re-arming after card/rhythm disarm while the Keyfob remains far away.
- Near-Keyfob behavior during an existing warning or siren.
- Warning cancellation, persistence/retrigger rule and return to armed state.
- Remote mute scope/duration, panic semantics and authorization by origin.
- Loss of beacons, I2C/sensor failure, reboot, corrupted NVS and recovery.
- Races between disarm, tether-open and motion events.

Propose explicit fault reporting, no invalid-input authorization, and no silent
disarm on faults. Safe boot outputs must not mean silently forgetting a prior
armed state.
**Closure:** approved transition table and boundary/race/fault tests.

<a id="d-15"></a>
### D-15 - NFC duty cycle versus radio sleep and alert latency

**Status:** OPEN; all original timing/performance targets retained.
**Owners:** embedded, electrical/RF. **Gates:** G2/G6.

Validate 40 ms NFC polling per 250 ms and greater than 80% average savings,
including wake/command/module overhead. Independently choose ESP-NOW beacon
and receive scheduling; these timings are not linked merely because both
systems are periodic. A sleeping Keyfob cannot receive an arbitrary instant
alert. Runtime, maximum acceptable alert latency and link-loss deadlines are TBD.
**Closure:** measured current/time traces and owner-approved quantified
latency/runtime criteria.

<a id="d-16"></a>
### D-16 - Onboard RGB source inconsistency

**Status:** OPEN. **Owners:** electrical, supplier liaison. **Gates:** G1/G2.

S3's schematic supplies RGB at 3.3 V, while the linked LED sheet states a
3.5 V minimum. C3 V2 supplies RGB at 5 V with direct 3.3 V data, below the
linked sheet's 0.7 x VDD high threshold at 5 V. Confirm the actual LED/revision
with Waveshare and measure logic/current/brightness. Do not infer compliance
from a successful example sketch, or raise MCU voltage.
**Closure:** corrected/applicable supplier data or an approved hardware solution
with measurements; final-case visibility still requires validation.

<a id="d-17"></a>
### D-17 - GY-521/MPU-6050 identity and lifecycle

**Status:** OPEN. **Owners:** electrical, embedded, sourcing. **Gate:** G1.

Retain MPU-6050 pending review, but identify the exact GY-521 manufacturer,
schematic and revision. TDK's indexed product page lists MPU-6050 as obsolete;
direct retrieval was blocked and lifecycle must be reconfirmed. Do not
silently substitute the recommended newer IMU: footprint, registers, drivers
and fusion behavior would change.
**Closure:** sourcing/lifecycle confirmation or approved substitute with a
separate electrical/software/physical impact review.

<a id="d-18"></a>
### D-18 - Quantified acceptance criteria

**Status:** OPEN. **Owners:** project lead and relevant test disciplines.
**Gate:** G1 before claims are tested.

Freeze SPL distance/weighting and duration, RSSI near/far behavior and acceptable
false-event rates, alert latency, runtime, charge time, environmental range,
attachment/drop loads, ingress target and production tolerances. The
specification's 12-degree, 400 ms, 1.5 s, 3 s, 40/250 ms, five-card and NFC
clearance requirements already exist and must not be replaced by proxies.
**Closure:** approved measurable acceptance matrix; no pass verdict for a TBD
criterion.

<a id="d-19"></a>
### D-19 - Power-switch accessibility and armed-state retention

**Status:** OPEN. **Owners:** electrical, embedded, mechanical, project lead.
**Gates:** G1/G2/G6.

An accessible slide switch, discharged cell or removable power source can
silence the device independently of NFC/Keyfob authorization. Decide guarded
switch/service access, off behavior, low-battery warnings and what state may
be restored after reset. Persistent state must be integrity-checked without
writing flash on every beacon/sample. No promise of alarm operation after
power removal is made.
**Closure:** approved tamper/power-loss policy and bench/final-case tests.

## 4. Mechanical and manufacturing decisions

<a id="d-13"></a>
### D-13 - Target dimensions are not a fit commitment

**Status:** OPEN; original dimensions remain BASELINE targets.
**Owners:** mechanical, electrical/RF, project lead. **Gate:** G1/G3.

Keep 45 x 30 x 16 Pod and 35 x 25 x 12 Keyfob as goals, not guaranteed
envelopes. The [feasibility screen](mechanical-requirements.md#feasibility)
rejects the documented reference PN532 module in the Pod target and shows
the 10 mm gap conflict for conventional battery stacking.
Choose verified smaller components, a different architecture or an explicitly
approved larger body. Do not scale components, omit connectors or reduce
clearances to make a drawing appear to fit.
**Closure:** selected maximum envelopes, approved target interpretation,
placement/tolerance study and physical fit validation.

<a id="d-14"></a>
### D-14 - Serviceable parametric enclosure construction

**Status:** PROPOSED. **Owners:** mechanical, manufacturing. **Gates:** G1/G3/G6.

Use native FreeCAD parametric base/lid assemblies with named parameters,
supported electronics, removable batteries, proper bosses/fasteners and
structural attachment loops. Material, process, fasteners, wall/rib values,
diffusers, vent treatment and tolerances are TBD.
All placements must preserve RF, thermal, acoustic, control, connector and
service constraints. No appearance-only mesh is a substitute for engineering CAD.
**Closure:** approved process/material, editable models, drawings, STEP/STL,
assembly trial and validation reports.

<a id="d-20"></a>
### D-20 - Component identity and release provenance

**Status:** PROPOSED verification rule. **Owners:** electrical, mechanical,
manufacturing. **Gates:** G1 through G7.

Every placed or purchased part needs exact manufacturer/MPN/revision, applicable
datasheet, verified footprint/pinout and maximum installed envelope. Expand
grouped support-circuit entries into individual BOM references before schematic
freeze. Reference-only EEMB, Elechouse and onsemi examples are not purchase
selections. Resolve vendor-document inconsistencies with measurements and/or
manufacturer clarification rather than guessing.
**Closure:** complete component register/BOM traceability and independent review.

<a id="d-21"></a>
### D-21 - Evidence register is not a completed physical freeze

**Status:** APPLIED-DOC for evidence controls; hardware selections remain OPEN.
**Owners:** electrical, mechanical, manufacturing, project lead. **Gate:** G1.

Retain the original component IDs and named specification families. Record
separate unit-specific constituents and package-specific references, but do
not substitute Joy-IT, EEMB, Elechouse, Vybronics, SHOUHAN, TDK or onsemi
comparisons into the build. Exact MCU order pages do not establish delivered
PCB revision, fitted BOM or complete installed envelope.

Use the [dimension register](dimension-register.csv) only within its stated
drawing scope. Manufacturer size claims without a mechanical drawing remain
unverified; blocked sources and manufacturer-authored mirrors are disclosed.
Unknown circuit/interface groups are not orderable BOM parts. No project
assembly is FROZEN while these identity, drawing, power and fit holds remain.

The [verified pinout review](verified-pinouts.md#c3-zero) corrected the C3
USB pad pair in the earlier logical table; no application GPIO was changed.
The LP401730/charger voltage-tolerance conflict and TP4056 internal source
discrepancy require independent review, not a nominal-voltage assumption.

**Closure:** supplier-controlled actual assembly identities/drawings,
reviewed cell/charger/source interface, complete constituent BOM and
maximum-envelope evidence, followed by the existing verification gates.
No PCB layout or CAD design is authorized by completion of the registers.

## 5. Revision history

| Revision | Date | Change | Approval status |
| --- | --- | --- | --- |
| 0.1 | 2026-11-11 | Initial eight-document engineering design basis; source verification, logical interfaces, risk register, feasibility analysis and staged roadmap | Documentation task completed subject to recorded checks; all hardware/behavior proposals remain unapproved |
| 0.2 | 2026-11-11 | Extended component/evidence/dimension/pinout registers; preserved research after interruption; corrected C3 USB pad pair; added documented cell/charger and packaging conflicts | Documentation evidence only; physical freeze blocked, no substitutions or hardware approval |

No completed engineering design was overwritten. G0 began with an empty work
log and no existing design documents, PCB or CAD models. Revision 0.2 preserves
that completed design basis and extends only the related verification records.
