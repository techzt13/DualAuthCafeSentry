# G1 Power Architecture Recommendation

Revision: 0.4 | Date: 2026-11-12 | Status: BQ25185 4.1 V selected for evaluation by owner under O-02; architecture NOT approved

**O-02 owner direction:** evaluate the TI BQ25185 at its 4.1 V setting.
This is not a component freeze or approval to purchase, design, build, connect
a cell, or use any battery/charger pairing. This remains a paper recommendation:
no circuit has been drawn, built or measured, and no power architecture is approved. It extends, and does not
replace, the [power architecture](power-architecture.md). Decisions D-03 and
D-04 remain OPEN. Evidence is in the [datasheet index](datasheet-index.md);
the battery and charger comparison is in the
[compatibility matrix](g1-battery-charger-compatibility.md).

## 1. New evidence that constrains the design

| ID | Finding | Evidence | Consequence |
| --- | --- | --- | --- |
| PF-1 | The Zero boards' ME6217 regulator document says VOUT must not exceed VIN + 0.3 V, because reverse current flows through a parasitic diode from VOUT to VIN | SRC-36, mirror of Micro One sheet V02, section "Output transistor" | **Feeding 3.3 V into the 3V3 pad while the 5 V / VBUS net is unpowered violates this limit.** The 3V3-injection idea in power architecture section 2.1 is not acceptable on an unmodified board unless the canonical datasheet says otherwise |
| PF-2 | ME6217 input range 2.0 to 6.5 V; dropout 100 mV typical, 180 mV maximum at 300 mA for 3.0 to 5.5 V outputs; 800 mA maximum only when VIN is at least VOUT + 1.0 V | SRC-36 | The 5 V pad can be fed below 3.7 V electrically, but the 3.3 V rail then sags; Waveshare's 3.7 to 6 V guidance (SRC-01, SRC-04) is not met over a full discharge |
| PF-3 | Both Espressif chips need 3.0 to 3.6 V and a supply able to deliver 0.5 A or more; documented transmit peaks are 340 mA (S3) and 335 mA (C3) | SRC-07 v2.2, SRC-08 v2.5 | A 200 mA regulator such as TPS7A02 is unsuitable; rail and battery must tolerate about 0.43 to 0.49 A peaks in the Pod |
| PF-4 | The ESP32-S3-Zero does not expose USB D-/D+ on pads; the ESP32-C3-Zero does (contacts 15 and 16) | SRC-02, SRC-05, [verified pinouts](verified-pinouts.md#c3-zero) | Only the C3 board could share one carrier-mounted USB-C connector for charging and data |
| PF-5 | Native USB VBUS and the external 5 V pad are one net on both boards | SRC-02, SRC-05 | Anything that powers the 5 V pad from the battery also energises the native USB-C VBUS pins |
| PF-6 | Power-path chargers exist that separate battery charge current from system load: BQ25185 (resistor-strapped), BQ25180 (I2C), BQ24074/75 | SRC-30, SRC-31, SRC-32 | The load-sharing requirement in power architecture section 4 can be met by one IC rather than a discrete circuit |
| PF-7 | BQ25185 regulates SYS to 4.5 V when an input is present, disconnects the battery at 3.0 V, limits input current to 100, 500 or 1100 mA, has an NTC input and a fixed 360 minute safety timer | SRC-30 | All behaviours are fixed by hardware straps; none depends on firmware |
| PF-8 | TI LM66100 ideal diode: 1.5 to 5.5 V, 1.5 A, 91 mohm typical and 125 mohm maximum at 3.6 V up to 85 deg C, reverse-current blocking with CE tied to VOUT | SRC-34 | A low-loss alternative to a Schottky diode between a system rail and the 5 V pad |
| PF-9 | No candidate battery documents a discharge rating that clearly covers the transmit peak; see compatibility matrix section 5 | SRC-37 to SRC-40 | Peak-current handling is an open safety and reliability question |

## 2. Options

All options keep the specified Waveshare Zero boards unless stated.

### Option A - power-path charger feeding the 5 V pad through an ideal diode

```text
Dedicated charge USB-C (CC pull-downs, input protection)
  -> BQ25185 IN
     BAT <-> protected pack P+ / P-      NTC on cell -> TS
     SYS -> slide-switch-controlled enable -> LM66100 -> Zero 5 V pad
                                                        -> onboard ME6217 -> 3V3
Zero native USB-C: service and programming only
```

- **For:** charge current and system load are separated (PF-6). Charge
  voltage, current, input limit, temperature window and timer are fixed in
  hardware (PF-7). The onboard regulator is used within its stated
  input range, so PF-1 is not violated. No board rework.
- **Against:** the native USB-C VBUS pins carry the battery-derived rail
  whenever the unit is on (PF-5). The battery must stay above roughly 3.4 V
  under peak load (section 3.2), which is below Waveshare's 3.7 V guidance
  and gives up part of the cell's capacity. It needs a custom carrier PCB,
  which is a later, separately authorised stage. BQ25185 is not one of the
  two specified charger families.
- **Source combinations, from the documents only:**

| Charge USB | Native USB | Battery | Expected behaviour | Evidence still needed |
| --- | --- | --- | --- | --- |
| Present | Absent | Present | SYS 4.5 V supplies the board; remaining input current charges the pack | Measured SYS, charge current and termination under radio bursts |
| Absent | Absent | Present | Battery supplies SYS, then the board; VBUS pins sit near battery voltage | Brownout voltage, native-port back-drive acceptability |
| Absent | Present | Present | 5 V pad is driven by the host; LM66100 blocks reverse current into SYS; pack is not charged | Reverse leakage into SYS and BAT measured; host behaviour with a pre-biased VBUS |
| Present | Present | Present | Board runs from the native host; charger charges the pack with SYS lightly loaded | No interaction between the two sources |
| Present | Any | Absent | SYS regulates from the input | Stable regulation and status indication without a pack |

### Option B - charge only when switched off

A simple charger without power path (MCP73831 class) and a switch that
connects the pack either to the charger or to the load, never both.

- **For:** keeps a specified charger family. Charge termination is not
  disturbed by system load. Fewest parts.
- **Against:** the unit cannot alarm while charging, which is a product
  behaviour change for the owner to accept. The switch carries the whole
  load: about 0.43 to 0.49 A in the Pod. The SHOUHAN MSK12C02 reference is
  rated 50 mA at 12 V DC (SRC-28) and C&K PCM12 is rated 0.3 A at 6 V DC
  (SRC-50); neither covers that current, so a rated switch or a load-switch
  IC is needed. MCP73831 has no temperature input, and its 4.232 V maximum is
  unresolved against five of the seven packs. PF-5 back-drive still applies.

### Option C - change the processor board (specification change)

Use a board whose maker has designed in battery charging, or a custom PCB
around an Espressif module. One lead was checked: the Seeed Studio XIAO
ESP32C3 page (SRC-53) states 21 x 17.8 mm, a battery charging chip, and
**380 mA fast charge**. That current is 2.5 times the 150 mA maximum of the
150 mAh packs examined, so that board is not suitable for them as supplied.
No integrated-charger board has been found that is documented as compatible
with a 150 to 250 mAh cell. A custom PCB would let the charger, regulator
and processor be chosen together but adds RF and manufacturing obligations.
This option replaces the specified ESP32-S3-Zero and needs owner approval.

### Option D - rework the Zero board

Cutting the VBUS trace or removing the onboard regulator would remove PF-1
and PF-5. It modifies a purchased assembly, has no manufacturer support and
is not recommended.

### Rejected arrangements

| Arrangement | Why it is rejected | Evidence |
| --- | --- | --- |
| Pack directly on the 5 V pad | USB VBUS would reach the cell without charge regulation | SRC-02, SRC-05; D-03 |
| External 3.3 V into the 3V3 pad, board unmodified | Violates the regulator's VOUT <= VIN + 0.3 V limit when USB is absent | PF-1 |
| Charger BAT pin shared with a running load | Load current corrupts termination; no power path in MCP73831, TP4056 or BQ25100 | SRC-13, SRC-14, SRC-33; D-04 |
| TPS7A02-class 200 mA regulator for the logic rail | Below the 0.5 A supply requirement | PF-3, SRC-35 |

## 3. Recommendation

**Recommend Option A for evaluation**, subject to owner approval of the
charger change and the native-port limitation, and to independent electrical
review before anything is built.

### 3.1 Recommended configuration to review

| Function | Recommended candidate | Setting to review | Basis |
| --- | --- | --- | --- |
| Charger and power path, both units | TI BQ25185DLHR-class, WSON-10 2.2 x 2.0 mm | Battery regulation strapped to **4.1 V** (130 kohm for 500 mA input limit per Table 6-1) | Maximum 4.1205 V is below every battery limit examined, including the strict 4.200 V reading |
| Charge current, Pod | Same | About 100 mA: `ICHG = 300 / RISET`, so 3.0 kohm nominal | Jauch LP502030JH maximum 0.5 C (125 mA); Renata ICP521630PM-01 normal 125 mA. With the +/-10 % accuracy, 90 to 110 mA |
| Charge current, Keyfob | Same | **Unresolved**: 30 mA (10 kohm) is the only value allowed over 0 to +45 deg C for Jauch LP402025JU; a higher value needs the NTC window raised to +15 deg C | Compatibility matrix section 4 |
| Cell temperature | 10 kohm-class NTC on the cell to TS | Network values TBD from the selected NTC and pack limits (0 to +45 deg C charge) | BQ25185 hot and cold thresholds, SRC-30 |
| Pack | Pod: Renata ICP521630PM-01 or Jauch LP502030JH+PCM. Keyfob: Renata ICP402025PC-01 or Jauch LP402025JU+PCM | Not selected | [Component shortlist](g1-component-shortlist.md) |
| Rail hand-off | TI LM66100 from SYS to the Zero 5 V pad, CE to VOUT | Not selected | PF-8 |
| Logic regulation | The Zero's own ME6217 | No added regulator | PF-1, PF-2 |
| Charge connector | GCT USB4125-GF-A, 6-contact power-only USB-C, with 5.1 kohm CC pull-downs | Not selected | SRC-52; 3.00 A VBUS rating |
| Power switch | Low-current enable of the LM66100 CE node rather than switching load current | Circuit TBD | Existing proposal in power architecture section 4, item 6 |

The 3.0 kohm, 10 kohm and 130 kohm values are worked examples from the
datasheet formula and table. They are not released component values.

### 3.2 Voltage headroom estimate

At a 0.43 A peak, using maximum resistances: BQ25185 battery FET 140 mohm
gives 60 mV; LM66100 125 mohm gives 54 mV. The ME6217 dropout is specified
only at 300 mA (180 mV maximum); scaled linearly to 0.43 A it is about
258 mV, which is an **estimate, not a datasheet value**.

```text
60 + 54 + 258 = 372 mV
battery voltage needed for a 3.0 V rail = 3.0 + 0.372 = about 3.37 V
```

The 3.3 V rail is therefore out of regulation, but above the chips' 3.0 V
minimum, for battery voltages between about 3.37 V and about 3.67 V at peak
load. The PN5321 MINI manual reports its own input falling to 3.19 to 3.23 V
under continuous RF from a 3.3 V supply (SRC-43), so its margin under a
sagging rail is unknown. Usable capacity down to 3.37 V is not stated in any
battery document and must be measured. A buck-boost regulator would recover
this capacity, but only by feeding the 3V3 pad, which PF-1 rules out without
board rework.

### 3.3 What this recommendation does not establish

- That any battery can supply the transmit peak (PF-9, risk R-34).
- The capacity actually stored at 4.1 V, or the resulting runtime.
- The behaviour of a USB-C source when the native port's VBUS is pre-biased.
  Some sources check that VBUS is discharged before enabling it; this must be
  tested with the intended chargers and cables, or the native port must be
  made inaccessible in the closed enclosure.
- Thermal behaviour: a linear charger dissipates
  `(VIN - VBAT) x ICHG`, about `(5.0 - 3.6) x 0.1 = 0.14 W` at 100 mA, inside
  a sealed body next to the cell. Closed-case temperature is unmeasured.
- Siren supply. A boosted piezo driver (Diodes PAM8904, 1.8 to 5.5 V input)
  could run from the 3.3 V rail; its load is not yet in the peak budget.
- RGB behaviour. The C3 board's LED is on the 5 V net, so under Option A it
  would see 3.4 to 4.5 V; decision D-16 still applies.

## 4. Measurements required before any approval

1. ME6217 identity and canonical datasheet; reverse leakage from 3V3 to the
   5 V net on a received board.
2. Battery current waveform during ESP-NOW transmit at the intended transmit
   power, with and without bulk capacitance, compared with the pack rating.
3. Rail voltage at the processor and the NFC module at 3.4 V, 3.6 V and
   4.1 V battery voltage under the worst simultaneous load.
4. Charge voltage, current, termination and timer on the exact pack, across
   the permitted temperature range, with the system running.
5. NTC trip temperatures at the cell.
6. All five source combinations in section 2, both USB-C orientations.
7. Native-port VBUS voltage with no cable, and source behaviour when a cable
   is attached in that state.
8. Closed-case cell, charger and regulator temperatures.

## 5. Revision record

| Revision | Date | Change |
| --- | --- | --- |
| 0.3 | 2026-11-12 | First issue: evidence-based options and a recommended evaluation architecture; nothing approved |
| 0.4 | 2026-11-12 | Recorded owner O-02 direction to evaluate BQ25185 at 4.1 V only; power architecture and all battery pairings remain unapproved |
