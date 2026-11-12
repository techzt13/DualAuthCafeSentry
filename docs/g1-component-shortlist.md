# G1 Component Shortlist

Revision: 0.4 | Date: 2026-11-12 | Status: candidates for owner decision; NOTHING selected or frozen

**Every part here is a candidate. None is selected, substituted into the
specification, purchased or frozen.** The physical component freeze remains
BLOCKED (decision D-21). Recommendations are the engineering preference on
current documents and still need owner approval and physical verification.

Read with the [compatibility matrix](g1-battery-charger-compatibility.md),
[power recommendation](g1-power-architecture-recommendation.md),
[mechanical feasibility](g1-mechanical-feasibility.md) and
[owner decisions](g1-owner-decisions.md). Sources are in the
[datasheet index](datasheet-index.md).

## 1. Evidence labels

- **D** - the document was downloaded and read in this session; its hash is
  in the [evidence folder](datasheets/README.md).
- **P** - a maker or retailer web page was fetched and read on 2026-11-12.
- **L** - a lead reported by delegated research and **not independently
  verified**. Treat as unconfirmed.

Availability is a page reading on 2026-11-12, not a supply commitment.
Distributor stock figures marked **L** came from search snapshots.

<a id="nfc"></a>
## 2. P-NFC and P-NFC-ANT: PN532 module and antenna

| Candidate | Maker, order code | Size | Key facts | Evidence | Availability |
| --- | --- | --- | --- | --- | --- |
| **PN5321 MINI with ferrite-backed antennas** | ELECHOUSE, SKU NFC_EX_MINI, hardware V2 | Board 25 x 16.4 x 4.4; supplied antennas 10 x 25 x 0.2 and 40 x 50 x 0.2; 100 mm leads | 13.56 MHz PN532; I2C/SPI/HSU selected by solder jumper; I2C address 0x24; I/O 3.3 V; current online manual input 2.7–5.5 V; active-low RST; no IRQ on host connector; current v1.1 manual says onboard 3.3 V I2C pull-ups | SRC-43 earlier rev.1.5 record; SRC-56 current online v1.1 docs | Not a purchase approval |
| PN532 NFC RFID Module V3 | ELECHOUSE | 42.7 x 40.4 x 4 published claim | Integral antenna; not compatible with current width target | D (SRC-21) | Not selected |
| PN532 breakout, product 364 | Adafruit | Page text 51 x 117.7 (L) | Integral antenna; far larger than Pod | L | L: out of stock |
| Grove NFC, 113020006 | Seeed Studio | 25.43 x 20.35 board (L); antenna size not found | Separate antenna; default UART | L | L: unclear |
| Gravity NFC, DFR0231-H | DFRobot | 110 x 50 (L) | Integral antenna | L | L |
| PN532 NFC HAT, 16958 | Waveshare | Raspberry Pi HAT format; no numeric size found | Integral antenna | L | L |

**Prototype candidate: ELECHOUSE PN5321 MINI with the 10 x 25 antenna.** It is the most compact documented PN532 option identified in the current research. This is not an owner component freeze.

Current online documentation (SRC-56) identifies the I2C host signals by module silkscreen, not by a numbered conductor/cable map:
- GND; 5V/3V3 supply; active-low RST; SCK and MISO unused in I2C.
- TX/MOSI/SDA is SDA; RX/SS/SCL is SCL.
- I2C address 0x24; 3.3 V I/O.
- No IRQ is exposed on the host interface. The schematic now leaves ESP32-S3 GPIO10 / P15-6 NC and polls the reader.
- The current v1.1 manual says onboard 3.3 V I2C pull-ups are present. An earlier downloaded v1.5 evidence record (SRC-43) describes unpopulated pull-up footprints and a different supply range. This is treated as a hardware/document revision discrepancy; no external pull-ups are populated until the received module is inspected.

The manual publishes board dimensions 25 x 16.4 x 4.4 mm and antenna options 10 x 25 x 0.2 mm or 40 x 50 x 0.2 mm with a 100 mm lead. The DWG archive has not yet been opened, so these are not tolerance-qualified envelope dimensions. Connector mating family and cable conductor order must be checked against the received item; the schematic deliberately uses signal names instead of pretending a numbered cable map exists.

The host I2C address 0x24 is already specified by the project. The manufacturer's published free-air read figures do not prove range through the finished 1.5 mm lid with the battery, piezo and nearby metal present. The project 10 mm nearest-surface battery and piezo separations remain applicable; antenna fit is still a major packaging constraint.

<a id="imu"></a>
## 3. P-IMU: MPU-6050 module

| Candidate | Maker, order code | Size | Key facts | Evidence | Availability |
| --- | --- | --- | --- | --- | --- |
| **MPU-6050 6-DoF sensor, product 3886** | Adafruit | Product page 26.0 x 17.8 x 4.6; official Eagle outline 25.40 x 17.78; four 2.5 mm mounting holes | STEMMA QT and 1 x 6 header; VIN 3–5 V, 3Vo output, GND, SCL, SDA, INT; level shifting and 10 kΩ I2C pull-ups; AD0 default low -> 0x68 | SRC-42 and newly inspected official board source SRC-54 | P: out of stock on 2026-11-12 |
| SEN-MPU6050 | Joy-IT | 25 x 20 x 7 published claim | 3.3 to 5 V supply, 3.3 V logic, 8 contacts | D (SRC-25) | Not shown |
| GY-521, generic | No single maker | Not documented | No controlled schematic or drawing | None | Widely listed; identity not controllable |
| SEN-11028 | SparkFun | 25.5 x 15.2 (L) | No regulator (L) | L | L: retired |
| SEN0142 | DFRobot | 14 x 21 (L) | Regulator and pull-ups on board (L) | L | L |

**Prototype candidate: Adafruit 3886**, because its board source, product number and manufacturer are identifiable. It is a distinct breakout, not a generic GY-521. O-04 remains the owner decision; this candidate is only represented provisionally in the Pod schematic.

The official six-pin header mapping from the Eagle source is: 1 VIN; 2 3Vo regulator output; 3 GND; 4 SCL; 5 SDA; 6 INT. The STEMMA QT connector uses GND, VIN, SDA and SCL. The source board includes a 10 kΩ AD0 pull-down by default and a solder jumper that connects AD0 to 3.3 V for address 0x69. The official guide says SCL/SDA are level-shifted and have 10 kΩ pull-ups. Do not connect 3Vo as an input and do not add another carrier pull-up pair until total bus pull-up resistance is checked.

The official source geometry contains four 2.5 mm mounting holes at (2.54, 2.54), (22.86, 2.54), (2.54, 15.24), and (22.86, 15.24) mm in the Eagle board coordinate system. The product-page 4.6 mm thickness is not a controlled assembled maximum for the chosen header/cable configuration. O-04 and physical fit remain open.

<a id="batteries"></a>
## 4. P-BATTERY and K-BATTERY: protected packs

All values D unless marked. Full comparison:
[compatibility matrix](g1-battery-charger-compatibility.md).

| Candidate | Unit | Capacity min / typ | Maximum size | Charge limit | Maximum discharge | Protection | Termination | Availability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Jauch LP502030JH+PCM+2 WIRES 50MM**, No. 246484, rev. 1.1 | Pod | 250 / 260 mAh | 32.0 x 20.5 x 5.4 after cycling | 4.2 V; 0.5 C maximum; 0 to +45 deg C | 1.0 C | Overcharge 4.28 V +/-0.025; over-discharge 3.00 V +/-0.05; no NTC stated | Bare wires 50 +/-3 mm, AWG26 | L: DigiKey active, in stock |
| **Renata ICP521630PM-01**, part 100691, V02 08/2019 | Pod | 240 / 250 mAh | 31.5 x 17.0 x 5.7 | 4.2 V; 125 mA normal, 250 mA maximum; 0 to 45 deg C | 250 mA continuous, 500 mA non-continuous | "Safety Circuit: Yes"; thresholds not published | Wire AWG 30; length not stated | L: Mouser non-stocked, 20 week lead |
| **Jauch LP402025JU+PCM+2 WIRES 50MM**, No. 246483, rev. 1.2 | Keyfob | 140 / 150 mAh | 27.0 x 20.5 x 4.5 after cycling | 4.2 V; 150 mA from +15 to +45 deg C; 30 mA from 0 to +15 deg C | 1.0 C, 150 mA | Overcharge 4.28 V +/-0.025; over-discharge 3.00 V +/-0.05; no NTC stated | Bare wires 50 +/-5 mm, AWG26 UL3302 | L: DigiKey active, in stock |
| **Renata ICP402025PC-01**, part 100644, V02 08/2019 | Keyfob | 150 / 155 mAh | 27.5 x 20.5 x 4.3 | 4.2 V; 77.5 mA normal, 155 mA maximum; 0 to 45 deg C | 155 mA continuous, 310 mA non-continuous | Overcharge 4.28 V +/-30 mV; over-discharge 2.8 V +/-70 mV (2016 specification, distributor-hosted) | Connector; JST SHR-02V reported (L) | L: Mouser non-stocked, 20 week lead |
| Renata ICP401835TPRT, part 101026, V01 11/2022 | Keyfob, over range | 205 / 215 mAh | 37.0 x 18.2 x 4.4 after 500 cycles | 4.2 V; 107.5 mA normal, 215 mA maximum | 215 mA continuous, 430 mA non-continuous | **Includes NTC**; thresholds not published | Wire AWG 30 | L |
| PKCELL LP402025 with PCM, Adafruit product 1317 | Keyfob | 142 / 150 mAh | 25.3 x 20.3 x 4.3 from the 2014 drawing | 4.2 V; 1 C quick charge; 0 to 45 deg C | 1 C | Drawing names IC S-8261AAJMD; no NTC (P) | JST PH 2-pin on 24 AWG leads | P: in stock |
| Varta 1/LPP 402025 CE PCM W, 56416 201 020 | Keyfob | 140 / 150 mAh | Pack size not stated | 4.2 V +/-50 mV; 140 mA | 280 mA continuous | Overcharge 4.275 V +/-0.020; "NTC: None" | Wires | OEM only, minimum 200 pieces |
| Jauch LP851719JU+PCM, No. 237924 | Keyfob | 180 / 200 mAh (L) | 22.0 x 18.0 x 8.7 (L) | 4.2 V | 1.0 C | As other Jauch packs (L) | Bare wires | L |

Corrections to earlier assumptions: Jauch has no "LP502030JU"; the 250 mAh
part is **LP502030JH**. Jauch LP402025JU is 140 mAh minimum and 150 mAh
typical, at the bottom edge of the Keyfob's 150 to 200 mAh requirement.
Jauch LP851719JU is too thick for the Keyfob cavity.

**Recommended candidates.**

- **Pod: Renata ICP521630PM-01 first, Jauch LP502030JH+PCM second.** The
  Renata pack is the only 250 mAh candidate with a stated non-continuous
  discharge rating (500 mA) above the documented transmit peak, and it is
  3.5 narrower. It is 17 wide rather than the "502030" size named in the
  specification, publishes no protection thresholds, and its minimum capacity
  is 240 mAh. The Jauch pack matches the 502030 description and publishes its
  thresholds, but its 1.0 C rating is below the transmit peak.
- **Keyfob: Renata ICP402025PC-01 first, Jauch LP402025JU+PCM second.**
  The Renata pack meets the 150 mAh minimum and has the highest stated
  non-continuous rating of the 150 mAh class, although that rating is still
  25 mA below the transmit peak.

Remaining uncertainties, all packs: no charge-voltage tolerance for five of
seven; no pack has a qualified NTC except Renata ICP401835TPRT; no pulse
discharge data; wire length and connector not always stated; capacity at a
4.1 V charge limit unknown; finished-pack swelling allowance beyond the
"after cycling" figures unknown.

<a id="chargers"></a>
## 5. P-CHARGER and K-CHARGER: charging and power path

| Candidate | Type | Regulation maximum | Power path | Temperature input | Package or size | Evidence | Availability |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **TI BQ25185** | IC, resistor-strapped | 4.1205 V at the 4.1 V setting; 4.221 V at 4.2 V | Yes, SYS 4.5 V | Yes, NTC | WSON-10, 2.2 x 2.0 nominal | D: SLUSF65B (SRC-30) | Not checked |
| TI BQ25180 | IC, I2C-programmed | +/-0.5 % of a 10 mV-step setting | Yes | Yes, with JEITA profile | DSBGA-8, 1.6 x 1.1 | D: SLUSE99C (SRC-31) | Not checked |
| TI BQ24074 / BQ24075 / BQ24079 | IC | 4.23 V; 4.141 V for BQ24079 | Yes | Yes | VQFN-16, 3.00 x 3.00 | D: SLUS810N (SRC-32) | Not checked |
| Microchip MCP73831T-2ACI/OT | IC, specified family | 4.232 V | No | No | SOT-23-5 | D: DS20001984H (SRC-13) | Not checked |
| Top Power TP4056 | IC, specified family | 4.242 V or 4.263 V, unresolved | No | TEMP pin | ESOP8 or EMSOP8 | D: REV_2.3 (SRC-14) | Not checked |
| TI BQ25100 | IC | 4.23 V | No | Yes | DSBGA-6, 1.60 x 0.90 | D: SLUSBV8C (SRC-33) | Not checked |
| Adafruit Micro-Lipo USB-C, product 4410 | Module, MCP73831 class | As MCP73831 | No | No | 24.0 x 19.0 x 7.2 published claim | P (SRC-42) | P: in stock |
| Adafruit bq25185 charger, product 6091 | Module, BQ25185 | Default 4.2 V setting | Yes, 4.5 V load output | Pad for a 10 kohm thermistor | 32.0 x 26.3 x 7.2 published claim | P (SRC-42) | P: out of stock |
| Adafruit bq24074 charger, product 4755 | Module, BQ24074 | 4.23 V | Yes, 4.4 V load output | Optional 10 kohm thermistor | Not stated | P (SRC-42) | P: in stock |

**Recommended candidate: TI BQ25185 at the 4.1 V setting**, for both units,
on a custom carrier. Reasons and limits are in the
[power recommendation](g1-power-architecture-recommendation.md). It is not
one of the specified MCP73831 or TP4056 families, so it needs owner approval
(O-02).

**No charger module is recommended.** The Adafruit 6091 and 4755 boards
default to 1 A and cannot be set below 250 mA and 500 mA by their jumpers.
Candidate packs allow 125 to 250 mA at most, so only the Renata 250 mAh
pack's maximum equals the lowest setting, with no margin. The Adafruit
4410 default of 100 mA is within the Pod packs' limits but it has no
temperature input, no power path and an unresolved 4.232 V maximum. All three
are too large for either enclosure
([mechanical feasibility](g1-mechanical-feasibility.md)).

Supporting candidates for the recommended architecture, all D:

| Function | Candidate | Key facts | Source |
| --- | --- | --- | --- |
| Rail hand-off to the Zero 5 V pad | TI LM66100, SC-70-6 | 1.5 to 5.5 V, 1.5 A, 91 mohm typical at 3.6 V | SRC-34 |
| Logic regulator, if a board change is ever approved | TI TPS63802 buck-boost | 2 A at 3.3 V for inputs of 2.3 V and above; 11 uA quiescent | SRC-35 |
| Same | TI TPS63900 buck-boost | More than 400 mA at 3.3 V; 75 nA quiescent; **below the 0.5 A supply requirement** | SRC-35 |
| Not suitable | TI TPS7A02 | 200 mA | SRC-35 |

<a id="piezo"></a>
## 6. P-PIEZO and driver

| Candidate | Size | Documented sound level and conditions | Maximum drive | Evidence | Status |
| --- | --- | --- | --- | --- | --- |
| **Same Sky CPT-2475-92T** | Diameter 24 +/-0.2 x 7.5 +/-0.2; pins on 10 pitch | **92 dB at 10 cm**, 10 Vp-p, 4,000 Hz, half-duty square wave; 8 mA at rated voltage; 14.7 / 21 / 27.3 nF | 1 to 30 Vp-p | D: datasheet 09/11/2024 (SRC-44) | Stock not checked |
| Murata PKM22EPPH4001-B0 | Diameter 22.0 x 8.2 (L) | 75 dB minimum, 87 dB typical at 10 cm, +/-1.5 Vo-p (L) | +/-15 Vo-p (L) | L: maker PDF returned 403 | L: end-of-life notice |
| Murata PKM13EPYH4000-A0 | Diameter 12.6 x 6.9 (L) | 70 dB minimum at 10 cm (L) | +/-15 Vo-p (L) | L | L |
| TDK PS1240P02BT | Diameter 12.2 x 6.5 (L) | 70 dB(A) minimum at 10 cm, 3 Vo-p (L, from a mirror) | 30 Vo-p (L) | L; maker PDF still blocked | L: in production |

**No externally driven piezo was found that documents 105 dB.** The
loudest documented part of 25 mm or less is 92 dB at 10 cm.

**Recommended candidate for evaluation: Same Sky CPT-2475-92T**, because it
is the only one whose level and test conditions were verified directly.

What the documents support, and what they do not:

- The specified driver, one 2N2222 switching the piezo from the battery or
  USB rail, applies at most about the rail voltage, 3.4 to 5 Vp-p. That is
  below this part's 10 Vp-p rated condition, so its level would be below
  92 dB. No inductor or boost stage is in the specification.
- If sound pressure scaled linearly with voltage, 18 Vp-p would give about
  `92 + 20 x log10(18 / 10) = 97.1 dB` and 30 Vp-p about 101.5 dB at 10 cm.
  **These are estimates, not datasheet values**; piezo output does not scale
  exactly. Even at the maximum rated drive the documents do not reach 105 dB
  at 10 cm.
- The specification does not give a measuring distance for 105 dB
  (decision D-18).
- The part is rated at 4,000 Hz. Its response across the specified 2.8 to
  4.2 kHz sweep, and at the 180 Hz and C6 to C7 tones, was not extracted.

| Driver candidate | Key facts | Evidence | Note |
| --- | --- | --- | --- |
| onsemi MMBT2222ALT1G, SOT-23 | 600 mA continuous collector current, 1100 mA peak | D: MMBT2222LT1/D rev. 13 (SRC-48) | Surface-mount member of the specified 2N2222 family. onsemi lists P2N2222AG (TO-92) as obsolete (L) |
| Diodes PAM8904, U-QFN | 1.8 to 5.5 V supply; charge pump 1x, 2x, 3x; 7.2 to 9 V output in 3x mode at 3 V, so about 18 Vp-p differential; 7.9 mA typical driving 15 nF at 4 kHz; 1 uA maximum shutdown | D: DS37246 rev. 6-2 (SRC-45) | Replaces the specified transistor driver; owner approval needed (O-05) |

<a id="motor"></a>
## 7. K-MOTOR and driver

| Candidate | Size | Rated | Start | Operating limit | Evidence | Availability |
| --- | --- | --- | --- | --- | --- | --- |
| **Precision Microdrives 308-100** | Diameter 8 +/-0.1 x 3.4 +/-0.1 plus a lead-exit tab; leads 45 +/-2, red positive, blue negative | 3 V; 66 mA typical, 94 mA maximum | 2.4 V maximum; 111 mA typical, 124 mA maximum | 3.6 V maximum | D: R002-V012 (SRC-46) | L: stocked design |
| Precision Microdrives 310-103 | Diameter 10 +/-0.1 x 2.7 +/-0.1; leads 41 +/-2 | 3 V; 58 mA typical, 90 mA maximum | 2.3 V maximum; 106 mA typical, 150 mA maximum | 3.6 V maximum; -20 to 70 deg C | D: R002-V011 (SRC-46) | L: in stock |
| Vybronics VCLP1020B002L | Diameter 10 +/-0.1 x 2.1 +/-0.1 | 3.0 V; 30 mA maximum | 2.3 V maximum; 80 mA maximum | 2.5 to 3.5 V | D: A/1 (SRC-27) | L: in stock |
| Vybronics VC0834B011F | Diameter 8.0 x 3.4 (L) | 3.0 V; 85 mA maximum (L) | 120 mA maximum (L) | 2.7 to 3.3 V | D for identity and voltage range: A/2, 2026-10-15 (SRC-47) | L: zero stock |

**Recommended candidate: Precision Microdrives 308-100**, because an 8 mm
body is the only diameter that passes the Keyfob plan screen. If the Keyfob
is enlarged, the Vybronics VCLP1020B002L draws a third of the current.

Remaining uncertainties: no candidate documents continuous operation; the
310-103 life test is 2 s on, 2 s off. Start current adds to the transmit
peak. Driving from the 3.3 V rail keeps both recommended motors inside their
voltage limits, but that rail may sag (power recommendation section 3.2) and
the motor's 2.4 V start voltage margin under sag is unmeasured.

Driver candidates: onsemi MMBT2222ALT1G (above) with Diodes 1N4148W-7-F,
SOD123 (D: DS30086 rev. 32-2, SRC-45), matching the specification's
"transistor/diode" wording. Base resistor and off-bias values are TBD.

<a id="switches"></a>
## 8. P-BUTTON, K-BUTTON, P-SWITCH, K-SWITCH

| Candidate | Type | Rating | Force and travel | Size | Evidence |
| --- | --- | --- | --- | --- | --- |
| **Alps Alpine SKSCLBE010** | Side-actuated tactile, surface mount | 12 V DC, 50 mA maximum; 1 V, 10 uA minimum | 2.2 +/-0.65 N; 0.2 +0.1/-0.05 mm | 3.5 x 3.55 x 1.25 (L) | D: specification 201707 (SRC-49); -30 to 85 deg C |
| **Alps Alpine SKRPABE010** | Top-actuated tactile, surface mount | 16 V DC, 50 mA maximum; 1 V, 10 uA minimum | 1.57 +/-0.49 N (L); travel 0.2 (L) | 4.2 x 3.2 x 2.5 (L) | D: specification 201707 (SRC-49); -40 to 90 deg C |
| C&K PTS810, PTS840 | Tactile | 50 mA (L) | L | L | L: maker documents returned 403 |
| **C&K PCM12SMTR** | Slide, SPDT, surface mount | **0.3 A at 6 V DC**; 10,000 cycles; -20 to 85 deg C | Not extracted | Not extracted | D: C&K catalogue page, distributor-hosted (SRC-50) |
| SHOUHAN MSK12C02 | Slide, the specified identifier | 50 mA at 12 V DC | 1.6 +/-0.1 travel | 8 x 2.8 x 1.4 body | D, mirror (SRC-28) |

**Recommended candidates:** Alps SKSCLBE010 for the Pod's recessed side
button; either Alps part for the Keyfob; C&K PCM12SMTR for both slide
switches as a documented, higher-rated part in the same style as the
specified MSK-12C02.

Remaining uncertainties: body dimensions marked L were not read from the
drawings. Neither slide switch is rated for the 0.43 to 0.49 A load, so the
switch must control an enable input, not carry load current. Whether
PCM12SMTR and MSK12C02 share a footprint was not checked. Availability was
not checked for any switch.

<a id="connectors"></a>
## 9. USB-C and battery connectors

| Candidate | Function | Rating | Size | Evidence |
| --- | --- | --- | --- | --- |
| **GCT USB4125-GF-A** | Charge-only USB-C receptacle, 6 contacts: CC1, CC2, 2 x VBUS, 2 x GND | 3.00 A VBUS total; 48 V DC; 20,000 cycles; -30 to 85 deg C | 8.94 wide x 6.80 +/-0.15 deep x 3.16 high; plug overhang shown | D: drawing A6, dated "20/11/25" as printed (SRC-52); stock L |
| GCT USB4105-GF-A | USB 2.0 receptacle, 16 contacts | 5.00 A VBUS total; 48 V DC; 20,000 cycles | Not read from the drawing | D: drawing (SRC-52); stock L |
| **JST PH**, 2.0 mm: PHR-2, S2B-PH-SM4-TB, B2B-PH-K-S | Battery connector | 2 A at AWG 24; 100 V; AWG 32 to 24 | Top entry 8 mounted height; side entry about 4.8 | D: catalogue page 1 (SRC-51) |
| JST SH, 1.0 mm: SHR-02V-S-B, SM02B-SRSS-TB | Battery connector | 1.0 A at AWG 28; 50 V; **AWG 32 to 28 only** | Side entry about 2.95 high | D: catalogue page 1 (SRC-51) |
| Molex PicoBlade, 1.25 mm | Battery connector | 1.0 A (L) | Mated height 3.40 right-angle (L) | L |

**Recommended candidates:** GCT USB4125-GF-A for a separate charge port;
JST PH for the Pod; JST SH for the Keyfob where height is critical.

Constraints found:

- The Jauch packs have AWG26 wires. That is inside the PH range and
  **outside the SH range** of AWG 32 to 28.
- The PKCELL pack is supplied with JST PH on 24 AWG leads. The Renata
  ICP402025PC-01 is reported to carry a JST SHR-02V (L).
- A side-entry PH header at about 4.8 high, or a top-entry one at 8, is a
  large share of the Keyfob's 9 internal height.
- Polarity, pin 1 and crimp parts are not fixed by any of these documents.
- The tether port and cable (P-TETHER-PORT, P-TETHER-CABLE) were not
  researched; decision D-08 is still open.

<a id="mcu"></a>
## 10. K-MCU-C3 versus K-MCU-S3

| Property | ESP32-C3-Zero, SKU 25452 | ESP32-S3-Zero, SKU 25081 | Source |
| --- | --- | --- | --- |
| PCB outline | 23.5 x 18 | 23.5 x 18 | SRC-24, SRC-03 |
| Transmit peak, 802.11b 1 Mbps at 21 dBm | 335 mA | 340 mA | SRC-08, SRC-07 |
| Receive, 802.11 HT20 | 84 mA | 88 mA | SRC-08, SRC-07 |
| USB D-/D+ on edge contacts | Yes, contacts 15 and 16 | No | SRC-05, SRC-02 |
| RGB LED supply | 5 V net | 3.3 V | SRC-05, SRC-02 |
| Same firmware target as the Pod | No | Yes | Specification |

**Recommendation: keep ESP32-C3-Zero as the proposed option (D-02).** The
documents give it no size advantage and only a 5 mA lower transmit peak. Its
one concrete advantage is exposed USB data contacts. Whole-board sleep and
beacon current, which decide Keyfob runtime, are not in any document and
must be measured on both boards before D-02 is closed.

## 11. Not researched in this session

Credential cards (P-CREDENTIAL), cell NTC parts (P-NTC, K-NTC), tether port
and cable, fasteners and inserts, battery insulation, acoustic mounting,
attachment hardware, passive values, input ESD protection and the fitted
Zero-board RGB, antenna and USB receptacle part numbers. All remain TBD.

## 12. Revision record

| Revision | Date | Change |
| --- | --- | --- |
| 0.3 | 2026-11-12 | First issue: G1 candidates with evidence class, recommendation and remaining uncertainty for each assembly |
