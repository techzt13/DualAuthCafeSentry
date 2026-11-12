# Last Worked On - Dual-Auth Cafe Sentry

Date: 2026-11-12 (hackathon implementation authorised; PCB and CAD are required deliverables)
Package revision: 0.3
Project stage: G0 design basis complete; G1 candidate research complete;
provisional PCB/CAD co-design STARTED by owner direction; component freeze
and battery-powered validation remain open
Next stage: create native KiCad projects and FreeCAD parametric assemblies

**PCB/schematic and CAD creation are now authorised and are required hackathon
deliverables. Native KiCad and FreeCAD files must be created; none are yet
claimed to exist. Firmware and manufacturing exports remain not started.
Nothing purchased or ordered. O-01 enlarges the Pod to at least approximately
55 mm length as a working lower bound; width 30 mm and height 16 mm remain
provisional. O-02 BQ25185 at 4.1 V and O-03/O-05 Direction A remain evaluation
choices, not frozen circuits. PAM8904E is the leading paper-screen driver
candidate only. Battery connection, energised testing and fabrication orders
remain separate and require their own review/approval.**

Before the next task, read [PROJECT_SPEC.md](PROJECT_SPEC.md),
[AGENTS.md](AGENTS.md), this file and the relevant `docs/` files. Some session
instructions refer to a parent-level `../AGENTS.md`; that file does not exist,
so the repository [AGENTS.md](AGENTS.md) governs. Neither governing file has
been changed by any task recorded here.

## 1. Current status

The G1 candidate research task is **complete as documentation**. The
**physical component freeze is BLOCKED**. Nothing is selected, purchased or
marked FROZEN. No battery and charger pairing is approved. O-01 Option A, O-02 Option A (evaluation only), and O-03/O-05 Direction A
(evaluation only; proposed SPL distance 10 cm) are recorded. Other owner
decisions remain open; no physical component is selected or frozen.

| Item | Current value |
| --- | --- |
| [docs/component-register.csv](docs/component-register.csv) | 122 rows, 30 columns, 122 unique `part_id` values |
| [docs/dimension-register.csv](docs/dimension-register.csv) | 122 rows, 24 columns; the same 122 IDs in the same order |
| Classification | 54 Pod, 43 Keyfob, 25 reference-only |
| Original IDs | All 75 IDs from G0 commit `13863c9` retained |
| Revision 0.2 rows | All 111 rows identical to commit `6149d7a` in both registers |
| Revision 0.3 rows | 11 appended G1 candidates, all `Reference only`, `CANDIDATE_OWNER_DECISION`, `REFERENCE_NOT_SELECTED` |
| `freeze_status` | HOLD_CIRCUIT 44, HOLD_IDENTITY 40, REFERENCE_NOT_SELECTED 25, NOT_DESIGNED 8, HOLD_SELECTION 4, HOLD_REVISION_ENVELOPE 1, FROZEN 0 |
| Numeric dimension rows | 22 partial, drawing-scoped rows (14 from revision 0.2, 8 new); 100 rows have no numeric dimensions |
| Controlled IDs | SRC-01..53, D-01..22, R-01..39 (all open), T-01..24, O-01, O-02, O-03/O-05 evaluation direction recorded; O-04 and O-06..15 open |

## 2. Repository and Git state

Repository: `techzt13/DualAuthCafeSentry` on GitHub (public), branch `master`.

| Commit | Date | Content |
| --- | --- | --- |
| `13863c9` | 2026-11-11 | G0 design basis, revision 0.1, 75-ID register; fixed baseline for original-ID checks |
| `13eb171` | 2026-11-12 | Revision 0.2 deliverables: 111-row registers, datasheet index, verified pinouts |
| `577067c` | 2026-11-12 | Revision 0.2 completion handoff and recovery records |
| `6149d7a` | 2026-11-12 | Saved validation evidence; fixed baseline for the 111 revision 0.2 rows |
| Commit containing this file | 2026-11-12 | Revision 0.3: G1 candidate research, evidence-folder manifest and this handoff |

At the start of this session `6149d7a` was `HEAD` and the live
`origin/master`, and the working tree was clean. The previous revision of
this file is in Git history: `git show 6149d7a:LAST-WORKED-ON.md`.

Empty local directories (`cad/`, `hardware/`, `firmware/`, `manufacturing/`,
`scripts/`, `docs/reports/`) contain no files and are not tracked.
`docs/datasheets/local/` holds research documents and is ignored by Git.

## 3. Work done in this session

### 3.1 Files created

| File | Content |
| --- | --- |
| [docs/g1-component-shortlist.md](docs/g1-component-shortlist.md) | Candidates per assembly with evidence class, recommendation and remaining uncertainty |
| [docs/g1-battery-charger-compatibility.md](docs/g1-battery-charger-compatibility.md) | Charge-voltage, current, temperature and discharge comparison; no pairing approved |
| [docs/g1-power-architecture-recommendation.md](docs/g1-power-architecture-recommendation.md) | Four options and a recommended evaluation architecture |
| [docs/g1-mechanical-feasibility.md](docs/g1-mechanical-feasibility.md) | Packing screens of the candidates against both enclosure targets |
| [docs/g1-piezo-driver-compatibility.md](docs/g1-piezo-driver-compatibility.md) | Manufacturer-data screen of CPT-2475-92T, PAM8904 and PAM8904E; no component selected |
| [docs/g1-owner-decisions.md](docs/g1-owner-decisions.md) | Fifteen owner decisions O-01 to O-15 and four authorisations A-1 to A-4 |
| [docs/datasheets/README.md](docs/datasheets/README.md) | Evidence policy, redistribution review and inventory of 61 local files |
| [docs/datasheets/SHA256SUMS](docs/datasheets/SHA256SUMS) | SHA-256 of the 61 local files |
| [docs/datasheets/.gitignore](docs/datasheets/.gitignore) | Keeps `local/` out of Git |

### 3.2 Files modified

| File | Change |
| --- | --- |
| [docs/component-register.csv](docs/component-register.csv) | 11 candidate rows appended; the 111 existing rows untouched |
| [docs/dimension-register.csv](docs/dimension-register.csv) | 11 matching rows appended; 8 carry drawing-scoped numeric values |
| [docs/datasheet-index.md](docs/datasheet-index.md) | Revision 0.3; section 8 adds SRC-30 to SRC-53, unverified leads and retrieval failures |
| [docs/engineering-risks.md](docs/engineering-risks.md) | Revision 0.3; R-34 to R-39 added; R-01 to R-33 unchanged and open |
| [docs/design-decisions.md](docs/design-decisions.md) | Revision 0.3; D-22 added; no earlier decision changed |
| [docs/power-architecture.md](docs/power-architecture.md) | Revision 0.3 notes in section 2.1 on the regulator reverse-voltage limit |
| [docs/mechanical-requirements.md](docs/mechanical-requirements.md), [docs/development-roadmap.md](docs/development-roadmap.md), [docs/architecture.md](docs/architecture.md) | Revision notes and links to the new documents only |
| [LAST-WORKED-ON.md](LAST-WORKED-ON.md) | Rewritten as this handoff |

Not changed: [PROJECT_SPEC.md](PROJECT_SPEC.md), [AGENTS.md](AGENTS.md),
[docs/pinout.md](docs/pinout.md), [docs/verified-pinouts.md](docs/verified-pinouts.md).

### 3.3 How the research was done

Three independent source-finding threads were delegated (batteries; NFC and
IMU modules; actuators, switches and connectors). Their reports were treated
as leads. Each document used for a register value or a recommendation was
then downloaded and read directly, and drawings were viewed as images where
text extraction was unreliable. Values that were not re-read are marked **L**
in the shortlist and do not populate numeric register fields.

## 4. Components researched and recommendations

Full detail and evidence: [component shortlist](docs/g1-component-shortlist.md).
"Recommended" means preferred on current documents; it is **not a selection**.

| Assembly | Recommended candidate, exact identifier | Main reason | Main blocker |
| --- | --- | --- | --- |
| P-NFC, P-NFC-ANT | Elechouse PN5321 MINI, SKU NFC_EX_MINI, hardware V2, with its 10 x 25 mm antenna | Only documented PN532 module small enough to consider: 25 x 16.4 x 4.4 mm board | No schematic; no IRQ pin; 10 mm pack separation does not fit the Pod target |
| P-IMU | Adafruit product 3886 | Identifiable maker, product number and PCB files | Out of stock; not a generic GY-521; MPU-6050 lifecycle lead |
| P-BATTERY | Renata ICP521630PM-01, then Jauch LP502030JH+PCM+2 WIRES 50MM | Renata states 500 mA non-continuous discharge | No charge-voltage tolerance; no NTC; Renata thresholds unpublished |
| K-BATTERY | Renata ICP402025PC-01, then Jauch LP402025JU+PCM+2 WIRES 50MM | Meets 150 mAh minimum; highest stated rating in class | Rating still 25 mA below the transmit peak; no NTC |
| P-CHARGER, K-CHARGER | TI BQ25185 at its 4.1 V setting, on a custom carrier | 4.1205 V maximum is below every battery limit; power path; NTC input | Not a specified charger family; no carrier stage authorised |
| Power path | Option A: BQ25185 SYS through TI LM66100 to the Zero 5 V pad | Keeps the onboard regulator inside its stated limits | Native USB-C VBUS pins energised from the battery |
| P-PIEZO | Same Sky CPT-2475-92T | Only part with verified level and conditions | 92 dB at 10 cm, not 105 dB; 24 mm diameter |
| Piezo driver | onsemi MMBT2222ALT1G; alternative Diodes PAM8904 | Specified family; boosted alternative documented | Boosted driver changes the specification |
| K-MOTOR | Precision Microdrives 308-100 | 8 mm body is the only one passing the Keyfob plan screen | No continuous-duty data |
| Buttons | Alps Alpine SKSCLBE010 (side), SKRPABE010 (top) | Maker specifications read | Body dimensions not read from drawings |
| Slide switches | C&K PCM12SMTR | 0.3 A at 6 V DC, six times the MSK12C02 reference | Still below load current; must switch an enable only |
| Charge connector | GCT USB4125-GF-A | 6-contact power-only USB-C, 3 A | 6.80 mm deep; charge-port circuit not designed |
| Battery connector | JST PH (Pod), JST SH (Keyfob) | Maker ratings read | AWG26 Jauch wires do not fit SH contacts |
| K-MCU | Keep ESP32-C3-Zero as the proposed option | Exposes USB D-/D+ on contacts 15 and 16 | No size advantage; board currents unmeasured |

Not researched: credential cards, cell NTC parts, tether port and cable,
fasteners, insulation, acoustic mounting, attachment hardware, passive
values, ESD protection, fitted Zero-board LED, antenna and USB part numbers.

## 5. Key findings

### 5.1 Battery and charger compatibility

Detail: [compatibility matrix](docs/g1-battery-charger-compatibility.md).

- The EEMB LP401730 limit is 4.220 V. Every fixed 4.2 V charger examined
  exceeds it: MCP73831-2 4.232 V, TP4056 4.242 V (or 4.263 V), BQ2407x and
  BQ25100 4.23 V, BQ25185 at 4.2 V 4.221 V.
- Five of seven finished packs (Jauch, Renata, PKCELL) state "4.2 V" with no
  tolerance. Only a charger whose maximum is at or below 4.200 V passes
  without the pack maker's written confirmation.
- Chargers that pass on documents for every battery: BQ25185 strapped to
  4.1 V (4.1205 V maximum), BQ24079 (4.141 V), BQ25180 programmed to 4.17 V
  or lower (4.19085 V). Capacity lost at the lower voltage is TBD.
- Pack protectors trip at 4.25 to 4.35 V and do not define a charging limit.
- Only Renata ICP401835TPRT includes an NTC. All other packs need a
  separately mounted cell thermistor.
- Jauch LP402025JU allows only 30 mA charging between 0 and +15 deg C.
- Adafruit charger boards 6091 and 4755 default to 1 A; their lowest jumper
  settings are 250 mA and 500 mA. Do not connect a candidate pack to them
  as supplied (risk R-37).
- **Every pairing is NOT APPROVED.**

### 5.2 Peak current against battery discharge limits

- Documented transmit peaks: ESP32-S3 340 mA, ESP32-C3 335 mA.
- Pod worst case from documents: 340 + 85.85 + 3.9 = 429.75 mA, or 493.9 mA
  using the PN532 IC maximum, before the LED and siren driver.
- Stated discharge limits: Jauch LP502030JH 250 mA; Renata ICP521630PM-01
  250 mA continuous and 500 mA non-continuous; Jauch LP402025JU 150 mA;
  Renata ICP402025PC-01 155 mA and 310 mA; Varta 280 mA; PKCELL 150 mA.
- Every 150 to 200 mAh pack, and the Jauch 250 mAh pack, is below the
  transmit peak. This is a flag, not a measured failure (risk R-34).

### 5.3 Power architecture

Detail: [power recommendation](docs/g1-power-architecture-recommendation.md).

- A mirror of the ME6217 regulator sheet says VOUT must not exceed
  VIN + 0.3 V. Feeding 3.3 V into the Zero 3V3 pad with the 5 V net
  unpowered violates that. The canonical sheet is still TBD.
- Native USB VBUS and the 5 V pad are one net on both Zero boards. Only the
  C3 board exposes USB D-/D+ on pads.
- Recommended for evaluation, Option A: dedicated charge USB-C, BQ25185,
  protected pack with NTC, SYS through an LM66100 ideal diode to the 5 V pad,
  native USB-C as a service port. Estimated battery voltage needed for a
  3.0 V rail at 0.43 A is about 3.37 V; part of that is an estimate.
- Option B (charge only when off) keeps MCP73831 but the Pod cannot alarm
  while charging. Option C changes the processor board. Option D reworks the
  board and is not recommended.
- Nothing has been drawn, built or measured.

### 5.4 Mechanical feasibility

Detail: [mechanical feasibility](docs/g1-mechanical-feasibility.md). Targets
are unchanged: Pod 45 x 30 x 16 mm, Keyfob 35 x 25 x 12 mm.

- **Pod: not achievable with the candidates found.** Module boxes other than
  the processor board total 15,078.5 mm3 against a 14,742 mm3 ideal cavity.
  With the smallest documented antenna (10 x 25 mm) and a 200 to 250 mAh
  pack, the 10 mm separation fails every axis-aligned placement tested.
  An end-to-end layout needs about 55 mm outside length; this is a lower
  bound, not a proposed size.
- **Keyfob: unproven and high risk.** It fails with any separate charger
  board. Without one it is marginal: an 8 mm motor has 0.4 mm total
  clearance, the board assembly must be at most about 4.5 mm high, and the
  6.80 mm deep charge receptacle does not fit the 4.5 to 5.0 mm left beside
  the pack.
- No externally driven piezo of 25 mm or less was found that documents
  105 dB. Owner has selected evaluation Direction A only: retain the 24 mm
  reference piezo and investigate a compatible boosted driver; 10 cm is the
  proposed SPL distance. CPT-2475-92T is documented at 92 dB/10 cm and 21 nF;
  PAM8904's 15 nF limit is below the piezo's 21 nF nominal value. PAM8904E is a promising paper-screen candidate: 47 nF load rating, 1.5–5.5 V supply and 20 Hz–300 kHz input; its EVB guide states 16 Vp-p from 3 V with 47 nF. It remains unqualified pending exact datasheet, manufacturer and system checks.

## 6. Validation performed and actual results

### 6.1 Validator runs in this session

The validator is session-local, not in the repository:

```sh
S=/Users/zacktudor/.copilot/session-state/2c446fbc-cda8-45b4-9d42-75911398d217/files
$S/component-freeze-review/pdf-tools/bin/python \
  $S/validate-component-registers.py --sources --handoff
```

| Run | Validator state | Result |
| --- | --- | --- |
| Start of session, on clean `6149d7a` | Revision 0.2 validator, unchanged | Not rerun; last recorded result PASS, 8108 checks |
| After the revision 0.3 edits | Revision 0.2 validator, unchanged | **FAIL: 20 of 10069 checks**, all listed below |
| After updating the validator | Revision 0.3 validator, `--sources` | PASS: 10686 checks, exit 0 |
| Final, with this handoff | Revision 0.3 validator, `--sources --handoff` | PASS: 10678 checks, exit 0 |

The 20 failures of the unchanged validator were all expectations of the
revision 0.2 state, not defects: the 111-row count; the 14 reference count;
the SRC-01..29 range; the fixed revision and date for the 11 new rows; the
list of 14 numeric rows; the D-01..21 and R-01..33 ranges (two checks each);
and the 12-file scope. No link, table, ASCII, URL-ledger, cross-register or
pin-map check failed. A copy of that validator is kept beside the current
one as `validate-component-registers.rev0.2.py`.

Changes made to the validator, and why they are not a loosening:

- Expected counts, ID ranges, numeric rows and file scope were moved to the
  revision 0.3 state.
- **Added:** both registers' first 111 rows must equal commit `6149d7a`
  exactly; the appended rows must be exactly the 11 named candidates; each
  candidate must be reference-only, `CANDIDATE_OWNER_DECISION` and tied to an
  owner decision; no row may be FROZEN; row order must match between
  registers; dimension-register revision and date are now checked.
- **Added:** O-01..15 must be complete and unique; no PDF, ZIP or DWG may be
  tracked by Git; no file may exist under the design-stage directories.
- **Added:** all 61 names in `SHA256SUMS` must appear in the evidence README;
  with `--sources`, the local folder must contain exactly those files with
  matching hashes and must be ignored by Git.
- **Added:** eleven arithmetic checks for the new documents.
- No existing check was removed.

Final validator output:

```text
Source PDFs: 14 signature/parser/page-count/SHA-256 checks completed.
Evidence folder: 61 local files match SHA256SUMS; folder is ignored by Git.
PASS: 10678 checks; 122 matching register rows; 111 revision 0.2 rows unchanged; 75 original IDs retained.
PASS: 22 drawing-qualified partial rows; all remaining numeric dimensions TBD; 11 candidates, none selected or FROZEN.
PASS: 356 local Markdown/CSV links and anchors; document formatting and 20-file allowed scope.
PASS: S3/C3 contact maps, PN532/MPU pin coverage, I2C notation and enclosure/voltage/current arithmetic.
No hardware, ERC/DRC, CAD-fit or manufacturing qualification is implied.
```

### 6.2 What the checks cover

| Check | Result |
| --- | --- |
| CSV headers and row counts | PASS: 122 rows each; 30 and 24 columns; no empty or ragged fields |
| Unique and matching IDs | PASS: 122 unique IDs, identical set and order in both registers |
| Preservation | PASS: 75 original IDs retained; 111 revision 0.2 rows byte-identical to `6149d7a` |
| Manufacturer and datasheet references | PASS: every source ID and every URL in the registers exists in the SRC-01..53 ledger |
| Evidence for dimensions | PASS at document level: exactly 22 numeric rows, each with an inspected drawing URL and source location; candidates without an inspected drawing stay TBD |
| Registers against documents | PASS: shared fields identical across registers; counts and controlled IDs consistent |
| C3 USB contacts and GPIO, S3 GPIO | PASS: contact maps unchanged; pad 15 = GPIO18 / D-, pad 16 = GPIO19 / D+ |
| Power arithmetic | PASS: regulation maxima, margins, peak budget and shortfalls recomputed |
| Mechanical arithmetic | PASS: volume, footprint, separation and Keyfob screens recomputed |
| Markdown links | PASS: all local links and anchors resolve; external URLs are not fetched |
| Scope | PASS: no governing file changed; no design-stage file; no document tracked by Git |

Additional checks outside the validator: both CSVs round-trip
byte-identically through Python `csv` with `QUOTE_ALL` and LF endings;
`git diff --check` is clean; the full diff was read before committing.

### 6.3 Design verification not performed

No ERC, DRC, CAD fit, assembly trial, battery, charging, protection, RF, NFC
read-range, acoustic, haptic, thermal or runtime test has been performed.
Every PASS above is a documentation-consistency check. External URL
availability, distributor stock and delegated leads are not validated.

## 7. Research documents

**On GitHub: none.** No manufacturer PDF, ZIP or drawing is tracked. No
redistribution right was found for any document, and several forbid copying
outright; see [docs/datasheets/README.md](docs/datasheets/README.md).

**Local only, on the research Mac, backup status not verified:**

| Location | Content |
| --- | --- |
| `docs/datasheets/local/` in the working copy, ignored by Git | **61 local files**: 50 primary PDFs, 10 single-page extracts, 1 ZIP |
| `/Users/zacktudor/.copilot/session-state/2c446fbc-cda8-45b4-9d42-75911398d217/files/component-freeze-review/` | The 14 PDFs and 8 extracts from revision 0.2, with text extractions, renders and the PDF tool environment |
| `/Users/zacktudor/.copilot/session-state/2c446fbc-cda8-45b4-9d42-75911398d217/files/g1-candidates/` | The 36 new PDFs, extracts, fetched web pages, text extractions and renders |

To verify: from `docs/datasheets/local/` run
`shasum -a 256 -c ../SHA256SUMS`. To restore on another machine, download
from the URLs in the evidence README and compare hashes. The Elechouse DWG
archive was downloaded and hashed but not opened.

`build_registers.py` and `refine_registers.py` in the first session folder
must **not** be rerun: the generator would overwrite the registers.

## 8. Pinout corrections and current allocations

No pinout changed in this session. Retained from revision 0.2:

- **Correction (SRC-05):** on the ESP32-C3-Zero V2, pad 15 = GPIO18 / USB D-
  and pad 16 = GPIO19 / USB D+. Revision 0.1 had the pair reversed.
- **S3-Zero P15:** 1 = GPIO43 TX through 499 ohm; 2 = GPIO44 RX; 3..15 =
  GPIO13..GPIO1; 16 = 3V3; 17 = GND; 18 = VBUS / 5 V pad. Reserved:
  GPIO0/3/45/46 straps, GPIO19/20 USB, GPIO21 RGB.
- **C3-Zero V2:** 1 = 5 V / VBUS; 2 = GND; 3 = 3V3; 4..14 = GPIO0..GPIO10;
  15 = GPIO18 D-; 16 = GPIO19 D+; 17 = GPIO20 RX; 18 = GPIO21 TX.
- **Pod baseline (specification):** GPIO4 SDA, GPIO5 SCL, GPIO6 piezo PWM,
  GPIO7 button, GPIO8/9 tether. **Proposed:** GPIO1 battery ADC, GPIO10 NFC
  IRQ, GPIO11 NFC RSTPD_N, GPIO12 IMU INT, GPIO13 charge status.
- **Keyfob proposed:** C3 GPIO0 ADC, GPIO1 status, GPIO3 motor, GPIO4 button;
  S3 alternative GPIO1, GPIO13, GPIO6, GPIO7.
- I2C: PN532 7-bit 0x24; MPU-6050 0x68 (AD0 low) or 0x69.

New constraint from this session: the recommended NFC module brings out
RSTPD_N but **no IRQ**, so the proposed GPIO10 connection would be unused and
polling required if that module is chosen. The module's I2C pull-up
positions are unpopulated.

## 9. Engineering decisions

Full text: [docs/design-decisions.md](docs/design-decisions.md). Nothing was
decided in this session except the documentation rule D-22.

| Decision | Status |
| --- | --- |
| D-01 Documentation before PCB/CAD | APPLIED-DOC |
| D-02 Keyfob processor selection | OPEN; C3 evaluation PROPOSED |
| D-03 Battery regulation and Zero-board USB isolation | OPEN, safety-critical; new evidence against 3V3 injection |
| D-04 Charger, temperature supervision and load sharing | OPEN; BQ25185 recommended for owner decision |
| D-05 Finished battery assemblies | OPEN; candidates shortlisted |
| D-06 Shared I2C and additional GPIO | GPIO4/5 BASELINE; supporting connections PROPOSED |
| D-07 Piezo driver and acoustic specification | OPEN; no 105 dB part found |
| D-08 Optional USB-C-form tether | OPEN; not researched |
| D-09 Paired encrypted ESP-NOW and freshness | PROPOSED |
| D-10 NFC compatibility and security claim | OPEN |
| D-11 Button recovery, learning and reset | OPEN |
| D-12 Alarm origin, priority and fault states | OPEN |
| D-13 Target dimensions are not a fit commitment | OPEN; Pod target not achievable with candidates found |
| D-14 Serviceable parametric enclosure construction | PROPOSED |
| D-15 NFC duty cycle versus radio sleep and alert latency | OPEN |
| D-16 Onboard RGB source inconsistency | OPEN |
| D-17 GY-521/MPU-6050 identity and lifecycle | OPEN; lifecycle lead recorded |
| D-18 Quantified acceptance criteria | OPEN |
| D-19 Power-switch accessibility and armed-state retention | OPEN |
| D-20 Component identity and release provenance | PROPOSED verification rule |
| D-21 Evidence register is not a physical freeze | APPLIED-DOC; hardware selections OPEN |
| D-22 G1 candidates are recommendations, not selections | APPLIED-DOC; every selection OPEN |

Decisions that only the owner can take are O-01 to O-15 in
[docs/g1-owner-decisions.md](docs/g1-owner-decisions.md). Seven change the
specification: O-01 Pod size, separation or battery; O-02 charger family;
O-03 sound level; O-04 IMU module; O-05 piezo driver; O-06 Keyfob size or
construction; O-07 battery capacity ranges. Eight are within it: O-08 NFC
module; O-09 power architecture; O-10 behaviour while charging; O-11 battery
supplier; O-12 Keyfob processor; O-13 motor; O-14 battery connector; O-15
handling of datasheets.

## 10. Unresolved questions (HOLD/TBD)

### 10.1 Components

- **PN532 module:** no schematic for the candidate; ROM suffix, regulator and
  the 2.7 to 5.5 V versus 3.3 to 5.0 V supply statement unresolved; DWG
  unopened; antenna thickness TBD.
- **MPU-6050 module:** candidate out of stock; schematic not inspected;
  lifecycle unconfirmed from a source that could be read directly.
- **Batteries:** no charge-voltage tolerance for five of seven packs; no
  pulse-discharge data; Renata thresholds unpublished; applicability of the
  2014 PKCELL drawing; connector, polarity and wire length.
- **Charger:** owner approval of a non-specified family; package drawing not
  inspected; NTC part and network; strap values are worked examples only.
- **Piezo and driver:** 10 cm is the proposed measurement distance, but 105 dB
  remains unproven and D-18 method is open. PAM8904E passes an initial paper
  screen only; actual load behaviour, output versus supply, permitted piezo
  drive, power, EMI, thermal limits and exact package remain to be verified.
- **Motor:** no continuous-duty data; start under a sagging rail.
- **Switches and connectors:** dimensions not read from drawings; footprint
  equivalence of PCM12SMTR and MSK12C02 unchecked; tether not researched.
- **Zero boards:** received revision, assembled height, regulator identity,
  fitted LED, antenna and USB receptacle part numbers.

### 10.2 Dimensions

- 100 register rows have no numeric dimensions. The 22 numeric rows are
  partial and exclude installed envelopes.
- Zero board assembled height and USB overhang are the largest single gap
  for the Keyfob.
- Numeric antenna keepouts (2.4 GHz and NFC) remain TBD.

### 10.3 Power

- Whether any candidate pack can supply the transmit peak (R-34).
- Capacity and runtime at a 4.1 V charge limit.
- Reverse leakage of the fitted regulator; behaviour of USB-C sources with
  a pre-biased VBUS (R-36).
- Keyfob charge current below +15 deg C.
- Closed-case temperature of a linear charger beside the cell.
- LED and siren-driver current are not in the peak budget.

### 10.4 Mechanical

- Pod: O-01 Option A selected; enlarged length lower bound about 55 mm, but full envelope and fit remain TBD.
- Keyfob: whether a carrier stage or a larger body is authorised (O-06).
- Piezo size against the sound-level target (O-03).
- Battery under the processor board would cover the ceramic antenna (R-17).

### 10.5 Research access

- TDK MPU-6050 and PS-series pages, Murata PKM specifications and C&K
  PDFs returned HTTP 403. DigiKey and Mouser blocked automated reads, so all
  their stock figures are unverified leads.
- No evidence gap in section 10.1 to 10.4 is a network failure; they need
  supplier answers, received parts or measurements.

## 11. Exact next step

**Continue the O-03/O-05 paper investigation; do not ask the owner to perform
hardware work.** First inspect the current full PAM8904E datasheet and package
drawings, then obtain manufacturer clarification from Diodes and Same Sky on
the driver/transducer load, drive waveform, frequency sweep and operation
above the piezo's 10 Vp-p rated condition. Compare at least one alternative
driver, build the battery-current/thermal/EMI paper budget, and keep D-18's
acoustic measurement method open until the owner reviews a complete proposal.
Use [docs/g1-piezo-driver-compatibility.md](docs/g1-piezo-driver-compatibility.md)
as the starting point. The owner does not need to buy, wire, open or test
anything now.

Other O-04 and O-06 to O-15 decisions and A-1 to A-4 authorisations remain
open. Do not treat this driver research as permission to begin design or
physical testing.

Then, in order, and only as far as the owner authorises:

1. Send written enquiries (A-2) to Jauch and Renata for charge-voltage
   tolerance, pulse-discharge rating and protection thresholds; to Elechouse
   for the PN5321 MINI schematic and antenna thickness; to Waveshare for the
   regulator identity and board height; to Top Power for the TP4056
   tolerance conflict.
2. Open the Elechouse DWG archive already held locally and record its
   dimensions; inspect the BQ25185 package drawing and the Adafruit 3886
   board files.
3. If samples are authorised (A-1), measure the items in owner decisions
   section 4 and record them in `docs/reports/`, labelled as measurements
   and kept separate from manufacturer data.
4. Update only the affected register rows; keep everything else TBD. Update
   the session validator's expected state and rerun it.
5. Re-screen both enclosures with the measured board height.

Do not rerun the register generator, repeat research already recorded, start
KiCad, FreeCAD, firmware or manufacturing work, connect any cell to a
charger, or purchase anything without independent electrical and physical
review and explicit human authorisation.

## 12. History

- **2026-11-11, G0 (`13863c9`, revision 0.1):** eight-document design basis
  and the original 75-row register.
- **2026-11-11 to 2026-11-12, revision 0.2 (`13eb171`, `577067c`,
  `6149d7a`):** registers extended to 111 rows; SRC-23..29 and D-21 added;
  C3 USB pad pair corrected. An earlier "Main pass failed" was a model
  connection timeout after `refine_registers.py` had succeeded; details are
  in [docs/datasheet-index.md](docs/datasheet-index.md) section 7 and in the
  previous revision of this file.
- **2026-11-12, revision 0.3:** G1 candidate research; 11 candidate rows;
  SRC-30..53, D-22, R-34..39 and O-01..15 added; evidence folder manifest
  created; no selection, purchase or design-stage work.
- **2026-11-12, revision 0.4:** owner selected O-01 Option A (enlarge Pod);
  owner-decisions and mechanical-feasibility documents updated.
- **2026-11-12, revision 0.5:** owner selected O-02 Option A (evaluate BQ25185
  at 4.1 V only); owner-decisions and power-recommendation documents updated.
  No purchase, design, build, battery connection, test or component freeze authorised.


## 13. Latest owner direction — O-03/O-05 (2026-11-12)

**Evaluation direction only:** retain the 24 mm Same Sky CPT-2475-92T as the
reference piezo and investigate a compatible boosted driver. The proposed
105 dB measurement distance is 10 cm. This does not approve 105 dB as a final
acceptance criterion, the piezo, a driver IC, a circuit or a component pairing.

Important compatibility finding: CPT-2475-92T is nominally 21 nF; Diodes
PAM8904 specifies a maximum 15 nF load. PAM8904 is therefore not a qualified
match. Do not design around it without written manufacturer confirmation or
a different piezo/driver combination. The piezo's documented SPL is 92 dB at
10 cm; 105 dB remains unproven.

Next technical checks:
1. Verify the transducer's full voltage, waveform, capacitance tolerance and
   response over the full 2.8–4.2 kHz sweep.
2. Identify boosted drivers with adequate capacitive-load rating, output
   topology, voltage, input frequency and protection; request manufacturer
   confirmation for borderline loads.
3. Calculate battery peak current, boost losses, decoupling and interaction
   with radio/NFC/IMU loads.
4. Review switching EMI, layout, output protection and thermal limits.
5. Define D-18's weighting, peak/average statistic, duty, alarm duration,
   sweep, tolerance and measurement geometry.
6. Obtain evidence for actual SPL from the exact transducer/driver and final
   enclosure; do not extrapolate SPL from voltage.
7. Recheck Pod packaging including driver IC, boost capacitors, acoustic port,
   antenna keepouts and mounting.
8. Establish controlled test procedures and hearing-safety controls before
   any physical test.

**No purchase, schematic/PCB design, construction, battery connection or
physical test is authorised.** O-03/O-05 and D-07/D-18 remain OPEN; G1
physical component freeze remains BLOCKED.

History update: O-03/O-05 Direction A and the 10 cm proposed distance were
recorded as evaluation-only on 2026-11-12. No part is selected or frozen.


## 14. Latest O-03/O-05 research update — PAM8904E (2026-11-12)

Created [docs/g1-piezo-driver-compatibility.md](docs/g1-piezo-driver-compatibility.md)
and linked it from the owner-decision document.

Verified manufacturer-data screen:
- Same Sky CPT-2475-92T: 24 mm x 7.5 mm, 10 Vp-p rated, 1–30 Vp-p
  operating range, 92 dB at 10 cm under 4 kHz / 10 Vp-p / half-duty
  square-wave conditions, and 14.7–27.3 nF capacitance at 120 Hz.
- Diodes PAM8904: 15 nF maximum load; not a qualified match for the 21 nF
  nominal reference piezo.
- Diodes PAM8904E: 47 nF maximum load, 1.5–5.5 V supply, 20 Hz–300 kHz
  input. The EVB guide states up to 16 Vp-p from 3 V with 47 nF. This makes
  it the leading paper-screen candidate, not an approved match.
- Important caution: the piezo's 10 Vp-p rating is below the EVB guide's
  16 Vp-p heavy-load example. Its 1–30 Vp-p operating range does not by itself
  prove safe long-duration operation at that waveform. Manufacturer
  confirmation is required before any component recommendation or test.
- 105 dB is not proven. The 92 dB datasheet figure is not labelled dBA.
  The 10 cm distance remains proposed; D-18 is still open.

Next: inspect current full PAM8904E datasheet and package drawing; request
written confirmation from Diodes and Same Sky; screen an alternative driver;
calculate power/current/thermal/EMI implications; and revisit acoustic
acceptance criteria. No purchase, schematic, PCB, construction, battery
connection or physical test is authorised.

Research source URLs:
- https://www.diodes.com/part/view/PAM8904E
- https://www.diodes.com/assets/Evaluation-Boards/PAM8904E_EVB-User-Guide.pdf
- https://www.sameskydevices.com/product/resource/cpt-2475-92t.pdf

Commit sequence: report 89ee70c; owner-decision update 58193fb; handoff update
pending verification.


## 15. O-03/O-05 deeper driver research — 2026-11-12

Expanded [docs/g1-piezo-driver-compatibility.md](docs/g1-piezo-driver-compatibility.md)
to revision 0.4 following direct inspection of the full Diodes PAM8904E
datasheet (DS41667 Rev. 4-2, July 2023), the March 2025 EVB guide and the
Same Sky CPT-2475-92T datasheet (dated 2024-09-11).

Additional verified findings:
- PAM8904E absolute maximum VIN 6.0 V and VOUT 15 V. 3x mode is limited to
  VDD 1.5–4.5 V; 1x and 2x modes are listed for 1.5–5.5 V. The datasheet
  warns against 3x mode at VIN >=4.5 V and says VOUT must not exceed 13.5 V
  in 3x mode.
- At VIN 3.0 V, 47 nF and 3.2 kHz, typical input current: 4.3 mA in
  single-ended 3x and 14.2 mA in differential 3x. These are typical,
  not maxima, and not measured with the CPT-2475-92T.
- Typical 3x start-up time 1.91 ms; typical shutdown delay 42 ms.
- Active 2 x 2 mm order codes: PAM8904EGPR (W-QFN2020-12, max height
  0.80 mm) and PAM8904EGPR-T (U-QFN2020-12, max height 0.65 mm).
  The 3 x 3 mm JPR/JER variants are marked NRND.
- EVB passive network: 2.2 uF / 16 V input capacitor, two 1 uF / 25 V
  charge-pump capacitors and 2.2 uF / 25 V output capacitor. These parts,
  placement and derating must be included in mechanical and electrical
  feasibility.
- Same Sky's frequency-response graph is not flat across the requested
  sweep; it shows a broad dip near 2 kHz and higher response around 4–5 kHz.
  Exact SPL at 2.8 and 4.2 kHz cannot be read as guaranteed numeric values.
  The 92 dB rating is specified at 4 kHz, 10 cm, rated 10 Vp-p and half-duty
  square wave; weighting is not stated.
- No second compact integrated driver with a verified capacitive-load rating
  adequate for this transducer was found in this research pass. PAM8904
  remains disqualified as a match due to its 15 nF load limit. A discrete
  boost plus output bridge is a distinct, more complex fallback architecture,
  not a drop-in substitute.

Current technical position:
- PAM8904E is the only integrated driver candidate found so far with a
  documented 47 nF load rating and a frequency input range that covers the
  proposed sweep. It remains a research candidate, not selected.
- The 47 nF rating is promising because the piezo is 21 nF typical and
  27.3 nF maximum at 120 Hz. Frequency-dependent impedance and actual
  output drive compatibility still require written manufacturer confirmation.
- The piezo is rated 10 Vp-p, while the EVB guide demonstrates up to 16 Vp-p
  from 3 V with 47 nF. Do not assume that output is safe for this transducer.
  Investigate low charge-pump mode first on paper, and obtain explicit
  manufacturer limits for waveform, duty and alarm duration.
- 105 dB at 10 cm remains unproven; O-03/O-05/D-07/D-18 remain OPEN.
  No purchase, schematic, PCB, construction, battery connection or test
  authorised.

Next research actions:
1. Prepare manufacturer technical enquiries for Diodes and Same Sky asking
   about the exact transducer/driver pairing, impedance at 2.8/4.0/4.2 kHz,
   permitted differential voltage, waveform, duty, alarm duration, and SPL
   response at both sweep endpoints. Do not claim these enquiries have been
   sent; external correspondence requires an available authorised channel.
2. Complete a documented paper input-current budget using the driver's
   typical 14.2 mA differential 3x datum only as a reference point, not a
   worst-case value. Add battery voltage range, driver mode, simultaneous
   radio/NFC/IMU/LED loads and the unresolved battery pulse-current limits.
3. Review charge-pump capacitor derating/ESR, thermal loss, 100 kHz switching
   EMI and layout guidance against NFC/IMU/radio sensitivity.
4. Compare a different sounder and a discrete driver architecture only if
   manufacturer confirmation does not support this pairing.
5. Keep the Pod packaging and acoustic acceptance criterion open until
   external passive components, sounder response and D-18 test method are
   known.

No local CAD/PCB or hardware work was started. No components were ordered.


## 16. Current follow-up documents — 2026-11-12

Created [docs/g1-piezo-manufacturer-questions.md](docs/g1-piezo-manufacturer-questions.md)
with a complete technical question set for Diodes Incorporated and Same Sky.
It covers driver/transducer compatibility, differential voltage, mode limits,
frequency sweep, waveform/duty/on-time, current maxima, capacitor derating,
EMI/thermal/layout, and guaranteed SPL data at 2.8/4.0/4.2 kHz.

**Correspondence status: NOT SENT.** No manufacturer reply is recorded.
The question set is prepared for later authorised correspondence; do not
describe the pairing as manufacturer-confirmed.

Updated [docs/g1-piezo-driver-compatibility.md](docs/g1-piezo-driver-compatibility.md)
to revision 0.3:
- Added an indicative 508.1 mA Pod peak-current arithmetic scenario
  (existing 493.9 mA screen plus 14.2 mA typical PAM8904E differential
  3x/47 nF/3.2 kHz datum). This is explicitly not a worst-case or validated
  current. It flags battery headroom: the scenario is 8.1 mA above the
  Renata pack's stated 500 mA non-continuous rating.
- Added the transducer frequency-response-graph warning: its response is
  not flat over the requested sweep, and exact SPL at 2.8/4.2 kHz is not
  guaranteed by the graph.
- PAM8904E remains the only integrated driver found in this research pass
  with a published load rating adequate on paper; it is not selected.
- O-03/O-05/D-07/D-18 remain OPEN; no component freeze or physical work
  authorisation.

Updated owner decisions to revision 0.8 and linked both the technical report
and manufacturer question set. All files remain documentation-only.

Exact next research step: complete a deeper alternative-sounder and discrete
driver architecture screen, then reconcile manufacturer questions and
current/thermal/EMI calculations. No purchase, schematic, PCB, construction,
battery connection or physical test is authorised.


## 17. Alternate transducer and discrete driver screen — 2026-11-12

Expanded the compatibility report to revision 0.4:
- VCC PT-PM24-0538-RK: 24 mm, 5.2 mm high, 90 dB at 10 cm, 3.8 kHz,
  5 V, 5 mA. It is compact but does not improve on the Same Sky 92 dB
  reference or approach 105 dB.
- Multitrack TFM-25: 80 dB(A) minimum at 10 cm, 9 Vp-p, 4.0 kHz ±0.5 kHz,
  9.5 nF ±30% at 1 kHz, 25 Vp-p allowable input. Smaller capacitance but
  materially lower documented sound level; not a better candidate for O-03.
- Discrete boost plus bridge is technically possible, supported as a
  general architecture by TI/Same Sky application literature. It adds
  inductor, switching node, high-voltage passives, output bridge, EMI and
  protection complexity. Resonant-inductor drive is not a good first option
  for a 2.8–4.2 kHz sweep because it is frequency-specific and sensitive to
  capacitance variation.
- No alternate sounder found in this pass that meets 105 dB at 10 cm in a
  24–25 mm body with verified conditions.

The leading research path remains PAM8904E + CPT-2475-92T, but no safe
voltage/duty/time operating point has been established. Manufacturer
questions are prepared but NOT SENT. No second compact integrated driver
has been verified.

Exact next step: perform a final consistency pass on the O-03/O-05 report,
owner decision and handoff; then await or obtain authorised manufacturer
responses before making any component recommendation. No external enquiry
has been sent, and no purchase, circuit design, build or test is authorised.


## 18. Hackathon implementation direction — owner-confirmed 2026-11-12

The owner clarified that this is a self-built hackathon project, not a
manufacturer qualification exercise. The required deliverables include
actual editable PCB and CAD designs. The owner confirmed the assistant should
proceed on that basis.

### Controlling direction

- Start provisional schematic and PCB design now; do not wait for supplier
  correspondence or closure of every G1 research question.
- Start parametric enclosure CAD now and co-design it with the PCB.
- Create separate Pod and Keyfob KiCad projects and FreeCAD models.
- Manufacturer questions are optional and only for a genuinely blocking
  technical issue. No enquiries have been sent.
- Unknowns are managed as explicit provisional inputs, not blanket blockers.
- Maintain sensible component limits and LiPo safety. Design permission does
  not imply battery connection, energised testing or fabrication orders.

### Actual current state

- Native KiCad projects: NOT YET CREATED.
- Native FreeCAD models: NOT YET CREATED.
- PCB schematic/layout: NOT STARTED.
- Enclosure parametric CAD: NOT STARTED.
- Gerbers, drill files, STEP/STL and assembly drawings: NOT STARTED.
- No components purchased; no physical testing claimed.

### Immediate implementation sequence

1. Inspect repository structure and existing project files before creating
   anything; retain the established register and source evidence.
2. Create the Pod and Keyfob KiCad project skeletons with project settings,
   board outlines and interface/connectors.
3. Create FreeCAD parametric Pod and Keyfob envelopes and a top-level assembly.
4. Build a shared component-envelope/interface register and coordinate system.
5. Place real component envelopes; mark placeholders and unknowns visibly.
6. Draft the power, MCU, NFC, IMU, audio and haptic schematic blocks.
7. Route boards only after footprint/pin mappings and schematic nets are checked.
8. Iterate the enclosures against the actual PCB and component envelopes.
9. Run ERC/DRC, geometry/clearance checks, export manufacturing files and
   write full assembly instructions.

### Working dimensions and design assumptions

- Pod: start at >=55 mm external length; 30 mm width and 16 mm height are
  provisional and may grow when actual packaging is modelled.
- Keep the proposed 10 mm NFC antenna-to-battery separation as a CAD keepout.
- Keyfob: 35 x 25 x 12 mm is a starting envelope, not an absolute limit.
- PAM8904E: first integrated-driver paper candidate only; isolate it as a
  provisional block until a drive mode within piezo limits is selected.
- Charger/power path: BQ25185 4.1 V evaluation direction only; power design
  remains provisional until the complete cell/charger/regulator path is
  internally checked.

### Repository references updated

- AGENTS.md: hackathon implementation mandate.
- PROJECT_SPEC.md: PCB/CAD deliverable amendment.
- docs/development-roadmap.md: parallel PCB/CAD workstreams.
- docs/g1-owner-decisions.md: provisional design authorisation recorded.
