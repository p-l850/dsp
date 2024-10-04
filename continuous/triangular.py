import numpy as np
import matplotlib.pyplot as plt
a=np.arange(6)
b=np.arange(4,0,-1.1)
y=np.concatenate([a,b])
plt.plot(y)
plt.show()