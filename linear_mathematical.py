import numpy as np
x=np.array(input("Enter elements of input sequence").split(",")).astype(int)
h=np.array(input("Enter elements of impulse response").split(",")).astype(int)
xn=x
hn=h
total=len(x)+len(h)-1
y=np.zeros(total)
if len(x)<len(h):
    (x,h)=(h,x)
if len(x)!=len(h):
    if len(x)>len(h):
        z=np.zeros(len(x)-len(h)).astype(int)
        h=np.concatenate((h,z))
size=len(x)
for n in range(total):
    sum=0
    for k in range(size):
        w=n-k
        if(w<0) or (w>size-1):
            sum+=0
        else:
            sum+=x[k]*h[w]
        y[n]=sum
print("linear convolution using mathematical expression:",y.astype(int))
print("Numpy.convolve:",np.convolve(xn,hn))