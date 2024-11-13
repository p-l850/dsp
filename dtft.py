n=np.arange(-5,6)
omega=np.linspace(-np.pi,np.pi,N)
for k in range(N):
    X_omega[k]=np.sum(x_n*np.exp(-1*j*omega[k]*n))
plt.plot(omega,np.abs(X_omega))