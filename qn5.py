import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dft(x):
#    N=len(x)
#    j=cm.sqrt(-1)
#    X=np.zeros(N,dtype='complex')
#    W=[]
#    for k in range(N):
#        a=0
#        for n in range(N):
#            a=cm.exp((-j)*2*np.pi*n*k/N)
#            a=np.around(a,0)
#            W.append(a)
#    w=np.array(W).reshape(N,N)
#    X=np.dot(x,w)
    X=np.fft.fft(x)
    return X
t=np.linspace(0,1,100)
y1=np.sin(2*np.pi*100.0*t)
y2=np.sin(2*np.pi*1000.0*t)
plt.subplot(2,1,1)
plt.plot(t,y1)
plt.subplot(2,1,2)
plt.plot(t,y2)
plt.show()
N1=len(y1)
N2=len(y2)
N=N1+N2-1
x1=np.pad(y1,(0,N-N1))
x2=np.pad(y2,(0,N-N2))
a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
x3=a*x1
x4=b*x2
x_lhs=(x3)+(x4)
print("LHS",np.trim_zeros(dft(x_lhs)))
X3=dft(x1)
X4=dft(x2)
x_rhs=a*X3+b*X4
print("RHS",np.trim_zeros(x_rhs))
np.fft.ifft(x)