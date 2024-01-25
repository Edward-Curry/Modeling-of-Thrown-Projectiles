# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import matplotlib.pyplot as plt 
import numpy as np
import math 

g=9.81 
dt=1e-3
v0=30
angle=math.pi/10

time=np.arange(0,10,dt) 	#making points for graph
vx0=math.cos(angle)*v0      # getting velovity in x and y direction
vy0=math.sin(angle)*v0

xa=vx0*time                    #plotting trajector x vs y
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
