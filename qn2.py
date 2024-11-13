import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
a=np.linspace(0,100,10)
x1=np.exp(-10*a)
x2=np.roll(x1,2)
x3=np.flip(x2)
x=x1
h=x3
#row=len(x)
#column=len(x)+len(h)-1
#if len(h)<column:
#    z=np.zeros(column-len(h))
#    h=np.concatenate((h,z))
#toeplitz=h
#for i in range(row-1):
#    h=np.roll(h,1)
#    toeplitz=np.concatenate(toeplitz,h)
#toeplitz.shape=(row,column)
#toeplitz=np.transpose(toeplitz)
#convolution=toeplitz
convolution=np.convolve(x,h)
convolution_time = np.linspace(0, 200, len(convolution))
plt.plot(convolution_time, convolution)

#plt.plot(convolution,a)
plt.show()