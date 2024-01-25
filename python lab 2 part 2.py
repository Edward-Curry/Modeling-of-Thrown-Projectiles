# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 14:57:56 2021

@author: ecurry
"""

import matplotlib.pyplot as plt 
import numpy as np
import math 

g=9.81 
dt=1e-3
v0=40
angle=math.pi/4

time=np.arange(0,10,dt)
vx0=math.cos(angle)*v0
vy0=math.sin(angle)*v0

xa=vx0*time
ya=-0.5*g*time**2+vy0*time
fig1=plt.figure()
plt.plot(xa,ya)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

def traj(angle,v0):
    vx0=math.cos(angle)*v0
    vy0=math.sin(angle)*v0
    x=np.zeros(len(time))
    y=np.zeros(len(time))
    x[0],y[0]=0,0
    x[1],y[1]=x[0]+vx0*dt,y[0]+vy0*dt

    i=1
    while y[i]>=0:
        x[i+1]=(2*x[i]-x[i-1])
        y[i+1]=(2*y[i]-y[i-1])-g*dt**2
    
        i += 1

    x=x[0:i+1]
    y=y[0:i+1]
    return x,y,(dt*i),x[i]



x, y, duration, distance = traj(angle,v0)
print ("Distance:", distance)
print ('Duration:', duration)

x,y,duration,distance = traj(angle,v0)

n=395
angles=np.linspace(0,math.pi/2,n)
maxrange=np.zeros(n)

for i in range(n):
    x,y,duration,maxrange[i] = traj(angles[i],v0)
angles=angles/2/math.pi*360


fig1=plt.figure()
plt.plot(angles,maxrange)
plt.xlabel("angle")
plt.ylabel("range")
plt.show()


print ("Optimum Angle",angles[np.where(maxrange==np.max(maxrange))])




n=395
vi=np.linspace(0,40,n)
maxrange=np.zeros(n)

for i in range(n):
    x,y,duration,maxrange[i] = traj(angle,vi[i])


fig1=plt.figure()
plt.plot(vi,maxrange)
plt.xlabel("initial velocity")
plt.ylabel("maxrange")
plt.show()









