import numpy as np
import matplotlib.pyplot as plt

t=np.arange(-10,10,0.01)
y=np.zeros(len(t))
w=float(input("enter the width"))
y[(t>-w/2)&(t<=0)]=1
y[(t<w/2)&(t>0)]=-1
plt.plot(y)
plt.show()