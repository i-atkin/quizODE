#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 12:09:30 2022

@author: i_atkin
"""

## Import needed modules
from pylab import *
import scipy.constants as pc
import numpy as np 
w = 10 #set angular velocity
N = 1000 #number of points
x = np.zeros(N)
#starting position
x[0] = 0.3
v = np.zeros(N)
#starting velocity
v[0] = 100
#creating time array
t = np.linspace(0,1,N)
dt = t[1] - t[0]
#euler-cromer method
for n in range(1,N):
    a = -w**2*(x[n-1])
    v[n] = v[n-1] + a * dt
    x[n] = x[n-1] + v[n]*dt
   

figure(1)
clf()
plt.plot(t,x)
xlabel("Time (s)")
ylabel("Position")
figure(2)
clf()
plt.plot(x,v)
xlabel("Position")
ylabel("Velocity")
#conserving energy... I see a circular path ?
#I've been unable to make my trajectory unstable- no spiral pattern