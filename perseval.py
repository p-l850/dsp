import numpy as np
import cmath as cm
x=np.array(input("Enter X(n)").split(",")).astype(int)
W=[]
j=cm.sqrt(-1)
N=len(x)
#for k in range(N):
#    a=0
#    for n in range(N):
#        a=cm.exp((-1j)*2*np.pi*k*n/N)
#        a=np.around(a,0)
#        W.append(a)
#w=np.array(W).reshape(N,N)
#X=np.dot(x,w)
X=np.fft.fft(x)
lhs=np.sum((abs(x))**2)
print(lhs)
rhs=np.sum((abs(X))**2)/N
print(rhs)
if lhs==rhs:
    print("perseval's theorem proved")