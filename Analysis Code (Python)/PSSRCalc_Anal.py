#!/usr/bin/env python
# coding: utf-8

# importing necesary libraries

import numpy as np
import matplotlib.pyplot as plt
plt.style.use(['science','notebook'])


# loading Vrms data from drive

Vrms_in_narr = np.loadtxt('0602Vrmsinputnarrow.TXT', delimiter = ',')
Vrms_in_wide = np.loadtxt('0602Vrmsinputwide.TXT', delimiter = ',')
Vrms_out_narr = np.loadtxt('0602Vrmsoutputnarrow.TXT', delimiter = ',')
Vrms_out_wide = np.loadtxt('0602Vrmsoutputwide.TXT', delimiter = ',')

# converting to plot-able arrays

f_in_n = []
Vrms_in_n=[]

f_in_w =[]
Vrms_in_w=[]

f_out_n=[]
Vrms_out_n=[]

f_out_w=[]
Vrms_out_w=[]

for i in Vrms_in_narr:
    f_in_n.append(i[0])
    Vrms_in_n.append(i[1])
    
for j in Vrms_in_wide:
    f_in_w.append(j[0])
    Vrms_in_w.append(j[1])
    
for k in Vrms_out_narr:
    f_out_n.append(k[0])
    Vrms_out_n.append(k[1])

for l in Vrms_out_wide:
    f_out_w.append(l[0])
    Vrms_out_w.append(l[1])


# returns power supply rejection ratio, given V in and V out


def PSRR(Vin,Vout):  
    return 20*np.log10(Vin/Vout)


# plotting the data

plt.plot(f_in_n,Vrms_in_n, label = 'input')
plt.plot(f_out_n,Vrms_out_n,label = 'output')
plt.xlabel('frequency (Hz)')
plt.ylabel('rms voltage (V)')
plt.loglog()
plt.legend()


# calculating PSRR from data above

PSRR_60_ours = PSRR(np.max(Vrms_in_n),np.max(Vrms_out_n))
PSRR_60_acopian = PSRR(115,1.5e-3)

print(PSRR_ours,PSRR_acopium)


# graph of PSRR for whole range

PSRR_wide = []  # creating PSRR for wide sweep

i = 0
while (i<len(Vrms_in_w)):
    PSRR_wide.append(PSRR(Vrms_in_w[i],Vrms_out_w[i]))
    i+=1

plt.plot(f_in_w,PSRR_wide)
plt.ylabel('PSRR')
plt.xlabel('frequency (Hz)')
plt.loglog()







