import numpy as np
import matplotlib.pyplot as plt
## www.iiserkol.ac.in/~rajesh/my_python.html
N=100
x=np.linspace(-2*np.pi,2*np.pi, N)
y1= np.sin(x)
y2= np.cos(x)
y=y1*y1+y2*y2
plt.plot(x, y1, 'C0-', label='sin(x)')
plt.plot(x, y2, 'C1-', label='cos(x)')
plt.plot(x, y, 'C2--', linewidth=3, label='sin^2(x)+cos^2(x)')
plt.xlabel('Angle [Radian]')
plt.ylabel('F(x)')
plt.title('Plot of Trignometric Functions')
plt.legend()
plt.ylim([-1.2, 1.2])
plt.grid(alpha=0.3)
plt.show()

