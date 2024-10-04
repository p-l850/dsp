import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,1,0.01)
f=float(input("Enter the frequency"))
y=np.cos(2*np.pi*f*t)
plt.plot(t,y)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()