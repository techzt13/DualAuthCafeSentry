# Pod power-stage design review

Date: 2026-11-13  
Status: **schematic design basis; not yet a wired or approved circuit**

## Objective

Translate owner decision O-02 into a conservative, source-grounded charger design direction while keeping all battery and system outputs unconnected until the complete board power path is reviewed.

## BQ25185 evaluation configuration

Use TI BQ25185, WSON-10 DLH, only as the current evaluation IC. The official August 2026 Rev. B data sheet pin map is:

| Pin | Signal | Draft net / function |
|---:|---|---|
| 1 | SYS | P_SYS_4V5_HOLD |
| 2 | BAT | P_BAT_HOLD |
| 3 | STAT2 | P_CHG_STAT2_HOLD |
| 4 | CE | P_CHG_CE_N_HOLD; active-low enable |
| 5 | GND | P_GND |
| 6 | TS/MR | P_BAT_NTC_HOLD |
| 7 | ILIM/VSET | R_ILIM/VSET to ground |
| 8 | ISET | R_ISET to ground |
| 9 | STAT1 | P_CHG_STAT1_HOLD |
| 10 | IN | P_USB_CHG_IN_HOLD |
| EP | Thermal pad | Ground copper/thermal layout per TI package guidance; exact land pattern still to be checked |

### Evaluation-only resistor settings

The current Rev. B Table 6-1 maps:
- 130 kΩ from ILIM/VSET to GND -> 4.1 V battery regulation and 500 mA input current limit.
- 100 kΩ -> 4.1 V and 1100 mA input current limit.

Use 130 kΩ as the conservative paper-evaluation value. Do not use 100 kΩ in this draft.

For ISET, the data sheet gives I_CHG = K_ISET / R_ISET, with K_ISET typical 300 AΩ and min/max 285/315 AΩ for charge currents above 10 mA. If (and only if) the Renata ICP521630PM-01 remains the candidate pack, a 4.7 kΩ resistor gives approximately 63.8 mA typical and 67.0 mA using the maximum K factor; applying the stated ±10% charge-current accuracy gives a rough upper screen of 74.5 mA. This remains below the pack's stated 125 mA normal charge current, but the pack pairing is not approved. This arithmetic does not approve that cell pairing; the pack's charge-voltage tolerance and thermal provisions remain unresolved.

### Required bypass components

TI specifies:
- IN to GND: at least 1 µF ceramic.
- SYS to GND: at least 10 µF ceramic, with at least 1 µF effective after DC-bias derating.
- BAT to GND: at least 1 µF ceramic.

Place each close to its corresponding IC pins. Select voltage ratings and case sizes only after effective capacitance, bias, temperature and layout checks.

### Temperature and status

TI describes a 10 kΩ NTC at 25°C with beta 3435 K for the TS input. If the pack has no built-in NTC, a separately mounted, mechanically retained cell thermistor is needed. The exact NTC, attachment method and pack thermal limits are not selected.

STAT1/STAT2 are open-drain outputs and may be pulled up through 1 kΩ to 20 kΩ. Any MCU pull-up must use the verified MCU I/O rail, not a 5 V pull-up. CE is active-low; do not leave its state ambiguous in the final schematic.

## Power-path boundary

The BQ25185 SYS output is regulated at 4.5 V in the normal regulation region. Do not label this as a 5 V rail or connect it directly to the Zero board's shared USB VBUS/5V node without proving the board's permitted input range, backfeed paths, and regulator sequencing.

Keep the following distinct and marked HOLD:
- P_USB_CHG_IN_HOLD: dedicated charger USB-C input, with CC resistors, ESD and connector details not yet designed.
- P_SYS_4V5_HOLD: charger system output.
- P_BAT_HOLD: protected battery connection.
- P_5V_BOARD_HOLD: processor-board 5V/VBUS shared node.
- P_3V3_BOARD_HOLD: processor-board regulator output.
- P_3V3_PERIPH_HOLD: module supply.
- P_AUDIO_VIN_HOLD: future audio-driver supply.

The previous concept of placing an ideal-diode stage between SYS and the Zero 5V pad is not yet released. An ideal diode prevents reverse current but does not boost 4.5 V to 5 V. Confirm whether the exact Zero board and regulator can operate from the complete SYS voltage range before choosing that path; otherwise add a properly designed boost/buck-boost stage or change the architecture.

## Blockers before energising

1. Freeze the exact protected cell pack and obtain its maximum charge voltage, charge-current limits, temperature limits and discharge pulse capability.
2. Select the actual cell NTC and mechanical attachment method.
3. Complete the dedicated USB-C input (CC1/CC2, ESD, connector, VBUS protection).
4. Reconcile SYS, battery and native USB VBUS source arbitration.
5. Verify the Zero-board input and regulator behaviour over battery and charger conditions.
6. Calculate worst-case simultaneous load, battery sag, charger thermal dissipation and board copper.
7. Confirm BQ25185 package drawing, thermal-pad land pattern and assembly constraints.
8. Only then draw and connect the final battery and board power nets.

## Primary sources

- [TI BQ25185 Rev. B data sheet, August 2026](https://www.ti.com/lit/ds/symlink/bq25185.pdf)
- [TI BQ25185 product page and current documentation](https://www.ti.com/product/BQ25185)

No battery/charger pairing is approved. This document is not an assembly or energising instruction.
