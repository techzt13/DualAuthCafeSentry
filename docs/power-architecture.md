# Dual-Auth Cafe Sentry - Power Architecture

Revision: 0.3 | Date: 2026-11-12 | Status: requirements; component pairing not approved

Revision 0.3 note: G1 candidate evidence is in the
[compatibility matrix](g1-battery-charger-compatibility.md) and the
[power recommendation](g1-power-architecture-recommendation.md). Two points
below are superseded by that evidence and are marked where they occur. The
requirements in this document are otherwise unchanged.

**LiPo charging, protection and power distribution are not approved for
construction or manufacture.** Exact cells, protected packs, charger modules,
regulators and actuator loads remain TBD. This document replaces no requirement
in the [project specification](../PROJECT_SPEC.md); proposed resolutions require
the [decision gates](design-decisions.md).

## 1. Unit-specific requirements

| Item | Sentry Pod | Pocket Keyfob |
| --- | --- | --- |
| Specified cell class | Nominal 3.7 V, 200-250 mAh LiPo; described as 502030 size | Nominal 3.7 V, 150-200 mAh LiPo; no size specified |
| Exact protected battery assembly | TBD: manufacturer, cell and pack suffix, PCM, leads, connector, thermistor | TBD independently; do not substitute the 250 mAh reference cell |
| Logic | ESP32-S3-Zero plus PN532 and MPU-6050 interfaces | C3-Zero evaluation option or S3-Zero alternative |
| Actuator | Passive piezo; waveform, rail voltage and peak current TBD | Nominal 3 V motor; operating range, startup/stall current and duty TBD |
| Charge input | USB-C; exact charger module/connector TBD | USB-C; exact charger module/connector TBD |
| Charger family allowed by specification | MCP73831 or TP4056; exact option/module TBD | USB-C charger unspecified; same families may be evaluated, not assumed selected |
| Switch | MSK-12C02 identifier; supplier, pinout and rating TBD | Miniature slide switch, exact part TBD |
| Required runtime / recharge time | TBD | TBD |
| Operating and charging environment | TBD from selected parts and intended use | TBD independently |

`3.7 V` is a nominal cell voltage, not a constant supply. The final cell's
maximum charge voltage, discharge endpoint and protection trip voltages must
come from its manufacturer. No assumed 4.2 V charger variant is approved merely
because the cell is called LiPo.

## 2. Verified facts and immediate conflicts

### 2.1 Zero-board power interface

The reviewed Waveshare schematics show:

| Board | Internal regulator | USB / external input | RGB supply |
| --- | --- | --- | --- |
| ESP32-S3-Zero | ME6217C33M5G | USB VBUS and 5 V pad share the regulator input net | 3.3 V |
| ESP32-C3-Zero V2 | ME6217C33M5G | USB VBUS and 5 V pad share the regulator input net | 5 V net |

Sources: [SRC-01](architecture.md#src-01),
[SRC-02](architecture.md#src-02), [SRC-04](architecture.md#src-04),
[SRC-05](architecture.md#src-05).

- Neither board schematic contains LiPo charging, cell protection or an
  independent battery/system power-path controller.
- Waveshare specifies 3.7-6 V for the external 5 V pad. A single cell can
  discharge below that input guidance. A board that boots with a freshly
  charged cell has not demonstrated full-discharge operation.
- A direct cell-to-5 V-pad connection can expose the cell to USB VBUS without
  charge regulation when a USB cable is inserted. **Do not make this connection.**
- An externally regulated 5 V feed also shares native USB VBUS. A diode only
  in that external feed does not prevent the board net from energizing the
  USB receptacle; the complete source topology must be reviewed.
- A regulated 3.3 V feed into the board's 3V3 pad is **not yet approved**.
  The onboard LDO output, reverse-current path, USB coexistence, power
  sequencing and C3's separately supplied RGB must be resolved first.
  **Revision 0.3:** a mirror of the ME6217 data sheet states that VOUT must
  not exceed VIN + 0.3 V ([SRC-36](datasheet-index.md#src-36)). On that
  evidence this feed is not acceptable on an unmodified board whenever the
  5 V net is unpowered. The canonical manufacturer document is still TBD.
- The regulator's advertised current capability is not a board thermal or
  whole-system load guarantee. Add sensor/LED loads and measure transients.

**P:** Prefer a regulated logic rail spanning the selected protected cell's
usable voltage range, evaluating buck-boost conversion where needed. Connection
to a Zero board remains conditional on a supported, verified isolation scheme.
**Revision 0.3:** because of the limit above, the G1 recommendation instead
feeds the board's 5 V pad from a power-path charger through an ideal diode
and uses the onboard regulator. It is a recommendation for owner decision,
not an approved design.
If that cannot be achieved without board rework, obtain approval for rework or
another power-interface/component strategy. Do not quietly remove an LDO or
change the MCU board in this documentation phase.

### 2.2 Charger families are not complete power subsystems

| Candidate | Manufacturer-verified behavior | Missing / selection-dependent requirements |
| --- | --- | --- |
| MCP73831 | Microchip DS20001984H: single-cell linear charger; programmable 15-500 mA; multiple regulated-voltage and termination options; thermal regulation; tri-state STAT | Exact order suffix and package; no cell-temperature input, separate SYS output or complete discharge/short-circuit protection; no integrated charge safety timer listed |
| TP4056 | NanJing Top Power ASIC rev. 2.3: 4.2 V version described; programmable up to 1 A; current-based termination; TEMP, CHRG, STDBY and CE pins | Actual manufacturer/variant on module, low-current programming accuracy, input/protection implementation; no separate SYS output or complete pack protection |

Sources: [SRC-13](architecture.md#src-13),
[SRC-14](architecture.md#src-14). A similarly marked clone or charger module
is not covered automatically.

A module sold as "with protection" may add a separate protection IC and FETs,
but those parts, thresholds, wiring and current ratings must be verified.
Reverse-discharge blocking inside a charger is not cell overdischarge,
overcurrent or short-circuit protection.

Many module settings are unsuitable for a small cell; do not assume any supplied
programming resistor is acceptable. **1 A equals 4 C for a 250 mAh cell and
approximately 6.67 C for a 150 mAh cell.** These are calculated ratios, not
approved charge rates.

## 3. Reference battery evidence - not a selection

### 3.1 Pod-capacity LP502030 comparison

The specification does not name a battery manufacturer. To test the meaning of
"502030", the EEMB **LP502030 bare cell** was checked against its linked
ZJQM-RD-SPC-H2305 specification, dated 2022-10-25
([SRC-16](architecture.md#src-16)).

| Property | Manufacturer value for this reference only |
| --- | --- |
| Capacity | 250 mAh nominal; 230 mAh minimum under specified test conditions |
| Nominal voltage | 3.7 V |
| Cell dimensions | Length <=31 mm; width <=20.5 mm; body thickness <=5.3 mm |
| Charge limit | 4.200 +/-0.050 V; maximum 250 mA, subject to temperature derating |
| End-of-charge current | 5 mA |
| Maximum discharge current | 500 mA |
| Discharge cutoff | 2.750 +/-0.005 V in the cell specification; not a system or PCM setpoint |
| Charging temperature | 0-45 deg C; at 0-20 deg C, charge current <=0.3 C |

The 0.3 C limit corresponds to 75 mA using its nominal 250 mAh capacity.
Even a generic "0.5 C is safe" rule would therefore be wrong over part of this
cell's specified temperature range.

This reference is not an approved protected pack. PCM, wiring, connector,
thermistor and swelling/service allowances are additional unknowns. The size
code must not be interpreted as a guaranteed finished 5 x 20 x 30 mm envelope.
The reference's 500 mA discharge limit also needs comparison with radio,
piezo/boost and LED peaks before it could be selected.

### 3.2 Keyfob-capacity LP401730 comparison

EEMB **LP401730**, ZJQM-RD-SPC-H0510 dated 2019-04-23, is another
**bare solder-tab cell**, not a selected protected pack
([SRC-26](datasheet-index.md#src-26)).

| Property | Manufacturer value for this reference only |
| --- | --- |
| Capacity / nominal voltage | 150 mAh nominal, 140 mAh minimum / 3.7 V |
| Charge voltage | **4.200 +/-0.020 V** |
| Maximum charge / termination current | 150 mA / 3 mA |
| Maximum discharge current | 300 mA; application peak-load compatibility unproved |
| Temperature | Charge 0-45 deg C; discharge -20 to 60 deg C |
| Body maxima | 31 x 17.5 x 4.3 mm; drawing also has L1 <=32 and tab dimensions |

Do not transfer LP502030's 0-20 deg C / 0.3 C charging rule to this cell;
it is not stated in the inspected LP401730 table. Finished-pack protection,
NTC, leads, polarity, connector and expansion limits remain TBD.

### 3.3 Nominal 4.2 V does not establish charging compatibility

| Reference | Documented regulation / limit | Comparison with LP401730 |
| --- | --- | --- |
| LP401730 | 4.200 +/-0.020 V charge limit | Upper limit **4.220 V** |
| MCP73831-2 | Page 3 VREG 4.168 / 4.20 / **4.232 V**, at the stated test conditions | Upper value exceeds cell limit by **12 mV** |
| TP4056 | Page 4 VFLOAT 4.158 / 4.2 / **4.242 V**, at 0-85 deg C | Upper value exceeds cell limit by **22 mV** |

Sources: [SRC-13](datasheet-index.md#src-13),
[SRC-14](datasheet-index.md#src-14), [SRC-26](datasheet-index.md#src-26).
These candidate pairings cannot be approved by their nominal labels.
Review complete temperature/tolerance/current/termination behavior and obtain
manufacturer clarification or an explicitly selected compatible pairing.
Neither software cutoff nor a pack protector is permission to exceed the
normal charging limit.

The original TP4056 REV_2.3 itself contains conflicting voltage accuracy:
page 4 gives the +/-1% bounds above, while page 17 demo-board text states
4.2 V +/-1.5%. This must be resolved with the manufacturer; do not select the
more convenient statement or apply either to an unknown clone/module.
No charger or battery substitution is made here.

## 4. Proposed functional power tree

The following contract applies **independently** to each unit. Component and
pin-level implementation remain TBD.

```text
USB-C charge VBUS
  -> qualified ESD/input protection, source-current control and reverse blocking
  -> charger input -------------------------> protected battery terminals
  -> system source/load-sharing circuit <--- protected battery terminals
  -> SYS
     -> switch-controlled logic regulation
        -> validated Zero-board supply interface
        -> validated sensor rails (Pod only)
     -> rated actuator supply and driver

Cell B+ / B- -> cell protection -> pack P+ / P-
Pack P- -> local system ground and charger return
Cell temperature sensor -> charge supervision / inhibit
Protected pack -> scaled battery monitor
Charger status -> voltage-safe MCU status / local charge indication
```

**Conditions on this proposal:**

1. The charger connects to protected pack terminals so a low-side protection
   FET is not bypassed by an accidental raw-cell negative connection.
   Verify the selected protection topology before assigning B-/P-.
2. The load-sharing circuit must distinguish battery charging current from
   system load and prevent backfeed between USB, SYS and battery.
3. A battery tied directly to both charger BAT and a running system is not
   equivalent to a regulated SYS path: system current can delay/prevent
   termination or cause incorrect recharge behavior.
4. Microchip AN1149 illustrates the need for additional load sharing
   ([SRC-15](architecture.md#src-15)); its example components and ratings
   are not selected for this project.
5. If simultaneous operation/charging is not implemented, an independently
   verified hardware load-disconnect strategy is required. A warning label or
   an MCU sleep instruction alone does not establish charge isolation.
6. **P:** Use the slide switch for a low-current enable path rather than
   switching an unverified peak actuator current. This changes the detailed
   switch wiring, not the required existence of a power switch. Enable bias,
   off leakage and charge-while-off behavior need approval.
7. Native programming USB is a second possible source. A production system
   must safely handle allowed combinations, or use a physical interlock that
   makes forbidden combinations impossible. Instructions alone are not the
   final protection.

The allocation of an external 3.3 V rail does not close the Zero-board
interface conflict described in section 2.1. **U-14 in the
[connection schedule](pinout.md) remains a wiring hold point.**

## 5. Charging, protection and supervision requirements

### 5.1 Battery qualification

Before energizing a battery assembly, record:

- Manufacturer, exact cell and finished-pack part numbers, chemistry and
  authentic supplier evidence.
- Cell voltage/current limits, temperature-dependent charging rules,
  permitted discharge current including pulses, cycle-life test conditions
  and storage/shipping requirements.
- Maximum finished dimensions including pouch seals, protection PCB,
  terminations and lead exit; approved swelling and compression constraints.
- Connector manufacturer and mating part, keyed polarity, wire gauge,
  insulation, current rating and strain relief. Do not infer polarity from
  connector appearance or wire colors alone.
- Whether protection and an NTC are present; if not, select and verify the
  separate circuits.

Do not solder directly to a bare pouch or improvise pack construction. Use a
manufacturer-qualified finished assembly or an independently reviewed
manufacturing process.

### 5.2 Charger configuration

- Choose the exact regulated-voltage suffix to match the selected cell,
  including worst-case charger tolerance, cable/PCB drops and cell limits.
- Set maximum charge current from the cell's **temperature-dependent**
  allowance, USB input capability and thermal design. Programming resistance,
  tolerance, package and measured charge current must be recorded.
- Evaluate preconditioning, termination ratio/current, recharge threshold,
  absent/deeply depleted cell handling and timeout requirements together.
  A chosen charger variant's termination behavior must be compatible with
  the chosen cell; do not assume all MCP73831 suffixes are equivalent.
- Use the exact charger's formula/table. MCP73831 and TP4056 programming
  constants are not interchangeable; neither are unverified clone guides.
- Qualify temperature sensing at the cell, not only at the charger die.
  MCP73831 needs a separate qualified charge-inhibit/temperature solution if
  retained. TP4056 TEMP requires a properly designed thermistor network;
  its datasheet explicitly says tying TEMP to ground disables that function.
- Define a safe charge timeout and fault indication. No firmware-only
  approach is approved until failure modes and independent protection are reviewed.
- Verify USB-C sink termination in both orientations, source current
  advertisement/allowance, inrush and input protection. Do not assume that
  fitting a USB-C socket permits arbitrary current or higher USB-PD voltages.

Reference **IC** pin functions, not a selected module connector map:

| Function | MCP73831, SOT-23-5 reference | TP4056, 8-pin reference | Required connection |
| --- | --- | --- | --- |
| Input supply | VDD pin 4 | VCC pin 4 | Qualified charge-input rail, local capacitors |
| Ground | VSS pin 2 | GND pin 3 | Protected/system return |
| Battery | VBAT pin 3 | BAT pin 5 | Protected battery positive |
| Current program | PROG pin 5 | PROG pin 2 | Datasheet-calculated resistor to ground |
| Charge status | STAT pin 1, tri-state | CHRG pin 7, open-drain | Voltage-safe status network |
| Finished status | STAT state | STDBY pin 6 | Local indication or unused-output treatment per datasheet |
| Temperature | No pin | TEMP pin 1 | Cell-temperature supervision; never assumed present on a module |
| Enable | PROG control per datasheet | CE pin 8 | Defined charge-enable/inhibit state |

The MCP73831 DFN pin map differs from SOT-23-5. Follow the selected package's
ground/thermal-pad and capacitor requirements exactly. Do not copy this
reference table into an unselected footprint.
Both complete package maps, including MCP73831 DFN EP9, are in
[verified pinouts](verified-pinouts.md#chargers).

### 5.3 Pack and load protection

Require independently verified overcharge, overdischarge, overcurrent and
short-circuit protection. Thresholds, tolerances, delay times, recovery method
and FET dissipation are TBD. Include appropriate input fault protection and
connector polarity controls; a charger is not a substitute.

Set the system's low-battery shutdown above destructive operation, with enough
margin for voltage sag and any final fault/state record. Do not use the
protector's last-resort disconnect as normal regulation or claim the siren
can keep operating after cell cutoff.

Temperature, current and short-circuit validation must use controlled fixtures,
current-limited sources and battery simulators where appropriate. Hazardous
cell abuse tests belong with qualified laboratories, not an improvised bench.

## 6. Rails, actuators and startup

| Net class | Requirement |
| --- | --- |
| `P_3V3` / `K_3V3` | P regulated logic rail, worst-case voltage/ripple/transients within every attached part's limits; exact regulator and Zero feed interface TBD |
| `P_NFC_SUPPLY` | Exact selected module input voltage; verify regulator/level shifters, switch-off and I2C pull-up supply |
| `P_IMU_SUPPLY` | Exact GY-521 input/IC voltage mapping; no dropout caused by an assumed 3.3 V module input |
| `P_AUDIO_RAIL` | One defined protected, switched supply matched to selected piezo and driver; voltage/boost need TBD |
| `K_MOTOR_RAIL` | Matched to selected nominal 3 V motor, not raw battery or 5 V USB |
| ADC monitor nodes | Resistor ratio/tolerance and filtering keep voltage within the selected ADC range; account for leakage, off-state injection and calibration |
| Charge-status nodes | Translate/isolate as required. MCP73831 tri-state STAT and a module's VIN-referenced LEDs must not be assumed 3.3 V-safe. |

For a passive piezo, identify capacitance, rated AC voltage, resonance,
permitted waveform and mounting conditions. A single NPN switch charging a
capacitive transducer does not establish the discharge half-cycle. Select a
proper discharge path or a different rated driver after evaluating waveform
and sound pressure. Do not infer 105 dB from transistor gain.

For the motor, size the driver, regulator, diode, traces and connectors against
startup/stall current. Place the diode with cathode at motor positive and
anode at the switching node. Add correctly rated local decoupling. A MOSFET
or dedicated driver may be evaluated, but it is a proposal, not an automatically
approved replacement for the specified transistor-driven approach.

The unselected [Vybronics reference](datasheet-index.md#src-27) operates at
2.5-3.5 V, with <=30 mA rated current at 3 V. Its <=80 mA starting-current
test is at the stated starting-voltage condition, not a universal stall
maximum at 3.5 V. Its 1 s on / 1 s off life test does not qualify indefinite
continuous-alert duty. The project motor remains TBD.

The unselected [SHOUHAN switch reference](datasheet-index.md#src-28) is
rated 50 mA at 12 V DC. It does not establish that the unspecified project
switch can carry radio/actuator peaks; enable-path switching remains conditional.

For both outputs, hardware off bias must work while firmware is absent,
resetting, flashing or asleep. Verify waveform clamps, switch dissipation,
rail droop, EMI and coupling into motion/radio measurements.

**RGB hold point:** the supplied LED sheet states 3.5-5.5 V operation and
VIH >=0.7 x VDD, while the S3 board supplies 3.3 V and the C3 V2 schematic
drives a 5 V-supplied LED directly from 3.3 V GPIO. At 5 V, the cited VIH
threshold is 3.5 V. These source-level mismatches may reflect a different
fitted LED; request clarification and test the exact boards rather than
declaring compliance. Do not raise the MCU's 3.3 V rail to compensate.

## 7. Power modes and source arbitration

| Condition | Required behavior / unresolved gate |
| --- | --- |
| USB absent, system on | Protected cell supplies SYS; regulation and transient margin proven down to approved cutoff |
| USB present, system on | Approved load sharing supplies system and charges cell without corrupting termination or exceeding source current |
| USB present, system off | Charge path remains functional if D-04/D-19 approve; system-off leakage and accurate termination verified |
| USB absent, system off | Defined low leakage; actuator controls remain off; storage discharge budget TBD |
| Native USB and charge/external supply both present | **Not approved until isolation/source-arbitration is verified** |
| Battery absent or protector disconnected | Defined safe input-powered behavior and fault indication; no unstable charger/regulator cycling |
| Low battery, overtemperature or supply fault | Explicit fault response; safe inhibit/shutdown; armed-state/restart policy pending D-12/D-19 |
| Alarm while charging | Worst-case combined input current, thermals, charge-current prioritization and feedback measured |

The physical switch can defeat deterrence if an attacker can reach it. Mechanical
access control and the intended power-loss behavior are open decisions; no
power architecture can promise operation without stored/supplied energy.

## 8. Power budget - measurements required

No runtime is predicted from chip-only sleep currents. Both Zero boards retain
regulator/LED loads, and a breakout may include permanently powered LEDs and
level shifters.

| Unit / mode | Loads to include | Average battery current | Peak / duration |
| --- | --- | --- | --- |
| Pod disarmed | Radio receive/beacons, NFC wake/poll, RGB, regulators; IMU readiness policy | TBD | TBD |
| Pod auto-armed / force-locked | Motion acquisition, radio, NFC, pulsing/steady RGB | TBD | TBD |
| Pod warning | All armed loads plus 1.5 s acoustic sequence | TBD | TBD |
| Pod full alarm | Siren waveform/possible conversion, white/red LED peaks, radio retries, sensors | TBD | TBD |
| Keyfob beacon/wait | Radio wake/RX/TX, retained memory, regulator, LED, divider | TBD | TBD |
| Keyfob two-pulse feedback | Radio and motor startup/running loads | TBD | TBD |
| Keyfob continuous alert | Sustained motor, radio RX and stop-command handling | TBD | TBD |
| Either unit charging/on or off | System input current, cell charge current, leakage and conversion losses separately | TBD | TBD |

Use measured battery-side average current for runtime:

```text
runtime_h = usable_capacity_mAh / average_battery_current_mA
```

Usable capacity depends on load, temperature, aging, regulator efficiency and
cutoff; nominal capacity is not entirely available.

For regulator/battery sizing, sum simultaneous loads, not their unrelated
averages:

```text
required_battery_peak_A >=
    sum(rail_voltage_V * rail_peak_current_A / conversion_efficiency)
    / minimum_loaded_battery_voltage_V
    + battery-side_quiescent_current_A
```

For linear charging, first-order heat is approximately
`(input_voltage - battery_voltage) * charge_current`, plus other device losses.
Validate junction/case/cell temperature in the actual closed enclosure; thermal
regulation of the charger die does not guarantee safe cell temperature.

For the NFC savings claim, measure charge over complete repeating cycles
including wake, command, RF and idle periods:

```text
I_NFC_average = measured_cycle_charge / cycle_period
savings = 1 - I_NFC_average / I_NFC_continuous_reference
acceptance target: savings > 0.80
```

Define the same supply, module, card conditions and functionality for both
measurements. Do not count only the RF-on current or omit the regulator and
always-on module LED.

## 9. Required power sign-off evidence

Before PCB release: exact battery/charger/protection/regulator identities;
reviewed source tree; annotated voltage/current budget; package pinout review;
hardware temperature/inhibit strategy; USB source arbitration and electrical
rule reports.

Before physical approval: measured charge voltage/current/termination over
specified temperature and load; protection behavior with suitable fixtures;
USB orientation and allowed simultaneous-source tests; startup/reset/off-state
tests; minimum-cell-voltage radio/actuator transients; final-case thermal,
acoustic and runtime results. Unmeasured items remain TBD, not pass.
