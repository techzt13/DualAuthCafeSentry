# Manufacturer-Verified Pinouts and Interface Holds

Revision: 0.3 | Date: 2026-11-12 | Status: document verification; NOT a wiring release

Read the [evidence index](datasheet-index.md), [component register](component-register.csv)
and [logical connection schedule](pinout.md) together. **V** means a documented
pin function, **S** a specification assignment, **P** a project proposal and
**TBD** missing evidence. No module-header orientation, connector polarity or
footprint is inferred from a generic product name.

All numbers below are identified as GPIO, schematic contact or IC package pin.
They are not interchangeable. Manufacturer drawing views must be used for
physical orientation; these tables are not footprint drawings. Confirm the
received assembly and markings before connecting power.

## 1. Waveshare board contacts

<a id="s3-zero"></a>
### 1.1 ESP32-S3-Zero: Pod and permitted Keyfob alternative

**V:** Waveshare classic no-header **SKU 25081**, ESP32-S3FH4R2 version;
not the -M/header or N8R8 variant. Basis: the revision-unstated
[S3 schematic, SRC-02](datasheet-index.md#src-02), the
[bottom-view drawing, SRC-03](datasheet-index.md#src-03) and
[order page, SRC-23](datasheet-index.md#src-23).
Received PCB revision and complete assembly envelope remain TBD.

| P15 schematic contact | Documented connection | Pod application | S3 Keyfob application |
| --- | --- | --- | --- |
| 1 | GPIO43 / UART0 TX through board R6, 499 ohm | Service only | Service only |
| 2 | GPIO44 / UART0 RX | Service only | Service only |
| 3 | GPIO13 | P: conditioned charging status | P: conditioned charging status |
| 4 | GPIO12 | P: MPU INT | Unassigned |
| 5 | GPIO11 | P: conditioned PN532 reset input | Unassigned |
| 6 | GPIO10 | Selected PN5321 MINI host interface has no IRQ; NC | Unassigned |
| 7 | GPIO9 | S: optional protected tether sense | Unassigned |
| 8 | GPIO8 | S: optional protected tether drive | Unassigned |
| 9 | GPIO7 | S: multifunction button to ground | P: button to ground |
| 10 | GPIO6 | S: piezo-driver control via 1 kohm | P: motor-driver control |
| 11 | GPIO5 | S: shared I2C SCL | Unassigned |
| 12 | GPIO4 | S: shared I2C SDA | Unassigned |
| 13 | GPIO3 | Reserved strap | Reserved strap |
| 14 | GPIO2 | Unassigned | Unassigned |
| 15 | GPIO1 / ADC1_CH0 | P: protected/scaled battery monitor | P: protected/scaled battery monitor |
| 16 | 3V3 / onboard LDO output | Power-interface hold | Power-interface hold |
| 17 | GND | Pod local ground | Keyfob local ground |
| 18 | VBUS / external 5 V pad | Shared native-USB input net; not raw battery | Same hold |

Additional underside schematic pads, all unassigned externally:

| Pad reference | GPIO | Constraint |
| --- | --- | --- |
| P2 | 45 | Strap; reserve |
| P3 | 42 | Unassigned |
| P4 | 41 | Unassigned |
| P5 | 40 | Unassigned |
| P6 | 39 | Unassigned |
| P7 | 38 | Unassigned |
| P12 | 14 | Unassigned |
| P14 | 15 | Unassigned |
| P16 | 16 | Unassigned |
| P17 | 17 | Unassigned |
| P18 | 18 | Unassigned |

Native USB D-/D+ use GPIO19/20 through the board's 22 ohm paths.
GPIO21 drives RGB DIN. BOOT K2 pulls GPIO0 to ground; RESET K1 pulls
CHIP_PU to ground. Reserve these functions. GPIO0/3/45/46 are silicon
straps; GPIO46 is not an available external application contact in this map.
Internal/memory or unexposed signals are not spare board pads
([SRC-07](datasheet-index.md#src-07)).

<a id="c3-zero"></a>
### 1.2 ESP32-C3-Zero: Keyfob evaluation option

**V:** Waveshare no-header **SKU 25452**, ESP32-C3FH4; reviewed schematic
filename **V2**, received revision TBD
([SRC-05](datasheet-index.md#src-05), [SRC-23](datasheet-index.md#src-23)).
Select this board **or** the S3 alternative, not both.

| C3 board-symbol contact | Documented connection | Keyfob application |
| --- | --- | --- |
| 1 | 5 V / native USB VBUS | Power-interface hold; not raw battery |
| 2 | GND | Keyfob local ground |
| 3 | VCC3.3 / onboard LDO output | External-feed isolation TBD |
| 4 | GPIO0 / ADC1_CH0 | P: protected/scaled battery monitor |
| 5 | GPIO1 | P: conditioned charging status |
| 6 | GPIO2 | Reserved strap |
| 7 | GPIO3 | P: motor-driver control |
| 8 | GPIO4 | P: button to ground |
| 9 | GPIO5 | Unassigned |
| 10 | GPIO6 | Unassigned |
| 11 | GPIO7 | Unassigned |
| 12 | GPIO8 | Reserved strap |
| 13 | GPIO9 | Reserved BOOT/strap |
| 14 | GPIO10 | Reserved onboard RGB DIN |
| 15 | GPIO18 / USB D- | Reserved native USB |
| 16 | GPIO19 / USB D+ | Reserved native USB |
| 17 | GPIO20 / UART0 RX | Service only |
| 18 | GPIO21 / UART0 TX | Service only |

**Correction to revision 0.1:** the old logical table reversed the USB pad
pair. The V2 schematic shows **GPIO18 at contact 15** and **GPIO19 at
contact 16**. The [logical table](pinout.md) is corrected; GPIO functions and
the original Pod assignments are unchanged.

GPIO2/8/9 are straps. GPIO4-7 share external pad-JTAG functions, so the
proposed button allocation assumes native USB debugging, not simultaneous
pad-JTAG use. GPIO11 is not exposed here; GPIO12-17 are flash/unexposed
([SRC-08](datasheet-index.md#src-08)). BOOT pulls GPIO9 to ground; the
onboard reset switch pulls CHIP_EN to ground.

<a id="native-usb"></a>
### 1.3 Existing native USB-C, not the unselected charging/tether port

These are the labels/nets in the two board schematics, **not** an exact
receptacle manufacturer footprint. S3 uses `Type_C1`; C3 uses `Port1`.

| USB contact labels | S3 connection | C3 V2 connection |
| --- | --- | --- |
| A4/B9 and A9/B4 | VBUS / P15-18 | USB VCC / board contact 1 |
| A1/B12 and A12/B1 | GND | GND |
| A6, B6 | D+ to GPIO20 through board path | D+ to GPIO19 |
| A7, B7 | D- to GPIO19 through board path | D- to GPIO18 |
| A5 / CC1 | R4, 5.1 kohm to GND | IP0 / R30, 5.1 kohm to GND |
| B5 / CC2 | R5, 5.1 kohm to GND | IP1 / R25, 5.1 kohm to GND |
| A8 / SBU1; B8 / SBU2 | Unconnected | Unconnected |
| MTB / shell connection | GND in schematic | GND in schematic |

The boards do not contain a LiPo charger or protector. External 5 V and native
USB share a net. Full receptacle part number, pad numbering convention, rated
current, retention, mating-plug envelope and ESD qualification are TBD.
Charging USB-C and the optional tether must not inherit this service-port
mapping without a reviewed design. See [power architecture](power-architecture.md).

<a id="board-constituents"></a>
### 1.4 Included regulator, LED and antenna

| Included part | Documented board connection | Remaining hold |
| --- | --- | --- |
| ME6217C33M5G, both schematics | Symbol pins 1 VIN, 2 GND, 3 EN, 4 BP, 5 VOUT; VIN/EN on USB/5 V input, VOUT on 3.3 V | Manufacturer datasheet/revision, reverse-current behavior and fitted identity TBD; this is schematic evidence only. S3 BP is NC; C3 BP has a bypass capacitor. |
| S3 RGB U1 | Symbol pins 1 VDD to 3.3 V, 2 DOUT NC, 3 VSS to GND, 4 DIN to GPIO21 | Exact fitted LED and package orientation TBD |
| C3 RGB WS_L1 | VDD to 5 V, DIN to GPIO10, VSS to GND, OUT unconnected | Schematic does not establish a physical package pin-number map |
| Each ceramic radio antenna | Module-internal RF/matching path | Exact antenna manufacturer, part, revision, contacts and numeric keepout TBD; not an external antenna connector |

The linked LED sheet is not proof of the fitted part. Its stated supply/VIH
limits conflict with the shown board rails/logic; do not approve either LED
interface by assuming a compatible variant
([SRC-20](datasheet-index.md#src-20)).

## 2. Pod sensor and NFC interfaces

<a id="module-headers"></a>
### 2.1 Evaluation module interfaces now represented in the Pod schematic

These are practical prototype candidates, not owner-frozen component selections. The physical modules and revisions received by the builder must be checked before wiring.

| Assembly | Evaluation candidate and documented interface | Remaining physical/electrical hold |
| --- | --- | --- |
| NFC module | ELECHOUSE PN5321 MINI SKU NFC_EX_MINI, hardware V2; I2C address 0x24; 3.3 V logic; silkscreen names GND, 5V/3V3, RST, SCK, MISO, TX/MOSI/SDA, RX/SS/SCL | Current v1.1 online manual and earlier downloaded v1.5 record differ; cable contact numbering, mating connector family and actual module revision must be confirmed. Host connector has no IRQ. |
| NFC antenna | Included ferrite-backed 10 x 25 mm antenna option; 0.2 mm stated thickness; 100 mm lead | Actual lead/connector revision and antenna drawing/installation tolerances remain TBD. Keep the project's 10 mm battery and piezo separation. |
| IMU | Adafruit MPU-6050 breakout product 3886; 1 x 6 header and STEMMA QT; VIN, 3Vo, GND, SCL, SDA, INT | O-04 remains open; no owner selection. Exact fitted revision/header height, board tolerances and received-unit inspection remain TBD. |
| GY-521 reference | MPU-6050-family interface required by the specification | No unique manufacturer is selected; Adafruit 3886 is a separate evaluation candidate, not silently treated as the generic GY-521. |

**PN5321 MINI I2C host signals (use silkscreen names, not cable colour/order):** GND; 5V/3V3 supply; active-low RST; SCK and MISO unused in I2C; TX/MOSI/SDA becomes SDA; RX/SS/SCL becomes SCL. The host header does not expose IRQ, so S3 GPIO10 / P15-6 is deliberately NC and firmware polling is required. The v1.1 online manual describes onboard 3.3 V I2C pull-ups; earlier v1.5 project evidence describes unpopulated pull-up footprints. Carrier pull-ups remain DNP until the received board is inspected.

**Adafruit 3886 six-pin header:** 1 VIN; 2 3Vo (regulator output, do not feed); 3 GND; 4 SCL; 5 SDA; 6 INT. The official board source shows a 10 kΩ AD0 pull-down by default and a solder-jumper option to 3.3 V, yielding 0x68 by default and 0x69 when high. The breakout includes its own I2C level shifting and 10 kΩ pull-ups; do not add carrier pull-ups without calculating the combined bus resistance. STEMMA QT uses GND, VIN, SDA and SCL.


<a id="pn532"></a>
### 2.2 PN532/C1 IC, HVQFN40 / SOT618-1

**V:** NXP rev. 3.6, pages 8-9, Table 3
([SRC-09](datasheet-index.md#src-09)). Exact PN5321A3HN/C1xx ROM/order
suffix and module applicability remain TBD. This is an IC reference, not a
module header or a complete bare-IC circuit.

| IC pin(s) | Manufacturer function | Project treatment / limitation |
| --- | --- | --- |
| 1 | DVSS | Digital ground within module |
| 2 | LOADMOD, output | Module RF implementation; no external application allocation |
| 3, 7 | TVSS1, TVSS2 | Transmitter grounds |
| 4, 6 | TX1, TX2, outputs | Verified module matching/antenna network only |
| 5 | TVDD | Transmitter supply; module implementation TBD |
| 8 | AVDD | Analog supply; module implementation TBD |
| 9 | VMID, output | Internal receiver-bias reference; not an external supply input |
| 10 | RX, input | RF receive/matching network |
| 11 | AVSS | Analog ground |
| 12, 13 | AUX1, AUX2, outputs | Test functions; no external allocation |
| 14, 15 | OSCIN, OSCOUT | Manufacturer-correct crystal circuit within module |
| 16, 17 | I0, I1, inputs | V: firmware boot I2C selection 1, 0; actual module strap translation TBD |
| 18 | TESTEN, input | Manufacturer requires ground for normal operation |
| 19 | P35, I/O | No external allocation |
| 20, 21, 22 | N.C. | No connection |
| 23 | PVDD | Pad supply, 1.6-3.6 V; host-interface reference |
| 24 | P30 / UART_RX, I/O | Debug UART alternative; no application connection |
| 25 | P70_IRQ, I/O | The IC has P70_IRQ, but the selected module does not expose IRQ; poll at host |
| 26 | RSTOUT_N, output | Reset indication only; never drive as reset |
| 27 | NSS / P50_SCL / HSU_RX, I/O | S: I2C SCL from Pod GPIO5 |
| 28 | MOSI / SDA / HSU_TX, I/O | S: I2C SDA to/from Pod GPIO4 |
| 29 | MISO / P71, I/O | No separate SPI allocation in I2C mode |
| 30 | SCK / P72, I/O | No separate SPI allocation in I2C mode |
| 31 | P31 / UART_TX, I/O | Debug alternative; no application allocation |
| 32, 33 | P32_INT0, P33_INT1, I/O | No external allocation |
| 34 | P34 / SIC_CLK, I/O | Secure-IC interface unused externally |
| 35, 36 | SIGOUT output, SIGIN input | Secure-IC interface unused externally |
| 37 | SVDD, output | Switchable secure-IC supply; not main power input |
| 38 | RSTPD_N, input | P: conditioned active-low reset/power-down from Pod GPIO11 |
| 39 | DVDD, output | Internal digital supply; not an arbitrary 3.3 V input |
| 40 | VBAT | Main external IC supply, 2.7-5.5 V |

Unused module interfaces must follow the actual module schematic. No invented
exposed-pad pin number, grounding prescription or floating-input policy is
added by this table. RF matching values and complete decoupling remain inside
the verified purchased assembly, or require a separately authorized design.

The firmware host address is **7-bit 0x24**: write byte **0x48**, read byte
**0x49**. NXP UM0701-02 boot straps I0=1/I1=0 do not establish another
module's switch labels ([SRC-10](datasheet-index.md#src-10)).

<a id="mpu6050"></a>
### 2.3 MPU-6050 IC, 24-pin QFN

**V:** InvenSense PS-MPU-6000A-00 rev. 3.4, page 21, from the disclosed
manufacturer-authored mirror ([SRC-11](datasheet-index.md#src-11)).
The column here is specifically **MPU-6050**, not MPU-6000.

| IC pin(s) | MPU-6050 function | Treatment / limitation |
| --- | --- | --- |
| 1 | CLKIN | Ground when unused |
| 2, 3, 4, 5 | NC | No connection |
| 6, 7 | AUX_DA, AUX_CL | Auxiliary sensor bus; not Pod SDA/SCL |
| 8 | VLOGIC | 1.71 V to VDD; not the MPU-6000 SPI CS function |
| 9 | AD0 | P: ground for address 0x68; high gives 0x69 |
| 10 | REGOUT | Manufacturer-specified regulator capacitor; module-internal |
| 11 | FSYNC | Ground when unused |
| 12 | INT | P: interrupt to Pod GPIO12; polarity/drive configured and verified |
| 13 | VDD | 2.375-3.46 V IC supply |
| 14, 15, 16, 17 | NC | No connection |
| 18 | GND | Ground |
| 19 | RESV | Do not connect |
| 20 | CPOUT | Manufacturer-specified charge-pump capacitor; module-internal |
| 21, 22 | RESV | Do not connect |
| 23 | SCL | S: Pod GPIO5 |
| 24 | SDA | S: Pod GPIO4 |

Exposed-pad treatment must follow verified manufacturer mounting guidance;
do not invent a numbered contact or tie from the package drawing alone.
Proposed address **0x68** has write/read bytes **0xD0/0xD1**;
alternative **0x69** has **0xD2/0xD3**. Audit actual AD0 and module pulls.
No address collision exists with PN532 0x24.

## 3. Charging, batteries and controls

<a id="chargers"></a>
### 3.1 Charger IC references, not selected USB-C modules

**V:** Microchip DS20001984H page 11
([SRC-13](datasheet-index.md#src-13)):

| MCP73831 function | SOT-23-5 pin | DFN8 pin(s) |
| --- | --- | --- |
| STAT | 1 | 5 |
| VSS | 2 | 6 |
| VBAT | 3 | 3, 4 |
| VDD | 4 | 1, 2 |
| PROG | 5 | 8 |
| NC | Not applicable | 7 |
| Exposed pad | Not applicable | EP9; connect to VSS |

MCP73831 STAT is **tri-state**, unlike MCP73832's open-drain STAT.
Full voltage/termination/package suffix is TBD. Neither package supplies
a separate SYS output, battery-temperature input or complete pack protection.

**V:** Top Power TP4056 REV_2.3 page 6; both listed
**TP4056-42-ESOP8** and **TP4056-42-EMSOP8**
([SRC-14](datasheet-index.md#src-14)):

| Pin | Function | Interface requirement |
| --- | --- | --- |
| 1 | TEMP | Cell-temperature network; grounding disables monitoring |
| 2 | PROG | Exact candidate-specific current-programming resistor |
| 3 | GND | Protected/system ground |
| 4 | VCC | Qualified charge input |
| 5 | BAT | Protected battery positive |
| 6 | STDBY | Active-low/high-impedance charge-complete status |
| 7 | CHRG | Active-low/high-impedance charging status |
| 8 | CE | Defined enable/inhibit state |

Do not assign a fictional EP pin 9 to TP4056 or copy a clone's footprint.
Thermal-pad electrical and land-pattern treatment require the exact package
documentation/review. These IC maps do not identify generic module
`IN+/IN-/B+/B-/OUT+/OUT-` pads, their protection contents or orientation.

**Hold:** the LP401730 reference's 4.220 V maximum charge limit is below
MCP73831-2's stated 4.232 V and TP4056's 4.242 V maxima under their cited
test conditions. TP4056 also contains conflicting tolerance statements.
See [power architecture](power-architecture.md); nominal voltage matching is
not compatibility approval.

<a id="battery-connectors"></a>
### 3.2 Finished batteries and connector halves

Each unit has separate battery, protection, plug and receptacle entries.
Exact cell/pack MPN, PCM B+/B-/P+/P- implementation, NTC contacts, pin-1
view, wire color, connector pitch, polarity and mating MPNs are **TBD**.
Do not assume a familiar connector shape fixes polarity.

EEMB LP502030 and LP401730 are **bare solder-tab cell references** with
positive/negative terminals identified in their own drawings, not numbered
pack connectors. They provide no qualified project PCM/NTC/lead assembly.
Do not improvise direct pouch soldering or use the raw negative terminal to
bypass a protector. Charger and system returns must follow the independently
reviewed finished-pack topology.

<a id="actuators"></a>
### 3.3 Piezo, motor and driver references

| Part / scope | Verified pin or connection evidence | Application hold |
| --- | --- | --- |
| Project passive piezo | No exact part; terminals/polarity TBD | Rated drive, discharge/clamp path, 105 dB conditions and drawing TBD |
| Project 2N2222-family transistor | GPIO6 -> specified 1 kohm -> base; emitter to GND; collector to piezo return is the S logical topology | Actual maker/package/contact numbers TBD |
| onsemi P2N2222AG reference | P2N2222A/D rev. 7, CASE29-11 STYLE17: 1 collector, 2 base, 3 emitter | Not selected; use drawing orientation and exact lead form, not a generic 2N2222 pin rule |
| Project coin motor/driver | Motor positive to rated rail; negative to switched return; flyback cathode to positive, anode to switched return is the logical contract | Motor, transistor, diode package contacts and connector TBD |
| Vybronics VCLP1020B002L reference | A/1 drawing: **red positive, blue negative**, UL3302 AWG32; no numbered connector | Not selected; 2.5-3.5 V operating range, duty/start/stall and final mounting still need application qualification |
| TDK PS1240P02BT research lead | No usable PDF obtained | Pinout, drawing, ratings and selection remain TBD |

Sources: [SRC-22](datasheet-index.md#src-22),
[SRC-27](datasheet-index.md#src-27), [SRC-29](datasheet-index.md#src-29).
An 80 mA starting-current limit under the Vybronics stated test is not a
guaranteed stall/current limit at every permitted supply voltage.

<a id="switches"></a>
### 3.4 Buttons and slide switches

Project buttons and slide-switch contact numbering are **TBD**. A four-leg
tactile switch must not be wired by guessing which legs are internally paired.
The Pod button remains GPIO7-to-ground; Keyfob button is proposed GPIO4 on
C3 or GPIO7 on S3.

The **SHOUHAN MSK12C02 reference**, spec A/0, shows signal contacts 1/2/3 and
shell lands marked 4 in its assembly drawing. Current canonical drawing,
common-contact/orientation truth table and applicability to the project's
unspecified **MSK-12C02** remain TBD; no common pin is guessed here.
Its 50 mA at 12 V DC rating does not qualify direct radio/motor power switching.
The low-current enable-path use remains a proposal
([SRC-28](datasheet-index.md#src-28)).

<a id="unselected-parts"></a>
## 4. Remaining part-level wiring holds

The [component register](component-register.csv) gives each row its
`connector_pinout`, `pinout_reference` and `freeze_blocker`.

- Audio bias, motor series/off-bias, I2C pull-ups and ADC top/bottom/filter
  roles have explicit separate entries, but exact parts, values and physical
  terminal maps remain TBD. Their logical nodes are in [pinout](pinout.md).
- Charge-programming resistors and optional NTC implementations are per-unit
  roles. Values cannot be frozen until exact cells, chargers and temperature
  requirements are reviewed.
- Power-path, protection, regulation, conditioning, decoupling and tether
  networks remain non-orderable circuit groups. Unidentified constituents
  must be expanded after the circuit is defined, not invented now.
- Harnesses and external interfaces need every contact, wire, mate, polarity,
  shield, unused-pin treatment and retention feature recorded before release.
- Mechanical-only parts have no electrical pinout; dimensions, material,
  mounting and EM interactions still require evidence.

Document cross-checks do not substitute for ERC, DRC, continuity/polarity
inspection, safe power tests or delivered-hardware measurements. No such
hardware/design validation has been performed.

## 5. Revision record

| Revision | Date | Change |
| --- | --- | --- |
| 0.2 | 2026-11-11 | Initial manufacturer pinout register; preserved logical proposals, corrected C3 USB pad pair and recorded all unselected-interface holds |
