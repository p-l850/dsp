import numpy as np
x1=np.array(input("Enter the input element sequence:").split(",")).astype(int)
x2=np.array(input("Enter the input element sequence:").split(",")).astype(int)
x,h=x1,x2
if len(x1)<len(x2):
    (x1,x2)=(x2,x1)
N1=len(x1)
N2=len(x2)
N=len(x1)+len(x2)-1
x1=np.pad(x1,(0,N-N1))
x2=np.pad(x2,(0,N-N2))
x3=np.zeros(N)
for n in range(N):
    for m in range(N):
        x3[n]+=x1[m]*x2[n-m]
print("\nLinear Convolution")
print("Output Sequence by circular Convolution: ",x3)
print("Output Sequence by numpy.convolve: ",np.convolve(x,h))
