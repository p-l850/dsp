import numpy as np
import matplotlib.pyplot as plt

n=np.arange(-10,10,1)
y=np.zeros(len(n))
y[n==0]=1
plt.stem(y)
plt.show()