# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:29:25 2021

@author: edwar
"""
import matplotlib.pyplot as plt 
import numpy as np
import math

g=9.81 
dt=1e-3
v0=40
angle= math.pi/4
height = 100
Y = 0.005

time=np.arange(0,10,dt)
vx0=math.cos(angle)*v0
vy0=math.sin(angle)*v0

def traj_friction(angle,v0):
    vx0=math.cos(angle)*v0
    vy0=math.sin(angle)*v0
    x=np.zeros(len(time))
    y=np.zeros(len(time))
    x[0],y[0]=0,0
    x[1],y[1]=x[0]+vx0*dt,y[0]+vy0*dt

    i=1
    while y[i]>=0:
        f = 0.5*Y*(height-y[i])*dt
        x[i+1]=(2*x[i]-x[i-1]+f*x[i-1])/(1+f)
        y[i+1]=(2*y[i]-y[i-1]+f*y[i-1]-g*dt**2)/(1+f)
    
        i += 1

    x=x[0:i+1]
    y=y[0:i+1]
    
    return x,y,(dt*i),x[i],

x, y, duration, distance = traj_friction(angle,v0)


print ("Distance:", distance)
print ('Duration:', duration)

fig1=plt.figure()
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()



n=395
angles=np.linspace(0,math.pi/2,n)
maxrange=np.zeros(n)

for i in range(n):
    x,y,duration,maxrange[i] = traj_friction(angles[i],v0)
angles=angles/2/math.pi*360


fig1=plt.figure()
plt.plot(angles,maxrange)
plt.xlabel("angle")
plt.ylabel("range")
plt.show()


print ("Optimum Angle",angles[np.where(maxrange==np.max(maxrange))])




