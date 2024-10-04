import numpy as np
import matplotlib.pyplot as plt

n=np.arange(0,1,0.01)
f=float(input("Enter the frequency"))
y=np.cos(2*np.pi*f*n)
plt.stem(y)
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.show()