#!/usr/bin/env python
# coding: utf-8

# Rayleigh-Jeans law
# --------
# #### By Orla O'Neill, 18314251 
# 
# This program considers the Rayleigh-Jeans law and Planck's function for the spectrum of a Blackbody:
# 
# Rayleigh-Jeans law:
# $$U(v,T)=\frac{8 \pi v^2}{c^3}kT$$
# Planck's Law:
# $$U(v,T)=\frac{8 \pi hv^3}{c^3}\frac{1}{e^{\frac{hv}{kT}}-1}$$
# 
# Where U is the energy density in $Jm^{-3}$, k is the Boltzmann constant (1.380649x$10^{-23}JK^{-1}$), v is the frequency in Hz, c is the speed of light (3x10$^8 ms^{-1}$), h is Plank's constant (6.626x10^${-34}$Js) and T is the temperature in K.
# 
# First the program will be able to calculate U from inputted values using Rayleigh-Jeans law. Then it will plot U over a number of frequencies at T=2000K.
# 
# Then it will plot Planck's law over multiple frequencies for different values of temperature.
# 
# After that, it will verify Wien’s displacement law from the previous graphs. This law states that the product of the maximum wavelenght and the temperature is a constant.
# 
# Finally, it will carry out a numerical intergration of Planck's law and show that this area is proportional to $T^4$ as is seen in Stefan-Boltzmann law.

# In[1]:


#importing necessary packages
import matplotlib.pyplot as plt
import numpy as np


# #### Part 1
# This program will ask you to input values for v and T. It will then use these values to calculate U with Rayleigh-Jeans law for the spectrum of a Blackbody, as printed above. It has been tested with the values $v=10^{12}$Hz and T=2000K

# In[2]:


#task 1:print the value of U(ν,T)

#contants
k=1.38*(10**(-23)) #J/K
c=3*(10**8) #m/s

#Calculating U
def U(v,t):
    u=(8*k*t*np.pi*v**2)/c**3
    return u #W/m

#inputs 
V=int(input("What is your value for v in Hz? ")) #Hz
T=int(input("What is your value for T in K? ")) #K

#results
u=U(V,T)
print("U =",u,"J/m^3")


# #### Part 2
# This program plots the Rayleigh-Jeans law over a range of frequencies. It uses the range $v=10^{11}$ to $v=10^{15}$ and T=2000K. It is a log graph so that it becomes a straight line graph.

# In[3]:


#task 2: plot the Rayleigh-Jeans law over a range of frequecies

#as it was hard for my laptop to handle large numbers, I created these varibles so I could easily change them to see what works
a=10**11 #lowest value of v
b=10**15 #highest value of v
n=1000000 #number points on plot

V=np.linspace(a,b,n) #frequency range in Hz
T=2000 #K

#calculating U
u=np.zeros(n)
for i in range(n):
    u[i]=U(V[i],T) #Jm^-3
    
#plot code
plt.plot(np.log(V),np.log(u)) #calculating the log of frequency and E density before plotting it
plt.title("Rayleigh-Jeans Law")
plt.xlabel("log(v)")
plt.ylabel("log(U)")
plt.show()


# #### Task 3
# This program plots Planck's law for multiple temperatures, using the same frequency range as above, 10$^{11}$ to 10$^{15}$.
# $$U(v,T)=\frac{8 \pi hv^3}{c^3}\frac{1}{e^{\frac{hv}{kT}}-1}$$

# In[4]:


#task 3: plot of Planck’s function

h=6.63*(10**(-34)) #Js

#calculating U
def planck(v,T):
    u=(8*np.pi*h*(v**3))/(c**3)*(1/(np.exp((h*v)/(k*T))-1)) #Plank's law formula
    return u

#T=2000K
U=np.zeros(n)
for i in range(n):
    U[i]=planck(V[i],2000)
plt.plot(V,U)

#T=3000K
W=np.zeros(n)
for i in range(n):
    W[i]=planck(V[i],3000)
plt.plot(V,W)

#T=4000K
X=np.zeros(n)
for i in range(n):
    X[i]=planck(V[i],4000)
plt.plot(V,X)

#T=5000K
Y=np.zeros(n)
for i in range(n):
    Y[i]=planck(V[i],5000)
plt.plot(V,Y)

#T=6000K
Z=np.zeros(n)
for i in range(n):
    Z[i]=planck(V[i],6000)
plt.plot(V,Z)

#plot code
plt.title("Plank's law")
plt.xlabel("Frequency Hz")
plt.ylabel("Energy Density J/m^3")
plt.legend(["T=2000K","T=3000K","T=4000K","T=5000K","T=6000K"], loc=4)
plt.show()


# #### Part 4
# This program finds the peak energy density for each value of temperature from the previous part. It then uses this to find $\lambda_{max}$, the frequency corresponding to the peak energy density. 
# It then uses $\lambda_{max}$ to verify Wien's displacement law:
# $$\lambda_{max}T=constant$$
# The program finishes by printing this product for all values of T. As these products are of the same value, Wien's dispalcement law is verified.

# In[5]:


#task 4: find the peak of the Planck function for each temperature

#function to find max frequency
def Wien(E,T):
    Emax=np.max(E) #finding highest value of U, energy density
    i=np.where(E==Emax) #finding postivition of max U in the array
    f=V[i] #finding frequency that corresponds to max U
    l=c/f #calculating for lambda
    return l*T #multiplying lambda by T to get Wien's constant

#calculating constant
c1=float(Wien(U,2000))
c2=float(Wien(W,3000))
c3=float(Wien(X,4000))
c4=float(Wien(Y,5000))
c5=float(Wien(Z,6000))

#results
print("Wien's dispalcement constant is calculated to be:")
print("{0:6.8f} mK at T=2000K.".format(c1))
print("{0:6.8f} mK at T=2000K.".format(c2))
print("{0:6.8f} mK at T=2000K.".format(c3))
print("{0:6.8f} mK at T=2000K.".format(c4))
print("{0:6.8f} mK at T=2000K.".format(c5)) 


# This code finds the value of Wien's displacement constant to be 5.1084x$10^{-3}$. The agreed value of Wien's displacement constant is 2.897x$10^{-3}$ mK. 

# #### Part 5
# For this part, the code uses two different methods of intergration to find the total energy density over the frequency range for multiple temperatures.
# 
# The first one it uses is the trapezium rule. This method divides the area under the graph into trapeziums, calculates the area of each of these pieces and adds them together. 
# $$Area=\frac{dx}{2}(y_0+y_n)+dx\sum_{i=1}^{n-1}y_i$$
# This method presumes that the pieces under the graph are trapeziums, this means it is not totally accurate.
# 
# The second method is Simpson's rule. This method takes three points and fits a quadratic to them, unlike the trapesium rule which takes two points and makes a straight line. 
# $$Area=\frac{dx}{3}(y_0+4y_1+2y_2+4y_3+...+2y_{n-2}+4y_{n-1}+f_n)$$
# The even terms are multiplied by 2 and the odd terms are multiplied by 4. The first and last terms do not follow this rule.
# 
# It does not account completely for the change between two points so it loses accuracy here.
# 
# Due to the fact that that Simpson's rule treats the transistion between two arcs rather than a straight line like the trapezium rule, it is the more accurate method.
# 
# After intergrating using these two methods, the function will devide each value of area by $T^4$ to show that

# In[6]:


#task 5:numerical integration of the Planck function for a few temperatures

dx=V[2]-V[1] 

###########################################################################################trapezium rule

def total_t_area(u):
    area=0
    area=(dx/2)*(u[0]+u[n-1]) #first and last values of y have to be halved in this rule
    for i in range(1,n-2):#starting at second term and finihing at second last
        trapizoid=dx*u[i] #calcualting elements of sum in equation above
        area=area+trapizoid #adding it all together
    return area

print("Numerical intergration of Plancks function using the trapesium rule:")

#T=2000K
areat_2000=total_t_area(U)
print("for T=2000K:{0:6.14f}".format(areat_2000))

#T=3000K
areat_3000=total_t_area(W)
print("for T=3000K:{0:6.14f}".format(areat_3000))

#T=4000K
areat_4000=total_t_area(X)
print("for T=4000K:{0:6.14f}".format(areat_4000))

#T=5000K
areat_5000=total_t_area(Y)
print("for T=5000K:{0:6.14f}".format(areat_5000))

#T=6000K
areat_6000=total_t_area(Z)
print("for T=6000K:{0:6.14f}".format(areat_6000))

######################################################################################################Simpson's rule

def totalsarea(u):
    area=0
    area=(dx/3)*(u[0]+u[n-1]) #calculating first and last terms as they are multiplied only by a factor of one
    for i in range(1,n-2): #starting at second term and finihing at second last
        if i%2==0:
            r=(dx/3)*2*u[i] #even no.s multiplied by 2
        else:
            r=(dx/3)*4*u[i] #odd no.s multiplied by 4
        area=area+r #adding it all up
    return area

print("Numerical intergration of Plancks function using Simpson's rule:")


#T=2000K
areas_2000=totalsarea(U)
print("for T=2000K:{0:6.14f}".format(areas_2000))

#T=3000K
areas_3000=totalsarea(W)
print("for T=3000K:{0:6.14f}".format(areas_3000))

#T=4000K
areas_4000=totalsarea(X)
print("for T=4000K:{0:6.14f}".format(areas_4000))

#T=5000K
areas_5000=totalsarea(Y)
print("for T=5000K:{0:6.14f}".format(areas_5000))

#T=6000K
areas_6000=totalsarea(Z)
print("for T=6000K:{0:6.14f}".format(areas_6000))


# Although the trapesium rule is less acurate than Simpson's rule, they are giving simiar results for the intergration of Planck's function for the given temperatures.

# In[7]:


stef_bolt_1=areas_2000/2000**4
stef_bolt_2=areas_3000/3000**4
stef_bolt_3=areas_4000/4000**4
stef_bolt_4=areas_5000/5000**4
stef_bolt_5=areas_6000/6000**4

print("The constant in Stefan-Boltzmann law is calculated to be:")
print("{0:6.14E} for T=2000".format(stef_bolt_1))
print("{0:6.14E} for T=3000".format(stef_bolt_2))
print("{0:6.14E} for T=4000".format(stef_bolt_3))
print("{0:6.14E} for T=5000".format(stef_bolt_4))
print("{0:6.14E} for T=6000".format(stef_bolt_5))


# While these numbers are not the same, they are very close. This verifies that the area under the plot of Planck's law (power) is directly proportional to $T^4$
