import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-10,10,0.01)
y=np.zeros(len(t))
y[t>=0]=1
plt.plot(t,y)
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.show()