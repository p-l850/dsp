import numpy as np
import matplotlib.pyplot as plt

n=np.arange(1,20,1)
y=np.exp(n)
plt.stem(y)
plt.show()