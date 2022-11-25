import math
import matplotlib.pyplot as plt
import numpy as np
from .Assign1 import matpro
import random


#Coupled ODE solving function

def CODE1(t0,x0,v0,dxdt,dvdt,h,t): 
    
    T=[]
    X=[]
    V=[]
    
    k1x=k2x=k3x=k4x=0
    k1v=k2v=k3v=k4v=0
    
    while t0 <= t:
        
        T.append(t0)
        X.append(x0)
        V.append(v0) 
        
        if t0+h>t and t0!=t: h=t-t0  
        
        k1x=h*dxdt(x0,v0,t0)
        k1v=h*dvdt(x0,v0,t0)
        
        k2x=h*dxdt(x0+k1x/2,v0+k1v/2,t0+h/2)
        k2v=h*dvdt(x0+k1x/2,v0+k1v/2,t0+h/2)
      
        k3x=h*dxdt(x0+k2x/2,v0+k2v/2,t0+h/2)
        k3v=h*dvdt(x0+k2x/2,v0+k2v/2,t0+h/2)
          
        k4x=h*dxdt(x0+k3x,v0+k3v,t0+h)
        k4v=h*dvdt(x0+k3x,v0+k3v,t0+h)
        
        x0 += (k1x+2*k2x+2*k3x+k4x)/6
        v0 += (k1v+2*k2v+2*k3v+k4v)/6
        
        t0=t0+h
     
    return T,V,X




#Shooting Method

def shoot(t0,x0,v0,dxdt,dvdt,h,tn):
    
    T,V,X=CODE1(t0,x0,v0,dxdt,dvdt,h,tn)
    return X[-1] #returns slope at boundary


def bound(t0,tn,x0,xn,dxdt,dvdt,v1,v2,h,e):
   
   iterations = 0
   
   k1 = shoot(t0,x0,v1,dxdt,dvdt,h,tn)
   k2 = shoot(t0,x0,v2,dxdt,dvdt,h,tn)
   v0 = v1 + (v2-v1)*(xn-k1)/(k2-k1)
   j = shoot(t0,x0,v0,dxdt,dvdt,h,tn)
   
   while abs(j-xn) > e:
       iterations += 1
     
       if j < xn: v1=v0
       else: v2=v0
    
       k1 = shoot(t0,x0,v1,dxdt,dvdt,h,tn)
       k2 = shoot(t0,x0,v2,dxdt,dvdt,h,tn)
       v0 = v1 + (v2-v1)*(xn-k1)/(k2-k1)
       j = shoot(t0,x0,v0,dxdt,dvdt,h,tn)
    
   return v0,iterations,j 


   
   
   

#Function to find dot product of two matrices
def dot(A,B):
    sum=0
    for i in range(len(A[0])):
        sum+=A[0][i]*B[0][i]
    return sum

#Function for returning dominant eigenvalue and corresponding eigenvector
def powriter(A,x0,e):
    
    sum=2
    y=x0
    z=matpro(A,y)
    k0=dot(z,x0)/dot(y,x0)
    y=z
    z=matpro(A,y)
    k1=dot(z,x0)/dot(y,x0)
    
    while abs(k1-k0)>e:
      sum+=1
      k0=k1
      y=z
      z=matpro(A,y)  
      k1=dot(z,x0)/dot(y,x0)
    
    print("Eigenvalue:",k1,", Iterations: ",sum,"\n\nEigenket:")
    
    #Finding normalized eigenvector
    sum=0 
    for i in range(len(y)):sum+=y[i][0]**2
    for i in range(len(y)):y[i][0]/=math.sqrt(sum)
    return(y)
    
    
    
    

#Function to solve partial differential equation
def pardif(x0,xL,Lt,Nx,Nt,func,t):
    
  hx = (xL - x0)/Nx  
  ht = Lt/Nt
  a = ht/hx**2
  V = [ [func(x0+j*hx)] for j in range(Nx+1)]
  X = [ [x0+j*hx] for j in range(Nx+1)]
  n = int(t/ht)
  
  for k in range(n):
   for i in range(Nx+1):  
      
      if i==0:
          V[i][0]=V[i][0]*(1-2*a)+V[i+1][0]*a
      elif i==Nx:
          V[i][0]=V[i-1][0]*a+V[i][0]*(1-2*a)      
      else:
          V[i][0]=V[i-1][0]*a+V[i][0]*(1-2*a)+V[i+1][0]*a
    
  return V,X


#Plots the state of the system described by the partial differential equation for a range of time steps
def pardif_plotter(x0,xL,Lt,Nx,Nt,func,n):
    
    fig = plt.figure()
    plt.xlabel("L")
    plt.ylabel("Temp")
    Y = X = []
    ht = Lt/Nt
    colour = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(n)]
    
    for i in range(n):
        Y,X = pardif(x0,xL,Lt,Nx,Nt,func,2*(i+1)*ht) 
        plt.plot(X,Y,color=colour[i])
