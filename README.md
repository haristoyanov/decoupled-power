# Linear Decoupled Power Supply

The goal of this project is to create a low-noise, decoupled power supply to power sensitive instrumentation in experimental research laboratories. This power supply will turn 120 VAC wall power into clean, adjustable output DC power, as well as break potential ground loops by being decoupled from the wall power by an isolation barrier. 

This power supply was designed by Mark Carlson at UBC, and we are closely following his original schematics.

# Table of Contents 
- [Motivation](#Motivation)
- [Parts List](#Parts-List)
- [Schematic](#Schematic)
- [Testing](#Testing)
- [Outlook](#Outlook)
- [Acknowledgements](#Acknowledgements)


# Motivation

Low noise, ground-decoupled DC is important for powering ADC/DACs and preamplifiers without introducing noise to the extremely sensitive measurement signals in an experimental condensed matter lab. Currently, the options are a stock DC power supply and a battery power supply. It is possible to improve on the DC power supply in terms of noise level, and the battery (while having low noise) has to be charged and has an unpredictable and possibly dangerous failure mode.
<div align="center">
<img src="https://github.com/haristoyanov/decoupled-power/blob/2b456b787f344512048ab51aedb26e7b7332418c/Figures/Images%20for%20README/setup.png">
</div>
</div>
<br/>
<br/>


# Parts List 
Below is a list of all circuit parts used for this project, excluding the Printed Circuit Boards themselves, which were ordered from OSHpark. The PCB design and schematics are included in the PCB folder of this repository. 

<div align="center">
<img src="https://github.com/haristoyanov/decoupled-power/blob/2b456b787f344512048ab51aedb26e7b7332418c/Figures/Images%20for%20README/partslist.png">
</div>

<br/>
<br/>


# Schematic 

This summary explains the relevant parts of the circuit from left to right.
1. The transformer takes wall power (120V AC at 60Hz) and outputs 16V AC at 60 Hz. This is the input to the power supply.
2. The diodes rectify the current, so that the top branch always has positive voltage and the bottom branch always has negative voltage.
3. The positive and negative voltage regulator ICs (TL1963A and LM2991, respectively) are supplied by the rectified AC, and decoupled using the capacitors to ground (filtering high-frequency noise and preventing output coupling to spikes or dips in the input AC). These output a DC voltage, with a shutdown (SHDN) indicator to show if they are working.
4. The exact output voltage is determined by the voltage on the ADJ pin. The 13K/1K voltage divider sets an output voltage of ±16 V on each branch.
5. The second stage of the circuit is powered by the ±16V. The first component is the 10V voltage reference IC (REF102), which outputs a more precise DC voltage than a voltage regulator. However, it only allows small current draw.
6. To set the exact output voltage, the two op-amp ICs (which are powered from the ±16V DC) take the 10V input from the voltage reference and output a voltage set by the voltage divider consisting of R35 and R36. In the given schematic, this outputs 15V from the top branch and -15V from the bottom.
7. The second op-amp matches and inverts the output of the first, ensuring a linear relationship between the positive and negative output.
8. The two transistors (Q30 and Q31) allow for more current draw from the 16V supply. This current is limited by the voltage regulator ICs, which allow 1A of current to flow.
9. The output goes through an Ethernet-style connector, whose indicator lights indicate whether each branch is outputing a voltage.

<div align="center">
<img src="https://github.com/haristoyanov/decoupled-power/blob/2b456b787f344512048ab51aedb26e7b7332418c/Figures/Images%20for%20README/schematic.png">
</div>

# Testing

The first testing after confirming a ±15V DC output involved determining the Power Supply Rejection Ratio (PSRR), which describes how well the power supply attenuates noise at a frequency of interest. The PSRR is defined as the 20 times the logarithm of the input to output voltage ripple ratio at 60 Hz. As such, an ideal DC power supply has an infinite PSRR.

<div align="center">
<img src="https://github.com/haristoyanov/decoupled-power/blob/2b456b787f344512048ab51aedb26e7b7332418c/Figures/Images%20for%20README/testsetup.png">
</div>

The testing was conducted through a capacitor to the analog input of a Stanford Research Systems SR1 spectrum analyzer.



Preliminary results indicate a power supply rejection ratio (from 120V AC wall power) of approximately 160. This compares to roughly 100 for the DC power supply that is currently used (Acopian TD15-40, estimated from the voltage ripple quoted in its datasheet). Below is a graph of root-mean-squared Voltage versus frequency on logarithmic axes for a narrow range of frequencies around 60 Hz. We used the data displayed in this plot to calculate our PSRR. 

<div align="center">
<img src="https://github.com/haristoyanov/decoupled-power/blob/5cff1c346d4bc823e72a9731822f1c751b559a75/Figures/Images%20for%20README/narrow.png">
</div>

<br />
<br />
It is also of interest to examine the performance of our power supply at a wide range of frequencies. Below is a plot of the voltage noise spectral density (V/rtHz) against the frequency (Hz) on logarithmic axes for a frequency range of 0 Hz to 1500 Hz. To get the total voltage noise in a certain bandwidth, one must integrate the square of the spectral density across that bandwidth and then take the square root of the result. After performing a rough integration across a bandwidth ranging from 10 Hz to 1500 Hz using the method described above, we found that the total voltage noise was reduced by a factor of approximately 100,000.

<div align="center">
<img src="https://github.com/haristoyanov/decoupled-power/blob/2b456b787f344512048ab51aedb26e7b7332418c/Figures/Images%20for%20README/widesweep.png">
</div>

<br />
<br />

More figures and the code used to analyze this data can be found in the appropriately named folders of this repository. 

# Outlook
We will machine protective boxes for convenience. Also, we will try to implement potentiometers to create an adjustable output.

# Acknowledgements
Thank you to the instructors, TAs, and our classmates for UCSB PHYS 13CL/CS15C, thank you to the Dr. Young and all the Young lab grad students and postdocs that helped us, and thank you to Dr. Folk and Mark Carlson at UBC for the schematics and designs.

