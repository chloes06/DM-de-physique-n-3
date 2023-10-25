import numpy as np
import matplotlib.pyplot as plt
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
x=[ ]
z=[ ]
x.append(x0)
z.append(z0)
vx=v0x
vz=v0z
ax=0.
az=-g
diffx=[ ]
diffz=[ ]
xth=v0x*t[0]
zth=-g*t[0]**2/2+v0z*t[0]
diffx.append(x[0]-xth)
diffz.append(z[0]-zth)
for i in range(0, n-1 ):
 x.append(x[i]+vx*deltat)
 z.append(z[i]+vz*deltat)
 vx = vx+ax*deltat
 vz =vz+az*deltat
 xth=v0x*t[i+1]
 zth=-g*(t[i+1]**2)/2.+v0z*t[i+1]
 diffx.append(x[i+1]-xth)
 diffz.append(z[i+1]-zth)

plt.subplot(1,3,1)
plt.plot(x,z,'k',linewidth=2)
plt.xlabel("X (m)",size=15)
plt.ylabel("Z (m)",size=15)
plt.grid()
plt.show()
plt.subplot(1,3,2)
plt.plot(t,diffx,'k',linewidth=2)
plt.xlabel("temps (s)",size=15)
plt.ylabel("X-Xth",size=15)
plt.grid()
plt.show()
plt.subplot(1,3,3)
plt.plot(t,diffz,'k',linewidth=2)
plt.xlabel("temps (s)",size=15)
plt.ylabel("Z-Zth",size=15)
plt.grid()
plt.show() 