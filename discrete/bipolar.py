import numpy as np
import matplotlib.pyplot as plt

n=np.arange(-10,10,1)
y=np.zeros(len(n))
w=float(input("Enter the width"))
y[(n>-w/2)&(n<=0)]=1
y[(n<w/2)&(n>0)]=-1
plt.stem(y)
plt.show()