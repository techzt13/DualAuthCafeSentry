# Last Worked On - Dual-Auth Cafe Sentry

Date: 2026-11-13
Package revision: 0.4
Project stage: native KiCad schematics are under active implementation; Pod schematic has MCU/module interfaces and a wired provisional NFC reset; Keyfob schematic now contains a provisional C3-Zero interface and protected motor-switch block. The Keyfob PCB now has a provisional upright C3-Zero 2x9 footprint, 37 x 25 mm carrier outline with an antenna relief notch, 22 assigned pad nets and top-side motor-driver passives; it remains unrouted and the land pattern/antenna clearance are unverified. The proposed Keyfob enclosure is 42 x 30 x 15.5 mm. The Pod PCB remains outline-only. FreeCAD macro exists but has not been run.

**Important live-state correction:** the older milestone notes below are historical. The live Keyfob schematic is NOT empty: it contains U1 ESP32-C3-Zero logical contacts, J1 motor wire pads, Q1 IRLML6344 low-side MOSFET, R1 100 Ω gate resistor, R2 100 kΩ gate pull-down, D1 flyback diode, C1 100 nF, C2 10 µF and SW1 active-low button. During this work D1 was changed from 1N4148W to Nexperia PMEG2010AEB,115 (20 V, 1 A, SOD-523); the schematic diode pin mapping and draft PCB footprint were updated. This is a paper-level correction, not an ERC/DRC or hardware validation.

Pod power and audio blocks are still not complete. Battery/charger pairings and all power rails remain HOLD. O-01 Pod enlargement and O-02/O-03/O-05 evaluation choices are not component approvals. Neither board is fabrication-ready; no physical parts are purchased, built or tested. CAD remains draft envelope geometry and no fit check is claimed.

Before continuing, read [PROJECT_SPEC.md](PROJECT_SPEC.md), [AGENTS.md](AGENTS.md), this file and relevant docs references. The repo is techzt13/DualAuthCafeSentry, branch master.

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
| K-BATTERY | Renata ICP521630PM-01, then Jauch LP402025JU+PCM+2 WIRES 50MM | Meets 150 mAh minimum; highest stated rating in class | Rating still 25 mA below the transmit peak; no NTC |
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
  Renata ICP521630PM-01 155 mA and 310 mA; Varta 280 mA; PKCELL 150 mA.
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


## 19. First native design workspace milestone — 2026-11-12

Created the first editable hardware/CAD source workspace in GitHub.

### KiCad starter projects created

- `hardware/sentry-pod/sentry-pod.kicad_pro`
- `hardware/sentry-pod/sentry-pod.kicad_sch`
- `hardware/sentry-pod/sentry-pod.kicad_pcb`
- `hardware/pocket-keyfob/pocket-keyfob.kicad_pro`
- `hardware/pocket-keyfob/pocket-keyfob.kicad_sch`
- `hardware/pocket-keyfob/pocket-keyfob.kicad_pcb`

Both PCB files contain only a provisional Edge.Cuts outline and a draft label.
Pod carrier outline: 49 x 24 mm. Keyfob carrier outline: 27 x 20 mm. These
are initial packaging placeholders, not approved final board sizes. No
footprints, nets, copper zones, routing or components are present. The
schematic sheets are intentionally empty starter sheets; no electrical
schematic is claimed complete. KiCad CLI/ERC/DRC validation has not been run
in this environment.

### FreeCAD parametric starter source created

- `cad/create_enclosures.FCMacro`
- `cad/README.md`

The macro creates editable FreeCAD documents for a Pod starting envelope
55 x 30 x 19.3 mm and Keyfob starting envelope 38 x 28 x 14 mm, including
lower shell, lid and translucent component-envelope placeholders. It saves
FCStd and draft STEP/STL exports to the user's home directory when run in
FreeCAD. FreeCAD is not installed in this execution environment, so no
FCStd/STEP/STL output has been generated or validated yet.

### Important corrections and next implementation work

- The mechanical requirements baseline originally says 45 x 30 x 16 mm; the
  owner later selected an enlarged Pod direction of at least approximately
  55 mm length. The 18.3 mm height is a calculated lower-bound starting
  envelope from the reference cell plus separation and assumed walls, not a
  proven fit. Continue parametric sizing rather than freezing these dimensions.
- Keyfob 38 x 28 x 14 mm is a provisional increase from the 35 x 25 x 12 mm
  target to make room for a 23.5 x 18 mm Zero module and assembly clearance.
- Pod NFC antenna and battery boxes in the macro are visual placeholders only;
  their placement must be revisited because the 10 mm nearest-surface gap,
  piezo separation, actual antenna and protected-pack envelope must all be met.
- First next task: install/use KiCad and FreeCAD locally to open the starter
  files, confirm parser validity, then build the real Pod schematic blocks and
  replace the blank PCB outline with the component/connector placement.
- Do not call these files a finished PCB or finished CAD assembly. They are
  native editable design starters and the first implementation milestone.


## 20. Pod low-voltage interface contract — 2026-11-12

Created `hardware/sentry-pod/interface-contract.md` (revision 0.1) as the
first actual electrical-design translation of the verified pinout records.

### Work completed

- Mapped the Waveshare classic no-header ESP32-S3-Zero SKU 25081 P15 contacts
  to the existing Pod logical nets, preserving the verified contact/GPIO
  distinction.
- Defined the Pod low-voltage interface boundary for shared I2C, PN532 IRQ
  and reset, MPU-6050 interrupt, button, optional tether, audio logic control,
  battery ADC and conditioned charge status.
- Recorded the PN532 0x24 and MPU-6050 0x68 address plan and the requirement
  to audit module pull-ups before adding carrier pull-ups.
- Marked the S3 3V3 and shared USB VBUS/5V contacts as power-interface HOLDs.
- Explicitly left physical module connector order, connector footprints,
  Zero-board pad footprint, module supply/logic compatibility and unknown
  pull-ups as TBD rather than inventing them.
- Updated `docs/hackathon-build-plan.md` and `hardware/README.md` to reflect
  the real implementation state instead of claiming that no native files
  exist.

### Validation and limitations

This is a logical interface contract based on
`docs/verified-pinouts.md`, `docs/pinout.md` and
`docs/power-architecture.md`. It is not a native schematic, physical wiring
release or footprint drawing. No KiCad ERC/DRC, electrical simulation,
physical module inspection or hardware test was run. The Pod schematic and
both PCB files remain starter-level; no fabrication order is permitted.

### Next work

1. Build a custom KiCad S3-Zero module interface symbol with verified P15
   contact labels; do not assign its physical footprint until drawing
   dimensions and contact geometry are checked.
2. Add the Pod logical module interfaces and bus labels to the schematic.
3. Continue the Keyfob interface contract and motor driver design.
4. Resume FreeCAD co-design with actual carrier-board and connector envelopes.


## 21. Keyfob low-voltage interface contract — 2026-11-12

Created `hardware/pocket-keyfob/interface-contract.md` (revision 0.1).

### Work completed

- Recorded the C3-Zero (SKU 25452, ESP32-C3FH4, V2 schematic) as the
  preferred evaluation controller, while preserving the S3-Zero alternative;
  O-12 remains an owner decision and neither is frozen.
- Mapped the C3 contact allocation for battery ADC, conditioned charge status,
  motor control, button, onboard RGB, native USB and service UART.
- Defined the motor-control boundary: GPIO drives only a transistor/driver
  input; the motor is not connected directly to an MCU pin. Hardware OFF
  bias, motor current, flyback path, PWM and duty limits remain to be designed.
- Recorded 3V3 and shared USB VBUS/5V power holds and kept battery wiring
  unreleased.
- Updated the hardware README and hackathon plan to include both interface
  contracts.

### Validation and limitations

The contract translates `docs/verified-pinouts.md` and `docs/pinout.md`.
It is not a native schematic or wiring release. No motor datasheet-based
driver values, physical footprints, ERC/DRC or hardware tests are claimed.
The Keyfob schematic remains an empty starter sheet and its PCB remains
outline-only.

### Next work

1. Convert both logical interface contracts into native KiCad schematic
   symbols and labelled blocks.
2. Inspect the exact Waveshare drawings to establish module pad geometry
   before assigning footprints.
3. Develop a provisional motor low-side driver and a separate Pod piezo
   driver block without connecting either to an unverified battery rail.
4. Continue enclosure-to-board integration.


## 22. Pod NFC reset circuit endpoint audit — 2026-11-12

The live Pod schematic was inspected directly after an earlier status message
incorrectly described the NFC reset network as unwired. The current file already
contains the required wire geometry. The earlier diagnosis was stale/incorrect;
no duplicate wires were added.

Verified endpoint mapping in
`hardware/sentry-pod/sentry-pod.kicad_sch`:

| Component | Pin endpoint | Connected net |
| --- | --- | --- |
| R1 pin 1 | (237.38, 126) | P_NFC_RESET_CTL |
| R1 pin 2 | (252.62, 126) | Q1 base through the routed wire |
| R2 pin 1 | (237.38, 140) | GND |
| R2 pin 2 | (252.62, 140) | Q1 base node; junction at (262.62, 137.46) |
| Q1 pin 1 / base | (272.38, 137.46) | R1/R2 base node |
| Q1 pin 2 / emitter | (272.38, 140) | GND |
| Q1 pin 3 / collector | (272.38, 142.54) | Reset node through routed wire |
| R3 pin 1 | (237.38, 154) | P_3V3_PERIPH_HOLD |
| R3 pin 2 | (252.62, 154) | P_NFC_RESET_N / Q1 collector |

The circuit is a low-side NPN reset sink: GPIO control through 10 kΩ base
resistor, 100 kΩ base-emitter pull-down, 10 kΩ reset pull-up to the held
peripheral rail. Q1 is provisionally MMBT3904, SOT-23; the schematic's
pin-number mapping is base=1, emitter=2, collector=3. The peripheral rail
remains intentionally unsourced, so the circuit must not be energised.

This is an endpoint/connectivity inspection, not KiCad ERC, SPICE simulation,
physical assembly or reset-timing validation. The complete schematic remains
a draft; footprints, board layout, power architecture and ERC/DRC are not
released.

### Next implementation steps

1. Build the Keyfob schematic's motor low-side switch with a default-OFF gate
   or base bias, a flyback path across the motor, and a dedicated motor
   connector; size the switch and suppression against the actual motor
   datasheet, not an assumed GPIO current.
2. Keep the motor rail as a named HOLD until the battery/regulator architecture
   is internally reconciled.
3. Add the Pod audio driver as a separately isolated provisional block; do not
   choose a drive mode exceeding the piezo's 10 Vp-p rating.
4. Continue CAD and PCB co-design only after exact module/connector footprints
   are source-grounded.
5. Run KiCad parser/ERC/DRC locally when available; do not claim these checks
   have passed yet.


## 23. Keyfob motor-driver schematic audit and flyback upgrade — 2026-11-13

Inspected the live hardware/pocket-keyfob/pocket-keyfob.kicad_sch and found that the previous handoff's statement that the Keyfob sheet was empty was obsolete. The sheet already contained the controller interface, button and a complete provisional motor low-side switch block.

### Live circuit

- U1: Waveshare ESP32-C3-Zero SKU 25452 logical contact symbol. GPIO3 / contact 7 is K_MOTOR_PWM; GPIO4 / contact 8 is K_BUTTON_N. The 5 V and 3V3 board contacts remain HOLD labels.
- Q1: Infineon IRLML6344TRPBF, N-channel SOT-23. Pin 1 gate, pin 2 source, pin 3 drain. The official data sheet specifies maximum RDS(on) 37 mΩ at VGS=2.5 V. At the motor's 124 mA maximum start current, a simple fully-enhanced conduction estimate is 0.57 mW (I²R); this is not a switching-loss or thermal validation.
- R1: 100 Ω in series with the gate.
- R2: 100 kΩ gate-to-source pull-down, establishing default OFF while the MCU pin is high impedance.
- J1: two solder-wire pads; pin 1 red motor positive to K_3V3_MOTOR_HOLD, pin 2 blue motor negative to K_MOTOR_SW.
- C1: 100 nF and C2: 10 µF between the held motor rail and ground. Their final values, voltage ratings and DC-bias derating remain to be checked.
- D1: upgraded from Diodes 1N4148W to Nexperia PMEG2010AEB,115 Schottky, 20 V / 1 A, SOD-523. Pin 1 cathode is on the motor positive rail; pin 2 anode is on the MOSFET drain / switched motor-negative node. This is the correct flyback polarity for a brushed DC motor. The PCB's D1 draft footprint was changed to SOD-523 geometry and matching pin order.
- SW1: active-low button from GPIO4 to ground; firmware must enable and debounce the MCU's internal pull-up.

### Source checks

- Precision Microdrives 308-100 official data: 3 V nominal; 3.6 V maximum operating; 94 mA maximum rated current; 124 mA maximum start current; 8 mm diameter and 3.4 mm body length. Continuous-alert duty remains undocumented in the reviewed source.
- Infineon IRLML6344 official data: 30 V N-channel MOSFET, maximum RDS(on) 37 mΩ at VGS=2.5 V.
- Nexperia PMEG2010AEB official data: 20 V reverse rating and 1 A forward-current class; SOD-523 pin 1 cathode and pin 2 anode.

### Limitations

The Keyfob PCB still lacks the MCU module's verified castellated land pattern, full netlist assignments, C1/C2 footprints, copper routing, ground return and antenna keepout. The existing 33 x 23 mm outline and component placement are mechanical placeholders only. The diode footprint is a draft representation of the SOD-523 package; check it against the current KiCad library and the manufacturer's land-pattern guidance before fabrication. No KiCad ERC/DRC, electrical simulation, bench test or enclosure fit test was run.

The Keyfob battery/charger, K_3V3_MOTOR_HOLD, battery ADC and charge-status conditioning remain unresolved. Do not energise this block from an unreviewed cell or USB source.

### Next work

1. Continue the Pod power subsystem as a separately reviewable, non-energised schematic block; keep the battery and system outputs explicitly HOLD until the full regulator/USB path is reconciled.
2. Add the isolated Pod piezo-driver evaluation block with drive voltage constrained by the piezo's 10 Vp-p rating; no 105 dB claim until measured at 10 cm with a defined weighting and waveform.
3. Complete the Keyfob PCB netlist and module land pattern from verified board drawings, then place C1/C2 and route only after the antenna keepout is known.
4. Extend the FreeCAD models using the real PCB and component envelopes, then run FreeCAD and KiCad locally for geometry, ERC and DRC checks.
5. Keep this file current after each committed design milestone. Do not describe either PCB/CAD model as validated or fabrication-ready until the checks are actually run.


## 24. Pod power and audio design reviews — 2026-11-13

Created two source-grounded design notes to move the Pod from abstract architecture toward actual schematic implementation without connecting unresolved battery or sound-drive rails.

### Power-stage review

- Added hardware/sentry-pod/power-stage-review.md.
- Recorded the current TI BQ25185 Rev. B pin map and conservative 4.1 V / 500 mA input-limit setting: 130 kΩ from ILIM/VSET to ground.
- Calculated a candidate 4.7 kΩ ISET value (~63.8 mA typical) only as a Renata ICP521630PM-01 evaluation screen; no cell/charger pairing is approved.
- Added required IN, SYS and BAT bypass values, NTC requirement and open-drain status interface.
- Corrected an important power-path assumption: BQ25185 SYS is a 4.5 V regulated output, not a 5 V source. An ideal diode does not boost it. The Zero shared USB VBUS/5V interface must remain HOLD until its actual input and regulator behaviour is verified.

### Audio-stage review

- Added hardware/sentry-pod/audio-stage-review.md.
- Same Sky CPT-2475-92T is rated 92 dB minimum at 10 cm at 10 Vp-p, 4 kHz, half-duty square wave; its published rating is 13 dB below the proposed 105 dB criterion.
- PAM8904E remains a candidate because its 47 nF load capability exceeds the transducer's 27.3 nF maximum capacitance figure, but only 1x mode is proposed for initial evaluation.
- 2x/3x operation is not approved. The actual differential waveform must be measured and kept within 10 Vp-p.
- No sound-level performance or 105 dB claim is made.

### Validation status

These are design reviews, not native wired circuits. The Pod power and audio schematic blocks are still to be drawn and source-checked. The power rails remain HOLD; no battery or charger is connected. No ERC/DRC, SPICE, acoustic, thermal or hardware test was run.

### Next work

1. Convert the Pod power-stage review into a dedicated, non-energised KiCad schematic block with explicit HOLD rails and exact BQ25185 pin mapping.
2. Convert the audio review into an isolated PAM8904E 1x-mode evaluation block; keep output terminals separate and voltage-limited.
3. Complete the Keyfob PCB netlist, module land pattern, capacitor placements and antenna keepout.
4. Continue CAD integration, then validate the source projects locally in KiCad and FreeCAD.


## 25. Native Pod power and audio evaluation schematics — 2026-11-13

Created two standalone, editable KiCad schematic blocks so the Pod power and sound circuits have real source files rather than only prose reviews:

- hardware/sentry-pod/pod-power-stage.kicad_sch
- hardware/sentry-pod/pod-audio-stage.kicad_sch

### Power block

- BQ25185 WSON-10 symbol uses the official pin map.
- R1=130k programs the 4.1 V battery setting and 500 mA input limit per current TI Rev. B Table 6-1.
- R2=4.7k is an evaluation-only current setting (~64 mA typical) based on the Renata pack candidate; it does not approve that pairing.
- CIN=1uF, CSYS=10uF (0805 draft footprint), CBAT=1uF.
- SYS, BAT, input, status, CE and TS/MR signals are labelled as HOLD. No battery, USB-C connector, thermistor or processor board is connected.

### Audio block

- PAM8904E W-QFN2020-12 Type US logical symbol uses the manufacturer pin map.
- EN1 is held low; EN2 has a 100k default-OFF pull-down and is the 1x enable; DIN has a 100k default-low pull-down.
- C1=2.2uF input, C2/C3=1uF charge-pump capacitors, C4=2.2uF output; values and effective capacitance remain to be checked.
- Differential VO1/VO2 go to a separate two-pin piezo connector. The piezo terminals are not grounded.
- C2 connects CP1 to CN1; C3 connects CP2 to CN2.
- 1x mode is the only evaluation mode. 2x/3x are not approved; measure the differential waveform and keep it within the transducer's 10 Vp-p rating.

### Validation status

These are standalone schematic blocks, not yet hierarchical sheets integrated into the main Pod schematic or assigned to routed PCBs. All supply/control/output nets are HOLD. The custom symbols and wire endpoints have not been opened in KiCad or passed through ERC. No PCB footprints, routing, simulation, thermal test or acoustic measurement are claimed.

### Next work

1. Open both standalone Pod schematic blocks in KiCad and correct any parser/ERC issues.
2. Integrate them into the main Pod project as hierarchical sheets only after pin/wire audits.
3. Complete the Keyfob board netlist and module land pattern.
4. Build the corresponding PCB placements and parametric enclosure fit checks, then run local ERC/DRC and FreeCAD validation.


## 26. Keyfob carrier footprint and draft net assignment — 2026-11-13

Created a custom KiCad footprint and assigned the first carrier-board nets.

### New footprint

- hardware/pocket-keyfob/footprints.pretty/C3Zero_Castellated_2x9.kicad_mod
- Existing local footprint table already points to hardware/pocket-keyfob/footprints.pretty.
- Footprint library ID: SentryKeyfob:C3Zero_Castellated_2x9.
- Waveshare public documentation gives the module outline as 18.0 x 23.5 mm and shows 2.54 mm castellated contact pitch. The footprint uses 9 contacts per side and maps contacts 1–18 in the documented perimeter order.
- The carrier land pads are provisionally 1.8 x 1.5 mm with row centres provisionally at ±7.62 mm (15.24 mm estimated spacing). These pad dimensions and row-centre datum are not specified by the public dimension drawing; this is an editable engineering estimate and must be checked against the actual module before fabrication.

### Keyfob PCB changes

- Added U1 footprint at the existing rotated 23.5 x 18 mm module envelope position.
- Added board net definitions and mapped U1 pins 1–5, 7 and 8 to the corresponding HOLD/control nets.
- Assigned motor-driver nets to J1, Q1, D1, R1 and R2.
- Added C1 100 nF (0603) and C2 10 µF (0805) top-side draft footprints at PCB local y=11.5, each connected between K_3V3_MOTOR_HOLD and K_GND.
- Corrected the D1 SOD-523 courtyard and body outline to the smaller package envelope.
- Renamed the controller 5V HOLD net consistently as K_5V_BOARD_HOLD.

### Validation and limits

A text-level S-expression balance check passed for the Keyfob schematic, PCB and custom footprint (balanced parentheses and closed strings). This is not a KiCad parser run. KiCad CLI and FreeCAD are not installed in the current execution environment. No ERC, DRC, copper routing, antenna keepout validation, module solder-fit, enclosure fit or electrical test has been run.

The PCB is now a populated placement/net-assignment draft, not a finished routed board. The 33 x 23 mm carrier outline remains provisional. The antenna zone, USB-C overhang, board orientation and pad geometry must be verified against the actual module. SW1 still has no released footprint because the switch part is not frozen.

### Next work

1. Open the Keyfob project in KiCad, run ERC/DRC and inspect U1's pad order/orientation against the actual module.
2. Establish the ceramic antenna keepout and USB overhang; move the motor and passives if required.
3. Add the physical button footprint after the switch choice and mechanical location are resolved.
4. Route the Keyfob PCB only after U1 and the antenna clearance are confirmed.
5. Continue the Pod PCB from the new isolated power/audio schematics and verify all custom schematic symbols in KiCad.


## 27. CAD envelope macro updated to match the Keyfob PCB draft — 2026-11-13

Updated cad/create_enclosures.FCMacro and cad/README.md.

### Macro changes

- The Keyfob motor reference cylinder now follows the PCB's current motor envelope position (PCB local 29,5 translated to CAD global 31.5,7.5).
- Added transparent reference solids for Q1, D1, R1, R2, C1, C2 and J1 at positions translated from the draft PCB.
- Added explicit C3-Zero antenna keepout and USB-C access placeholders. Their end/orientation is intentionally flagged for inspection; the USB placeholder may overlap other envelopes to reveal unresolved packaging.
- Reference solids are retained in the FCStd document and in separate assembly-reference STEP/STL exports. Enclosure-only STEP/STL exports remain separate.
- The battery remains a bare-cell reference envelope, not a protected pack.

### Run instructions

cad/README.md now contains the full macOS FreeCAD 0.21+ procedure, including the Python-console command and output folder ~/DualAuthCafeSentry-CAD.

### Validation status

FreeCAD is not installed in this execution environment, so the macro has not been run. No FCStd, STEP or STL output is claimed. No geometry validity, component fit, USB access, antenna clearance, motor coupling, battery safety or enclosure fit has been verified. The Keyfob shell remains 38 x 28 x 15.5 mm; carrier remains 33 x 23 mm. The USB/antenna orientation is a major open mechanical check.


## 28. C3-Zero footprint row order and spacing corrected from Waveshare drawings — 2026-11-13

Inspected the official Waveshare pinout and dimension images. The earlier draft footprint had the two pad rows reversed and used an over-wide row spacing. Corrected both the embedded U1 footprint in the PCB and the local custom footprint library:

- Contact 1–9 are on the USB-facing left edge in the official top view, ordered from top to bottom.
- Contact 18–10 are on the right edge, ordered from top to bottom.
- Contact pitch is 2.54 mm.
- The row-centre spacing is now a provisional 15.24 mm (±7.62 mm from the footprint origin), inferred from the official drawing; it is not explicitly dimensioned as a numeric row-spacing callout.
- The module outline remains 18.0 x 23.5 mm.
- Pad size remains provisional 1.8 x 1.5 mm and must be checked against the actual module.

The PCB net assignments remain attached to pad numbers and were not changed. The 90-degree module rotation is unchanged. No KiCad parser/ERC/DRC or physical solder-fit check has been run.


## 29. Keyfob passives moved to top-side and footprint layers corrected — 2026-11-13

Moved Q1, D1, R1, R2, C1 and C2 to F.Cu. The battery sits directly below the carrier board with only about 0.9 mm vertical clearance, so bottom-side component placement was a poor fit assumption. C1/C2 were also moved from the motor's draft body area to PCB local y=11.5, between the motor body and motor-wire pad region.

Corrected footprint drawing layers to F.SilkS/F.Fab/F.CrtYd and adjusted the hand-drawn capacitor land pads to approximate standard 0603/0805 dimensions. The Keyfob CAD macro now places the same component envelopes above the carrier PCB.

This is still a placement study. The C3 USB-C connector access envelope may conflict with the motor position, and the antenna keepout location must be checked against the received module. No local KiCad or FreeCAD validation has been run.


## 30. Keyfob upright-module layout revision — 2026-11-13

The previous rotated 90-degree C3-Zero layout was not a satisfactory packaging direction because the USB-C connector and antenna end shared a congested carrier-board region. Reworked the Keyfob mechanical evaluation layout:

- Carrier PCB increased to 37 x 25 mm.
- C3-Zero is upright at PCB (18.5,13.0), 0-degree rotation; USB-C faces the top case wall and the ceramic antenna faces the opposite end.
- Module contacts 1–9 are on the USB-facing left edge, top-to-bottom; 18–10 are on the right edge. This corrects the footprint to the official Waveshare top-view pinout.
- Added an 8 x 3.5 mm centre-bottom Edge.Cuts relief notch under the assumed antenna area, preserving side land rails.
- Added a provisional 10 x 4.8 mm USB-C wall cutout in the CAD macro.
- Motor moved to PCB local (32,5), on the right-hand side, separated laterally from the protected-pack candidate.
- Proposed Keyfob enclosure increased to 42 x 30 x 15.5 mm to provide 1 mm nominal clearance around the 37 x 25 carrier.
- CAD battery envelope changed to Renata ICP402025PC-01 candidate dimensions 27.5 x 20.5 x 4.3 mm; pack leads/connector are not modelled.

The exact antenna area, USB connector shell, recommended carrier pad dimensions and row datum still need confirmation against the physical module. The antenna notch and USB cutout are provisional. The plastic wall near the antenna requires RF testing. No FreeCAD or KiCad run, fit check, ERC/DRC, RF test or physical validation has occurred.


## 31. Sentry Pod 3D packaging study expanded — 2026-11-13

The earlier 55 x 30 x 19.7 mm Pod model represented only a battery-to-antenna lower-bound stack and did not include the board, modules or piezo. Replaced it with a larger **72 x 30 x 29 mm packaging-study envelope** and added reference solids to the FreeCAD macro:

- 49.5 x 24 x 1.6 mm carrier PCB.
- Renata ICP521630PM-01 protected-pack candidate, 31.5 x 17 x 5.7 mm.
- Waveshare ESP32-S3-Zero module, 23.5 x 18 mm.
- Adafruit 3886 IMU breakout, 26 x 17.8 x 4.6 mm.
- Elechouse PN5321 MINI, 25 x 16.4 x 4.4 mm, underside of carrier.
- 25 x 10 x 1 mm NFC antenna placeholder.
- CPT-2475-92T 24 x 7.5 mm piezo reference.

The proposed layout places the battery at the left end, PN532 module on the underside at the right end, MCU and IMU on the top side, the piezo above the left/centre area and the NFC coil at the right-hand lid region. Arithmetic gives 10.5 mm battery-to-coil and 12.5 mm piezo-to-coil horizontal separation. This is a clash-study hypothesis, not a physical fit or RF/acoustic validation.

Created hardware/sentry-pod/packaging-review.md with the component stack and remaining checks. Updated PROJECT_SPEC.md and docs/mechanical-requirements.md to identify 72 x 30 x 29 mm Pod and 42 x 30 x 15.5 mm Keyfob as current packaging-study envelopes only; neither is a final owner-approved size.

No FreeCAD run, STEP/STL generation, KiCad ERC/DRC, acoustic test, RF test or physical fit check has been performed. Pod PCB remains outline-only. The 105 dB sound target is not met by the current 92 dB piezo candidate.
