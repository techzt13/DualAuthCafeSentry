# Pocket Keyfob — MCU and actuator interface contract

Revision: 0.1 | Date: 2026-11-12 | Status: DRAFT — logical interfaces only; not a wiring release

This document defines the Keyfob controller and low-voltage signal contract using the verified Waveshare board contact maps. It keeps the C3-Zero as the current evaluation option, with the S3-Zero as a documented alternative. The owner has not frozen the MCU choice. No physical module connector footprint, battery circuit or motor driver is released by this document.

## 1. Controller options

### Preferred evaluation path: Waveshare ESP32-C3-Zero

- SKU 25452, ESP32-C3FH4, no-header board, schematic filename V2.
- The V2 schematic maps contact 15 to GPIO18 / USB D- and contact 16 to GPIO19 / USB D+.
- Exact received board revision, contact geometry and assembled envelope remain TBD.

### Alternative: Waveshare ESP32-S3-Zero

- Classic no-header SKU 25081, ESP32-S3FH4R2 version.
- Use the S3 Keyfob allocation in `docs/verified-pinouts.md` and `docs/pinout.md`.
- Select exactly one controller on the final carrier. Do not create a dual-footprint assumption without a real mechanical/electrical reason.

## 2. C3-Zero logical interface allocation

The contact numbers below are V2 board-symbol contact numbers. They are not a physical connector footprint numbering convention.

| C3 contact | Verified board signal | Carrier net | Proposed use | State |
|---:|---|---|---|---|
| 1 | 5 V / native USB VBUS | K_5V_BOARD | Board input shared with USB VBUS | HOLD |
| 2 | GND | K_GND | Local ground | Verified contact |
| 3 | VCC3.3 / onboard LDO output | K_3V3_BOARD | Regulator output | HOLD |
| 4 | GPIO0 / ADC1_CH0 | K_BAT_ADC | Protected/scaled battery monitor only | Proposed |
| 5 | GPIO1 | K_CHARGE_STATUS_N | Conditioned charge-active status | Proposed |
| 6 | GPIO2 | — | Reserved strap | No connect |
| 7 | GPIO3 | K_MOTOR_PWM | Motor-driver control | Proposed |
| 8 | GPIO4 | K_BUTTON_N | User button to ground | Proposed |
| 9 | GPIO5 | — | Unassigned | No connect |
| 10 | GPIO6 | — | Unassigned | No connect |
| 11 | GPIO7 | — | Unassigned | No connect |
| 12 | GPIO8 | — | Reserved strap | No connect |
| 13 | GPIO9 | — | BOOT/strap | Reserved |
| 14 | GPIO10 | — | Onboard RGB DIN | Reserved |
| 15 | GPIO18 / USB D- | — | Native USB | Reserved |
| 16 | GPIO19 / USB D+ | — | Native USB | Reserved |
| 17 | GPIO20 / UART0 RX | K_UART_RX | Service/debug | Reserved |
| 18 | GPIO21 / UART0 TX | K_UART_TX | Service/debug | Reserved |

GPIO4-7 share external pad-JTAG functions; this allocation assumes native USB debugging rather than simultaneous pad-JTAG use. Do not repurpose strap or native USB contacts for application I/O.

## 3. C3-Zero alternative interface allocation

If the S3-Zero is chosen instead, use:
- GPIO1 / P15-15: protected/scaled battery ADC.
- GPIO13 / P15-3: conditioned charge status.
- GPIO6 / P15-10: motor-driver control.
- GPIO7 / P15-9: active-low button.
- GPIO21: onboard RGB DIN, reserved.
- GPIO19/20: native USB D-/D+, reserved.
- GPIO43/44: service UART, reserved.

The S3 contact table and restrictions are in `docs/verified-pinouts.md`, section 1.1.

## 4. Logical signal contracts

### 4.1 Motor control

- Net: `K_MOTOR_PWM`; C3 GPIO3 or S3 GPIO6.
- MCU pin drives only a logic-level transistor/driver input, never the motor directly.
- Provide a hardware-defined OFF state during reset, boot, brownout and MCU unpowered conditions.
- Motor supply must be derived from a reviewed power rail and must not be assumed to equal either raw cell voltage or USB VBUS.
- The motor needs a correctly rated low-side switch or dedicated driver, local decoupling and a flyback path appropriate to the selected motor technology.
- The current 308-100 motor candidate is not a frozen selection; operating voltage, startup/stall current, continuous-duty limits and mounting remain to be verified from the exact datasheet.
- PWM frequency, duty policy, maximum continuous vibration time and thermal behavior remain TBD.

### 4.2 User button

- Net: `K_BUTTON_N`; C3 GPIO4 or S3 GPIO7.
- Active-low input, switch to local ground.
- Pull-up voltage must match the selected MCU I/O domain.
- Debounce, wake-from-sleep behavior, gesture timings and reset behavior remain firmware/system decisions; do not add a strap conflict.

### 4.3 Battery and charge status

- `K_BAT_ADC`: protected/scaled/filtered cell monitor only. Never connect the raw cell directly to the ADC.
- `K_CHARGE_STATUS_N`: conditioned status input only. Do not connect an unknown 5 V STAT output directly.
- Divider impedance, ADC attenuation, filter, protection, status polarity and charger output type remain TBD until the final power circuit is selected.

## 5. Power interface holds

The C3-Zero 3V3 pin is the onboard regulator output. Its 5V pin is on the same net as native USB VBUS. Neither pin is approved as a direct single-cell input.

- `K_3V3_BOARD`: HOLD pending regulator reverse-current and sequencing analysis.
- `K_5V_BOARD`: HOLD pending a complete power-source and USB backfeed solution.
- No LiPo charger or cell protector is present on the Zero board.
- No battery-to-board wiring is released.
- The exact Keyfob pack, charger, charge current and power-path architecture remain unresolved.

## 6. Physical and PCB holds

No connector footprint is released in this revision. Confirm the exact Waveshare board drawing, contact geometry, assembly height and physical orientation before designing the carrier footprint. Confirm the motor can's dimensions, lead exit, adhesive area and vibration coupling before placing it in the enclosure. Battery connector and USB-C charge receptacle remain TBD.

## 7. Evidence

- `docs/verified-pinouts.md`, sections 1.2 and 1.3.
- `docs/pinout.md`, section 2.
- `docs/power-architecture.md`, sections 2 and 4.
- `docs/g1-owner-decisions.md`, O-06 and O-12 to O-14.
- `docs/g1-component-shortlist.md`, Keyfob MCU and motor candidate entries.

This is a design translation of existing evidence, not a new manufacturer verification. No ERC/DRC, electrical simulation, battery test, motor test or physical fit test has been performed.

## Revision history

| Revision | Date | Change |
|---|---|---|
| 0.1 | 2026-11-12 | First Keyfob MCU and actuator logical interface contract. |
