import numpy as np
x=np.array(input("Enter input matrix").split(",")).astype(int)
h=np.array(input("Enter the impulse response").split(",")).astype(int)
M=len(h)
L=int(input("Enter block size"))
N=L+M-1
x_padded=np.concatenate(np.zeros(M-1),x)
h_padded=np.concatenate(h,np.zeros(N-M))
y=[]
for i in range(0,len(x.padded),L):
    x_segment=x_padded[i:i+N]
    conv_result=np.convolve(x_segment,h_padded)
    y.extend(conv_result[M-1:N])
y=np.array(y[:len(x)+M-1])
print("Output Sequence:",y)