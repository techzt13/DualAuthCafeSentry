# Pod audio-stage design review

Date: 2026-11-13  
Status: **standalone editable KiCad schematic exists; isolated non-energised evaluation draft, not acoustic qualification**

Native schematic: [pod-audio-stage.kicad_sch](pod-audio-stage.kicad_sch). It is a standalone sheet and has not yet been integrated into the main Pod project or passed through KiCad ERC.

## Owner criteria

- Proposed measurement distance: 10 cm.
- Target: 105 dB; measurement weighting and environment are not yet specified.
- This remains a proposed evaluation criterion, not a proven output or final approval.

## Transducer screen

Same Sky CPT-2475-92T official data sheet:
- 24.0 mm diameter × 7.5 mm height.
- Rated drive: 10 Vp-p.
- Rated frequency: 4 kHz.
- Current consumption: maximum 8 mA at 10 Vp-p, 4 kHz, half-duty square wave.
- SPL: 92 dB minimum at 10 cm under those exact rated conditions.
- Capacitance at 120 Hz: 21 nF typical, 27.3 nF maximum.

Source: [Same Sky CPT-2475-92T data sheet](https://www.sameskydevices.com/product/resource/cpt-2475-92t.pdf).

This component does not meet a 105 dB minimum on its published rating: its published minimum is 13 dB lower. A 13 dB increase corresponds to approximately 4.47 times the sound-pressure amplitude or 20 times the acoustic intensity. The final enclosure may change the measured result, but no acoustic gain should be assumed.

## Driver candidate screen

Diodes Incorporated PAM8904E is a paper-screen candidate:
- Supports up to 47 nF piezo load; this exceeds the CPT-2475-92T's 27.3 nF maximum measured at 120 Hz, but the different test conditions and frequency dependence still need review.
- Supply range 1.5 V to 5.5 V.
- 1x, 2x and 3x charge-pump modes.
- 3x mode is limited to VIN below 4.5 V; the data sheet warns not to use 3x at VIN >=4.5 V and states a 13.5 V VOUT recommended maximum.
- Active package options include PAM8904EGPR (W-QFN2020-12 Type US) and PAM8904EGPR-T (U-QFN2020-12 Type UX). Their package heights differ and the exact land pattern still needs to be checked.

Source: [Diodes Incorporated PAM8904E data sheet](https://www.diodes.com/datasheet/download/PAM8904E.pdf).

## Conservative next schematic direction

- Use PAM8904E only as an isolated evaluation block, not a selected production part.
- Start with 1x mode only. EN1=0, EN2=1 selects 1x mode when DIN is active. Do not enable 2x or 3x until the actual differential waveform at the transducer terminals has been measured and proven within the 10 Vp-p transducer rating.
- Keep driver VIN on a separately reviewed low-voltage rail. Do not feed it from the BQ25185 4.5 V SYS output without first checking the mode limits and actual waveform.
- Use the data-sheet reference passive network as the starting point: 2.2 µF input, two 1 µF charge-pump capacitors and 2.2 µF output capacitor. Check DC-bias derating, voltage rating, ESR and layout before footprint freeze.
- Drive DIN with the Pod MCU's audio-control signal. EN1/EN2 must have defined reset defaults so the driver cannot enter a boosted mode during MCU boot.
- Keep VO1/VO2 differential output isolated from MCU ground and route directly to the piezo connector. Do not ground either piezo terminal in a differential configuration.

## Measurement and acceptance

The sound claim must not be made until a calibrated sound-level meter is used at a controlled 10 cm distance, with documented A/C/Z weighting, time weighting, tone frequency, duty cycle, supply voltage, enclosure configuration and microphone orientation. Measure the differential piezo voltage at the same time. Do not exceed 10 Vp-p at the transducer.

A separate transducer with a published SPL rating closer to or above 105 dB at 10 cm may be required. This is an engineering selection task, not a reason to contact a manufacturer before evaluating public data.

No 105 dB performance is claimed. No circuit has been physically tested.
