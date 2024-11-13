import numpy as np
x=np.array(input("Enter x").split(",")).astype(int)
h=np.array(input("Enter h").split(",")).astyep(int)
L=int(input("Enter L"))
Lx=len(x)
M=len(h)
Ls=Lx+M-1
y=np.zeros(Ls)
for i in range(0,Lx,L):
    x_block=x[i:i+L]
    X_padded=np.pad(x_block,y[(0,(M-1))])
    y_block=np.convolve(x_block,h)
    y[i:i+len(y_block)]+=y_block[:min(len(y)-i,len(y_block))]
print(y)