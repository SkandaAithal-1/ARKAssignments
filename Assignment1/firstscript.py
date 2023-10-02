import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = np.cos(x)*np.exp(x)
    return y

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = f(x)

plt.figure(num=0)

plt.plot(x, y)
#plt.show()
plt.savefig("Assignment1.png")