# Component Evidence and Datasheet Index

Revision: 0.2 | Date: 2026-11-11 | Status: verification register; physical freeze BLOCKED

Completion review: 2026-11-12. Existing source evidence was preserved; no
component selection or specification was changed during recovery.

This extends, rather than replaces, the revision 0.1 design basis. Read the
[component register](component-register.csv),
[dimension register](dimension-register.csv) and
[verified pinouts](verified-pinouts.md) together.
[PROJECT_SPEC.md](../PROJECT_SPEC.md) remains unchanged.

**A verified document is not a verified purchased assembly. No procurement,
PCB layout, CAD design, battery circuit or manufacturing release is authorized
by these registers. No reference part has been substituted into either unit.**

## 1. Freeze result and evidence rules

The specified Waveshare board identities can be tied to manufacturer order
pages: **ESP32-S3-Zero, SKU 25081**, and the permitted Keyfob option
**ESP32-C3-Zero, SKU 25452**, both without pre-soldered headers. The S3 reference
is the ESP32-S3FH4R2, 4 MB flash / 2 MB PSRAM version, not the newer N8R8
option on the same store page. The Keyfob's S3 alternative remains separate.
No received PCB revision, full installed board envelope or power-interface
approval has been established.

GY-521 and PN532 describe module families, not uniquely identified assemblies.
The project also lacks exact finished battery packs, charger modules, piezo,
motor, switches, connectors and supporting circuit selections. Consequently,
**no project assembly is marked FROZEN**.

- **Document-verified:** an identified manufacturer's document was inspected
  for the stated fact, with its scope and revision recorded.
- **Manufacturer-authored mirror:** the inspected PDF identifies its
  manufacturer, model and document revision, but was obtained from another
  host. This is disclosed; it is not evidence that an unspecified module is
  made by that manufacturer.
- **Drawing-verified, partial:** only the dimensions actually controlled or
  called out in the manufacturer drawing are populated as numeric dimensions.
  A nominal PCB outline is not a maximum assembled envelope.
- **TBD / unverified:** identity, applicability, drawing, tolerance or access
  is missing. Search snippets, marketplace dimensions, photographs without
  dimension callouts and third-party CAD models do not qualify a dimension.
- **Reference only:** a comparison, not an approved replacement. Its facts must
  not be copied into the corresponding unselected project component.

Document dates are not automatically hardware revisions. In particular, the
C3 schematic filename says V2, the S3 schematic does not state a revision,
and `v2` in a downloadable STEP filename does not establish the received S3
PCB revision.

### Register conventions

The original 16 component-register columns are retained, with explicit
revision/access, drawing, connector/pinout, mounting, keepout, purchasing,
parentage and freeze-control fields added. `revision` is the **register**
revision; `component_revision` and `drawing_revision` concern the hardware
and evidence. `pinout_reference` is relative to this documentation directory.

Each original part ID is retained. Definite constituent parts, including
antennas, native USB receptacles, charger ICs, connector halves and identified
resistor/filter roles, have separate unit-specific rows. `parent_ids` prevents
double-counting included parts. Semicolon-separated MCU parents are mutually
exclusive alternatives, not two populated boards.

`CIRCUIT_GROUP` and `INTERFACE_GROUP` rows preserve unresolved design scope;
they are **not orderable components**. Their remaining contents and quantities
are TBD until the circuit or assembly is defined. Purchased modules are
controlled as assemblies: these registers do not pretend to reconstruct an
undisclosed supplier BOM or identify every internal passive. These remaining
scope gaps block a complete BOM freeze.

The dimension register has one row per component-register ID. Numeric nominal
and maximum columns describe only `dimension_scope`; every missing value is
`TBD`, never zero. Published claims and whole-enclosure targets are kept in a
separate text column. Hole/terminal coordinates, leads, adhesives, service
space and complete installed envelopes must still be included before CAD.

| Freeze status | Meaning |
| --- | --- |
| HOLD_REVISION_ENVELOPE | Published board identity exists; revision, full envelope and integration remain open |
| HOLD_SELECTION | An allowed alternative or physical component is not selected |
| HOLD_IDENTITY | Manufacturer, exact part or applicable evidence is missing |
| HOLD_CIRCUIT | A circuit/group is not sufficiently defined to select all physical parts |
| NOT_DESIGNED | Future custom mechanical/carrier part; no design created |
| REFERENCE_NOT_SELECTED | Evidence/comparison only; not in the approved build |

The completed revision 0.2 register contains **111 entries**: **54 Pod**,
**43 Keyfob** and **14 reference-only**. All 75 original IDs are retained;
the dimension register covers the same 111 IDs. These are controlled records,
not 111 separately purchased parts.

Dimension axes follow each row's `dimension_scope`, not automatically the
longest side or eventual assembly coordinates. BSC/basic dimensions are not
maximum tolerance bounds. In particular, MCP73831 DFN uses drawing D=2.00
and E=3.00 BSC, A=0.90 nominal / 1.00 maximum (C04-123C). PN532's drawn
D/E/A maxima 6.1/6.1/1.0 exclude the drawing's permitted protrusions up to
0.075 per side. Neither is a maximum module/installed-envelope claim.

## 2. Manufacturer evidence ledger

`SRC-01` through `SRC-22` preserve the original
[architecture source IDs](architecture.md#src-01). New evidence uses
`SRC-23` through `SRC-29`. Page numbers below are PDF page numbers unless
otherwise stated. No document is represented as a measurement of delivered
hardware.

### Board, sensor and charger evidence

| ID | Official source / inspected copy | Revision, evidence and limitations |
| --- | --- | --- |
| <a id="src-01"></a>SRC-01 | [Waveshare S3-Zero wiki](https://www.waveshare.com/wiki/ESP32-S3-Zero) | Rechecked: model, no-header / -M distinction, 3.7-6 V external-input guidance, GPIO21 RGB, USB/BOOT/UART and qualitative antenna guidance. Not a board current/thermal qualification. |
| <a id="src-02"></a>SRC-02 | [S3-Zero schematic](https://files.waveshare.com/wiki/ESP32-S3-Zero/ESP32-S3-Zero-Sch.pdf) | One sheet, revision unstated; downloaded and inspected. P15 and bottom pads, USB, LDO and LED nets. No cell charger/protector. |
| <a id="src-03"></a>SRC-03 | [S3-Zero 2D drawing](https://files.waveshare.com/wiki/ESP32-S3-Zero/ESP32-S3-Zero-2D-size.jpg) | Inspected manufacturer bottom-view drawing: 23.50 x 18.00 PCB, 2.54 pitch and 15.24 row spacing. No Z stack or tolerance-controlled assembly envelope. Round underside pads are not mounting screw holes. |
| <a id="src-04"></a>SRC-04 | [Waveshare C3-Zero wiki](https://www.waveshare.com/wiki/ESP32-C3-Zero) | Rechecked: ESP32-C3FH4, 3.7-6 V input guidance, GPIO10 RGB, BOOT9, USB18/19 and UART21/20; qualitative antenna guidance only. |
| <a id="src-05"></a>SRC-05 | [C3-Zero V2 schematic](https://files.waveshare.com/wiki/ESP32-C3-Zero/ESP32-C3-Zero-Sch-V2.pdf) | One sheet; V2 in filename, received revision TBD. Downloaded/inspected; 5 V RGB rail, shared USB/5 V power net, 18 board contacts. |
| <a id="src-06"></a>SRC-06 | [C3-Zero wiki dimensional image](https://www.waveshare.com/w/upload/e/e7/ESP32-C3-Zero_02.jpg) | Original G0 evidence retained. Additional store drawing directly inspected as SRC-24; neither provides the complete installed height. |
| <a id="src-07"></a>SRC-07 | [Espressif ESP32-S3 datasheet](https://documentation.espressif.com/esp32-s3_datasheet_en.pdf) | G0-inspected v2.2 retained: silicon pin functions, ADC, straps and electrical limits. Not re-downloaded during resume; do not equate silicon specifications with the Zero board. |
| <a id="src-08"></a>SRC-08 | [Espressif ESP32-C3 datasheet](https://documentation.espressif.com/esp32-c3_datasheet_en.pdf) | G0-inspected v2.5 retained, with the same silicon-versus-board limitation. |
| <a id="src-09"></a>SRC-09 | [NXP PN532/C1 datasheet](https://www.nxp.com/docs/en/nxp/data-sheets/PN532_C1.pdf) | Rev. 3.6, 2017-11-28, 222 pages. Pages 5, 8-9 and 213: PN5321A3HN/C1xx ordering family, all 40 pins and SOT618-1 outline. Actual ROM suffix and module applicability TBD. |
| <a id="src-10"></a>SRC-10 | [NXP UM0701-02](https://www.nxp.com/documents/user_manual/141520.pdf) | G0-inspected rev. 02, 2007-11-05 retained: startup I0=1/I1=0 for I2C; 7-bit address 0x24, write byte 0x48. Not a selected module's switch/contact drawing. |
| <a id="src-11"></a>SRC-11 | [TDK canonical MPU-6050 PDF](https://product.tdk.com/system/files/dam/doc/product/sensor/mortion-inertial/imu/data_sheet/mpu-6000-datasheet1.pdf); [inspected manufacturer-authored SparkFun mirror](https://cdn.sparkfun.com/assets/a/4/6/8/e/MPU_6050.pdf) | PS-MPU-6000A-00 rev. 3.4, 2013-08-19, 52 pages. Canonical request returned HTTP 403. Mirror inspected: pins on page 21, package/tolerances on page 41, mounting guidance in section 11. Not a GY-521 drawing. |
| <a id="src-12"></a>SRC-12 | [TDK MPU-6050 product page](https://product.tdk.com/en/search/sensor/mortion-inertial/imu/info?part_no=MPU-6050) | G0 manufacturer-index lifecycle warning retained; direct access was blocked. Current lifecycle and genuine supply require reconfirmation, not an automatic IMU substitution. |
| <a id="src-13"></a>SRC-13 | [Microchip DS20001984H](https://ww1.microchip.com/downloads/en/DeviceDoc/MCP73831-Family-Data-Sheet-DS20001984H.pdf); [product page](https://www.microchip.com/en-us/product/MCP73831) | 2020, 29 pages; PDF inspected. Page 3 electrical limits; page 11 both pin maps; page 20 DFN drawing; pages 22-24 SOT-23 drawing/land pattern. Product-page request returned 403, not the PDF. Full charger order suffix and project module remain TBD. |
| <a id="src-14"></a>SRC-14 | [Top Power original TP4056 datasheet](https://www.toppwr.com/uploadfile/file/20241228/676f612b9f2dd.pdf) | REV_2.3, revision history dated 2023-07-24, 17 pages, Chinese original. Pages 3-4, 6, 13-14: TP4056-42-ESOP8 / -EMSOP8, ratings, pins and both package drawings. Page 17 demo text conflicts with the page 4 voltage tolerance; see section 4. |
| <a id="src-15"></a>SRC-15 | [Microchip AN1149](https://ww1.microchip.com/downloads/en/AppNotes/01149b.pdf) | G0-inspected DS01149B, 2008 retained. Load-sharing reference only, not the selected charger module or an approved source tree. |
| <a id="src-16"></a>SRC-16 | [EEMB LP502030 page](https://www.eemb.com/product-130); [official cell specification](https://eemb.oss-accelerate.aliyuncs.com/uploads/20230309/b2e2e0f9d6717cad520c61d9d9deb4bd.pdf) | ZJQM-RD-SPC-H2305, 2022-10-25, 9 pages. Pages 3-4 inspected, including actual cell drawing. Bare solder-tab cell, not a protected pack. The drawing adds L1 and tab dimensions beyond the simple body-size table. |

### Retained interface evidence and existing comparisons

| ID | Source | Scope |
| --- | --- | --- |
| <a id="src-17"></a>SRC-17 | [ESP-IDF S3 ESP-NOW](https://docs.espressif.com/projects/esp-idf/en/v6.1/esp32s3/api-reference/network/esp_now.html), [C3 ESP-NOW](https://docs.espressif.com/projects/esp-idf/en/v6.1/esp32c3/api-reference/network/esp_now.html) | G0 protocol evidence retained; not mechanical/component qualification or a frozen firmware toolchain. |
| <a id="src-18"></a>SRC-18 | [ESP-IDF C3 sleep](https://docs.espressif.com/projects/esp-idf/en/v6.1/esp32c3/api-reference/system/sleep_modes.html) | G0 evidence retained; actual board sleep current and alert timing unmeasured. |
| <a id="src-19"></a>SRC-19 | [NXP AN10927](https://www.nxp.com/docs/en/application-note/AN10927.pdf) | G0-inspected rev. 4.1, 2018-07-05 retained: UID types. No exact external credential selected. |
| <a id="src-20"></a>SRC-20 | [Waveshare-linked XL-0807RGBC-WS2812B sheet](https://files.waveshare.com/wiki/common/XL-0807RGBC-WS2812B.pdf) | G0 evidence retained; source revision/manufacturer and fitted-LED equivalence TBD. Do not assign its package dimensions to the actual LEDs. Rail/VIH discrepancy remains open. |
| <a id="src-21"></a>SRC-21 | [Elechouse V3 manufacturer page](https://www.elechouse.com/elechouse/images/product/PN532_module_V3/); [V3 guide](https://www.elechouse.com/elechouse/images/product/PN532_module_V3/PN532_%20Manual_V3.pdf) | Guide rev. B, 2013-11-05, 13 pages. Pages 2-4 inspected: two published size claims, integral antenna, switch settings and wire routing. No dimensioned module/coil/keepout drawing located; dimensions remain unverified for freeze. |
| <a id="src-22"></a>SRC-22 | [onsemi P2N2222A/D](https://www.onsemi.com/download/data-sheet/pdf/p2n2222a-d.pdf); [product page](https://www.onsemi.com/products/discrete-power-modules/general-purpose-and-low-vcesat-transistors/p2n2222a) | Rev. 7, 2013-01; 8-page retrieved file. Pages 1-2 ratings/pins; pages 6-7 CASE 29-11, issue AM, 2007-03-09. Manufacturer-authored package data, not authorization to use its pin order for generic 2N2222 parts. |

### Additional physical-component evidence

| ID | Source | Revision, evidence and limitations |
| --- | --- | --- |
| <a id="src-23"></a>SRC-23 | [S3 SKU 25081](https://www.waveshare.com/esp32-s3-zero.htm?sku=25081); [C3 SKU 25452](https://www.waveshare.com/esp32-c3-zero.htm?sku=25452) | Official order pages inspected. Exact no-header identities; -M/header, N8R8 and kit options are not interchangeable. Store SKU is not a PCB revision or a stock/price commitment. |
| <a id="src-24"></a>SRC-24 | [C3 store dimensional drawing](https://www.waveshare.com/img/devkit/ESP32-C3-Zero/ESP32-C3-Zero-details-size.jpg) | Directly inspected: 23.50 x 18.00 PCB, 2.54 pitch, first-pad datum 1.59, left pad-center datum 1.38, corner R1.00. USB overhang is visible but not dimensioned; height and assembly tolerances TBD. |
| <a id="src-25"></a>SRC-25 | [Joy-IT SEN-MPU6050](https://joy-it.net/en/products/SEN-MPU6050); [datasheet](https://joy-it.net/files/files/Produkte/SEN-MPU6050/SEN-MPU6050_Datasheet_2021-11-04.pdf); [manual](https://joy-it.net/files/files/Produkte/SEN-MPU6050/SEN-MPU6050_Manual_2024-04-15.pdf) | Brand/supplier SIMAC Electronics GmbH / Joy-IT; datasheet 2021-11-04, manual 2024-04-15. Datasheet and manual page 2 inspected: 3.3-5 V supply, 3.3 V logic, 8 named contacts, 2.54 pitch. 25 x 20 x 7 is a published claim, not a located mechanical drawing. PCB revision/footprint remain TBD; not the selected GY-521. |
| <a id="src-26"></a>SRC-26 | [EEMB LP401730](https://www.eemb.com/product-125); [official cell specification](https://eemb.oss-accelerate.aliyuncs.com/uploads/20230309/202fb8205636483684d73d1caac2e13b.pdf) | ZJQM-RD-SPC-H0510, 2019-04-23, 9 pages. Pages 3-4 inspected: 150 mAh nominal / 140 mAh minimum, 3.7 V, tight 4.200 +/-0.020 V charging limit, 150 mA charge / 300 mA discharge maxima, cell/tab drawing. Bare cell only; no project pack or PCM selected. |
| <a id="src-27"></a>SRC-27 | [Vybronics VCLP1020B002L](https://www.vybronics.com/coin-vibration-motors/with-brushes/v-clp1020b002l); [official specification/drawing](https://www.vybronics.com/wp-content/uploads/datasheet-files/Vybronics-VCLP1020B002L-datasheet.pdf) | A/1, 2020-07-01, 14 PDF pages (cover plus 13 numbered pages). Former CLP1020B002L identity explained on PDF page 3. Pages 4-5 ratings; page 10 precautions; page 12 outline, tape and red-positive/blue-negative leads. Reference only; continuous-duty and final-case performance not qualified. |
| <a id="src-28"></a>SRC-28 | [SHOUHAN-authored MSK12C02 specification, Shotech mirror](https://www.shotech.de/Datasheet/shotech/SHOU-HAN-MSK12C02_C431540.pdf); [manufacturer-named purchase listing](https://www.digikey.com/en/products/detail/shenzhen-shouhan-technology-co-ltd/MSK12C02/30542588) | A/0, 2015-03-26, 10 PDF pages. Manufacturer Shenzhen SHOUHAN Technology Co., Ltd. PDF pages 3-4 and 10 inspected. Final assembly drawing has blank date/revision boxes; canonical manufacturer-hosted copy and applicability to the unspecified MSK-12C02 remain TBD. Marketplace attributes were not used as specifications. |
| <a id="src-29"></a>SRC-29 | [TDK PS1240P02BT product](https://product.tdk.com/en/search/sw_piezo/sw_piezo/piezo-buzzer/info?part_no=PS1240P02BT); [official PS catalog](https://product.tdk.com/system/files/dam/doc/product/sw_piezo/sw_piezo/piezo-buzzer/catalog/piezoelectronic_buzzer_ps_en.pdf) | Manufacturer-index lead only. Product/catalog access returned 403; the `/en/system/` catalog path also failed. Two authorized-distributor mirror URLs failed at transport level. No PDF was obtained; drawing, revision and electrical/SPL verification remain **TBD**. Not selected. |

## 3. Priority components: what is and is not established

| Project component | Verified evidence | Evidence still needed to freeze |
| --- | --- | --- |
| P-MCU; K-MCU-S3 | Waveshare classic no-header SKU and published PCB/pad documentation | Received PCB revision, fitted BOM/LED, maximum Z/USB/solder envelope, exact keepout and qualified power interface |
| K-MCU-C3 | Waveshare no-header SKU and V2 schematic; board XY outline | Selection versus S3, received revision, same physical/power evidence |
| P-NFC and P-NFC-ANT | NXP IC documentation; separate Elechouse reference | Exact module and antenna identity, coil and mounting drawing, maximum envelope, supply/I2C levels and RF keepout |
| P-IMU | MPU-6050 IC evidence; separate Joy-IT reference | Manufacturer-specific GY-521 order/revision, schematic and mechanical drawing; genuine IC/lifecycle |
| P-BATTERY; K-BATTERY | Separate EEMB bare-cell references with drawings | Finished protected-pack MPN/drawing, PCM, leads, connector/polarity, NTC, expansion limits and application approval |
| P-CHARGER; K-CHARGER | Original Microchip and Top Power IC families | Exact USB-C module/IC option, module drawing/schematic, programming resistor, CC, protection, temperature supervision and source/load sharing |
| P-PIEZO | Passive transducer required; no qualified exact part | Accessible official datasheet/drawing, voltage/capacitance, acoustic mounting and 105 dB test conditions; the blocked TDK lead closes none of these |
| K-MOTOR | Complete Vybronics reference drawing and stated electrical tests | Actual motor selection, startup/stall at the chosen rail, continuous-alert duty, adhesive/lead routing and haptic qualification |

## 4. Conflicts requiring decisions, not silent substitutions

1. **NFC size:** Elechouse V3 publishes 42.7 x 40.4 x 4 and rounded
   43 x 41 x 4 mm. Even the smaller claimed width exceeds the Pod's 30 mm
   outside target. A dimensioned drawing is still missing; the large published
   size is sufficient to flag this reference as an impractical flat-under-lid
   candidate, not to certify its dimensions.
2. **NFC separation:** the existing 1.5 mm wall/base/lid screen gives 13 mm
   Pod internal height. The LP502030 reference's maximum body thickness 5.3
   plus the specified 10 mm coil separation needs 15.3 mm before the antenna,
   supports or leads. The prior 18.3 mm conditional external lower bound
   remains valid, not a newly approved enclosure size.
3. **Battery tabs are not zero-sized:** both EEMB drawings specify L1 <=32 mm
   in addition to L <=31 mm and terminal dimensions. They are not finished
   PCM/connector envelopes. The Keyfob's ideal 32 mm internal length leaves
   no clearance for an L1-at-maximum cell before termination/pack design.
4. **Keyfob motor space:** the Vybronics body is diameter 10 +/-0.1 mm and
   2.1 +/-0.1 mm thick, with separate 0.15 mm nominal tape, a lead-exit
   feature and 25 +/-1 mm lead callout. Straight side-by-side screens with a
   23.5 x 18 board give 33.6 mm length or 28.1 mm width, exceeding the
   ideal 32 x 22 cavity. This flags stacking/placement work; it is not a
   universal no-fit proof.
5. **Tight battery charging tolerance:** LP401730 states 4.200 +/-0.020 V,
   hence 4.220 V upper limit. MCP73831-2 allows 4.232 V in its page 3 test
   conditions, and TP4056 page 4 allows 4.242 V at 0-85 deg C. These exceed
   that cell's limit by 12 mV and 22 mV respectively. A nominal "4.2 V"
   label does not establish compatibility. Cell, charger and full-temperature
   system tolerances require independent review.
6. **TP4056 internal source conflict:** page 4 gives 4.158-4.242 V
   (nominal +/-1%); page 17 demo-board text says 4.2 V +/-1.5%.
   Obtain manufacturer clarification. Neither statement qualifies a generic
   TP4056 module or permits a 1 A setting for these small cells.
7. **Elechouse logic claims conflict:** the guide/page describes standard
   5 V I2C/UART in one place and 3.3-24 V TTL in another. Do not treat this
   as permission to apply those levels to ESP32 or PN532 IC pins. Actual
   level-shifter/pull-up implementation and supply behavior require a schematic.
8. **Switch rating:** the SHOUHAN reference is rated 50 mA at 12 V DC,
   not an arbitrary battery/actuator power switch. Its 1.6 +/-0.1 mm travel,
   1.5 mm actuator extension, solder feet and locating posts also need space.
   It is not automatically the project's MSK-12C02.
9. **Unchanged critical holds:** shared native USB/external 5 V nets,
   unapproved external regulation, RGB supply/logic discrepancies, actual
   antenna keepouts and exact acoustic performance remain open.

The complete board-symbol review also corrected a revision 0.1 documentation
error: C3 GPIO18/USB D- is contact **15**, GPIO19/USB D+ is contact **16**.
The [logical table](pinout.md) and [verified map](verified-pinouts.md#c3-zero)
now agree with SRC-05. Application GPIO assignments are unchanged.

Both enclosure targets therefore remain unverified. See
[mechanical requirements](mechanical-requirements.md#feasibility) and
[power architecture](power-architecture.md) for assumptions and safety gates.

## 5. Retrieval and interruption record

On the 2026-11-11 resume, the existing 75-row revision 0.1 register was intact;
the three new register/index files had not been created. No background shell or delegated
agent remained running. Fourteen cached source PDFs were checked by signature,
parser, page count, visible identity and SHA-256, not by file existence alone.
Relevant drawings were visually inspected where text extraction was ambiguous.

A resumed manufacturer-endpoint check returned HTTP 200. The failed TDK
requests were HTTP 403; Mouser PS-catalog mirrors returned HTTP/2/empty-reply
transport errors, including the resumed alternate request. This does not prove
that every failure was caused by the user's Wi-Fi interruption.

No blocked/empty response is used as a verified datasheet. The following
follow-ups need Internet access or documents supplied directly by the maker:

- Retrieve the current TDK PS catalog and confirm PS1240P02BT drawing/revision,
  ratings and application suitability, or investigate a separately identified
  passive transducer. No 105 dB transducer has been qualified.
- Obtain canonical/current TDK MPU-6050 lifecycle evidence and confirm actual
  module provenance; the inspected mirror remains explicitly identified.
- Obtain current manufacturer-controlled SHOUHAN drawing/identity if that
  reference is proposed for selection.
- Obtain supplier-controlled drawings and schematics for the actual PN532,
  GY-521, charger modules and finished packs. Their absence is a selection
  gap, not simply a network failure.

### Inspected PDF fingerprints

These identify the source bytes inspected, not approval of their application.
Manufacturer PDFs are linked, not republished into this repository.

| Source / PDF | Pages | SHA-256 |
| --- | --- | --- |
| SRC-02 S3 schematic | 1 | `4bbdae93cde588eb87e20d7cda5b38fb729444d55cae0b579b329f23f0d69503` |
| SRC-05 C3 V2 schematic | 1 | `3fd4a8f696b47149eb5cbc61ef2325540f1a64c95c49b48e72ece54424044ab2` |
| SRC-09 PN532 | 222 | `46c4f04c44a36dfded8088e62cbcfe8cd3f785c460bb14f161ce0160ef84822d` |
| SRC-11 MPU manufacturer-authored mirror | 52 | `a4fdf69590b8cbab1cf0a5bcd359327b0ac022061fb233855aff2e191e7e3584` |
| SRC-13 MCP73831/2 | 29 | `75297f2a5235599368381adfb63df2652cc22d757f171f388147b2ab3d32776f` |
| SRC-14 TP4056 | 17 | `7ad1448a1539a093f534c45321f871d0536eec9619cc45ac4642820a600749d7` |
| SRC-16 LP502030 | 9 | `2179c91988de022cba7de275521c54ee4877a66348551ccdaf5efa3a2188689f` |
| SRC-21 Elechouse V3 | 13 | `3800d5935532d664015514c0199d2ce4313b3feccf563759642b424048a0cf07` |
| SRC-22 P2N2222A | 8 | `e67cb25a25529a21b464d2422c676b1c6194efd1069c8162425f4fdeda443618` |
| SRC-25 Joy-IT datasheet | 1 | `9f58e38b5c7fa0a6f69b53ca410e0b67a46adbe8265765fa0a41075234ed149a` |
| SRC-25 Joy-IT manual | 9 | `b4cdb3b074bdb758afdf78de94d01771370bf53e6a68893ac0b62a162d3ba47e` |
| SRC-26 LP401730 | 9 | `f07bffe0e5178a41f2c27e2ccb1d510b42b232bd62cf12e2c4f0ae36f7db3e12` |
| SRC-27 Vybronics motor | 14 | `eebdf5c027636a2a9570cc7043df9d4d80d3a8ac4e8df721d236c2f2e575a8b1` |
| SRC-28 SHOUHAN manufacturer-authored mirror | 10 | `5fcf67dbf95f3fbac1ce022137e316ac906860b5ef807aa1b5bad66d053200cf` |

## 6. Required release evidence

Resolve every applicable row's `freeze_blocker`, select one Keyfob board,
replace all remaining circuit/group placeholders with reviewed part-level
definitions, and obtain maximum installed envelopes and actual connector
orientations. Obtain supplier confirmation for ambiguous revisions and source
conflicts. Perform independent electrical/physical verification before release.
No change to a component, capacity, enclosure size or clearance is implicit.

## 7. Completion and recovery review - 2026-11-12

The later "Main pass failed" was a Copilot model-service connection timeout
(`ETIMEDOUT`) after five retries, not a failed CSV refinement. The saved
refinement command completed with exit code 0 and reported 111 IDs preserved.
The validation script was saved but had not run before the model failure.
The log does not establish whether the timeout originated in local networking
or upstream service/network conditions; earlier manufacturer retrieval failures
are separate evidence-access holds.

Recovery inspected all four deliverables and reused the 14 cached PDFs.
The first validation run exposed a checker bug: its test-ID pattern required
an ID-only cell and missed the roadmap's valid `T-01 GPIO / startup` style.
The checker was corrected, not the 24 valid roadmap entries. Original-ID
preservation is compared with fixed G0 commit
`13863c939cae64e06590eb81724b75ade7a83eb5`, not a moving `HEAD`.

Final validation results and the exact next action are recorded in
[LAST-WORKED-ON.md](../LAST-WORKED-ON.md). A completed documentation/evidence
task still does not close the physical component freeze.
