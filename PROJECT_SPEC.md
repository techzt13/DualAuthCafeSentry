# PROJECT SPECIFICATION: Dual-Auth Cafe Sentry
**Target Event:** Hack Club Fallen 2026 Hardware Hackathon (Showcase: Maker Faire Shenzhen)
**Category:** Consumer Security Hardware / Embedded Systems (Phone-Free Anti-Theft Device)

---

## 1. Executive Summary
The **Dual-Auth Cafe Sentry** is a keychain-sized, standalone anti-theft security pod designed to actively deter snatch-and-run theft of backpacks, laptops, and personal gear in public spaces (cafes, libraries, classrooms, gyms). Unlike passive recovery trackers (such as Apple AirTag) that require a smartphone and only locate items *after* they are stolen, the Cafe Sentry provides **instant, active deterrence** without needing a phone.

It combines two independent authentication methods:
1. **Hands-Free ESP-NOW Proximity Keyfob:** Automatically arms when the user walks >4 meters away and disarms upon return, providing silent haptic feedback on the keyfob.
2. **Instant 13.56 MHz NFC Card Tap:** Allows manual force-locking and unlocking using any enrolled card (student ID, transit card, or NFC tag) stored in non-volatile flash memory.

---

## 2. System Architecture & Functionalities

### A. Authentication & State Machine
- **State 0: DISARMED (Green LED):** Motion monitoring paused. Pod listens for NFC tap or Keyfob distance threshold.
- **State 1: AUTO-ARMED via Keyfob (Pulsing Red LED):** Triggered when ESP-NOW RSSI drops below the ~4-meter threshold for 3 consecutive seconds. Sends an acknowledgment packet to vibrate the Pocket Keyfob twice. Automatically disarms when the Keyfob returns within range.
- **State 2: FORCE-LOCKED via NFC (Solid Crimson LED):** Triggered by tapping an authorized 13.56 MHz card while disarmed. Overrides proximity auto-unlock (so gear stays locked even while the user sits nearby) until the same or another enrolled card is tapped again.
- **State 3: WARNING CHIRP (Flashing Amber LED):** Triggered by minor initial movement. Emits a brief two-tone sonar chirp for 1.5 seconds to warn accidental passersby without causing a false alarm.
- **State 4: FULL LOCKDOWN SIREN (High-Intensity Red/White Strobe):** Triggered if movement/tilt persists past Stage 3, or immediately if the USB-C continuity loop is unplugged/cut. Blasts a 105dB dual-frequency piezo siren (sweeping 2.8 kHz – 4.2 kHz) and sends an instant alert packet to vibrate the Pocket Keyfob continuously.
- **Failsafe Disarm:** A recessed physical tactile button accepts a custom 4-beat rhythm code (e.g., short-short-long-short) to disarm the pod if both the Keyfob and NFC card are lost.

### B. NFC Subsystem Experience (Key Highlight)
- **Multi-Credential Enrollment:** Holding the side button for 3 seconds enters "Learn Mode" (breathing violet LED). Tapping any 13.56 MHz card reads its 4-byte or 7-byte UID and saves up to 5 cards permanently to NVS flash memory (`Preferences` / `NVS`).
- **Factory Reset:** Holding the side button for 10 seconds clears all stored UIDs.
- **Power-Saving Duty Cycle:** Polls the PN532 for 40ms every 250ms (4 Hz) to keep response instantaneous while cutting average NFC current draw by >80%.
- **Signature Audio Choreography:** Uses a passive piezo transducer driven by hardware PWM to play distinct harmonic chimes for Arming (`C6 -> G6`), Disarming (`G6 -> E6 -> C6`), Enrollment (`C6 -> E6 -> G6 -> C7`), and Unauthorized Card Tap (`180 Hz` muted double-thud).

### C. Smart False-Alarm Rejection (Sensor Fusion)
- Uses **MPU-6050** quaternion/tilt-angle calculation rather than raw accelerometer spikes alone.
- Ignores brief ambient table vibrations (e.g., someone setting down a cup).
- Triggers only if the pod tilts **>12 degrees** from its armed resting orientation OR sustains continuous movement for **>400ms**.

### D. Physical USB-C "Tripwire" Continuity Loop
- A short braided steel-core USB-C tether cable loops from an output GPIO pin on the pod, through a laptop lock slot or bag handle, and back into a continuity-sense input pin (`INPUT_PULLDOWN`).
- Unplugging or severing the loop while armed immediately triggers **State 4 (Full Lockdown Siren)** bypassing the warning chirp.

---

## 3. Hardware Bill of Materials (BOM)

### Unit 1: Sentry Pod (Attached to Bag/Laptop)
- **MCU:** ESP32-S3-Zero (native USB-C, ESP-NOW radio, onboard WS2812B RGB LED)
- **IMU:** GY-521 (MPU-6050) 6-Axis Accelerometer & Gyroscope (I2C)
- **NFC Reader:** PN532 NFC Module (configured in I2C mode: `SEL0=1, SEL1=0`)
- **Audio:** Passive Piezo Buzzer / Transducer (85dB–105dB) driven by an NPN transistor (2N2222) + 1kΩ base resistor for maximum volume
- **Failsafe Input:** 1x Mini Tactile Push Button
- **Power:** 3.7V 200mAh–250mAh LiPo Battery (502030 size) + USB-C LiPo Charger Module (MCP73831 or TP4056) + Mini Slide Power Switch (MSK-12C02)

### Unit 2: Pocket Keyfob (Carried by User)
- **MCU:** ESP32-C3-Zero or ESP32-S3-Zero (running light-sleep beacon loop)
- **Haptics:** 1x Miniature Coin Vibration Motor (3V, driven via transistor/diode)
- **Input:** 1x Mini Tactile Button (manual remote mute / panic trigger)
- **Power:** 3.7V 150mAh–200mAh LiPo Battery + USB-C Charger Module + Mini Slide Switch

---

## 4. Pinout & Wiring Map (Sentry Pod)
- **Shared I2C Bus (MPU-6050 & PN532):**
  - `GPIO 4` -> `SDA` (both sensors)
  - `GPIO 5` -> `SCL` (both sensors)
  - `3.3V` -> `VCC` | `GND` -> `GND`
- **Piezo Siren (PWM via 2N2222 Transistor):**
  - `GPIO 6` -> 1kΩ Resistor -> Transistor Base (Collector to Buzzer `-`, Emitter to `GND`, Buzzer `+` to `VBUS/Battery+`)
- **Failsafe Rhythm Button:**
  - `GPIO 7` -> Button Pin 1 (`INPUT_PULLUP`) | Button Pin 2 -> `GND`
- **USB-C Tripwire Loop (Optional):**
  - `GPIO 8` (`OUTPUT HIGH`) -> Tether Loop -> `GPIO 9` (`INPUT_PULLDOWN`)

---

## 5. Industrial Design & Enclosure Specs
- **Target Dimensions:** ~45mm × 30mm × 16mm (Sentry Pod); ~35mm × 25mm × 12mm (Keyfob).
- **Aesthetic:** Two-tone industrial finish—matte dark charcoal or frosted translucent resin body (to diffuse internal RGB status lighting) paired with a flat top lid featuring an engraved NFC tap zone.
- **Mechanical Constraints:**
  - Keep top lid wall thickness **≤1.5mm** directly over the PN532 antenna coil.
  - Keep LiPo battery and piezo buzzer **≥10mm away** from the PN532 coil to prevent magnetic/RF detuning.
  - Include an acoustic sound vent directly over the piezo buzzer and a reinforced top loop for a carabiner clip.


---

## 6. Hackathon build implementation amendment (2026-11-12)

The required project deliverables include editable PCB designs and editable
CAD designs, not merely a component research report or breadboard concept.
The project must progress to a manufacturable prototype package for both the
Sentry Pod and Pocket Keyfob.

- Required electronics deliverables: native KiCad schematic and PCB projects,
  verified connector/pin assignments, BOM, Gerbers, drill files, and fabrication
  notes for each custom board.
- Required mechanical deliverables: native parametric FreeCAD enclosure and
  assembly models for both units, dimensioned drawings, and STEP/STL exports.
- Required integration deliverables: PCB/enclosure fit checks, mounting,
  battery and connector access, NFC antenna keepout, piezo acoustic opening,
  motor mounting, cable routing and assembly instructions.
- Existing dimensions are starting constraints, not a reason to stop CAD.
  The Sentry Pod length direction is at least approximately 55 mm; 30 mm width
  and 16 mm height remain provisional. The Keyfob 35 x 25 x 12 mm target is
  also provisional and may be adjusted to achieve a buildable assembly.
- Unknown component details must be labelled and managed as provisional
  design inputs. They should not prevent independent work on board outlines,
  mechanical envelopes, interface placement and parametric enclosure structure.
- Manufacturer correspondence is not a prerequisite to begin schematic,
  PCB or CAD design. Use published documentation and engineering judgement;
  record assumptions and validate the resulting design before fabrication.

This amendment establishes the hackathon implementation scope. It does not
claim that any current candidate circuit is safe, tested, frozen or ready to
manufacture, and it does not authorise automatic purchasing.
