# G1 Battery and Charger Compatibility Matrix

Revision: 0.3 | Date: 2026-11-12 | Status: document comparison; NO pairing approved

**No battery, charger or pairing is selected, frozen or approved for
construction.** This compares published limits only. Nothing here has been
measured. LiPo charging requires independent electrical review and physical
verification before any cell is connected ([AGENTS.md](../AGENTS.md)).

Sources are in the [datasheet index](datasheet-index.md). Values were read
from the downloaded documents listed in the
[evidence folder](datasheets/README.md) unless marked **L** (delegated lead,
not independently verified).

## 1. Battery charge-voltage limits

| Battery | Capacity, min / typ | Stated charge voltage | Hard upper limit that the document supports | Source |
| --- | --- | --- | --- | --- |
| EEMB LP502030, bare cell, reference | 230 / 250 mAh | 4.200 +/-0.050 V | **4.250 V** | SRC-16 |
| EEMB LP401730, bare cell, reference | 140 / 150 mAh | 4.200 +/-0.020 V | **4.220 V** | SRC-26 |
| Jauch LP502030JH+PCM+2 WIRES 50MM | 250 / 260 mAh | "4.2 V", no tolerance | **Not stated**; strict reading 4.200 V | SRC-37 |
| Jauch LP402025JU+PCM+2 WIRES 50MM | 140 / 150 mAh | "4.2 V", no tolerance; 4.1 V at +45 to +50 deg C | **Not stated**; strict reading 4.200 V | SRC-37 |
| Renata ICP521630PM-01 | 240 / 250 mAh | "4.2 V CV", no tolerance | **Not stated**; strict reading 4.200 V | SRC-38 |
| Renata ICP402025PC-01 | 150 / 155 mAh | "4.2 V CV", no tolerance | **Not stated**; strict reading 4.200 V | SRC-38 |
| Renata ICP401835TPRT, includes NTC | 205 / 215 mAh | "4.2 V CV", no tolerance | **Not stated**; strict reading 4.200 V | SRC-38 |
| Varta 1/LPP 402025 CE PCM W | 140 / 150 mAh | "4.2(+/-50mV)" maximum charge voltage | **4.250 V** | SRC-39 |
| PKCELL LP402025 with PCM (Adafruit 1317) | 142 / 150 mAh | "4.2V", no tolerance | **Not stated**; strict reading 4.200 V | SRC-40 |

Five of the seven finished packs publish no charge-voltage tolerance. A pack
protector does not supply one: its overcharge threshold is a last-resort
disconnect, well above the normal charging limit.

| Pack protector | Overcharge detection | Over-discharge detection | Source |
| --- | --- | --- | --- |
| Jauch LP502030JH and LP402025JU | 4.28 V +/-0.025 V (4.255 to 4.305 V) | 3.00 V +/-0.05 V | SRC-37 |
| Renata ICP402025PC-01 | 4.28 V +/-30 mV (4.250 to 4.310 V) | 2.8 V +/-70 mV | SRC-38, distributor-hosted 2016 specification |
| Varta 1/LPP 402025 CE PCM W | 4.275 V +/-0.020 V (4.255 to 4.295 V) | 2.300 V +/-0.035 V | SRC-39 |
| PKCELL LP402025, drawing names IC S-8261AAJMD | 4.325 V +/-25 mV at 25 deg C per the ABLIC table (4.300 to 4.350 V) | 2.500 V +/-50 mV | SRC-40 drawing, SRC-41 table |
| Renata ICP521630PM-01, ICP401835TPRT | "Safety Circuit: Yes"; thresholds not published | Not published | SRC-38 |

The Adafruit 1317 page says the pack cuts out at 3.0 V. The IC named in the
linked 2014 PKCELL drawing detects over-discharge at 2.500 V. The shipped
pack may differ from the 2014 document; this is unresolved.

## 2. Charger regulation-voltage limits

| Charger | Minimum / typical / maximum | Stated conditions | Source |
| --- | --- | --- | --- |
| Microchip MCP73831-2 | 4.168 / 4.20 / **4.232 V** | VDD = VREG + 1 V, 10 mA, -5 to +55 deg C | SRC-13 page 3 |
| Top Power TP4056 | 4.158 / 4.2 / **4.242 V**; page 17 text says +/-1.5 %, which would be **4.263 V** | 0 to 85 deg C; internal conflict unresolved | SRC-14 pages 4 and 17 |
| TI BQ24072/73/74/75 | 4.16 / 4.20 / **4.23 V** | Junction 0 to 125 deg C | SRC-32 |
| TI BQ24079 | 4.059 / 4.100 / **4.141 V** | Junction 0 to 125 deg C | SRC-32 |
| TI BQ25100 / BQ25101 | 4.16 / 4.2 / **4.23 V** | Junction 0 to 125 deg C, 0 to 250 mA | SRC-33 |
| TI BQ25185, 4.2 V setting | +/-0.5 %: 4.179 / 4.200 / **4.221 V** | Junction -40 to 125 deg C | SRC-30 |
| TI BQ25185, 4.1 V setting | +/-0.5 %: 4.0795 / 4.100 / **4.1205 V** | Same | SRC-30 |
| TI BQ25185, 4.05 V setting | +/-0.5 %: 4.02975 / 4.050 / **4.07025 V** | Same | SRC-30 |
| TI BQ25180, I2C setting V | +/-0.5 % of V in 10 mV steps, 3.5 to 4.65 V | Junction -40 to 125 deg C | SRC-31 |
| TI BQ25180 at 4.19 V | 4.16905 / 4.190 / **4.21095 V** | Same | SRC-31 |
| TI BQ25180 at 4.17 V | 4.14915 / 4.170 / **4.19085 V** | Same | SRC-31 |

The BQ25185 and BQ25180 accuracy line reads "summary for all settings,
typical measurement at VBATREG = 4.2V". The +/-0.5 % figures are the table's
minimum and maximum columns and are used as limits here. The BQ25185 feature
list names a 4.02 V option while its Table 6-1 gives 4.05 V; the table was
inspected as an image and is used.

## 3. Voltage comparison

**PASS** means the charger's documented maximum does not exceed the battery
document's hard upper limit. It is a necessary condition only.
**UNRESOLVED** means the battery document states no tolerance, so only a
charger maximum at or below 4.200 V passes without manufacturer confirmation.

| Charger maximum | Limit 4.250 V (EEMB LP502030, Varta) | Limit 4.220 V (EEMB LP401730) | No tolerance stated (Jauch, Renata, PKCELL) |
| --- | --- | --- | --- |
| TP4056, 4.242 V or 4.263 V | UNRESOLVED: passes only if page 4 governs | FAIL by 22 mV or more | UNRESOLVED |
| MCP73831-2, 4.232 V | PASS | FAIL by 12 mV | UNRESOLVED; exceeds 4.200 V by 32 mV |
| BQ2407x / BQ25100, 4.23 V | PASS | FAIL by 10 mV | UNRESOLVED; exceeds 4.200 V by 30 mV |
| BQ25185 at 4.2 V, 4.221 V | PASS | FAIL by 1 mV | UNRESOLVED; exceeds 4.200 V by 21 mV |
| BQ25180 at 4.19 V, 4.21095 V | PASS | PASS, 9.05 mV margin | UNRESOLVED; exceeds 4.200 V by 10.95 mV |
| BQ25180 at 4.17 V, 4.19085 V | PASS | PASS | **PASS**, 9.15 mV below 4.200 V |
| BQ24079, 4.141 V | PASS | PASS | **PASS** |
| BQ25185 at 4.1 V, 4.1205 V | PASS | PASS | **PASS**, 79.5 mV below 4.200 V |

**Findings.**

1. The LP401730 conflict recorded in revision 0.2 is confirmed and is wider
   than the two original charger families. Every fixed 4.2 V charger examined,
   including the +/-0.5 % BQ25185, exceeds that cell's 4.220 V limit.
2. A lower regulation setpoint resolves the voltage conflict on paper for
   every battery listed: BQ25185 strapped to 4.1 V, BQ24079, or BQ25180
   programmed to 4.17 V or lower.
3. A lower setpoint stores less charge. None of the battery documents states
   capacity at a reduced charge voltage. The loss is **TBD** and must be
   measured against the 200 to 250 mAh and 150 to 200 mAh requirements.
4. Neither specified charger family can meet a 4.200 V strict limit.
   MCP73831 options are 4.20, 4.35, 4.40 and 4.50 V; TP4056 is 4.2 V only.
   Using a different charger IC is a specification change that needs owner
   approval (decision O-02 in [owner decisions](g1-owner-decisions.md)).
5. For the five packs without a stated tolerance, written confirmation from
   the pack manufacturer of the permitted charging-voltage range would
   establish whether a 4.2 V charger is acceptable. That evidence is missing.

## 4. Remaining compatibility conditions

Voltage is one of several conditions. Each row is unresolved unless stated.

| Condition | Battery evidence | Charger evidence | Status |
| --- | --- | --- | --- |
| Charge current, Pod pack | Jauch LP502030JH: standard 0.2 C, maximum 0.5 C (125 mA at 250 mAh). Renata ICP521630PM-01: normal 125 mA, maximum 250 mA | BQ25185 5 mA to 1 A by resistor, +/-10 % at 40 mA and above; MCP73831 15 to 500 mA | Programmable within limits; exact resistor and tolerance analysis TBD |
| Charge current, Keyfob pack | Jauch LP402025JU: 30 mA standard; maximum 150 mA from +15 to +45 deg C, **30 mA from 0 to +15 deg C**, 75 mA at 4.1 V from +45 to +50 deg C | BQ25185 has no automatic cool-temperature current reduction in its electrical table; BQ25180 has programmable JEITA reduction | A single fixed current above 30 mA is not permitted below +15 deg C; needs NTC window or 30 mA setting |
| Module default currents | As above | Adafruit 4410: 100 mA default, 500 mA by jumper. Adafruit 6091: 1 A default, 500 or 250 mA by jumper. Adafruit 4755: 1 A default, 500 mA or 1.5 A by jumper | **6091 and 4755 defaults (1 A) exceed every candidate pack's maximum.** The lowest 6091 jumper setting, 250 mA, equals the Renata ICP521630PM-01 maximum with no margin and exceeds all others. 4410 default is within the Pod pack limit and within the Keyfob limit only at +15 deg C and above |
| Temperature supervision | Only Renata ICP401835TPRT states an included NTC. Jauch states none; Varta states "NTC: None"; Adafruit states no thermistor | MCP73831 has no temperature input. BQ25185, BQ25180 and BQ2407x have a TS input for an external 10 kohm-class NTC | A separately mounted, qualified cell NTC is required for every pack except the Renata NTC pack; implementation TBD |
| Termination | LP401730 3 mA; LP502030 5 mA; Varta "7mA or timer 2.5h"; others not stated | BQ25185 10 % of charge current; BQ25180 programmable down to 0.5 mA; MCP73831 option-dependent | Ending at a higher current than the cell figure charges less, not more; confirm per pairing |
| Safety timer | Varta recommends a 2.5 h timer; others not stated | BQ25185 fixed 360 min; BQ25180 180 to 720 min; BQ2407x 5 h default; MCP73831 has none | A 30 mA setting on a 150 mAh pack needs about 5 h before taper, close to the BQ25185 limit; TBD |
| Over-discharge | Pack protectors trip between 2.3 and 3.0 V | BQ25185 disconnects the battery at 3.0 V (BUVLO); BQ25180 2.0 to 3.0 V selectable | The BQ25185 3.0 V cut-off is above the Renata, Varta and PKCELL thresholds and equal to the Jauch nominal threshold; which trips first, and recovery, are TBD |
| System load while charging | Not a battery property | BQ25185, BQ25180 and BQ2407x have a separate SYS output; MCP73831, TP4056 and BQ25100 do not | See the [power recommendation](g1-power-architecture-recommendation.md) |
| Discharge capability | See section 5 | Not a charger property | **Conflict**; see section 5 |

## 5. Discharge limits against documented peak loads

Peak load figures are from the chip and module documents, not measurements.

| Load | Documented figure | Source |
| --- | --- | --- |
| ESP32-S3 transmit, 802.11b 1 Mbps at 21 dBm | 340 mA peak | SRC-07, v2.2 |
| ESP32-C3 transmit, 802.11b 1 Mbps at 21 dBm | 335 mA peak | SRC-08, v2.5 |
| Elechouse PN5321 MINI, 3.3 V, 10 x 25 mm antenna, continuous RF | 84.4 mA mean, 85.85 mA maximum at 100 Hz sampling | SRC-43 page 10 |
| PN532 IC total supply, continuous wave | 150 mA maximum | SRC-09 table 295 |
| MPU-6050, all axes and DMP | 3.9 mA | SRC-11 |
| Coin motor, start | 80 mA (Vybronics VCLP1020B002L) to 150 mA (Precision Microdrives 310-103) | SRC-27, SRC-46 |

Pod simultaneous worst case from these figures:
`340 + 85.85 + 3.9 = 429.75 mA` at the 3.3 V rail, before the RGB LED and
the siren driver. With the PN532 IC maximum instead of the module
measurement: `340 + 150 + 3.9 = 493.9 mA`.
Keyfob: `335 + 80 = 415 mA` to `335 + 150 = 485 mA` if the motor shares the
rail. Through a linear regulator the battery current is at least the rail
current.

| Battery | Documented maximum discharge | Against the transmit peak alone |
| --- | --- | --- |
| Jauch LP502030JH+PCM | 1.0 C, 250 mA at minimum capacity | **Exceeded by 90 mA** |
| Renata ICP521630PM-01 | 250 mA continuous; 500 mA non-continuous | Within the non-continuous figure; duration undefined |
| EEMB LP502030 cell | 500 mA | Within; Pod worst case 493.9 mA leaves 6.1 mA |
| Renata ICP401835TPRT | 215 mA continuous; 430 mA non-continuous | Within the non-continuous figure only |
| Jauch LP402025JU+PCM | 1.0 C, 150 mA | **Exceeded by 185 mA** |
| Renata ICP402025PC-01 | 155 mA continuous; 310 mA non-continuous | **Exceeded by 25 mA** |
| Varta 1/LPP 402025 CE PCM W | 280 mA continuous | **Exceeded by 55 mA** |
| PKCELL LP402025 (Adafruit 1317) | 1 C, 150 mA | **Exceeded by 185 mA** |
| EEMB LP401730 cell | 300 mA | **Exceeded by 35 mA** |

**Finding.** Every 150 to 200 mAh battery examined has a documented
discharge limit below the documented radio transmit peak at maximum transmit
power. The Jauch 250 mAh pack is also below it. These are continuous or
unspecified-duration ratings compared with a millisecond-scale radio burst,
so this is a flag, not a proof of failure. Closing it needs one of:
manufacturer pulse-discharge data, a reduced and measured transmit power,
local bulk capacitance with measured cell current, or a higher-rate cell.
None of that evidence exists yet. See risk R-34.

## 6. Pairing status

| Unit | Pairing examined | Voltage | Current | Temperature | Discharge | Overall |
| --- | --- | --- | --- | --- | --- | --- |
| Pod | Jauch LP502030JH+PCM with BQ25185 at 4.1 V | PASS on documents | Programmable within 125 mA | External NTC required, TBD | Pack limit below transmit peak | **NOT APPROVED** |
| Pod | Renata ICP521630PM-01 with BQ25185 at 4.1 V | PASS on documents | Programmable within 250 mA | External NTC required, TBD | Within non-continuous rating | **NOT APPROVED**; most complete on paper |
| Pod | Either pack with MCP73831-2 (Adafruit 4410, 100 mA) | UNRESOLVED | Within limits | No temperature input | As above | **NOT APPROVED** |
| Keyfob | Jauch LP402025JU+PCM with BQ25185 at 4.1 V | PASS on documents | 30 mA below +15 deg C | External NTC required, TBD | Pack limit far below transmit peak | **NOT APPROVED** |
| Keyfob | Renata ICP402025PC-01 with BQ25185 at 4.1 V | PASS on documents | Programmable within 155 mA | External NTC required, TBD | Non-continuous rating 25 mA below transmit peak | **NOT APPROVED** |
| Keyfob | Renata ICP401835TPRT with BQ25185 at 4.1 V | PASS on documents | Programmable within 215 mA | **NTC included** | Within non-continuous rating | **NOT APPROVED**; 215 mAh typical exceeds the 150 to 200 mAh range; 37 mm length |
| Keyfob | PKCELL LP402025 (Adafruit 1317) with Adafruit 4410 | UNRESOLVED | 100 mA default within 150 mA | No temperature input, no NTC | Pack limit far below transmit peak | **NOT APPROVED** |

No pairing is approved because no pairing has all conditions established by
evidence. The lowest-risk direction on the documents is a BQ25185-class
charger at the 4.1 V setting with an external cell NTC and a pack whose
manufacturer states a non-continuous discharge rating. That direction needs
owner approval, because the BQ25185 is not one of the two specified charger
families.

## 7. Revision record

| Revision | Date | Change |
| --- | --- | --- |
| 0.3 | 2026-11-12 | First issue: charge-voltage, current, temperature and discharge comparison for G1 candidates |
