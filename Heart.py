import matplotlib.pyplot as plt
import scipy as np

x=np.linspace(-2,2,1000)
y3=np.real(np.sqrt(abs(x)*(1-abs(x))))
y4=np.real(-np.sqrt(1-np.sqrt(abs(x))))
plt.plot(x,y3,color="red")
plt.plot(x,y4,color="red")
plt.xlim([-2,2])
plt.show()
