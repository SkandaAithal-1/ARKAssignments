import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(loc=5.0, scale=2.0, size=100000)
y = np.random.uniform(low=0, high=10, size=100000)

'''
To generate the same numbers everytime :
state = np.random.RandomState(123234)
x = state.normal(loc=5.0, scale=2.0, size=100000)
y = state.uniform(low=0, high=10, size=100000)
'''

xMean = np.mean(x)
xStd = np.std(x)
yMean = np.mean(y)
yStd = np.std(y)

'''
The mean and standard deviation in case of x are expected to be 5 and 2
'''

print(f"Mean of x is {xMean}, Standard Deviation of x is {xStd}")

'''
The mean in case of y is expected to be 5
'''

print(f"Mean of y is {yMean}, Standard Deviation of y is {yStd}")

'''
The output is around the expected values.
'''

plt.figure(num=0)
plt.hist(x, bins=1000)
plt.show()