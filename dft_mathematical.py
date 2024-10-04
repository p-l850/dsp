import matplotlib.pyplot as plt
import cmath as cm
import numpy as np

x=np.array(input("Enter input elements:").split(",")).astype(int)
N=len(x)
X=np.zeros(len(x)).astype(complex)
j=cm.sqrt(-1)
for k in range(N):
    sum=0
    for n in range(N):
        a=x[n]*np.exp((-1*j*2*np.pi*k*n)/N)
        sum+=a
    X[k]=np.around(sum,3)
print("DFT using Mathematical eqn:",X)


X1=np.zeros().astype(complex)
W=[]
for k in range(N):
    a=0
    for n in range(N):
        a=np.exp((-1*j*2*np.pi*k*n)/N)
        W.append(a)
W=np.array(W).reshape(N,N)
X1=x.dot(W)
X1=np.around(X1,2)
print("DFT using Matrix Method: ",X1)
print("Twiddle Factor: \n",np.around(W,2))
