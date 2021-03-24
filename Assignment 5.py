#!/usr/bin/env python
# coding: utf-8

# Assignment 5
# ----
# #### By Orla O'Neill, 18314251
# 
# This code deals with a file that has data on a number of stars. It will extract the necessary information from the file and will use that information to plot the Hertzsprung-Russell diagram, or something like it.

# ## Task 1
# In this part. The code will open the data file and will organise it into different arrays for use later.

# In[1]:


#reading first line

file=open("StarData.txt","r")
print(file.readline())


# In[2]:


#reading all lines, returning last line

data=file.readlines()

for line in data:
    columns=line.split()
    
print(line)
print(columns)


# In[3]:


#loading file and splitting up lines

with open("StarData.txt") as data:
    lines=data.read().splitlines()
    
print(lines)


# In[4]:


#setting up data arrays to recieve data from the columns

#empty arrays for the data
StarID=[]
ApparentVMag=[]
Colour=[]
Parallax=[]
ParallaxUncertainty=[]

#filling the arrays with the data
for line in lines:
    columns=line.split()
    StarID.append(columns[0])
    ApparentVMag.append(columns[1])
    Colour.append(columns[2])
    Parallax.append(columns[3])
    ParallaxUncertainty.append(columns[4])


# ## Task 2
# 
# In this part, the code plots the apparent magnitude of the star vs. its colour. It does this by first converting the necessary arrays of strings to arrays of floats and then using matplotlib to plot them.

# In[9]:


#scatter plot of apparent magnatude vs. colour

#importing the necessary libraries
import matplotlib.pyplot as plt
import numpy as np

#converting the arrays of strings to arrays of floats
y=np.asarray(ApparentVMag, dtype=np.float64, order='C')
x=np.asarray(Colour, dtype=np.float64, order='C')

#plot code
plt.scatter(x,y,s=0.5)
plt.title("apparent magnitude versus colour")
plt.xlabel("colour (mB − mV)")
plt.ylabel("apparent magnitude (mV)")
plt.xlim(-0.5,2.5)
plt.show()


# ## Task 3
# 
# Absolute magnatude (M) can be calulated from apparent magnitude (m) as follows:
# $$m-M=5log(\frac{d}{10})$$
# Where d is the disatnce from Earth to the star in parsecs.
# 
# The distance is calculated with the parallax angle
# $$d=\frac{1}{p}$$
# 
# Using this information, the code calculates the absolute magnitude and plots it against colour to get the Hertzsprung-Russell diagram.
# 
# Then, it counts the number of red giants, main series and white dwarf stars that can be seen on the graph.

# In[6]:


#calculating absolute magnitude and plotting 

#conveting array of strings to floats
Parallax=np.asarray(Parallax, dtype=np.float64, order='C')

#calcuating distance
d=1/Parallax
#calculating absolute magnitude
AbMag=y-5*np.log(d/10)

#plot code
plt.scatter(x,AbMag,s=0.5)
plt.title("absolute magnitude versus colour")
plt.xlabel("colour (mB − mV)")
plt.ylabel("absolute magnitude")
plt.xlim(-0.5,2.5)
plt.ylim(-20,20)
plt.gca().invert_yaxis()
plt.show()


# In[7]:


#counting star types

#star type count starts at 0
RedCount=0
MainCount=0
WhiteCount=0

#arrays of star types for part 4
RedGiantsX=[]
RedGiantsMag=[]
MainSequenceX=[]
MainSequenceMag=[]
WhiteDwarfsX=[]
WhiteDwarfsMag=[]

#red giant
for i in range(len(x)):
    if 0.75<=x[i]<=1.75 and -12.5<=AbMag[i]<=-2.5:
        
        #adding the star to the count
        RedCount=RedCount+1
        
        #adding the star to the arrays
        RedGiantsX.append(x[i])
        RedGiantsMag.append(AbMag[i])

#main squence
#it was counted in 3 different for loops as the main sequence is not much of a rectangle
for i in range(len(x)):
    if -.25<=x[i]<=.75 and -10<=AbMag[i]<=5:
        
        #adding the star to the count
        MainCount=MainCount+1
        
        #adding the star to the arrays
        MainSequenceX.append(x[i])
        MainSequenceMag.append(AbMag[i])
        
for i in range(len(x)):
    if .75<x[i]<1.2 and -2<=AbMag[i]<=5:
        
        #adding the star to the count
        MainCount=MainCount+1
        
        #adding the star to the arrays
        MainSequenceX.append(x[i])
        MainSequenceMag.append(AbMag[i])
        
for i in range(len(x)):
    if 1.2<=x[i]<=2 and -2.5<=AbMag[i]<=15:
        
        #adding the star to the count
        MainCount=MainCount+1
        
        #adding the star to the arrays
        MainSequenceX.append(x[i])
        MainSequenceMag.append(AbMag[i])

#whitedwarf
for i in range(len(x)):
    if -0.25<=x[i]<=1 and 5<=AbMag[i]<=15:
        
        #adding the star to the count
        WhiteCount=WhiteCount+1
        
        #adding the star to the arrays
        WhiteDwarfsX.append(x[i])
        WhiteDwarfsMag.append(AbMag[i])

#returning results
print("The number of red giants is",RedCount)
print("The number of main squence stars is",MainCount)        
print("The number of white dwarfs is",WhiteCount)        


# To get the ranges for the different star types, the coder compaired the plot above to the Hertzsprung-Russell diagram and tried to find where each group started and ended. This could mean that stars were left out or stars may have been counted twice in different groups.

# ## Task 4
# 
# In this part, the code plots the scatter in part 3 again, but this time it colours the stars based off of if they are red giants, main squence or white dwarf stars. It also adds the scale of luminosity, in units of Solar Luminosities, to the plot so that we can compair the brightness of the stars to that of the sun.

# In[8]:


#adding right y-axis and colour to the plot

#plotting each type with a different color
plt.scatter(RedGiantsX,RedGiantsMag,s=0.5,c="red")
plt.scatter(MainSequenceX,MainSequenceMag,s=0.5,c="yellow")
plt.scatter(WhiteDwarfsX,WhiteDwarfsMag,s=0.5,c="blue")


#plot code
plt.title("Absolute Magnitude versus Colour")
plt.xlabel("Colour (mB − mV)")
plt.ylabel("Absolute Magnitude")
plt.gca().invert_yaxis()

#creating right y-axis
rightAxis=plt.twinx()
rightAxis.set_ylim(8.77*10**-7,8.55*10**9)
rightAxis.set_ylabel("Luminosity (Solar Liminosities)")
rightAxis.semilogy()
plt.show()


# The predicted weakness in the coders method from part 3 is highlighted in this plot. It is clear to see that some of the main squence stars have been incorrectly counted as red giants and white dwarfs.
