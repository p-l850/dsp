import numpy as np
def ff1(x):
    N=len(x)
    W=[]
    x1=np.zeros(N).astype(int)
    for k in range (N):
        a=0
        for n in range (l):
            a=np.exp((-2j*np.pi*n*k)/N)
            W.append(a)
    w=np.array(w).reshape(l,l)
    x1=np.dot(x,w)
    x1=np.around(x1,2)
    return x1
def fft(x):
    N=len(x)
    if N<=1:
        return x

    even=ff1(x[::2])
    odd=ff1(x[1::2])

    twiddle=np.exp(-2*j*np.pi*np.arange(N)/N)
    return np.concatenate([even+twiddle[:N//2]*odd,even+twiddle[N//2:]*odd])

r=[1,2,3,4,5,6,7,8]
y=ff1(r)
print(y)
