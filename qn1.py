import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
x1=np.array(input("enter x").split(",")).astype(int)
x2=np.array(input("enter x").split(",")).astype(int)
N=5
X1=np.zeros(N)
W=[]
for k in range(N):
    a=0
    for n in range(N):
        a=cm.exp((-1j)*2*np.pi*k*n/N)
        a=np.around(a,0)
        W.append(a)
    w=np.array(W).reshape(N,N)
X1=np.dot(x1,w)
X=np.multiply(X1,X2)
W2=[]
for k in range(N):
    a=0
    for n in range(N):
        a=X*cm.exp((j)*2*np.pi*n*k/N)
        a=np.around(a,0)
        W2.append(a)
    w2=np.array(W2).resize(N,N)
x=np.dot(X,w2)
print("Circular convolution=IDFT of X",X)