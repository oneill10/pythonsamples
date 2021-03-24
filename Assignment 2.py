#!/usr/bin/env python
# coding: utf-8

# Young's Twin Slit Experiment
# -------
# #### By Orla O'Neill 
# #### 18314251
# 
# This code considers Young's twin slit experiment. This experiment is governed by the following equation:
# 
# $$I=I_0[\frac{sin(\alpha)}{\alpha}]^2[cos(\beta)]^2$$
# $$\alpha=\frac{\pi a}{\lambda}sin\theta , \beta=\frac{\pi d}{\lambda}sin\theta$$
# 
# Where $I_0$ is the initial intensity, a is the width of one slit, d is the distance between the slits, L is the distance between the slits and the screen and $\lambda$ is the wavelenght of the light.
# 
# ##### Task 1:
# The code plots the intensity pattern $\frac{I}{I_0}$ of light observed from two slits to create a 1D image.
# ##### Task 2:
# A second plot is added to the first. This one plots the pattern as if there was one slit.
# ##### Task 3:
# This part makes the 1D plot into a 2D plot that resembles the apperence of the viewing card in the experiment.
# ##### Task 4:
# Finally, the 2D plot is editted so that it incorperates the fall off of the diffraction pattern as it moves away from the horizontal axis.

# In[2]:


#imports
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


#task 1

#setting parameters
a=0.09 #mm
L=480 #mm
d=0.4 #mm
lamb=0.000670 #mm

N=2500
y=np.linspace(-8,8,N)

def findII0(y,a,L,d,lamb):

    #calculating theta
    theta=np.arctan(abs(y)/L)

    #calculating alpha and beta
    alpha=np.pi*a*np.sin(theta)/lamb
    beta=np.pi*d*np.sin(theta)/lamb

    #calculating I/I0
    IoverI0=((np.sin(alpha)/alpha)**2)*((np.cos(beta))**2)
        
    return IoverI0

IoverI01=findII0(y,a,L,d,lamb)

#plotting I/I0
plt.plot(y,IoverI01)
plt.title("Two-slit interference pattern")
plt.xlabel("Distance from the slit to the screen in mm")
plt.ylabel("I/I0")
plt.show()


# In[4]:


#task 2

#same calculation but let d=0
IoverI02=findII0(y,a,L,0,lamb)

#plot code
plt.plot(y,IoverI01)
plt.plot(y,IoverI02)
plt.legend(["Two slits","One slit"])
plt.title("Interference pattern for one slit and two slits")
plt.xlabel("Distance from the slit to the screen (mm)")
plt.ylabel("I/I0")
plt.show()


# In[26]:


#task 3

#make I/I0 and the distnace into a grid
x_1,y_1=np.meshgrid(IoverI01,y)

#plot the gird to show the intereference pattern
plt.imshow(x_1,cmap="inferno")

#plot code
plt.ylim(0,1500)
plt.xlim(250,2250)
plt.title("Task 3: Young's slits interference pattern")
plt.xlabel("Distance from slits to screen (mm)")
plt.ylabel("Height of screen (mm)")
plt.show()


# In[28]:


#task 4

#finding the fall off of the diffraction pattern
theta=np.arctan(abs(y)/L)
alpha=np.pi*0.2*np.sin(theta)/lamb
IoverI04=(np.sin(alpha)/alpha)**2

#adding the fall off to the plot in the last part
z=np.array([i**2+j**2 for j in IoverI04 for i in IoverI01])
Z=z.reshape(N,N)

#plot code
plt.imshow(Z,cmap="inferno")
plt.ylim(1000,1500)
plt.xlim(900,1600)
plt.title("Task 4: Young's slits interference pattern adjusted")
plt.xlabel("Distance from slits to screen (mm)")
plt.ylabel("Height of screen (mm)")
plt.show()

