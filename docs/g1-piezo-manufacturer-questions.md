# O-03/O-05 Manufacturer Technical Questions

Date: 2026-11-12
Status: Prepared for review; NOT SENT

Purpose: obtain written manufacturer guidance before any component selection,
schematic, purchase or physical test. These questions are not an assertion
that the proposed pairing is supported.

## 1. Questions for Diodes Incorporated — PAM8904E

Product page:
https://www.diodes.com/part/view/PAM8904E

Datasheet:
https://www.diodes.com/datasheet/download/PAM8904E.pdf

Evaluation-board guide:
https://www.diodes.com/assets/Evaluation-Boards/PAM8904E_EVB-User-Guide.pdf

Reference transducer: Same Sky CPT-2475-92T, 24 mm diameter, 7.5 mm body,
rated 10 Vp-p, 1–30 Vp-p stated operating range, 21 nF typical and
27.3 nF maximum capacitance measured at 120 Hz. Project input sweep:
2.8–4.2 kHz. Proposed measurement distance: 10 cm. Proposed 105 dB target
is not yet approved and is not represented as achieved.

Please confirm:

1. Is PAM8904E explicitly suitable for the CPT-2475-92T, given the
   transducer's 14.7–27.3 nF capacitance at 120 Hz? Does the 47 nF load
   specification apply to this type of piezoelectric transducer and its
   impedance over 2.8–4.2 kHz?
2. What is the actual differential voltage waveform (peak-to-peak and
   common-mode) across VO1/VO2 in 1x, 2x and 3x modes for VIN values from
   3.0 to 4.1 V with this load? Please distinguish output rail VOUT from
   differential voltage across the transducer.
3. Which mode, if any, keeps the transducer within its 10 Vp-p rated drive
   condition throughout the 3.0–4.1 V supply range? Does operation above
   10 Vp-p require written transducer-maker approval?
4. Are there recommended limits for continuous on-time, burst duration,
   duty cycle, input waveform and frequency changes while active?
5. What are the guaranteed maximum VIN currents (not only typical values)
   for single-ended and differential output with 21 nF and 27.3 nF loads at
   2.8, 3.2, 4.0 and 4.2 kHz, in each mode?
6. Are there additional constraints for the 100 kHz charge-pump switching
   ripple, charge-pump capacitor ESR, DC-bias derating, capacitor ripple
   current, layout, thermal dissipation or PCB copper area?
7. Please confirm current status and recommended new-design order code,
   package outline, recommended land pattern, assembly restrictions and
   any known errata or PCNs for PAM8904EGPR and PAM8904EGPR-T.
8. Does the device support continuously changing DIN frequency from
   2.8 to 4.2 kHz without mode restart, missing cycles or audible artefacts?
   Please provide any relevant timing or slew restrictions.

## 2. Questions for Same Sky — CPT-2475-92T

Product page:
https://www.sameskydevices.com/product/audio/buzzers/audio-transducers/cpt-2475-92t

Datasheet:
https://www.sameskydevices.com/product/resource/cpt-2475-92t.pdf

Please confirm:

1. Is the 10 Vp-p rated voltage specified as differential voltage directly
   across the two terminals? Is the 1–30 Vp-p operating range an absolute
   survivability range, or is operation throughout that range supported
   for repeated alarm use?
2. What are the maximum recommended peak-to-peak voltage, RMS voltage,
   duty cycle, continuous on-time, burst duration and lifetime limits?
3. Can the transducer be driven by a differential square-wave output from
   a charge-pump driver such as PAM8904E? Are there restrictions on common
   mode, waveform symmetry, DC offset or edge rate?
4. Please provide impedance or capacitance data at 2.8, 3.2, 4.0 and
   4.2 kHz, including tolerance and temperature dependence.
5. Please provide guaranteed SPL at 10 cm at 2.8, 4.0 and 4.2 kHz using
   10 Vp-p and a clearly specified waveform and duty cycle. Please state
   weighting (if any), microphone conditions, orientation and tolerance.
6. Does the published frequency-response graph use the same rated voltage,
   10 cm distance and measurement setup as the 92 dB specification? Please
   provide the underlying data or a table for the 2.8–4.2 kHz region.
7. Is operation above 10 Vp-p permitted for a pulsed alarm? If yes, provide
   a maximum recommended voltage and corresponding duty/on-time/temperature
   limits in writing. If not, please state the rated limit explicitly.
8. Are there mechanical mounting, cavity, port, gasket or front-volume
   recommendations that materially affect SPL and response?

## 3. Decision rules after replies

- If both manufacturers confirm compatibility within the piezo's permitted
  voltage, duty and duration, update the paper current and acoustic budgets.
- If PAM8904E requires exceeding the transducer's rated condition and Same
  Sky does not approve it, do not use that pairing. Compare a different
  transducer or a separately engineered output stage.
- If no manufacturer can substantiate 105 dB at 10 cm, O-03 must be revisited
  with the owner using documented performance and a safe, measurable target.
- Do not convert manufacturer claims into an achieved product result.
- No purchase, design, assembly, battery connection or test is authorised
  by this question set.

## 4. Correspondence status

No enquiry has been sent. The repository contains no manufacturer response.
External correspondence must be sent through an authorised channel and
responses retained as evidence before any claim of confirmation is made.
