import numpy as np 
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 100)
f = 1 #1Hz

plt.plot(t, 1*np.sin(2*np.pi*f*t+0),"-", label='sin(2$\pi$ft)')
plt.plot(t, 0.7*np.sin(2*np.pi*f*t-1), ls="--", label='0.7sin(2$\pi$ft-1)')

plt.xlabel("Time")
plt.title("Sine Wave")
plt.legend()
plt.grid()
plt.show()
