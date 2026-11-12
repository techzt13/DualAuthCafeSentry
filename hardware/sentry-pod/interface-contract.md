# Sentry Pod — MCU and low-voltage interface contract

Revision: 0.1 | Date: 2026-11-12 | Status: DRAFT — logical interfaces only; not a wiring release

This document turns the manufacturer-verified Waveshare ESP32-S3-Zero contact map and the project's logical pin allocation into an explicit carrier-board interface contract. It is the first electrical-design block for the Pod. It deliberately does not assign an unverified physical connector footprint or pretend that the PN532/IMU module headers have been identified.

## 1. Controller identity and scope

Controller candidate: Waveshare classic no-header ESP32-S3-Zero, SKU 25081, ESP32-S3FH4R2 version. The exact received PCB revision and complete assembled envelope remain TBD. The carrier is a custom PCB; the Zero remains a plug-in module candidate until its physical contact geometry, soldering method and keepout are reconciled against the actual board drawing.

This block covers:
- MCU module contact allocation.
- Shared 3.3 V logic-domain I2C bus contract.
- PN532 host signals and reset/IRQ conditioning boundary.
- MPU-6050 host signals.
- User button, tether, audio-control and battery-monitor logic signals.
- Service/debug and reserved contacts.

It does not yet implement the battery/charger/power path, the PN532 or IMU module connector pin order, the audio power stage, or any cell connection.

## 2. Verified S3-Zero contacts used by the Pod

The numbers below are the Waveshare P15 schematic contact numbers, not a generic 0.1-inch header numbering convention. They must not be transferred directly to a footprint until the bottom-view drawing and actual received module are checked.

| P15 contact | Verified board signal | Carrier net | Proposed use | State |
|---:|---|---|---|---|
| 1 | GPIO43 / UART0 TX through board R6 499 ohm | P_UART_TX | Service/debug only | Reserved |
| 2 | GPIO44 / UART0 RX | P_UART_RX | Service/debug only | Reserved |
| 3 | GPIO13 | P_CHARGE_STATUS_N | Conditioned charger status | Proposed |
| 4 | GPIO12 | P_IMU_INT | IMU interrupt | Proposed |
| 5 | GPIO11 | P_NFC_RESET_N | Conditioned PN532 reset input | Proposed |
| 6 | GPIO10 | P_NFC_IRQ_N | PN532 IRQ input, if exposed | Proposed |
| 7 | GPIO9 | P_TETHER_SENSE | Optional protected tether sense | Spec allocation |
| 8 | GPIO8 | P_TETHER_DRIVE | Optional protected tether drive | Spec allocation |
| 9 | GPIO7 | P_BUTTON_N | Multifunction button to ground | Spec allocation |
| 10 | GPIO6 | P_AUDIO_PWM | Audio-driver logic input via 1 kohm series/base path | Spec allocation |
| 11 | GPIO5 | P_I2C_SCL | Shared I2C clock | Spec allocation |
| 12 | GPIO4 | P_I2C_SDA | Shared I2C data | Spec allocation |
| 13 | GPIO3 | — | Reserved strap | No connect |
| 14 | GPIO2 | — | Unassigned | No connect |
| 15 | GPIO1 / ADC1_CH0 | P_BAT_ADC | Protected/scaled battery monitor only | Proposed |
| 16 | 3V3 / onboard LDO output | P_3V3_BOARD | Board power interface | HOLD |
| 17 | GND | P_GND | Local ground | Verified contact |
| 18 | VBUS / external 5 V pad | P_5V_BOARD | Shared native-USB input net | HOLD |

Additional underside pads are not used in this first carrier contract. GPIO0, GPIO3, GPIO45 and GPIO46 are strap-related and are not reassigned. Native USB D-/D+ and RGB DIN remain reserved to the onboard interface.

## 3. Logical signal contracts

### 3.1 I2C bus

- Net names: `P_I2C_SDA`, `P_I2C_SCL`.
- MCU allocation: GPIO4 SDA, GPIO5 SCL.
- Intended devices: PN532 host interface at 7-bit address 0x24 and MPU-6050 at 0x68 (if AD0 is verified low).
- Pull-ups: one shared pair only after the actual module pull-ups and logic voltage are audited. Do not blindly fit carrier pull-ups in parallel with module pull-ups.
- Pull-up rail: 3.3 V only if both module interfaces are proven 3.3 V compatible.
- Bus frequency, rise-time, cable/trace capacitance and clock-stretching behavior remain TBD.
- Add footprints for optional DNP pull-ups only after the module-level audit; do not populate by assumption.

### 3.2 PN532 signals

- `P_NFC_IRQ_N`: GPIO10 input, active-low readiness per the logical interface plan; connect only if the selected module exposes IRQ and its output level is compatible.
- `P_NFC_RESET_N`: GPIO11 control through a voltage-safe, power-sequenced conditioning stage. Do not connect directly until the selected module's reset pin and unpowered behavior are known.
- I2C SCL/SDA share the bus above.
- The selected PN5321 MINI module's actual header pin order, supply input, level shifters, pull-ups and IRQ/reset availability remain TBD. The carrier must use a clearly keyed module connector only after the module drawing/schematic is available.

### 3.3 IMU signals

- I2C SCL/SDA share the bus.
- `P_IMU_INT`: GPIO12 input. Initial firmware proposal is active-high data-ready; electrical polarity, output type and module pull-ups must be checked against the actual board.
- MPU-6050 AD0 is intended low for address 0x68 only if the selected module exposes and implements it accordingly.
- The GY-521 label is not a manufacturer identity. No connector order or footprint is assigned.

### 3.4 User and actuator control signals

- `P_BUTTON_N`: GPIO7 input, active low, external switch to local ground. Pull-up and debounce values remain to be designed.
- `P_TETHER_DRIVE`: GPIO8 optional continuity excitation through current limiting and protection. Never drive an exposed tether directly from an unprotected GPIO.
- `P_TETHER_SENSE`: GPIO9 input with defined external bias, filtering and ESD strategy. Exact tether connector and circuit remain TBD.
- `P_AUDIO_PWM`: GPIO6 logic control only. It is not a piezo output and must not connect directly to the piezo. The boosted driver remains an isolated provisional block.
- `P_BAT_ADC`: GPIO1 ADC input from a protected, scaled and filtered monitor network only. Never connect a raw LiPo terminal directly to this pin.
- `P_CHARGE_STATUS_N`: GPIO13 receives a conditioned logic signal only. Do not connect a 5 V charger status pin directly.

## 4. Power interface holds

The controller module's 3V3 pin is the onboard regulator output; the 5V/VBUS pin is shared with native USB VBUS. Neither is a freely interchangeable supply input.

- `P_3V3_BOARD`: HOLD. Do not externally drive until regulator reverse-current, sequencing and USB coexistence are resolved.
- `P_5V_BOARD`: HOLD. Do not connect a single-cell battery directly. Any external source must account for the native USB receptacle being on the same net.
- The BQ25185 4.1 V charger direction is evaluation-only. The charger, battery, SYS path, ideal-diode stage and Zero interface are not yet a released circuit.
- All module supply pins and I/O pull-ups remain disconnected from the final schematic until the chosen module's actual power and logic-level implementation is verified.

## 5. Physical connector and footprint holds

No physical connector footprint is released in this revision:
- The S3-Zero is a no-header board. Contact pitch, pad geometry, board-edge relationship, soldering strategy and keepouts must be taken from the exact Waveshare drawing and checked against a received board.
- PN5321 MINI module header pin order and antenna connector are not established by the current verified pinout record.
- IMU module header order, pitch and mounting pattern are not established.
- Tether, battery, charge USB-C and actuator connectors are not yet assigned exact manufacturer part numbers and footprints.

Do not route or order a PCB from this logical contract alone.

## 6. Immediate schematic implementation plan

1. Place the S3-Zero as an explicitly named module interface block, with the 18 P15 contacts and the verified signal labels above. Keep its physical footprint unset until pad geometry is reconciled.
2. Add logical connector blocks for PN532, IMU, button, tether, audio-control, battery monitor and charge-status interfaces. Unknown connector pin numbers must be marked TBD rather than fabricated.
3. Add the shared I2C bus labels and document the 0x24 / 0x68 address plan.
4. Add visible power-interface HOLD notes on 3V3 and 5V/VBUS.
5. Add ERC-exempt no-connects only where the board contact is deliberately reserved; do not blanket-mark unresolved pins as no-connect.
6. Continue with the Keyfob interface contract and provisional motor-driver topology.
7. Only after exact physical module/contact drawings are mapped should the carrier footprints and PCB placement be created.

## 7. Evidence

Primary project records:
- `docs/verified-pinouts.md`, sections 1.1, 1.3, 1.4, 2.1 and 2.2.
- `docs/pinout.md`, section 1.
- `docs/power-architecture.md`, sections 2 and 4.
- `docs/g1-owner-decisions.md`, O-02 and O-03/O-05.

The interface mapping is a design translation of those records, not a new manufacturer verification. No ERC, DRC, power test, module fit or physical wiring check has been performed.

## Revision history

| Revision | Date | Change |
|---|---|---|
| 0.1 | 2026-11-12 | First Pod MCU and low-voltage logical interface contract, based on existing verified pinout records. |
