# Research Document Evidence Folder

Revision: 0.3 | Date: 2026-11-12 | Status: local evidence copy; documents not published

This folder preserves the identity of every document inspected for the
[datasheet index](../datasheet-index.md). It does **not** republish them.

## 1. What is and is not in Git

| Item | In Git / on GitHub | Purpose |
| --- | --- | --- |
| [README.md](README.md) | Yes | Policy, inventory and source attribution |
| [SHA256SUMS](SHA256SUMS) | Yes | SHA-256 of all 61 local files, in `shasum` format |
| [.gitignore](.gitignore) | Yes | Excludes `local/` from Git |
| `local/` (60 PDFs and 1 ZIP) | **No** | Local copies on the machine that performed the research |

**Zero manufacturer PDFs are committed or pushed.** `local/` exists only on
the research machine at `docs/datasheets/local/`. Its backup status is not
verified. The originals also remain in the Copilot session cache recorded in
[LAST-WORKED-ON.md](../../LAST-WORKED-ON.md).

## 2. Why the documents are not republished

The repository is public. A redistribution right was looked for in each
document and was not found for any of them:

- Texas Instruments data sheets state that TI grants permission to use them
  only for developing an application that uses the TI product, and that
  "Other reproduction and display of these resources is prohibited."
- The Nanjing Micro One ME6217 sheet states that reproduction or copying
  without express permission is strictly prohibited.
- The GCT USB4105/USB4125 drawings state that they are confidential, are the
  copyright of Global Connector Technology and must not be copied or disclosed
  without written consent.
- NXP, Microchip, onsemi, Diodes Incorporated, ABLIC, Espressif and InvenSense
  documents carry copyright or all-rights-reserved notices and grant no
  redistribution licence.
- The Waveshare, EEMB, Elechouse, Joy-IT, Jauch, Renata, Varta, PKCELL,
  Vybronics, Precision Microdrives, Same Sky, Alps Alpine, JST, C&K and
  SHOUHAN documents contain no licence statement in their extracted text.
  Absence of a statement is not permission.

The Joy-IT manual mentions an MIT licence, but that applies to its software
library, not to the manual. No document was found to be redistributable, so
none is committed. This is a conservative reading, not legal advice. If an
owner obtains written permission for a specific document, it may be added
with that permission recorded here.

## 3. How to restore or verify the local copies

1. Download each document from the URL in section 4 into
   `docs/datasheets/local/` under the listed file name.
2. From `docs/datasheets/local/`, run `shasum -a 256 -c ../SHA256SUMS`.

A matching hash proves the file is byte-identical to the inspected copy.
A different hash means the publisher has changed the document; the new
revision must be re-inspected before any register value is trusted.
Single-page extracts and the page renders used for visual inspection were
derived locally from the listed parent PDF and cannot be re-downloaded.

Retrieval dates: files in section 4.1 on 2026-11-11; files in sections 4.2
to 4.6 on 2026-11-12. A successful download on those dates is not a promise
that the URL still resolves.

## 4. Inventory

Hosting: **M** manufacturer, **D** distributor or retailer hosting the
manufacturer's document, **T** third-party mirror. Source IDs refer to the
[datasheet index](../datasheet-index.md).

### 4.1 Component-evidence task (14 primary PDFs and 8 extracts)

| Local file | Pages | Source | Host | Document |
| --- | --- | --- | --- | --- |
| `s3-schematic.pdf` | 1 | SRC-02 | M | Waveshare ESP32-S3-Zero schematic |
| `c3-v2-schematic.pdf` | 1 | SRC-05 | M | Waveshare ESP32-C3-Zero V2 schematic |
| `pn532-ic.pdf` | 222 | SRC-09 | M | NXP PN532/C1 rev. 3.6 |
| `pn532-ic-page-213.pdf` | 1 | SRC-09 | Extract | Package outline page of the above |
| `mpu6050-manufacturer-mirror.pdf` | 52 | SRC-11 | T | InvenSense PS-MPU-6000A-00 rev. 3.4, SparkFun-hosted |
| `mcp73831.pdf` | 29 | SRC-13 | M | Microchip DS20001984H |
| `mcp73831-page-20.pdf`, `mcp73831-page-23.pdf` | 1 each | SRC-13 | Extract | DFN and SOT-23 drawings |
| `tp4056.pdf` | 17 | SRC-14 | M | Top Power TP4056 REV_2.3 |
| `tp4056-page-13.pdf`, `tp4056-page-14.pdf` | 1 each | SRC-14 | Extract | ESOP8 and EMSOP8 drawings |
| `eemb-lp502030.pdf` | 9 | SRC-16 | M | EEMB LP502030 cell specification |
| `eemb-lp502030-drawing.pdf` | 1 | SRC-16 | Extract | Cell drawing page |
| `elechouse-v3.pdf` | 13 | SRC-21 | M | Elechouse PN532 V3 guide rev. B |
| `p2n2222a.pdf` | 8 | SRC-22 | M | onsemi P2N2222A/D rev. 7 |
| `joyit-mpu6050-datasheet.pdf`, `joyit-mpu6050-manual.pdf` | 1, 9 | SRC-25 | M | Joy-IT SEN-MPU6050 |
| `eemb-lp401730.pdf` | 9 | SRC-26 | M | EEMB LP401730 cell specification |
| `vybronics-vclp1020b002l.pdf` | 14 | SRC-27 | M | Vybronics VCLP1020B002L A/1 |
| `vybronics-vclp1020b002l-drawing.pdf` | 1 | SRC-27 | Extract | Outline drawing page |
| `shouhan-msk12c02-mirror.pdf` | 10 | SRC-28 | T | SHOUHAN MSK12C02 A/0, Shotech-hosted |
| `shouhan-msk12c02-mirror-page-10.pdf` | 1 | SRC-28 | Extract | Assembly drawing page |

### 4.2 G1 power candidates

| Local file | Pages | Source | Host | Document and URL |
| --- | --- | --- | --- | --- |
| `ti-bq25185.pdf` | 32 | SRC-30 | M | TI SLUSF65B, <https://www.ti.com/lit/ds/symlink/bq25185.pdf> |
| `ti-bq25185-page-16.pdf` | 1 | SRC-30 | Extract | Table 6-1 resistor map page |
| `ti-bq25180.pdf` | 58 | SRC-31 | M | TI SLUSE99C, <https://www.ti.com/lit/ds/symlink/bq25180.pdf> |
| `ti-bq24074.pdf` | 55 | SRC-32 | M | TI SLUS810N, <https://www.ti.com/lit/ds/symlink/bq24074.pdf> |
| `ti-bq25100.pdf` | 34 | SRC-33 | M | TI SLUSBV8C, <https://www.ti.com/lit/ds/symlink/bq25100.pdf> |
| `ti-lm66100.pdf` | 23 | SRC-34 | M | TI SLVSEZ8A, <https://www.ti.com/lit/ds/symlink/lm66100.pdf> |
| `ti-tps63900.pdf` | 40 | SRC-35 | M | TI SLVSET3D, <https://www.ti.com/lit/ds/symlink/tps63900.pdf> |
| `ti-tps63802.pdf` | 38 | SRC-35 | M | TI SLVSEU9D, <https://www.ti.com/lit/ds/symlink/tps63802.pdf> |
| `ti-tps7a02.pdf` | 48 | SRC-35 | M | TI SBVS277C, <https://www.ti.com/lit/ds/symlink/tps7a02.pdf> |
| `me6217-semikey-mirror.pdf` | 10 | SRC-36 | T | Micro One ME6217 V02, <https://cdn.semikey.com/upload/pdfs/7b/e4/7be455574826533ba0e2da975ad5acc2.pdf> |
| `esp32-s3-datasheet.pdf` | 87 | SRC-07 | M | Espressif ESP32-S3 datasheet v2.2 |
| `esp32-c3-datasheet.pdf` | 78 | SRC-08 | M | Espressif ESP32-C3 datasheet v2.5 |

### 4.3 G1 battery candidates

| Local file | Pages | Source | Host | Document and URL |
| --- | --- | --- | --- | --- |
| `jauch-lp502030jh-pcm.pdf` | 2 | SRC-37 | M | Jauch 246484 rev. 1.1, <https://www.jauch.com/downloadfile/66ced1afd16e56368a3baa9709610e3a5/matd_246484_lp502030jhpcm2_wires_50mm.pdf> |
| `jauch-lp402025ju-pcm.pdf` | 2 | SRC-37 | M | Jauch 246483 rev. 1.2, <https://www.jauch.com/downloadfile/677e3528e2de71444db6cca90654e9171/matd_246483_20200507_140mah_-_lp402025ju_1s1p_2_wire_50mm.pdf> |
| `jauch-lp851719ju-pcm.pdf` | 2 | SRC-37 | M | Jauch 237924 rev. 1.2, <https://www.jauch.com/downloadfile/677e33c97ce2259996c3e0a625aa7071d/matd_237924_20200507_180mah_-_lp851719ju_1s1p_2_wire_50mm.pdf> |
| `renata-icp521630pm-01.pdf` | 1 | SRC-38 | M | Renata ICP521630 V02 08/2019, <https://www.renata.com/en-us/downloads/?product=icp521630pm-01&fileid=fb9cc7a6eec92dccb1aceb95d6> |
| `renata-icp402025pc-01.pdf` | 1 | SRC-38 | M | Renata ICP402025 V02 08/2019, <https://www.renata.com/en-us/downloads/?product=icp402025pc-01&fileid=7c3ca5178ae13a0827c8eaa4b0> |
| `renata-icp401835tprt.pdf` | 1 | SRC-38 | M | Renata ICP401835TPRT V01 11/2022, <https://www.renata.com/en-us/downloads/?product=icp401835tprt&fileid=98a7e2068a84661aff18656f05> |
| `renata-icp402025pc-01-spec-conrad.pdf` | 14 | SRC-38 | D | Renata product specification V2.0, 2016-03-10, <https://asset.conrad.com/media10/add/160267/c1/-/en/000252023DS01/datasheet-252023-renata-icp402025pc-1-non-standard-battery-rechargeable-prismatic-plug-lipo-37-v-155-mah.pdf> |
| `varta-lpp402025-pcm-anglia.pdf` | 1 | SRC-39 | D | Varta 56416 201 020 rev. 3, <https://www.anglia.com/registration/pcn_ptn/docs/pcn/PCN_VAR_56416201020_1.pdf> |
| `adafruit-1317-lp402025-pcm.pdf` | 5 | SRC-40 | D | PKCELL QA.S.0228 edition A, <https://cdn-shop.adafruit.com/product-files/1317/C1515_-_Li-Polymer_402025_150mAh_3.7V_with_PCM.pdf> |
| `pkcell-lp402025-page-5.pdf` | 1 | SRC-40 | Extract | Pack drawing page of the above |
| `ablic-s8261.pdf` | 34 | SRC-41 | M | ABLIC S-8261 rev. 5.5_00, <https://www.ablic.com/en/doc/datasheet/battery_protection/S8261_E.pdf> |

### 4.4 G1 NFC candidate

| Local file | Pages | Source | Host | Document and URL |
| --- | --- | --- | --- | --- |
| `elechouse-pn5321-mini-manual.pdf` | 15 | SRC-43 | M | Elechouse PN5321 MINI datasheet rev. 1.5, <https://www.elechouse.com/wp-content/uploads/2024/07/Elechouse-Pn5321-Mini-Product-Manual-V1.pdf> |
| `elechouse-miniv2-dimension.zip` | - | SRC-43 | M | DWG archive, not opened, <https://www.elechouse.com/wp-content/uploads/2024/07/MINIV2_dimention.zip> |

### 4.5 G1 actuator and driver candidates

| Local file | Pages | Source | Host | Document and URL |
| --- | --- | --- | --- | --- |
| `samesky-cpt-2475-92t.pdf` | 5 | SRC-44 | M | Same Sky CPT-2475-92T, 09/11/2024, <https://www.sameskydevices.com/product/resource/cpt-2475-92t.pdf> |
| `diodes-pam8904.pdf` | 10 | SRC-45 | M | Diodes DS37246 rev. 6-2, <https://www.diodes.com/assets/Datasheets/PAM8904.pdf> |
| `diodes-1n4148w.pdf` | 5 | SRC-45 | M | Diodes DS30086 rev. 32-2, <https://www.diodes.com/assets/Datasheets/BAV16W_1N4148W.pdf> |
| `pmd-310-103.pdf` | 8 | SRC-46 | M | Precision Microdrives 310-103 R002-V011, <https://precisionmicrodrives.com/cdn/catalog_product/89437681-576e-46e1-97cf-5ae185adeb1c/310-103-datasheet.pdf> |
| `pmd-308-100.pdf` | 7 | SRC-46 | M | Precision Microdrives 308-100 R002-V012, <https://precisionmicrodrives.com/cdn/catalog_product/445ff874-bf32-474d-9e41-d7606db3b147/308-100-datasheet.pdf> |
| `vybronics-vc0834b011f.pdf` | 10 | SRC-47 | M | Vybronics VC0834B011F A/2, <https://www.vybronics.com/wp-content/uploads/datasheet-files/Vybronics-VC0834B011F-datasheet.pdf> |
| `onsemi-mmbt2222.pdf` | 10 | SRC-48 | M | onsemi MMBT2222LT1/D rev. 13, <https://www.onsemi.com/download/data-sheet/pdf/mmbt2222lt1-d.pdf> |

### 4.6 G1 switch and connector candidates

| Local file | Pages | Source | Host | Document and URL |
| --- | --- | --- | --- | --- |
| `alps-skrpabe010.pdf` | 6 | SRC-49 | M | Alps Alpine SKRPABE010 specification 201707, <https://tech.alpsalpine.com/cms.media/product_spec_skrpabe010_en_c1c577738a.pdf> |
| `alps-sksclbe010.pdf` | 6 | SRC-49 | M | Alps Alpine SKSCLBE010 specification 201707, <https://tech.alpsalpine.com/cms.media/product_spec_sksclbe010_en_f052c78d76.pdf> |
| `ck-pcm12smtr-future.pdf` | 2 | SRC-50 | D | C&K PCM series catalogue pages, <https://www1.futureelectronics.com/doc/C%20&%20K%20COMPONENTS/PCM12SMTR.pdf> |
| `jst-ph.pdf` | 5 | SRC-51 | M | JST PH catalogue, <https://www.jst-mfg.com/product/pdf/eng/ePH.pdf> |
| `jst-sh.pdf` | 4 | SRC-51 | M | JST SH catalogue, <https://www.jst-mfg.com/product/pdf/eng/eSH.pdf> |
| `gct-usb4105.pdf` | 2 | SRC-52 | M | GCT USB4105 drawing, <https://gct.co/files/drawings/usb4105.pdf> |
| `gct-usb4125.pdf` | 2 | SRC-52 | M | GCT USB4125 drawing rev. A6, <https://gct.co/files/drawings/usb4125.pdf> |

Totals: 14 + 36 = 50 primary PDFs, 8 + 2 = 10 single-page extracts and
1 ZIP archive, 61 files.

## 5. Revision record

| Revision | Date | Change |
| --- | --- | --- |
| 0.3 | 2026-11-12 | Folder created; 61 local files fingerprinted; redistribution review recorded; no document published |
