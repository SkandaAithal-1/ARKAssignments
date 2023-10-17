import numpy as np
from normalFunction import normGenerator as ng
import matplotlib.pyplot as plt

def motionModel(x, u, alpha) -> list:
    sample1 = ng(mean=0, sigma=(alpha[0]*np.absolute(u[0])+alpha[1]*u[2]))
    sample2 = ng(mean=0, sigma=(alpha[2]*u[2]+alpha[3]*(np.absolute(u[0])+np.absolute(u[1]))))
    sample3 = ng(mean=0, sigma=alpha[0]*np.absolute(u[1])+alpha[1]*u[2])
    u1r1 = u[0] + sample1.sample()
    u1r3 = u[2] + sample2.sample()
    u1r2 = u[1] + sample3.sample()

    x_ = x[0] + u1r3*np.cos(x[2]+u1r1)
    y_ = x[1] + u1r3*np.sin(x[2]+u1r1)
    theta_ = x[2] + u1r1 + u1r2

    return [x_, y_, theta_]

def main():
    x = [2, 4, 0]
    u = [np.pi/2, 0, 1]
    alpha = [0.1, 0.1, 0.01, 0.01]
    results = []
    for i in range(5000):
        results.append(motionModel(x, u, alpha))
    results = np.array(results)
    
    results = results[:, :2]
    plt.scatter(results[:, 0], results[:, 1], s=0.1)
    plt.show()

if __name__ == "__main__":
    main()
