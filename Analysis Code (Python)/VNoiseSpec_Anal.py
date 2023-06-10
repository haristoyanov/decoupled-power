#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['science','notebook'])

# VrtHz data from drive

VrtHz_in1 = np.loadtxt('0602inputwide.TXT', delimiter = ',')
VrtHz_out1 = np.loadtxt('0602outputwide.TXT', delimiter = ',')
VrtHz_ref1 = np.loadtxt('0602noisefloorSR.TXT', delimiter = ',')


# converting to plot-able arrays

f_in = []
VrtHz_in=[]

f_out=[]
VrtHz_out=[]

f_ref=[]
VrtHz_ref=[]

for i in VrtHz_in1:
    f_in.append(i[0])
    VrtHz_in.append(i[1])
    
for j in VrtHz_out1:
    f_out.append(j[0])
    VrtHz_out.append(j[1])
    
for k in VrtHz_ref1:
    f_ref.append(k[0])
    VrtHz_ref.append(k[1])
    
# cutting off at 1.5 kHz because noise is at floor above

f_in, VrtHz_in, f_out,VrtHz_out,f_ref,VrtHz_ref = f_in[0:1500],VrtHz_in[0:1500], f_out[0:1500],VrtHz_out[0:1500],f_ref[0:1500],VrtHz_ref[0:1500]

# treating for the noise floor of our spectrum analyzer (about 10nV/rtHz)
f_ref = np.array(VrtHz_ref)
VrtHz_ref = np.array(VrtHz_ref)
f_in = np.array(f_in)
VrtHz_in = np.array(VrtHz_in)
f_out = np.array(f_out)
VrtHz_out = np.array(VrtHz_out)

VrtHz_in= VrtHz_in-VrtHz_ref
VrtHz_out = VrtHz_out-VrtHz_ref

# plotting our data

plt.plot(f_in,VrtHz_in,label = 'input voltage noise')
plt.plot(f_out,VrtHz_out,label='output voltage noise' )
plt.loglog()
plt.legend()
plt.xlabel('frequency(Hz)')
plt.ylabel('Voltage noise (V/rtHz)')

# integrating to the find **rough estimate** of total voltage noise
# did not include the first 10 Hz because not interested in very low f for our lab


f_in_sq = f_in[10:1500]
VrtHz_in_sq = VrtHz_in[10:1500]**2
VrtHz_out_sq = VrtHz_out[10:1500]**2

i = 0
sum_in = 0
sum_out = 0
while (i<len(f_in_sq)-1):
    sum_in = sum_in + (f_in[i+1]-f_in[i])*(0.5*(VrtHz_in_sq[i+1] + VrtHz_in_sq[i]))
    sum_out = sum_out + (f_in[i+1]-f_in[i])*(0.5*(VrtHz_out_sq[i+1] + VrtHz_out_sq[i]))
    i+=1

# subtracting the peaks aroud 60 Hz because that is not voltage noise but rather signal
## **rough** estimate of peak as 20 Hz bandwidth around 60 Hz for input spectrum
    
f_in_5565 = f_in[50:70]
VrtHz_in_sq_5565 = VrtHz_in[50:70]**2
VrtHz_out_sq_5565 = VrtHz_out[50:70]**2

sum_5565_in = 0
sum_5565_out = 0
j = 0

while (j<len(f_in_5565)-1):
    sum_5565_in = sum_5565_in + (f_in_5565[j+1]-f_in_5565[j])*(0.5*(VrtHz_in_sq_5565[j+1] + VrtHz_in_sq_5565[j]))
    sum_5565_out = sum_5565_out + (f_in_5565[j+1]-f_in_5565[j])*(0.5*(VrtHz_out_sq_5565[j+1] + VrtHz_out_sq_5565[j]))
    j+=1

sum_in1 = sum_in - sum_5565_in
sum_out1 = sum_out - sum_5565_out

# final calculation of total voltage noise

Vnoise_in_tot = np.sqrt(sum_in1)
Vnoise_out_tot = np.sqrt(sum_out)

print(Vnoise_in_tot,Vnoise_out_tot, Vnoise_in_tot/V_noise_out_tot)





