import numpy as np
import matplotlib.pyplot as plt

x1=np.array(input("Enter x1:").split(",")).astype(int)
x2=np.array(input("Enter x2:").split(",")).astype(int)
h=x1
x=x2
N1=len(x1)
N2=len(x2)
N=N1+N2-1
x1=np.pad(x1,(0,N-N1))
x2=np.pad(x2,(0,N-N2))
x3=np.zeros(N)
for i in range(N):
    sum=0
    for j in range(N):
        m=i-j+1
        if m<=0:
            m=N+m
        x3[i]+=x1[j]*x2[m-1]
print("Circular Convolution:",x3)
print("Normal",np.convolve(x1,x2))