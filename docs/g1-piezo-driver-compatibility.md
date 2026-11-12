# O-03/O-05 Piezo and Driver Compatibility Investigation

Date: 2026-11-12
Revision: 0.1
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
| Package options | Includes W-QFN2020-12 / U-QFN2020-12 options, as well as 3 x 3 mm options | A 2 x 2 mm package option exists, but package suffix, land pattern, height and assembly requirements must be checked |
| Protection/features | Automatic standby/wake; thermal shutdown, overcurrent, overvoltage and undervoltage protection stated by manufacturer | Useful safeguards, but do not replace external design review or system-level protection |

The 47 nF maximum-load rating covers the transducer's datasheet capacitance
range numerically. However, the transducer capacitance is specified at 120 Hz;
its effective electrical behaviour at 2.8–4.2 kHz and at the driver's output
waveform must be checked. Obtain and inspect the current full PAM8904E
datasheet, recommended application circuit, capacitor requirements, pin
configuration and operating-condition tables before any design decision.

The transducer's 10 Vp-p rating is lower than the PAM8904E EVB guide's
16 Vp-p heavy-load example. Although the transducer datasheet lists a
1–30 Vp-p operating range, that range alone does not prove the sounder is
qualified for the driver's output waveform, alarm duration, temperature or
mechanical mounting. Start any future review at or below the transducer's
10 Vp-p rated condition unless the manufacturer confirms a higher continuous
or pulsed operating condition in writing. No high-voltage test is authorised.

## 4. Current assessment

| Question | Current answer |
| --- | --- |
| Does the PAM8904E pass an initial capacitive-load screen? | **Yes, provisionally:** 47 nF driver rating versus 27.3 nF maximum piezo datasheet capacitance |
| Does it accept the required sweep frequency? | **Yes on input-frequency range:** 2.8–4.2 kHz is inside 20 Hz–300 kHz |
| Does this prove correct output waveform/amplitude across the sweep? | No |
| Does it prove 105 dB at 10 cm? | No |
| Is 105 dB acoustically demonstrated? | No; the piezo's documented figure is 92 dB at 10 cm under its specified 4 kHz test |
| Is the PAM8904E selected? | No — research candidate only |
| Is the piezo selected? | No — reference candidate only |
| Is any schematic, PCB or physical test authorised? | No |

**Research recommendation:** promote PAM8904E to the first boosted-driver
candidate for further datasheet and application review. Retain at least one
alternative driver candidate in the comparison until the full electrical,
power, thermal, package and waveform checks are complete.

## 5. Required checks before recommending a component

1. Retrieve and inspect the current full PAM8904E datasheet and package
   drawings. Confirm the exact orderable package, pinout, absolute maximum
   ratings, output swing versus supply/load, charge-pump mode truth table,
   capacitor values/ratings/ESR, startup, shutdown, fault behaviour and
   thermal derating.
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
5. Check driver switching frequency and charge-pump transients for EMI
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
