import numpy as np
import matplotlib.pyplot as plt

n=np.arange(0,0.5,0.01)
f=float(input("Enter the frequency"))
y=np.sin(2*np.pi*f*n)
plt.stem(y)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()