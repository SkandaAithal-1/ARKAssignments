import numpy as np

def diffdrive(x, y, theta, vl, vr, t, l):
    if (vl!=vr):
        R = (l/2)*((vl+vr)/(vl-vr))
        w = (vl - vr)/l
        ICCx = x + R*np.sin(theta)
        ICCy = y - R*np.cos(theta)
        rotMat = np.array([[np.cos(w*t), -np.sin(w*t),0],[np.sin(w*t), np.cos(w*t),0],[0,0,1]])
        tempPos = np.array([x-ICCx, y-ICCy, 0])
        rotPos = np.matmul(rotMat, tempPos.T)
        rotPos += np.array([ICCx, ICCy, w*t]).T
        xN, yN, thetaN = rotPos[0], rotPos[1], rotPos[2]
    else:
        v = (vl+vr)/2
        xN = x + v*np.cos(theta)*t
        yN = y + v*np.sin(theta)*t
        thetaN = theta
    print(f"New position x, y, theta = {xN, yN, thetaN}")
    return xN, yN, thetaN

def command():
    vl = float(input("Enter vl : "))
    vr = float(input("Enter vr : "))
    t = float(input("Enter theta : "))
    return vl, vr, t

def main():
    l = 0.5
    x, y, theta = diffdrive(1.5, 2, np.pi/2, 0.3, 0.3, 3, l)
    x, y, theta = diffdrive(x, y, theta, 0.1, -0.1, 1, l)
    x, y, theta = diffdrive(x, y, theta, 0.2, 0, 2, l)
    
    op = int(input("Do you want to give more commands[0/1] : "))
    while (op==1):
        vl, vr, t = command()
        x, y, theta = diffdrive(x, y, theta, vl, vr, t, l)
        op = int(input("Do you want to give more commands[0/1] : ")) 


if __name__ == "__main__":
    main()
