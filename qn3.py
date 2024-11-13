import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,1,0.01)
y=np.sin(2*np.pi*100*t)
plt.plot(t,y)
plt.show()