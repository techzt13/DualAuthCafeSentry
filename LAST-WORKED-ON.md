# Last Worked On - Dual-Auth Cafe Sentry

Date: 2026-11-11
Package revision: 0.1
Completed stage: G0 engineering design-basis documentation
Next stage: G1 component/requirement decisions and verification

**PCB/schematic creation: not started. CAD enclosure creation: not started.
Hardware safety, physical fit and manufacturing readiness: not approved.**

## Task completed

Read the complete [PROJECT_SPEC.md](PROJECT_SPEC.md) and
[AGENTS.md](AGENTS.md), the repository instruction files and the previously
empty work log. Inspected the existing repository before creating the requested
professional engineering package. The specification and engineering
instructions were not changed; no completed design was overwritten.

Created:

| File | Contents |
| --- | --- |
| [docs/architecture.md](docs/architecture.md) | Separate Pod/Keyfob electrical and mechanical architecture; state, NFC, ESP-NOW and sensor/alarm contracts; 22 source entries |
| [docs/component-register.csv](docs/component-register.csv) | 75 unique entries: 40 Pod, 30 Keyfob and 5 reference-only; exact identities/dimensions or explicit TBDs |
| [docs/pinout.md](docs/pinout.md) | Original Pod GPIO4-9 retained; proposed additional and Keyfob allocations; I2C addresses; complete logical connection/unused-pin schedule |
| [docs/power-architecture.md](docs/power-architecture.md) | Charging, protection, regulation, source isolation, actuator supplies, power-budget method and qualification requirements |
| [docs/mechanical-requirements.md](docs/mechanical-requirements.md) | Construction, placement, assembly/removal, named future parameters and conditional target-size feasibility |
| [docs/design-decisions.md](docs/design-decisions.md) | 20 controlled decisions and initial revision history; proposals remain unapproved |
| [docs/engineering-risks.md](docs/engineering-risks.md) | 33 open electrical, mechanical, functional and release risks with closure evidence |
| [docs/development-roadmap.md](docs/development-roadmap.md) | G0-G7 dependencies, exact next actions and 24 acceptance-test entries |

Verified-document facts, specification requirements, proposals and unknowns are
distinguished throughout. EEMB LP502030, Elechouse PN532 V3 and onsemi P2N2222A
are comparisons, not approved substitutions or purchase selections.

## Important findings and unresolved dependencies

1. Both reviewed Waveshare Zero schematics lack LiPo charging/protection.
   Their native USB VBUS and external 5 V pad share a net. Direct raw-cell
   wiring, regulator coexistence and simultaneous USB/external supply use
   require a reviewed solution before battery-powered construction.
2. Finished battery packs, charger modules, the actual PN532 and GY-521
   modules, piezo, motor, discrete packages, connectors, switches and materials
   remain incompletely selected. Charge current, temperature supervision,
   protection, load sharing and peak loads cannot be approved yet.
3. I2C host addresses are PN532 **0x24** and proposed MPU-6050 **0x68**
   (0x69 with AD0 high). PN532 0x48 is the write-address byte, not the 7-bit
   host address. Module straps, supply levels and reset input/output names
   still require actual-board verification.
4. Both Zero PCB outlines are documented as 23.5 x 18 mm. The unselected
   Elechouse NFC module is wider than the original Pod target. Under the
   explicit 1.5 mm wall/base/lid screen, a maximum-thickness 5.3 mm reference
   cell plus the required 10 mm NFC gap already needs 15.3 mm inside, exceeding
   the 13 mm available. The derived 18.3 mm external lower bound is conditional
   and excludes other parts; it is not a new enclosure specification.
5. The 45 x 30 x 16 Pod and 35 x 25 x 12 Keyfob remain targets, not guaranteed
   fits. The Keyfob's battery/motor/charger/USB Z stack is still unknown.
6. RSSI cannot guarantee a universal 4 m threshold; sleeping receivers cannot
   guarantee instantaneous unsolicited alerts. The 40/250 ms NFC duty ratio
   gives 84% ideal inactive time, not proof of >80% actual current savings.
7. UID-only NFC authentication, arbitrary-card compatibility, privileged
   learn/reset gestures, remote mute/panic, force-lock alarm origin and
   power-loss/re-arm behavior require explicit owner decisions.
8. Waveshare's board RGB rails/logic and its linked LED sheet have apparent
   compatibility mismatches. Actual fitted LED/revision and operation require
   supplier clarification and measurement.

Manufacturer PDFs, board schematics and dimension images were reviewed for
the cited facts. TDK's direct MPU-6050 PDF/page requests returned HTTP 403;
the full manufacturer-authored datasheet was inspected through the documented
SparkFun mirror. The lifecycle warning is from TDK's indexed product page
and must be reconfirmed. Access limitations are recorded in the source index,
not treated as successful direct verification.

## Validation results

| Check | Result |
| --- | --- |
| Requested deliverables | PASS: all eight files exist and are nonempty |
| CSV parsing/schema | PASS: 16 columns, 75 unique part IDs, no empty/ragged fields; source IDs and revision fields checked |
| Markdown structure | PASS: consistent table columns, balanced code fences, ASCII text and final newlines |
| Local links/anchors | PASS for the eight-document package; handoff links use the same relative-path convention |
| Source/decision/risk/test IDs | PASS: complete unique SRC-01..22, D-01..20, R-01..33 and T-01..24 sets |
| GPIO review | PASS at documentation level: original Pod assignments preserved, no duplicate Pod/C3 table roles, separate S3 Keyfob map checked |
| Feasibility arithmetic | PASS: cavity volumes, battery/gap lower bound, Keyfob residual area, ideal NFC ratio and reference-cell temperature derating recomputed |
| Whitespace | PASS: standard-library checks and Git checks; new files checked with `git diff --no-index --check` with no whitespace diagnostics |
| Scope preservation | PASS: specification/instructions unchanged; no PCB, CAD, firmware, manufacturing or project tooling files created |
| ERC / DRC | NOT RUN: no project schematic or PCB exists |
| CAD / physical fit | NOT RUN: no enclosure model or assembled prototype exists |
| Charging, protection, RF, sensor, acoustic, haptic, thermal and runtime testing | NOT PERFORMED: requires selected hardware, approved circuits/criteria and safe fixtures |

Git's no-index comparison returns 1 for an ordinary new-file difference; the
whitespace check was verified with clean/error controls and assessed using its
diagnostics. No hardware performance is inferred from documentation checks.
Temporary manufacturer-review downloads and the isolated PDF-reading
environment were removed; no project dependency files were added.

## Exact next steps

1. Review and decide D-03/D-04/D-05 power and battery architecture, D-08 tether
   inclusion/form factor, D-10/D-11/D-12/D-19 authorization and fault behavior,
   and D-13/D-18 size interpretation and measurable acceptance criteria.
2. Identify exact manufacturer/MPN/revision for each required assembly in the
   [component register](docs/component-register.csv). Obtain authentic
   schematics/datasheets, finished-pack drawings and maximum component heights.
3. Confirm actual module supply/pull-up/reset behavior, RGB variant and IMU
   sourcing/lifecycle. Measure connector, lead, protection-board and mating-plug
   envelopes; do not use IC-only or nominal cell dimensions as assembly sizes.
4. Re-run the two enclosure envelope studies with those parts and the existing
   NFC clearances. Obtain explicit approval for any changed component,
   capacity, size, tether or performance requirement.
5. Prepare independently reviewed, current-limited bench procedures for the
   G2 power/sensor/radio/actuator tests. Do not energize unqualified LiPo
   circuits or place automatic orders.
6. Start native KiCad and FreeCAD co-design only after the roadmap prerequisites
   and explicit authorization are satisfied.

Before the next major task, reread [PROJECT_SPEC.md](PROJECT_SPEC.md),
[AGENTS.md](AGENTS.md), this log and the relevant design documents.
