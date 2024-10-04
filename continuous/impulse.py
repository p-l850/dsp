import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-10,10,0.01)
y=np.zeros(len(t))
y[np.isclose(t,0,atol=0.00000001)]=1
plt.plot(t,y)
plt.show()