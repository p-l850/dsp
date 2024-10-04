import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-10,10,0.1)
y=np.zeros(len(t))
T=float(input("Enter the width"))
y[np.all([(t>=-T/2),(t<=T/2)],axis=0)]=1
plt.plot(t,y)
plt.show()