# O-03/O-05 Piezo and Driver Compatibility Investigation

Date: 2026-11-12
Revision: 0.2
Status: PAPER RESEARCH ONLY — no component selected, no circuit approved

## 1. Scope and owner direction

The owner chose O-03/O-05 Direction A for evaluation only:
- Retain the 24 mm Same Sky CPT-2475-92T as the reference transducer.
- Investigate a boosted driver compatible with that transducer.
- Use 10 cm as the proposed sound-level measurement distance.
- Keep 105 dB as an unapproved target. Weighting, level statistic, duration,
  tolerance, waveform and complete test geometry remain open under D-18.

This report is a datasheet screen, not an engineering design, measured result,
component approval or safety review.

## 2. Verified manufacturer data

### 2.1 Same Sky CPT-2475-92T

Manufacturer datasheet:
https://www.sameskydevices.com/product/resource/cpt-2475-92t.pdf

Manufacturer product page:
https://www.sameskydevices.com/product/audio/buzzers/audio-transducers/cpt-2475-92t

| Parameter | Manufacturer data | Engineering implication |
| --- | --- | --- |
| Type | Externally driven piezo transducer | Requires an external driver |
| Body | 24.0 mm diameter x 7.5 mm | Matches the current reference size, but mounting/port still need space |
| Rated drive | 10 Vp-p | Reference condition for published SPL |
| Operating range | 1–30 Vp-p | Broad operating range; does not mean every waveform/voltage is qualified for continuous alarm use |
| SPL | 92 dB at 10 cm, 4 kHz, 10 Vp-p, 1/2-duty square wave | Not evidence of 105 dB |
| Rated frequency | 4 kHz | Project sweep endpoints 2.8 and 4.2 kHz need response evidence |
| Current | Maximum 8 mA at rated voltage/frequency/waveform | Not a complete current model for a boosted driver |
| Capacitance | 14.7 nF min, 21 nF typical, 27.3 nF max, measured at 120 Hz | Driver must be screened against the maximum, with frequency-dependent behaviour checked |

The 92 dB figure is a manufacturer-specified dB value; the retrieved
datasheet does not state A-weighting. It must not be relabelled dBA.

The datasheet's frequency-response graph is also relevant: it is not a
flat response across the requested sweep, showing a broad dip around 2 kHz
and a higher region around 4–5 kHz. The graph does not provide a numeric
acceptance table at exactly 2.8 and 4.2 kHz, so no exact endpoint SPL should
be inferred from it. This reinforces the need to obtain manufacturer response
data or measure both sweep endpoints, not just 4 kHz.

## 3. Driver comparison

### 3.1 Diodes Incorporated PAM8904 — not a qualified match

Manufacturer datasheet:
https://www.diodes.com/_files/datasheets/PAM8904.pdf

The manufacturer specifies a maximum 15 nF piezo load. The CPT-2475-92T
is 21 nF typical and 27.3 nF maximum. The PAM8904 is therefore below the
transducer's nominal and maximum capacitance and is not a qualified match.
Do not design around this pairing without explicit written manufacturer
confirmation. It is not the preferred candidate for this transducer.

### 3.2 Diodes Incorporated PAM8904E — promising evaluation candidate

Manufacturer product page:
https://www.diodes.com/part/view/PAM8904E

Manufacturer evaluation-board guide:
https://www.diodes.com/assets/Evaluation-Boards/PAM8904E_EVB-User-Guide.pdf

| Parameter | Manufacturer information | Screening result |
| --- | --- | --- |
| Supply range | 1.5–5.5 V | Encompasses a nominal single-cell supply range on paper; exact system rail and transient behaviour still need checking |
| Piezo load | Up to 47 nF | Exceeds CPT-2475-92T's 27.3 nF stated maximum at 120 Hz; promising paper match, not final compatibility proof |
| Input frequency | 20 Hz–300 kHz | Encompasses 2.8–4.2 kHz |
| Output | Product page states up to 27 Vp-p from 4.5 V; 18 Vp-p from 3 V | Output depends on supply, charge-pump mode and load |
| Heavy-load condition | EVB guide states up to 16 Vp-p from 3 V with 47 nF load | Use this as a conservative documented reference for a heavy load; do not assume 27 Vp-p under this condition |
| Package options | W-QFN2020-12 (US) and U-QFN2020-12 (UX) are both listed Active; 2.00 x 2.00 mm body, maximum height 0.80 mm for US and 0.65 mm for UX | Small footprint is plausible. GPR (US) and GPR-T (UX) are the active orderable suffixes in the datasheet; verify lifecycle/availability at procurement time |
| Protection/features | Automatic standby/wake; thermal shutdown, overcurrent, overvoltage and undervoltage protection stated by manufacturer | Useful safeguards, but do not replace external design review or system-level protection |

The 47 nF maximum-load rating covers the transducer's datasheet capacitance
range numerically. The current manufacturer datasheet (DS41667 Rev. 4-2,
July 2023) and March 2025 evaluation-board guide have now been inspected.
The transducer capacitance is specified at 120 Hz; its effective electrical
behaviour at 2.8–4.2 kHz and at the driver's output waveform still needs
manufacturer confirmation. The EVB guide's external network uses 2.2 uF
input decoupling (16 V), two 1 uF charge-pump capacitors (25 V), and a
2.2 uF output capacitor (25 V). These are reference values, not a design
approval; DC-bias derating, package, ESR, ripple and voltage margin must be
checked for the final selected capacitors.

The transducer's 10 Vp-p rating is lower than the PAM8904E EVB guide's
16 Vp-p heavy-load example. The datasheet's 1–30 Vp-p operating range does
not override its 10 Vp-p rated condition or prove suitability for a particular
waveform, duty or alarm duration. The PAM8904E datasheet gives 1x/2x/3x
charge-pump modes; at VIN=3.0 V its table lists VOUT of 3 V, 6 V and 9 V
respectively (47 nF, 3.2 kHz conditions). In differential configuration the
output swing must be interpreted from the full driver topology, not simply
assumed equal to the VOUT rail. A conservative future study should begin by
checking 1x mode across the complete battery range, because higher modes may
exceed the piezo's 10 Vp-p rated condition. The manufacturer must confirm
actual differential piezo voltage and permitted drive. No high-voltage test
is authorised.

### 3.3 Full-datasheet checks completed for PAM8904E

The full Diodes DS41667 Rev. 4-2 datasheet was inspected, along with the
March 2025 EVB guide.

- Absolute maximum VIN is 6.0 V; VOUT absolute maximum is 15 V. The datasheet
  explicitly warns not to use 3x mode at VIN >= 4.5 V and says VOUT must not
  exceed 13.5 V in 3x mode.
- 3x mode is only specified for VDD 1.5–4.5 V; 1x and 2x modes are listed
  across 1.5–5.5 V. A single-cell battery charged to the proposed 4.1 V
  ceiling is inside the stated 3x supply ceiling, but the entire cell
  operating range, transients and charge-state extremes still need review.
- At VIN=3.0 V, 47 nF and 3.2 kHz, typical operating input current is listed
  as 4.3 mA in single-ended 3x mode and 14.2 mA in differential 3x mode.
  These are typical datasheet values, not maximum-current guarantees and
  not values measured with the 21 nF transducer. Use 14.2 mA as an initial
  conservative planning reference for a differential 3x paper budget, not
  as a verified worst case.
- The 3x-mode start-up time is listed as typically 1.91 ms; shutdown delay
  is typically 42 ms. Firmware alarm timing must account for this if the
  mode is used.
- The IC has short-circuit protection and thermal shutdown at a junction
  temperature above 150 C. These are fault protections, not acceptable
  operating-temperature targets.
- The active 2 x 2 mm package order codes listed are PAM8904EGPR
  (W-QFN2020-12, Type US, max height 0.80 mm) and PAM8904EGPR-T
  (U-QFN2020-12, Type UX, max height 0.65 mm). The larger 3 x 3 mm
  JPR/JER order codes are marked NRND in the datasheet. Do not use those
  NRND options as the preferred new-design path.
- The EVB reference circuit uses two 1 uF / 25 V charge-pump capacitors,
  one 2.2 uF / 25 V output capacitor, and one 2.2 uF / 16 V input capacitor.
  This external passive network and its placement consume more area than
  the IC body alone.

These findings strengthen PAM8904E as a candidate but do not establish a
qualified pairing. The datasheet's 47 nF test condition is helpful, but
manufacturer confirmation is still needed for this particular transducer's
impedance and drive rating across the complete sweep.

### 3.4 Alternative-driver screen

The original PAM8904 is rejected for this reference transducer because its
15 nF maximum load is below the transducer's 21 nF typical capacitance.
A broad search for other compact, integrated boosted piezo drivers did not
produce a second candidate with a manufacturer-verified capacitive-load
rating adequate for the CPT-2475-92T. Do not promote an unrelated generic
boost converter as a drop-in piezo driver: a discrete boost supply plus
push-pull output stage is a different architecture requiring its own
component-level voltage, current, EMI, fault and safety design.

For now the comparison is:
- PAM8904E: only integrated driver found in this research pass with a
  published 47 nF load capability; first candidate for manufacturer review.
- PAM8904: not qualified due to 15 nF load ceiling.
- Discrete boost plus output bridge: possible fallback architecture, but
  not yet researched sufficiently to recommend and likely larger/more
  complex for the Pod.

No second integrated IC is presented as a false equivalent. A further
manufacturer/distributor search should be done before any component freeze.

### 3.5 Alternative transducer screen

Manufacturer/distributor evidence:
- VCC PT-PM24-0538-RK: https://www.digikey.co.uk/en/products/detail/visual-communications-company-vcc/PT-PM24-0538-RK/28009446
- Multitrack TFM-25 datasheet: https://www.multitrack-buzzer.de/wp-content/gallery/external-driven-piezo-transducer/pdf/TFM-25.pdf


Two additional externally driven parts were found, but neither improves the
documented sound-level result for this project:

| Part | Published evidence | Assessment |
| --- | --- | --- |
| VCC PT-PM24-0538-RK | 24 mm diameter, 5.2 mm max height, 90 dB at 10 cm, 3.8 kHz, 5 V; 5 mA | Compact and close to the sweep centre, but 2 dB below the Same Sky reference and does not approach 105 dB on published data |
| Multitrack TFM-25 | 4.0 kHz ±0.5 kHz resonance; 80 dB(A) minimum at 10 cm, 9 Vp-p square wave; 9.5 nF ±30% at 1 kHz; 25 Vp-p allowable input | Smaller/lower capacitance, but much lower published SPL; no reason to replace the 24 mm Same Sky reference for the current goal |

These are evidence leads only. They do not close O-03 and are not proposed
selections. The TFM-25's stated 80 dB(A) is not directly comparable to the
Same Sky unweighted/unspecified 92 dB figure.

### 3.6 Discrete driver architecture screen

Same Sky's technical article describes single-switch, buffer, half-bridge,
full-bridge and resonant approaches. TI's reference article describes a
TLV61046A boost converter feeding a transistor output stage, with a
charge-pump/totem-pole arrangement for bipolar drive. These demonstrate that
a discrete boost-plus-bridge architecture is technically possible, but they
are not a ready-made design for this product.

For this project:
- A single transistor from the battery rail cannot provide a boosted
  differential waveform; its output is limited by the supply.
- A full bridge can theoretically place approximately twice the rail
  voltage across a load, but does not by itself boost the rail.
- A boost converter plus a suitable output bridge could provide higher
  voltage, but adds inductor, switching node, high-voltage capacitors,
  transistor/driver stages, protection, layout and EMI complexity.
- A resonant-inductor approach is a poor first choice for a 2.8–4.2 kHz
  sweep because the response depends strongly on the tuned frequency and
  transducer capacitance; Same Sky's design article warns this approach is
  frequency-specific and sensitive to capacitance variation.

Conclusion: retain PAM8904E as the first integrated-driver evaluation
candidate. Keep a boost-plus-bridge architecture as a fallback research
branch only if Diodes/Same Sky cannot confirm a safe compatible drive
condition. Do not start circuit design from the cited reference articles.

## 4. Current assessment

| Question | Current answer |
| --- | --- |
| Does the PAM8904E pass an initial capacitive-load screen? | **Yes, provisionally:** 47 nF driver rating versus 27.3 nF maximum piezo datasheet capacitance |
| Does the full datasheet give relevant current data? | Yes: typical 14.2 mA differential 3x / 47 nF / 3.2 kHz; not a maximum and not the exact piezo |
| Is there a second verified integrated driver candidate? | No; the research pass did not find another compact part with a documented load rating adequate for this transducer |
| Were alternate transducers screened? | Yes: VCC PT-PM24-0538-RK (90 dB at 10 cm) and TFM-25 (80 dB(A) minimum at 10 cm); neither meets the target |
| Is a discrete driver fallback feasible in principle? | Yes, boost plus bridge is a known architecture, but it is not designed or qualified for this project |
| Is the smallest package active? | Yes; PAM8904EGPR and EGPR-T are listed Active; 2 x 2 mm body, 0.80/0.65 mm maximum height |
| Does it accept the required sweep frequency? | **Yes on input-frequency range:** 2.8–4.2 kHz is inside 20 Hz–300 kHz |
| Does this prove correct output waveform/amplitude across the sweep? | No |
| Does it prove 105 dB at 10 cm? | No |
| Is 105 dB acoustically demonstrated? | No; the piezo's documented figure is 92 dB at 10 cm under its specified 4 kHz test |
| Is the PAM8904E selected? | No — research candidate only |
| Is the piezo selected? | No — reference candidate only |
| Is any schematic, PCB or physical test authorised? | No |

**Research recommendation:** keep PAM8904E as the sole currently verified
integrated-driver candidate for this piezo, but do not select it yet. The
most important next technical gate is written confirmation from Diodes and
Same Sky that the driver can safely operate the exact transducer across the
sweep at an output waveform not exceeding the transducer's permitted drive.
If that cannot be established, the project must compare a different piezo
or a separately engineered discrete driver architecture.

### 4.1 Initial battery-current planning implication

The existing Pod peak-current screen in LAST-WORKED-ON.md is 493.9 mA
using the PN532 IC maximum case, before the siren driver, LED and any
unaccounted transients. Adding the PAM8904E datasheet's 14.2 mA typical
differential 3x-mode current at 47 nF / 3.2 kHz gives an illustrative
508.1 mA arithmetic scenario (493.9 + 14.2 mA).

This is **not** a worst-case or validated system current: the 14.2 mA is a
typical value, the actual transducer is 21 nF typical rather than 47 nF,
operating voltage and mode are not frozen, and simultaneous load timing is
unknown. It does show that the siren driver cannot be omitted from the
battery budget. The illustrative figure already exceeds the Renata
ICP521630PM-01's stated 500 mA non-continuous rating by 8.1 mA; that
comparison is a warning only, not proof of a failure or a final battery
selection. Other candidate packs have lower documented peak limits.

Do not reduce this to a claim that the PAM8904E itself draws 14.2 mA in
every mode. The data point applies to the stated differential 3x / 47 nF /
3.2 kHz test condition. A proper budget needs a guaranteed maximum or
manufacturer-confirmed current for the actual piezo and chosen mode, plus
the processor/radio/NFC/IMU/LED coincidence profile and battery impedance.

## 5. Required checks before recommending a component

1. Full PAM8904E datasheet and EVB guide have now been inspected. Remaining
   work is to confirm exact orderable suffix and package land pattern, review
   capacitor derating/ESR/ripple, and obtain written confirmation of output
   swing versus supply/load for the actual transducer.
2. Ask Diodes Incorporated to confirm whether the CPT-2475-92T is a suitable
   47 nF-class load, given that its 14.7–27.3 nF capacitance is specified at
   120 Hz. Ask for any restrictions on waveform, output voltage, frequency,
   duty cycle and continuous/pulsed alarm duration.
3. Ask Same Sky to clarify impedance/capacitance behaviour and SPL response
   at 2.8, 4.0 and 4.2 kHz, and whether operation above the 10 Vp-p rated
   condition is supported for the proposed waveform and duty.
4. Build a paper current budget using the actual battery voltage range,
   charge-pump mode, output load and alarm pattern. Include efficiency,
   input current, startup/inrush, reservoir-capacitor ripple and simultaneous
   ESP32 radio, NFC, IMU and LED loads. Compare the resulting pulse current
   with battery-maker discharge limits; those limits are not yet resolved.
5. Reconcile the added siren-driver current with the existing 493.9 mA Pod peak screen; do not assume the 14.2 mA typical datum is a maximum. Check driver switching frequency and charge-pump transients for EMI
   coupling into PN532 NFC, ESP32 radio and IMU. Review manufacturer layout
   guidance, return-current paths, decoupling and acoustic output routing.
6. Confirm package and external capacitor footprints, capacitor height,
   piezo pin clearance, mounting, acoustic port and antenna keepouts in the
   enlarged Pod envelope. No CAD or PCB work is authorised yet.
7. Close D-18 before judging sound performance: weighting, peak/average/RMS
   statistic, sweep waveform, duty cycle, alarm duration, tolerance,
   microphone calibration/class, orientation, distance reference point and
   enclosure configuration.
8. Require manufacturer evidence or controlled calibrated measurement of the
   exact transducer/driver/enclosure combination. Do not infer SPL from
   voltage or compare unweighted dB with dBA as if identical.
9. Define a safe, supervised test method and exposure controls before any
   acoustic testing. A 105 dB target is potentially hazardous; do not listen
   close to the sounder or conduct informal tests.

## 6. Explicit hold points

No purchase, supplier order, schematic, PCB/carrier design, construction,
battery connection, high-voltage piezo test or acoustic exposure test is
authorised by this report. Independent electrical review and explicit owner
authorisation remain required before any physical work.

O-03, O-05, D-07 and D-18 remain OPEN. G1 physical component freeze remains
BLOCKED. This report changes no component-register row to selected or FROZEN.

## 7. Revision history

| Revision | Date | Change |
| --- | --- | --- |
| 0.1 | 2026-11-12 | Initial paper screen of CPT-2475-92T, PAM8904 and PAM8904E; PAM8904E promoted as a promising evaluation candidate only |
| 0.2 | 2026-11-12 | Inspected full PAM8904E datasheet and EVB guide; recorded mode limits, input-current figures, active package suffixes, external capacitors and alternative-driver search outcome |
| 0.3 | 2026-11-12 | Added indicative 508.1 mA Pod peak-current scenario and documented battery-rating warning; no current or component approved |
| 0.4 | 2026-11-12 | Added two alternate transducer screens and discrete boost/bridge fallback architecture assessment; no selection or design authorised |
