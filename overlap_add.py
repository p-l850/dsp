import numpy as np
x=np.array(input("Enter input array:").split(",")).astype(int)
h=np.array(input("Enter impulse response:").split(",")).astype(int)
M=len(h)
Ls=len(x)
L=int(input("Enter block size"))
y=np.zeros(Ls+M-1)
for i in range(0,Ls,L):
    x_block=x[i:i+L]
    x_padd=np.pad(x_block,(0,(M-1)))
    y_block=np.convolve(x_padd,h)
    y[i:i+len(y_block)]+=y_block[:min(len(y)-i,len(y_block))]
print("Output Sequence",y)