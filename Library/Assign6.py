import math
import matplotlib.pyplot as plt
import numpy as np
from .Assign1 import matpro


#Forward Euler
def ForEuler(x0,y,func,h,x):
    
    A=[]
    B=[]
    
    while x0<=x:
        A.append(x0)
        B.append(y)
        if x0+h>x: h=x-x0
        y=y+h*func(y,x0)
        x0=x0+h
    
    print("Solution at",x, " is:", y)
    return A,B




#RK2
def RK2(x0,y,func,h,x): 
    
    A=[]
    B=[]
    k1=k2=0
    
    while x0<=x:
        A.append(x0)
        B.append(y)
        if x0+h>x: h=x-x0
        k1=h*func(y,x0)
        k2=h*func(y+k1/2,x0+h/2) 
        y+=k2
        x0=x0+h
    
    print("Solution at",x, " is:", y)  
    return A,B
   

#RK4
def RK4(x0,y,func,h,x): 
    
    A=[]
    B=[]
    k1=k2=k3=k4=0
    
    while x0<=x:
        A.append(x0)
        B.append(y)
        if x0+h>x: h=x-x0
        k1=h*func(y,x0)
        k2=h*func(y+k1/2,x0+h/2)
        k3=h*func(y+k2/2,x0+h/2)
        k4=h*func(y+k3,x0+h)
        
        y+= (k1+2*k2+2*k3+k4)/6
        x0=x0+h
    
    print("Solution at",x, " is:", y)      
    return A,B

 
#Plotter   
def Plotter(A,B,func):
       
    f = plt.figure()
    z = np.arange(A[0],A[-1],0.0001)
    plt.plot(z, func(z),color='blue')
    plt.plot(A,B, color='green')
    plt.show()
    




def CODE1(t0,x0,v0,dxdt,dvdt,h,t): 
    
    T=[]
    X=[]
    V=[]
    
    k1x=k2x=k3x=k4x=0
    k1v=k2v=k3v=k4v=0
    #k1z=k2z=k3z=k4z=0
    
    while t0 <= t:
        
        T.append(t0)
        X.append(x0)
        V.append(v0) 
        if t0+h>t and t0!=t: h=t-t0  
        
        k1x=h*dxdt(x0,v0,t0)
        k1v=h*dvdt(x0,v0,t0)
        #k1z=h*func(y,t0)
        
        k2x=h*dxdt(x0+k1x/2,v0+k1v/2,t0+h/2)
        k2v=h*dvdt(x0+k1x/2,v0+k1v/2,t0+h/2)
        #k2z=h*func(y+k1z/2,t0+h/2)
        
        k3x=h*dxdt(x0+k2x/2,v0+k2v/2,t0+h/2)
        k3v=h*dvdt(x0+k2x/2,v0+k2v/2,t0+h/2)
        #k3z=h*func(y+k2z/2,t0+h/2)
          
        k4x=h*dxdt(x0+k3x,v0+k3v,t0+h)
        k4v=h*dvdt(x0+k3x,v0+k3v,t0+h)
        #k4z=h*func(y+k3z,t0+h)
        
        x0 += (k1x+2*k2x+2*k3x+k4x)/6
        v0 += (k1v+2*k2v+2*k3v+k4v)/6
        #z+= (k1z+2*k2z+2*k3z+k4z)/6
        t0=t0+h
     
    return T,V,X





def CODE2(t0,x,y,z,func1,func2,func3,h,t): 
    
    T=[]
    X=[]
    Y=[]
    Z=[]
    k1x=k2x=k3x=k4x=0
    k1y=k2y=k3y=k4y=0
    k1z=k2z=k3z=k4z=0
    
    while t0<t+h:
        
        T.append(t0)
        X.append(x)
        Y.append(y)
        Z.append(z) 
        
        k1x=h*func1(x,y,z,t0)
        k1y=h*func2(x,y,z,t0)
        k1z=h*func3(x,y,z,t0)
        
        k2x=h*func1(x+k1x/2,y+k1y/2,z+k1z/2,t0+h/2)
        k2y=h*func2(x+k1x/2,y+k1y/2,z+k1z/2,t0+h/2)
        k2z=h*func3(x+k1x/2,y+k1y/2,z+k1z/2,t0+h/2)
        
        k3x=h*func1(x+k2x/2,y+k2y/2,z+k2z/2,t0+h/2)
        k3y=h*func2(x+k2x/2,y+k2y/2,z+k2z/2,t0+h/2)
        k3z=h*func3(x+k2x/2,y+k2y/2,z+k2z/2,t0+h/2)
     
        k4x=h*func1(x+k3x,y+k3y,z+k3z,t0+h)
        k4y=h*func2(x+k3x,y+k3y,z+k3z,t0+h)
        k4z=h*func3(x+k3x,y+k3y,z+k3z,t0+h)
        
        x+= (k1x+2*k2x+2*k3x+k4x)/6
        y+= (k1y+2*k2y+2*k3y+k4y)/6
        z+= (k1z+2*k2z+2*k3z+k4z)/6
        t0=t0+h
    
    print("Solution at t=",t, ", are: x=", x,", y =",y,", z =",z)      
    return X,Y,Z,T




def shoot(t0,x0,v0,dxdt,dvdt,h,tn):
    
    T,V,X=CODE1(t0,x0,v0,dxdt,dvdt,h,tn)
    return X[-1]


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

#Lagrange Function
    
def Lagrange(x,y,a):
    n=len(x)
    r=0
    p=1
    for i in range(n):
        for j in range(n):
           if j!=i:
            p=p*((a-x[j])/(x[i]-x[j]))
        r=r+(p*y[i])
        p=1
    return r
   
   
   
   



def dot(A,B):
    sum=0
    for i in range(len(A[0])):
        sum+=A[0][i]*B[0][i]
    return sum

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
    
    sum=0 
    for i in range(len(y)):sum+=y[i][0]**2
    for i in range(len(y)):y[i][0]/=math.sqrt(sum)
    return(y)
    