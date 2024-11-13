import numpy as np
import matplotlib.pyplot as plt

x=np.array(input("Enter the sequece").split(",")).astype(int)
h=np.array(input("Enter the sequence").split(",")).astype(int)
row=len(h)
column=len(x)+len(h)-1
if column>len(h):
    z=np.zeros(column-len(h))
    h=np.concatenate(h,z)
toeplitz=h
for i in range(row-1):
    h=np.roll(h,1)
    toeplitz=np.concatenate((toeplitz,h))
toeplitz.shape=(row,column)
toeplitz=np.transpose(toeplitz)
print("Output",np.dot(toeplitz,x).astype(int))