import numpy as np
import matplotlib.pyplot as plt

n=np.arange(-10,10,1)
y=np.copy(n)
y[n<0]=0
plt.stem(y)
plt.xticks(n)
plt.show()