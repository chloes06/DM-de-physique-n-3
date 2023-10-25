import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
g=9.81
v0=300.
alpha=45.
v0x=v0*np.cos(np.pi*alpha/180.)
v0z=v0*np.sin(np.pi*alpha/180.)
x0=0.
z0=0.
ti=0.
tf=2*v0*np.sin(np.pi*alpha/180.)/g
n=1000
deltat=(tf-ti)/(n-1)
t=[ ]

t = np.linspace(ti,tf,n)
def SecondMembre(Y,t):
 x = Y[0]
 z = Y[1]
 vx = Y[2]
 vz = Y[3]
 dxdt = vx
 dzdt = vz
 dvxdt = 0
 dvzdt = -g
 return[dxdt,dzdt,dvxdt,dvzdt]
CondInit=np.array([x0,z0,v0x,v0z])

Ys=odeint(SecondMembre,CondInit,t)
x=Ys[:,0]
z=Ys[:,1]
diffx=[ ]
diffz=[ ]
for i in range(0,n):
 xth=v0x*t[i]
 zth=-g*t[i]**2/2+v0z*t[i]
 diffx.append(x[i]-xth)
 diffz.append(z[i]-zth)

 plt.subplot(1, 4, 1)
 plt.plot(t, x, 'k', linewidth=2)
 plt.xlabel("temps (s)", size=15)
 plt.ylabel("X", size=15)
 plt.grid()
 plt.show()
 plt.subplot(1, 4, 2)
 plt.plot(t, z, 'k', linewidth=2)
 plt.xlabel("temps (s)", size=15)
 plt.ylabel("Z", size=15)
 plt.grid()
 plt.show()
 plt.subplot(1, 4, 3)
 plt.plot(t, diffx, 'k', linewidth=2)
 plt.xlabel("temps (s)", size=15)
 plt.ylabel("Xnum-Xth", size=15)
 plt.grid()
 plt.show()
 plt.subplot(1, 4, 4)
 plt.plot(t, diffz, 'k', linewidth=2)
 plt.xlabel("temps (s)", size=15)
 plt.ylabel("Znum-Zth", size=15)
 plt.grid()
 plt.show()
 # plt.subplot(1,2,2)
 # plt.plot(x,vn,'k',linewidth=2)
 # plt.grid()
 # plt.show()
