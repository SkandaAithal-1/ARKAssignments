import numpy as np
import matplotlib.pyplot as plt

scan = np.loadtxt('laserscan.dat')
angle = np.linspace(-np.pi/2, np.pi/2, np.shape(scan)[0], endpoint='true')

Tr = np.array([[1/np.sqrt(2), -1/np.sqrt(2), 1],[1/np.sqrt(2), 1/np.sqrt(2), 0.5],[0, 0, 1]])
Tc = np.array([[-1, 0, 0.2],[0, -1, 0],[0, 0, 1]])
#plt.subplot()
'''plt.axes(projection = 'polar')
for i in range(np.shape(scan)[0]):
    plt.polar(angle[i], scan[i], 'g.')
plt.show()'''

tranScan = np.array([scan*np.cos(angle), scan*np.sin(angle)])
transRPoints = np.zeros(tranScan.shape)  #Points after transformation using Tc. Points with respect to the Robot's Frame of Reference
transGPoints = np.zeros(tranScan.shape) # Points with respect to Global frame of reference.
laser = np.matmul(Tr, Tc)
for i in range(tranScan.shape[1]):
    transRPoints[:,i] = np.matmul(Tc, np.array([tranScan[0,i], tranScan[1,i], 1]))[:2]

for i in range(tranScan.shape[1]):
    transGPoints[:,i] = np.matmul(Tr, np.array([transRPoints[0,i], transRPoints[1,i],1]))[:2]

plt.figure()
plt.plot(1, 0.5, 'r+') #Robot in red
plt.plot(laser[0,2], laser[1,2], 'b+') #Laser in blue
plt.plot(transGPoints[0], transGPoints[1], '.k')
plt.gca().set_aspect('equal')
plt.show()