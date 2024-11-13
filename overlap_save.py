import numpy as np
x=np.array(input("Enter x(n)").split(",")).astype(int)
h=np.array(input("Enter h(n)").split(",")).astype(int)
L=int(input("Enter L"))
M=len(h)
Ls=L+M-1
x_padded=np.concatenate(np.zeros(0,(M-1)),x)
h_padded=np.concatenate(h,np.zeros(0,(Ls-M)))
for i in range(0,len(x_padded),Ls):
    x_segment=x_padded[i:i+Ls]
    conv_result=np.convolve(x_padded,h_padded)
    y.extend(conv_result[M-1:Ls])
y=np.array(y[:len(x)+M-1])
print("Output signal:",y)