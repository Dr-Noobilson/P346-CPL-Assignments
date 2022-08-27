import matplotlib.pyplot as plt
import math

c=12345
a=1103515245
m=32768

#Question 1: Function for LCG
def rand(t):
 b=(a*t+c)%m
 return b



#Question 2: Function for finding volume of sphere using throwing method
def sphere(k,l):
 n=999000
 x=0
 for i in range(n):
#Finding the number of points within radius 1 unit
  if (i/n)**2+k**2+l**2<=1:x=x+1             
  k=rand(k)/m                                     
  l=rand(l)/m

 print(x/n)
 
 
#Question 3: Function for simulating random walks
def walk(n,k,j):   
#Initializing position at origin
 x=[0]
 y=[0]
 rms=0
 for i in range(1,n+1):
  x.append(k)
  y.append(j)

#LCG function modified to obtain range between -1 to 1
  k=2*rand(k)/m-1
  j=2*rand(j)/m-1
  rms=rms+(x[i]-x[i-1])**2+(y[i]-y[i-1])**2
  
 print("RMS:",round(math.sqrt(rms/n),4))
 print("Displacement:",round(math.sqrt(x[n]**2+y[n]**2),4))
 
 plt.plot(x,y) 

 
    
