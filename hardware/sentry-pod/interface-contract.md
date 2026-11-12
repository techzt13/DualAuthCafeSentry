# Sentry Pod — MCU, NFC and IMU interface contract

Revision: 0.4 | Date: 2026-11-12 | Status: DRAFT — low-voltage logic captured; not a wiring or fabrication release

This document is the live interface contract for the first Sentry Pod KiCad schematic. It distinguishes verified module signal names from carrier-side net names and keeps the unfinished battery/power and acoustic circuits isolated.

## 1. Controller and scope

Controller evaluation module: Waveshare classic no-header ESP32-S3-Zero, SKU 25081, ESP32-S3FH4R2. Manufacturer drawing gives an 18.00 x 23.50 mm outline, 2.54 mm contact pitch and 15.24 mm row spacing. The exact received board revision, plated-castellation land dimensions, antenna exclusion boundary and maximum assembled height remain TBD. No carrier footprint is assigned to U1 until those details are reconciled.

The custom carrier PCB is intended to host this Zero, the NFC reader interface, IMU interface, button and future power/actuator circuits. This revision captures the MCU and low-voltage sensor/reset circuit blocks only.

## 2. MCU contact allocation

Contact numbers are Waveshare P15 schematic references, not a generic 0.1-inch connector pin numbering system.

| P15 | Board signal | Carrier net | Use |
|---:|---|---|---|
| 1 | GPIO43 / UART0 TX through 499 ohm board resistor | P_UART_TX | Service only |
| 2 | GPIO44 / UART0 RX | P_UART_RX | Service only |
| 3 | GPIO13 | P_CHARGE_STATUS_N | Conditioned charge status, not wired yet |
| 4 | GPIO12 | P_IMU_INT | IMU interrupt |
| 5 | GPIO11 | P_NFC_RESET_CTL | Active-high reset command into transistor stage |
| 6 | GPIO10 | NC | Selected PN5321 MINI host interface has no IRQ output; poll reader |
| 7 | GPIO9 | P_TETHER_SENSE | Optional protected input, not wired yet |
| 8 | GPIO8 | P_TETHER_DRIVE | Optional protected excitation, not wired yet |
| 9 | GPIO7 | P_BUTTON_N | Recessed button to ground |
| 10 | GPIO6 | P_AUDIO_PWM | Logic control only; acoustic circuit separate |
| 11 | GPIO5 | P_I2C_SCL | Shared I2C |
| 12 | GPIO4 | P_I2C_SDA | Shared I2C |
| 13 | GPIO3 | NC | Strap reserved |
| 14 | GPIO2 | NC | Unassigned |
| 15 | GPIO1 / ADC1_CH0 | P_BAT_ADC | Protected/scaled monitor only; not wired yet |
| 16 | 3V3 LDO output | P_3V3_BOARD_HOLD | Isolated power hold |
| 17 | GND | GND | Ground reference |
| 18 | VBUS / shared USB 5 V | P_5V_BOARD_HOLD | Isolated power hold |

The pin map is based on `docs/verified-pinouts.md#s3-zero` and the Waveshare schematic. USB D-/D+, GPIO21 RGB DIN, BOOT and RESET remain reserved.

## 3. NFC module interface — provisional candidate

Evaluation module: **ELECHOUSE PN5321 MINI, SKU NFC_EX_MINI, hardware V2**, with the 10 x 25 mm ferrite-backed antenna. This is a practical module candidate, not an owner-approved component freeze. The board is reported as 25 x 16.4 x 4.4 mm; the antenna is 10 x 25 x 0.2 mm with a 100 mm lead. The module's exact installed cable/connector geometry and antenna keepout drawing have not been reconciled.

The manufacturer manual signal names for I2C mode are used instead of invented cable contact numbers:

| Module silkscreen / signal name | Carrier function | Schematic treatment |
|---|---|---|
| GND | Ground | GND |
| 5V / 3V3 supply input | Reader supply | P_3V3_PERIPH_HOLD — unsourced hold |
| RST | Active-low PN532 RSTPD_N | P_NFC_RESET_N |
| SCK | SPI-only / unused in I2C | NC |
| MISO | SPI-only / unused in I2C | NC |
| TX / MOSI / SDA | I2C SDA | P_I2C_SDA |
| RX / SS / SCL | I2C SCL | P_I2C_SCL |

The host address is 7-bit **0x24**. The module does **not** expose IRQ on this host interface; P15 contact 6 / GPIO10 is therefore NC and firmware must poll. RSTOUT_N is not a module host connector signal.

**No physical 7-pin cable conductor order is asserted.** The manual names the signals but the current evidence does not provide a fully controlled pin-number-to-wire-colour map for the actual supplied cable. The schematic uses signal names as logical pins only. Before fitting a physical connector, match the actual module silkscreen, connector drawing and cable.

### PN532 reset conditioning circuit

Q1 is a provisional Nexperia MMBT3904 NPN, SOT-23. Datasheet pin map: 1=B, 2=E, 3=C. U1 GPIO11 / P_NFC_RESET_CTL drives Q1 base through R1=10 kΩ. R2=100 kΩ biases base to emitter/GND. Q1 emitter is GND; collector is P_NFC_RESET_N. R3=10 kΩ pulls P_NFC_RESET_N up to P_3V3_PERIPH_HOLD.

This inverts the control: GPIO11 high asserts the active-low module reset. The pull-up rail is deliberately unsourced until the power tree is designed. Do not connect the module or energise this rail yet. Q1 and resistor values are provisional design values, not measured or qualified.

### I2C pull-ups

R4 and R5 are optional 4.7 kΩ pull-ups to P_3V3_PERIPH_HOLD and are marked DNP by default. The current ELECHOUSE manual revision fetched directly describes onboard 3.3 V I2C pull-ups, while an earlier revision/evidence record describes unpopulated pull-up footprints. Treat this as a module revision discrepancy. Do not populate carrier pull-ups until the actual module is inspected and total parallel pull-up resistance is checked.

## 4. IMU module interface — provisional candidate

Evaluation module: **Adafruit MPU-6050 breakout, product 3886**. It is not a generic GY-521 and the project owner's O-04 component decision remains open. The Adafruit product page publishes 26.0 x 17.8 x 4.6 mm; the official open board-source geometry is 25.40 x 17.78 mm. The source board includes four 2.5 mm mounting holes. The stated 4.6 mm height must be checked against the actual fitted header/cable assembly.

The breakout's 1 x 6 header mapping from its published Eagle design is:

| Header pin | Signal | Carrier treatment |
|---:|---|---|
| 1 | VIN | P_3V3_PERIPH_HOLD — unsourced hold |
| 2 | 3Vo | Regulator output; NC |
| 3 | GND | GND |
| 4 | SCL | P_I2C_SCL |
| 5 | SDA | P_I2C_SDA |
| 6 | INT | P_IMU_INT |

The board also has STEMMA QT connectors; their standard signal order is GND, VIN, SDA, SCL. The six-pad header is the intended schematic interface in this draft. Use VIN as the supply input and never feed the 3Vo output. The breakout contains 3.3 V regulation/level shifting and I2C pull-ups. Its AD0 default pull-down is 10 kΩ, giving address 0x68; its solder jumper can select 0x69. INT polarity/drive must be configured deliberately in firmware. Do not add another pair of I2C pull-ups until the complete bus is assessed.

No physical mating connector is fitted to the carrier PCB in this revision. The exact header orientation and assembly choice remain open.

## 5. User and remaining logic interfaces

- SW1: logical active-low button between P_BUTTON_N and GND. Exact tactile switch, resistor/pull-up choice, travel and footprint are not frozen. The first schematic relies on a firmware/input pull-up proposal; hardware bias must be added if reset/unpowered behavior or the selected GPIO requires it.
- P_TETHER_DRIVE / P_TETHER_SENSE: remain logical labels only. An exposed tether must not connect directly to an unprotected GPIO; current limit, ESD, reverse connection and fault-state circuit are not yet designed.
- P_AUDIO_PWM: logic command only. It does not connect directly to a piezo. Driver and transducer remain a separate isolated design block.
- P_BAT_ADC: protected/scaled/filtered battery monitor only; no raw cell connection.
- P_CHARGE_STATUS_N: conditioned logic input only; no 5 V charger status connection.

## 6. Power holds

`P_3V3_BOARD_HOLD` is the Zero's onboard LDO output. `P_5V_BOARD_HOLD` is the Zero's shared USB VBUS / external 5 V pad. Neither is a free input. The peripheral rail `P_3V3_PERIPH_HOLD` is an intentionally unsourced placeholder. The future BQ25185-at-4.1-V direction remains evaluation-only. No battery, charger, regulator, load-sharing or USB isolation circuit is approved or wired here.

## 7. Current KiCad files and status

- `sentry-pod.kicad_sch`: editable MCU, NFC, IMU, button, PN532 reset conditioner and optional DNP I2C pull-up schematic blocks.
- `sentry-pod.kicad_sym`: project symbol library.
- `sym-lib-table`: project-local symbol library registration.

This is a logical schematic draft. The reset conditioner is now electrically wired at the schematic level; the external modules remain provisional and have no released physical connector order, U1 has no carrier footprint, and there is no placement/routing or power circuit. Structural S-expression checks must be rerun after this revision. KiCad/Eeschema is not installed in the execution environment, so no native KiCad parse, ERC or DRC has been run. No board-level wiring, power-up, fabrication or physical fit is validated.

## 8. Evidence and revision history

Evidence:
- Waveshare ESP32-S3-Zero official wiki and 2D drawing: `docs/datasheet-index.md#src-02`, `#src-03`.
- ELECHOUSE PN5321 MINI manual and revision discrepancy: `docs/datasheet-index.md#src-43`, `#src-56`.
- Adafruit product 3886 and official Eagle board files: `docs/datasheet-index.md#src-54`.
- Nexperia MMBT3904 datasheet: `docs/datasheet-index.md#src-55`.
- Existing verified contact/IC maps: `docs/verified-pinouts.md`.

| Revision | Date | Change |
|---|---|---|
| 0.1 | 2026-11-12 | Logical Pod MCU and sensor interface contract. |
| 0.2 | 2026-11-12 | Records the captured schematic, PN5321 MINI host signal names/no-IRQ polling behavior, NPN reset inversion, Adafruit 3886 header mapping, pull-up and power holds. |
| 0.3 | 2026-11-12 | Added the actual R1/R2/R3/Q1 reset-stage wires and reset-net labels to the native KiCad schematic; physical module and power holds remain. |


Revision 0.4 implementation note (2026-11-12): the native schematic now wires the optional R4/R5 pull-up positions to the intended SDA/SCL nets and the held 3.3 V peripheral rail. They remain DNP by default. The Pod reset conditioning network is also fully wired in the schematic. These repairs close missing logical wires only; no power source, module footprint, PCB net routing or ERC/DRC result is implied.
