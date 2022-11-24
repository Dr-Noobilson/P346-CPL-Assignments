import math
import matplotlib.pyplot as plt
import numpy as np


#Forward Euler
def ForEuler(x0,y,func,h,x):
    
    A=[]
    B=[]
    
    while x0<x+h:
        A.append(x0)
        B.append(y)
        y=y+h*func(y,x0)
        x0=x0+h
    
    print("Solution at",x, " is:", y)
    return A,B




#RK2
def RK2(x0,y,func,h,x): 
    
    A=[]
    B=[]
    k1=k2=0
    
    while x0<x+h:
        A.append(x0)
        B.append(y)
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
    
    while x0<x+h:
        A.append(x0)
        B.append(y)
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
    
    
    
"""    
def code(K,func,h):
    
    A=[]
    B=[]
    k1=k2=k3=k4=0
    n=len(K)
    t=K[-1]
    
    while t<t+h:
        
      for i in range(len(K)):
          
        A.append(t)
        B.append(y)
        k1=h*func(*K[0:n-1],t)
        k2=h*func(K[i]+k1/2,t+h/2)
        k3=h*func(y+k2/2,x0+h/2)
        k4=h*func(y+k3,x0+h)
        
        y+= (k1+2*k2+2*k3+k4)/6
        t=t+h
    
    print("Solution at",x, " is:", y)      
    return A,B

 """



def CODE1(t0,x,y,func1,func2,h,t): 
    
    A=[]
    B=[]
    C=[]
    k1x=k2x=k3x=k4x=0
    k1y=k2y=k3y=k4y=0
    #k1z=k2z=k3z=k4z=0
    A.append(t0)
    B.append(x)
    C.append(y) 
    
    while t0<t+h:
          
        k1x=h*func1(x,y,t0)
        k1y=h*func2(x,y,t0)
        #k1z=h*func(y,t0)
        
        k2x=h*func1(x+k1x/2,y+k1y/2,t0+h/2)
        k2y=h*func2(x+k1x/2,y+k1y/2,t0+h/2)
        #k2z=h*func(y+k1z/2,t0+h/2)
        
        k3x=h*func1(x+k2x/2,y+k2y/2,t0+h/2)
        k3y=h*func2(x+k2x/2,y+k2y/2,t0+h/2)
        #k3z=h*func(y+k2z/2,t0+h/2)
          
        k4x=h*func1(x+k3x,y+k3y,t0+h)
        k4y=h*func2(x+k3x,y+k3y,t0+h)
        #k4z=h*func(y+k3z,t0+h)
        
        x+= (k1x+2*k2x+2*k3x+k4x)/6
        y+= (k1y+2*k2y+2*k3y+k4y)/6
        #z+= (k1z+2*k2z+2*k3z+k4z)/6
        t0=t0+h
        
        A.append(t0)
        B.append(x)
        C.append(y) 
    
    print("Solution at t=",t, ", are: x=", x,", y =",y)      
    return B,C,A





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




def shoot(x0,xn,y0,func1,func2,z,h):
    
    X,Y,Z=CODE1(x0,z,y0,func1,func2,h,xn)
    return Y[-1]


def bound(x0,xn,y0,yn,func1,func2,z1,z2,h,e):
   
   R=0
   k1=shoot(x0,xn,y0,func1,func2,z1,h)
   k2=shoot(x0,xn,y0,func1,func2,z2,h)
   t=z1+(z2-z1)*(yn-k1)/(k2-k1)
   j=shoot(x0,xn,y0,func1,func2,t,h)
   
   while abs(j-yn)>e:
     
     R=R+1
     if j<yn:z1=t
     else: z2=t
    
     k1=shoot(x0,xn,y0,func1,func2,z1,h)
     k2=shoot(x0,xn,y0,func1,func2,z2,h)
     t=z1+(z2-z1)*(yn-k1)/(k2-k1)
     j=shoot(x0,xn,y0,func1,func2,t,h)
    
   print("z(0) =",t,", Iterations:",R)