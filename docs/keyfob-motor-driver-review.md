# Keyfob motor-driver review

Date: 2026-11-13  
Status: **provisional schematic block; not an approved power design**

## Circuit implemented

The Keyfob schematic uses a low-side N-channel MOSFET to switch the brushed vibration motor. The ESP32-C3-Zero GPIO3 signal drives the MOSFET gate through R1. R2 pulls the gate to source so the motor remains off while the controller is resetting, booting or unpowered.

| Ref | Draft value / part | Function |
|---|---|---|
| U1 | Waveshare ESP32-C3-Zero, SKU 25452 | Controller interface; GPIO3 drives motor control |
| Q1 | Infineon IRLML6344TRPBF, SOT-23 | Low-side N-MOSFET; pin 1 G, pin 2 S, pin 3 D |
| R1 | 100 Ω, 0603 | Gate series resistor |
| R2 | 100 kΩ, 0603 | Gate-to-source default-OFF pull-down |
| J1 | Two solder-wire pads | 308-100 motor leads; pin 1 red positive, pin 2 blue negative |
| D1 | Nexperia PMEG2010AEB,115, SOD-523 | Flyback diode; pin 1 cathode to motor rail, pin 2 anode to switched node |
| C1 | 100 nF, 0603 | Local high-frequency bypass placeholder |
| C2 | 10 µF, 0805 | Local reservoir placeholder |
| SW1 | Two-pin momentary switch | GPIO4 active-low user button |

## Motor operating envelope

The Precision Microdrives 308-100 official data sheet lists:
- Rated operating voltage: 3 V.
- Maximum operating voltage: 3.6 V.
- Maximum rated current: 94 mA.
- Maximum start current: 124 mA.
- Body: 8.0 mm diameter by 3.4 mm length.
- Typical winding inductance: 59.54 mH and typical terminal resistance: 316 Ω.

Source: [Precision Microdrives 308-100 data sheet](https://precisionmicrodrives.com/cdn/catalog_product/445ff874-bf32-474d-9e41-d7606db3b147/308-100-datasheet.pdf).

The motor is a candidate, not a frozen selection. Continuous-alert duty, vibration in the actual enclosure, start under battery sag and long-term life are not established by the reviewed data.

## MOSFET screen

Infineon's official IRLML6344 data sheet gives a 30 V drain-source rating and maximum on-resistance of 37 mΩ at VGS = 2.5 V. The ESP32 GPIO high level is expected to exceed 2.5 V when correctly powered, but actual GPIO high voltage and board sequencing must be checked.

A first-order conduction estimate at 124 mA is:

P = I²R = (0.124 A)² × 0.037 Ω ≈ 0.00057 W

This excludes switching loss, gate-charge loss, parasitics, transient stress and layout effects. It is not a thermal qualification.

Source: [Infineon IRLML6344 data sheet](https://www.infineon.com/assets/row/public/documents/24/49/infineon-irlml6344-datasheet-en.pdf).

## Flyback upgrade

The earlier 1N4148W candidate has a 150 mA maximum average rectified current rating. That is close to the motor's 124 mA maximum start current and leaves limited design margin for repetitive PWM recirculation and thermal/layout variation.

The draft now uses Nexperia PMEG2010AEB,115:
- 20 V reverse voltage.
- 1 A forward-current rating under the data-sheet thermal conditions.
- SOD-523 package.
- Pin 1 cathode; pin 2 anode.

Wire it directly across the motor: cathode to the positive motor rail, anode to the MOSFET drain / motor-negative node. The diode must be physically close to the motor connector and switching loop. Its reverse leakage at the maximum motor rail and junction temperature still needs checking.

Source: [Nexperia PMEG2010AEB data sheet](https://assets.nexperia.com/documents/data-sheet/PMEG2010AEB.pdf).

## Open engineering checks

1. Confirm the exact 308-100 motor candidate and wire polarity against the received motor.
2. Confirm K_3V3_MOTOR_HOLD can supply 124 mA startup pulses without collapsing the MCU rail.
3. Select the actual battery, protection and regulated rail; do not connect the motor to raw battery or USB VBUS by assumption.
4. Verify motor PWM frequency and duty. Test startup at minimum battery voltage and under simultaneous radio activity.
5. Confirm diode thermal behaviour and motor recirculation waveform with an oscilloscope.
6. Confirm C1/C2 voltage rating and effective capacitance after DC-bias derating.
7. Check MOSFET gate voltage during reset, brownout and unpowered MCU states.
8. Complete the Keyfob module land pattern, board net assignments, antenna keepout, routing and enclosure fit.
9. Run KiCad ERC/DRC and a physical prototype test.

No battery, charger or power source is connected to this block. No hardware validation is claimed.
