# Dual-Auth Cafe Sentry - Pinout and Connection Schedule

Revision: 0.1 | Date: 2026-11-11 | Status: logical interface allocation, not wiring release

Read with [architecture and evidence labels](architecture.md) and
[power architecture](power-architecture.md). **S** preserves the specification;
**V** is documented hardware; **P** is proposed; **TBD** blocks final wiring.

All GPIO numbers are Espressif GPIO numbers, not physical header positions.
The Waveshare schematic pad references below are document-local references,
not a fabricated connector footprint. Confirm orientation against the actual
received board. Unselected module/connector contact numbers remain TBD.

## 1. Sentry Pod GPIO allocation

Basis: Waveshare S3 schematic [SRC-02](architecture.md#src-02) and Espressif
[SRC-07](architecture.md#src-07). The six specified GPIO4-9 functions are retained.

| GPIO | S3 schematic pad | Net / function | Direction and normal behavior | Status / startup constraint |
| --- | --- | --- | --- | --- |
| 1 | P15-15 | `P_BAT_ADC` | ADC1_CH0 from protected-pack divider/filter | P; never raw battery on ADC; divider and attenuation TBD |
| 4 | P15-12 | `P_I2C_SDA` | Bidirectional open-drain; PN532 SDA and MPU SDA | S; pull-ups only to validated 3.3 V interface |
| 5 | P15-11 | `P_I2C_SCL` | I2C clock, open-drain; PN532 SCL and MPU SCL | S; support clock stretching and bounded timeouts |
| 6 | P15-10 | `P_AUDIO_PWM` | PWM to 1 kohm base resistor, then proposed NPN base | S allocation; external off bias required; complete driver TBD |
| 7 | P15-9 | `P_BUTTON_N` | Input with pull-up; switch closes to ground | S; active low; debounce and gesture policy TBD |
| 8 | P15-8 | `P_TETHER_DRIVE` | Static high when continuity monitoring enabled, through protection | S, optional; safe/current-limited during boot and short circuits |
| 9 | P15-7 | `P_TETHER_SENSE` | Input with pull-down; high = closed logical loop | S, optional; external bias/filter/protection TBD |
| 10 | P15-6 | `P_NFC_IRQ_N` | Input from PN532 P70_IRQ, active-low readiness | P; route if exposed and level-compatible; no assumed pull-up value |
| 11 | P15-5 | `P_NFC_RESET_N` | Conditioned control of PN532 RSTPD_N | P; reset input, not RSTOUT_N; no injection into an unpowered module |
| 12 | P15-4 | `P_IMU_INT` | Input from MPU-6050 INT | P; configure active-high data-ready initially; output mode/pulls verified with module |
| 13 | P15-3 | `P_CHARGE_STATUS_N` | Conditioned 3.3 V charge-active input | P; not direct connection to a 5 V charger STAT pin |
| 21 | Onboard U1 DIN | RGB data | Board-installed status LED | V; reserved; supply/logic discrepancy in D-16 |
| 19 / 20 | Native USB path | USB D- / D+ | Native programming/debug USB | V; reserved; not available for tether |
| 0 | Onboard BOOT K2 | Boot strap | Onboard pull-up/button | V; reserve, do not use as the failsafe button |
| 43 / 44 | P15-1 / P15-2 | UART0 TX / RX | Service/debug only; TX path includes board resistor | V; no application peripheral assigned |

Unused application allocations:

- GPIO2 is spare; GPIO3 and GPIO45 are reserved strapping pins, not general
  spare outputs. GPIO46 is also a silicon strap and is not a usable exposed
  application connection on the reviewed board.
- Additional bottom-pad signals GPIO14-18 and GPIO38-42 are unassigned;
  leave externally unconnected unless a later approved allocation requires them.
- GPIO26-37 are internal/memory-related or unexposed; do not assign them.
  GPIO47/48 are not available as board application pads in the reviewed
  schematic. Do not infer availability from a different ESP32-S3 module.
- Leave unused external pads NC and give unused inputs an appropriate firmware
  state only after checking straps and board connections. Do not add blanket
  pull resistors to every unallocated chip pin.
- RESET/CHIP_PU and BOOT remain service-accessible without sharing alarm controls.

## 2. Pocket Keyfob GPIO allocation

All external allocations here are **P**; the specification does not provide
a Keyfob pin map. Select exactly one board option under
[D-02](design-decisions.md#d-02).

### 2.1 C3-Zero evaluation option

Basis: [SRC-05](architecture.md#src-05), [SRC-08](architecture.md#src-08).
Pad numbers refer to the V2 schematic board symbol.

| GPIO | Schematic pad | Net / function | Connection and safe state |
| --- | --- | --- | --- |
| 0 | 4 | `K_BAT_ADC` | ADC1_CH0 from protected-pack divider/filter; no raw cell connection |
| 1 | 5 | `K_CHARGE_STATUS_N` | Charge-active signal after voltage-domain conditioning |
| 3 | 7 | `K_MOTOR_PWM` | Driver control through base/gate network; external off bias |
| 4 | 8 | `K_BUTTON_N` | Button to ground, pull-up input; verify wake behavior in selected sleep configuration |
| 10 | 14 and onboard LED | RGB data | Board-installed LED; reserve; C3 V2 LED supply is the 5 V net |
| 18 / 19 | 16 / 15 and USB | USB D- / D+ | Reserve for native USB, including if exposed on pads |
| 9 | 13 and BOOT | Boot strap/button | Reserve; do not use as remote-control button |
| 21 / 20 | 18 / 17 | UART0 TX / RX | Service/debug; otherwise NC |

GPIO2 and GPIO8 are reserved straps. GPIO5-7 are unassigned external pads.
GPIO4-7 also have pad-JTAG functions: this allocation assumes native USB
debugging, not simultaneous use of external pad JTAG. GPIO11 is not exposed
as an application pad in this board symbol; GPIO12-17 are flash/unexposed.
Do not change these reserved functions to obtain more outputs without review.

### 2.2 Permitted S3-Zero alternative

| Net | Proposed S3 GPIO / pad | Notes |
| --- | --- | --- |
| `K_BAT_ADC` | 1 / P15-15 | ADC1_CH0 |
| `K_CHARGE_STATUS_N` | 13 / P15-3 | Same conditioned status contract |
| `K_MOTOR_PWM` | 6 / P15-10 | Off-biased driver input |
| `K_BUTTON_N` | 7 / P15-9 | Pull-up input, switch to ground |
| RGB data | 21 / onboard | 3.3 V LED rail in reviewed schematic; D-16 applies |
| USB D- / D+ | 19 / 20 | Reserved |
| BOOT; UART0 TX / RX | 0; 43 / 44 | Reserved service functions |

S3 strap and memory restrictions from section 1 still apply. All other
accessible application pads are NC for this Keyfob option. Do not apply the
C3 pin map to an S3 board.

## 3. I2C bus and module interfaces

| Device | 7-bit address used by host APIs | Wire address bytes | Address/configuration connection |
| --- | --- | --- | --- |
| PN532 | **0x24** | Write 0x48; read 0x49 | Fixed firmware address; choose I2C during startup |
| MPU-6050 | **0x68** proposed | Write 0xD0; read 0xD1 | AD0 tied to ground after checking module straps |
| MPU-6050 alternative | **0x69**, not simultaneous with the above for one device | Write 0xD2; read 0xD3 | AD0 high at the device's permitted logic level |

There is no address collision between these devices.

**V:** NXP UM0701-02 Table 7 specifies startup I0 = 1, I1 = 0 for I2C;
the specification's `SEL0=1, SEL1=0` is consistent **if** the module labels map
directly to these pins. The PN532 datasheet's internal `Selif` register table
uses a different encoding presentation; do not convert that table directly to
external switch positions. Confirm the actual board schematic and ROM response.
Elechouse V3 specifically documents switch 1 ON / 2 OFF; that is not a rule
for every PN532 board ([SRC-10](architecture.md#src-10),
[SRC-21](architecture.md#src-21)).

**P:** Bring up at 100 kHz. Both ICs document operation up to 400 kHz; increase
only after checking the complete bus, driver and wiring
([SRC-09](architecture.md#src-09), [SRC-11](architecture.md#src-11)).

Required bus implementation:

- One effective pull-up network on SDA and SCL to the validated logic rail.
  Audit all onboard pull-ups and level shifters; parallel resistors change the
  effective value. Resistor values, bus capacitance and trace/wire length are TBD.
- Verify rise time, low-level voltage, device sink current, clock stretching,
  wake transitions and behavior when either module is off.
- Keep I2C local to the Pod; do not place it on the external tether.
- Handle PN532 status-byte/ACK framing rather than treating it as an
  ordinary register-only sensor. Readiness/response deadlines and bus recovery
  must not pause motion sampling indefinitely.
- No silent continuation after address/probe failures. Report the missing
  function and apply an approved degraded-arming policy.

### 3.1 Pin directions and unused module pins

| Assembly terminal / IC reference | Required destination or treatment |
| --- | --- |
| PN532 module VCC | `P_NFC_SUPPLY`, voltage/interface TBD from actual module schematic; not automatically 3.3 V just because the IC's host I/O is 3.3 V |
| PN532 module GND | `P_GND` |
| PN532 SDA / SCL | `P_I2C_SDA` / `P_I2C_SCL`; at IC level SDA pin 28, SCL pin 27 |
| PN532 P70_IRQ / IRQ | `P_NFC_IRQ_N`, conditioned as needed; IC pin 25 |
| PN532 RSTPD_N | `P_NFC_RESET_N` through a validated interface; IC pin 38, active-low reset/power-down **input** |
| PN532 RSTOUT_N / RSTO | Reset-status **output**, IC pin 26; NC unless deliberately monitored; never driven as reset |
| PN532 I0 / I1 | Module strap network; verified mapping to IC pins 16 / 17 required |
| PN532 SPI/HSU alternative terminals | No separate SPI/UART wiring; several pins are multiplexed with SDA/SCL. Unused outputs NC; unused inputs treated per selected module schematic, not left arbitrarily floating. |
| PN532 antenna/matching connections | Stay within the verified module/antenna assembly. No invented coil or matching values; external antenna cable/connector remains TBD if selected. |
| GY-521 VCC / GND | `P_IMU_SUPPLY` / `P_GND`; establish regulator input versus IC supply before power connection |
| MPU SDA / SCL | `P_I2C_SDA` / `P_I2C_SCL`; IC pins 24 / 23 |
| MPU AD0 | Ground for proposed 0x68; IC pin 9; confirm existing pull resistor |
| MPU INT | `P_IMU_INT`; IC pin 12; configurable push-pull/open-drain and polarity |
| GY-521 XDA / XCL | Auxiliary sensor bus unused, external NC; do not connect to main SDA/SCL |
| MPU CLKIN / FSYNC | IC pins 1 / 11 to ground when unused, per manufacturer; verify this is already implemented on module |
| MPU VLOGIC / VDD / GND | IC pins 8 / 13 / 18; verify module connection and voltage sequencing |
| MPU REGOUT / CPOUT | IC pins 10 / 20 with manufacturer-specified local capacitors, normally module-internal |
| MPU reserved / NC pins | Follow SRC-11 section 7.1; no guessed ties on a future bare-IC design |

## 4. Complete logical connection schedule

This schedule covers every required functional connection and identifies the
unresolved interfaces. It is **not** a claim that connector pin numbers or
discrete values are complete. For purchased boards, internal connections are
governed by their verified schematic. A bare-IC redesign requires its own
complete schematic, not just these module contracts.

### 4.1 Pod signals and loads

| ID | From -> to | Required implementation / unresolved detail |
| --- | --- | --- |
| P-01 | S3 GPIO4 -> PN532 SDA + MPU SDA | Shared `P_I2C_SDA`; 3.3 V effective pull-up to logic rail |
| P-02 | S3 GPIO5 -> PN532 SCL + MPU SCL | Shared `P_I2C_SCL`; same pull-up qualification |
| P-03 | PN532 IRQ -> S3 GPIO10 | `P_NFC_IRQ_N`; voltage, polarity and accessible module contact verified |
| P-04 | S3 GPIO11 -> PN532 RSTPD_N | Conditioned `P_NFC_RESET_N`; reset bias and unpowered state TBD |
| P-05 | MPU INT -> S3 GPIO12 | `P_IMU_INT`; chosen polarity and mode in firmware |
| P-06 | MPU AD0 -> `P_GND` | Proposed 0x68 strap; do not fight an existing fixed-high module connection |
| P-07 | S3 GPIO6 -> 1 kohm resistor -> Q audio base | Original nominal value retained; exact resistor and transistor part/package TBD |
| P-08 | Q audio emitter -> `P_GND`; collector -> piezo negative | Baseline low-side topology; rated return routing and collector waveform must be verified |
| P-09 | `P_AUDIO_RAIL` -> piezo positive | One defined protected/rated supply, TBD; not an electrical short between VBUS and battery |
| P-10 | Q audio base -> off-bias resistor -> emitter | P; value TBD; avoid startup chirps or sustained drive during reset |
| P-11 | Piezo terminals / switching node -> discharge/clamp network | P; exact topology/parts TBD after transducer selection; not automatically a motor flyback circuit |
| P-12 | S3 GPIO7 -> button switched contact; other contact -> `P_GND` | Pull-up at logic side; tactile switch internal paired terminals must be identified |
| P-13 | Protected pack output -> ADC divider -> S3 GPIO1 | Divider bottom/filter return to `P_GND`; scaling, leakage, tolerances and off-state behavior TBD |
| P-14 | Charger status -> conditioning -> S3 GPIO13 | Normalized `P_CHARGE_STATUS_N`; do not apply charger VIN to GPIO |
| P-15 | S3 GPIO21 -> onboard RGB DIN | Existing board connection; DOUT remains board NC; supply discrepancy unresolved |
| P-16 | S3 GPIO8 -> output protection -> tether outbound contact | Optional; see tether contract below |
| P-17 | Tether return contact -> input protection/filter -> S3 GPIO9 | Optional; defined pull-down to `P_GND` at MCU side |
| P-18 | Logic/sensor bypass and driver bulk capacitors -> local rail / `P_GND` | Values, voltage ratings, ESR and placement from selected parts and transient tests |

### 4.2 Keyfob signals and loads

Use GPIO3/4/0/1 on C3 or GPIO6/7/1/13 on the S3 alternative as allocated above.

| ID | From -> to | Required implementation / unresolved detail |
| --- | --- | --- |
| K-01 | `K_MOTOR_PWM` -> base/gate network -> motor switch control | Transistor/driver and resistor values TBD; hardware off bias to emitter/source |
| K-02 | Motor switch emitter/source -> `K_GND`; collector/drain -> motor negative | Size for startup/stall current and dissipation, not average haptic current |
| K-03 | `K_MOTOR_RAIL` -> motor positive | Regulated/rated rail for the selected nominal 3 V motor |
| K-04 | Flyback diode anode -> motor negative; cathode -> `K_MOTOR_RAIL` | Exact diode reverse-voltage/current/energy ratings TBD; short loop at motor/driver |
| K-05 | Motor bypass/bulk capacitors -> `K_MOTOR_RAIL` / `K_GND` | Suppress brush/commutation and switching transients; values TBD |
| K-06 | `K_BUTTON_N` GPIO -> button; other switched contact -> `K_GND` | Pull-up, debounce, sleep wake and gesture qualification |
| K-07 | Protected pack output -> ADC divider/filter -> `K_BAT_ADC` | Divider bottom/filter to `K_GND`; bounded ADC voltage including tolerance |
| K-08 | Charger status -> conditioning -> `K_CHARGE_STATUS_N` | Same normalized, voltage-safe status contract as Pod |
| K-09 | Board GPIO10 (C3) or GPIO21 (S3) -> onboard RGB DIN | Optional Keyfob indication; board-installed LED still affects power even if not used |

### 4.3 Power, USB and service connections - repeat independently per unit

Prefix every net with `P_` or `K_`; **never join the two units' pack outputs**.

| ID | From -> to | Contract |
| --- | --- | --- |
| U-01 | Cell positive/negative -> protector B+/B- | Inside approved protected pack, or explicit qualified protector assembly |
| U-02 | Protector P+/P- -> protected-pack positive / local GND | All charging and load returns use protected terminals; no raw B- bypass |
| U-03 | Charge USB-C VBUS -> input protection/current limiting/reverse blocking -> charger input | Nominal 5 V sink; source-current contract, exact parts and port mapping TBD |
| U-04 | Charge USB-C GND -> local GND | Cable/connector current rating and shield treatment verified |
| U-05 | Charge USB-C CC1 and CC2 -> individual sink-termination networks -> GND | Must work in both orientations; nominal 5.1 kohm Rd appears on the reviewed Zero designs, but charger module implementation must be checked |
| U-06 | Charge USB-C D+/D-, SBU and shield | Charge-only design: no data connection to MCU by default; connector/controller-required treatment and shield/ESD topology TBD |
| U-07 | Charger BAT -> protected pack positive; charger ground -> protected return | Charging voltage/current/temperature regulation per selected cell and charger |
| U-08 | Charger PROG -> programming resistor -> ground | Candidate-specific resistor selected only after battery limits and tolerances are known |
| U-09 | Cell thermistor -> charger TEMP / independent temperature controller | Required temperature supervision implementation TBD; never assume TEMP tied low supplies protection |
| U-10 | Charger status outputs -> local indication and/or isolated logic status | Exact LED/current-limit parts TBD; unused outputs NC only if datasheet permits |
| U-11 | Input and protected pack -> qualified load-sharing/source-selection circuit -> `SYS` | P for simultaneous use/charge; otherwise a verified hardware load-disconnect policy is needed |
| U-12 | Slide switch -> regulator/load-switch enable network | P; charge path remains connected when system off. Exact switch contact numbering and reset-safe enable bias TBD. |
| U-13 | `SYS` -> qualified regulator(s) -> MCU/sensor and actuator rails | 3.3 V logic proposed; motor/audio rails separately matched; no unregulated cell on logic |
| U-14 | Regulator output -> Zero power interface | **Blocked:** choose and verify external 3V3 feed isolation or another approved board-input topology; do not parallel regulators |
| U-15 | Zero USB VBUS -> onboard regulator input / 5 V pad | V existing connection; simultaneous external feed needs real isolation, not just an extra diode elsewhere |
| U-16 | Zero USB D-/D+ -> S3 GPIO19/20 or C3 GPIO18/19 | V native service/programming interface; keep its differential path intact |
| U-17 | Zero USB CC1/CC2 -> onboard Rd -> GND; SBU NC; shell -> board GND | V from reviewed schematics; verify received revision and system-level ESD |
| U-18 | BOOT and RESET buttons; UART TX/RX and GND -> service access | Preserve onboard pulls/reset circuit; avoid externally driving an unpowered unit |
| U-19 | Rail decoupling, bulk capacitors and protection returns -> local GND | Requirements from exact regulator/charger/driver datasheets, not generic default values |

Every proposed connector must eventually have a keyed pin-1 view, mating part,
contact numbering, net assignment, wire specification, polarity and retention
method. Those details are TBD for charge, battery, motor, piezo and tether
assemblies until exact hardware is selected.

<a id="tether"></a>
## 5. Optional tether interface - hold point

Logical path:

```text
GPIO8 -> current-limited/protected output -> outbound insulated conductor
      -> secured cable loop/return connection -> return insulated conductor
      -> overvoltage/ESD protection + filtering -> GPIO9
GPIO9 MCU-side node -> defined pull-down -> Pod ground
```

The required physical topology (captive outbound cable and return plug, or a
fully detachable assembly), number of receptacles and every USB-C contact
number are **TBD**. The mechanical braid must not be presumed to be a reliable
insulated electrical conductor.

- Do not connect GPIO8/9 directly to USB VBUS, CC, the native USB data path or
  an unqualified external connector.
- USB-C reversibility, pin adjacency, standard charger/cable misconnection,
  ESD, exposed metal, shorts to ground/power and off-state injection all need
  documented protection and tests. GPIO clamp diodes are not the protection
  architecture.
- Do not use a standard-looking USB-C connector as proof of USB compliance.
  A mechanically keyed non-USB alternative is recommended for review, but
  changing the specified form factor requires owner approval.
- If the optional feature is omitted, leave the external interface unpopulated,
  GPIO8 safely inactive and GPIO9 defined low, and disable tether arming logic.
  If fitted, initial open-loop arming behavior remains a D-08 decision; do not
  interpret a missing tether as a healthy closed loop.
- Static continuity detects opens but not an intentional bridge. A coded or
  challenged loop would be a separately approved enhancement.

## 6. Allocation review result

Document-level check: no duplicate external GPIO roles within a selected unit
configuration; no PN532/MPU address collision; original Pod GPIO4-9 retained;
radio/USB/boot reservations identified. This does **not** close module supply,
connector, pull-up, driver, battery, sleep or startup verification.
ERC, DRC and electrical measurements have not been run because no project
schematic or PCB has been created.
