import numpy as np
import matplotlib.pyplot as plt

n=np.arange(-10,10,1)
T=float(input("Enter the width"))
y=np.zeros(len(n))
y[np.all([(n>=-T/2),(n<=T/2)],axis=0)]=1
plt.stem(y)
plt.xticks(n)
plt.show()