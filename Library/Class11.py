import math
from .Assign2 import rand
import matplotlib.pyplot as plt
import numpy as np

m=32768

def radioact(Na,T,dt,e):
    Nb=0
    N=Na
    L=0.6931*dt/T
    r=int(T/dt)
    A,B,X=[Na],[0],[0]
    D=[0]
    decays=0
    
    for j in range(r+1):
        
     for i in range(N):
        e=rand(e)/m
        if e/Na<L:
            Na-=1
            Nb+=1
            decays += 1
        
     A.append(Na)
     B.append(Nb)
     X.append((j+1)*dt)
     D.append(decays)
     N=Na
     decays = 0
        
    f=plt.figure()
    plt.scatter(X,A,marker=".")
    plt.scatter(X,B,marker=".")
    plt.show() 
    
    f1=plt.figure() 
    plt.bar(X,D)
    plt.xlim([0,5])
    plt.show()
    
    
    
def radioact2(Na,T1,T2,dt,e):
    Nb,Nc=0,0
    N=Na
    L1=0.6931*dt/T1
    L2=0.6931*dt/T2
    r=int(max(T1,T2)/dt)
    A,B,C,X=[Na],[0],[0],[0]

    
    for j in range(r+1):
        
     for i in range(N):
        e=rand(e)/m
        if e/Na<L1:
            Na-=1
            Nb+=1

            
     N=Nb
     for i in range(N):
        e=rand(e)/m
        if e/Na<L2:
            Nb-=1
            Nc+=1 
        
     A.append(Na)
     B.append(Nb)
     C.append(Nc)
     X.append((j+1)*dt)
     N=Na
        
    f1=plt.figure()
    plt.plot(X,A)
    plt.plot(X,B)
    plt.plot(X,C)
    plt.show()
    
    f=plt.figure()
    plt.scatter(X,A,marker=".")
    plt.scatter(X,B,marker=".")
    plt.scatter(X,C,marker=".")
    plt.show()   
    
    f6=plt.figure()
    plt.bar(B,X,align='edge', width=0.2)
    plt.xlim([0,40])
    plt.show()


def f1(x):
    return 2500  
    
#For Question 2
def equi(Nl,T,dt,seed):
    
    Q,Nr,p = Nl,0,1
    r = int(T/dt)
    A,B,X = [Nl],[0],[0]
    seed1 = seed
    
    for j in range(r+1):
              
      seed=(Nl/Q)*rand(seed1)/m
      seed1=(Nr/Q)*rand(seed)/m
        
      if seed < seed1: p = 0
      elif seed > seed1: p = 1
      else: p=round(rand(seed)/m)
      
      if p == 1:
        Nl -= 1
        Nr += 1
      else:
        Nr -= 1
        Nl += 1   
         
      A.append(Nl)
      B.append(Nr)
      X.append((j+1)*dt)
    
    y=2500 
    print("At time:",X[-1],"\nNumber of particles on left side =",Nl,"\nNumber of Particles on right side =",Nr)   
    f=plt.figure()
    plt.plot(np.arange(0,X[-1]*1.5,(X[-1]*1.5)/3),[y,y,y],label="Equilibrium line",color='black') 
    plt.plot(X,A,label='Left Side')
    plt.plot(X,B,label='Right Side')
    plt.xlabel("Time")
    plt.ylabel("Number of particles")
    plt.legend() 
    plt.grid()
    plt.show()