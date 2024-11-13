import numpy as np
x=np.array(input("enter x(n):").split(",")).astype(int)
h=np.array(input("enter h(n):").split(",")).astype(int)
hn=h
row=len(x)
column=len(x)+len(h)-1
if len(h)<column:
    z=np.zeros(column-len(h))
    h=np.concatenate((h,z))
toeplitz=h
for i in range (1,row):
    h=np.roll(h,1)
    h[0:i]=0
    toeplitz=np.concatenate((toeplitz,h))
toeplitz=toeplitz.reshape(row,column)
toeplitz=np.transpose(toeplitz)
print("toeplitz is:",toeplitz)

print("Output sequence:",np.dot(toeplitz,x).astype(int))
print("Using Convolve:",np.convolve(x,hn))