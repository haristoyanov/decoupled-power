# Linear Decoupled Power Supply

The goal of this project is to create a low-noise, decoupled power supply to power sensitive instrumentation in experimental research laboratories. This power supply will turn 120 VAC wall power into clean, adjustable output DC power, as well as break potential ground loops by being decoupled from the wall power by an isolation barrier. 

This power supply was designed by Mark Carlson at UBC, and we are closely following his original schematics.

# Motivation

Low noise, ground-decoupled DC is important for powering ADC/DACs and preamplifiers without introducing noise to the extremely sensitive measurement signals in an experimental condensed matter lab. Currently, the options are a stock DC power supply and a battery power supply. It is possible to improve on the DC power supply in terms of noise level, and the battery (while having low noise) has to be charged and has an unpredictable and possibly dangerous failure mode.
<div align="center">
<img width="589" alt="Screenshot 2023-06-09 at 6 09 12 PM" src="https://github.com/haristoyanov/decoupled-power/assets/133173558/73556322-234e-40cd-8953-b06da64c9e48">
</div>

# Schematic 

This summary explains the relevant parts of the circuit from left to right.
1. The transformer takes wall power (120V AC at 60Hz) and outputs 16V AC at 60 Hz. This is the input to the power supply.
2. The diodes rectify the current, so that the top branch always has positive voltage and the negative branch always has negative voltage.
3. The positive and negative voltage regulator ICs (TL1963A and LM2991, respectively) are supplied by the rectified AC, and decoupled using the capacitors to ground (filtering high-frequency noise and preventing output coupling to spikes or dips in the input AC). These output a DC voltage, with a shutdown (SHDN) indicator to show if they are working.
4. The exact output voltage is determined by the voltage on the ADJ pin. The 13K/1K voltage divider sets an output voltage of ±16 V on each branch.
5. The second stage of the circuit is powered by the ±16V. The first component is the 10V voltage reference IC (REF102), which outputs a more precise DC voltage than a voltage regulator. However, it only allows small current draw.
6. To set the exact output voltage, the two op-amp ICs (which are powered from the ±16V DC) take the 10V input from the voltage reference and output a voltage set by the voltage divider consisting of R35 and R36. In the given schematic, this outputs 15V from the top branch and -15V from the bottom.
7. The second op-amp matches and inverts the output of the first, ensuring a linear relationship between the positive and negative output.
8. The two transistors (Q30 and Q31) allow for more current draw from the 16V supply. This current is limited by the voltage regulator ICs, which allow 1A of current to flow.
9. The output goes through an Ethernet-style connector, whose indicator lights indicate whether each branch is outputing a voltage.

<div align="center">
<img width="1251" alt="Screenshot 2023-06-09 at 6 42 34 PM" src="https://github.com/haristoyanov/decoupled-power/assets/133173558/45a32355-8772-45dc-814c-7ff42b976d89">
</div>

# Preliminary testing

The first testing after confirming a ±15V DC output involved determining the Power Supply Rejection Ratio (PSRR). The power supply ratio is defined as the logarithm of the ouput/input (squared) voltage ripple ratio. For 60Hz noise in particular, the ripple is the integral of the voltage noise spectral density (Fourier transform of the input) over a small bandwidth near 60 Hz for the input (16V AC) and output (±15V DC). As such, an ideal DC power supply has an infinite PSRR.

<div align="center">
<img width="630" alt="Screenshot 2023-06-09 at 6 44 04 PM" src="https://github.com/haristoyanov/decoupled-power/assets/133173558/bba38b9a-e980-4df8-bfa3-ca94d0122f6e">
</div>

The testing was conducted through a capacitor to the analog input of a Stanford Research Systems SR1 spectrum analyzer.



Preliminary results indicate a power supply rejection ratio (from 120V AC wall power) of approximately 160. This compares to roughly 100 for the DC power supply that is currently used (estimated from the voltage ripple quoted in the datasheet). Below is a graph of root-mean-squared Voltage versus frequency on logarithmic axes for a narrow range of frequencies around 60 Hz. We used the data displayed in this plot to calculate our PSRR. 

<div align="center">
<img width="537" alt="image" src="https://github.com/haristoyanov/decoupled-power/assets/99318653/ef4b98ba-cb4f-4346-ad62-4142d06d3991">
</div>

It is also of interest to examine the performance of our power supply at a wide range of frequencies. Below is a plot of the voltage noise spectral density in V/rtHz against the frequency in Hz on logarithmic axes for a frequency range of 0 Hz to 1500 Hz. To get the total voltage noise in a certain bandwidth, one must integrate the square of the spectral density across that bandwidth and then take the square root of the result. 

<div align="center">
<img width="555" alt="image" src="https://github.com/haristoyanov/decoupled-power/assets/99318653/450a2adf-b919-48ae-baff-ac4db87e1f2b">
</div>

# Outlook
We will machine protective boxes for convenience. Also, we will try to implement potentiometers to create an adjustable output.

# Acknowledgements
Thank you to the instructors, TAs, and our classmates for UCSB PHYS 13CL/CS15C, thank you to the Dr. Young and all the Young lab grad students and postdocs that helped us, and thank you to Dr. Folk and Mark Carlson at UBC for the schematics and designs.

