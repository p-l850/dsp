import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-10,10,0.1)
y=np.copy(t)
y[t<0]=0
plt.plot(t,y)
plt.show()