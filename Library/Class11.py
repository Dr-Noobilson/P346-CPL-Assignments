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
    
    for j in range(r+1):
        
     for i in range(N):
        e=rand(e)/m
        if e/Na<L:
            Na-=1
            Nb+=1
        
     A.append(Na)
     B.append(Nb)
     X.append((j+1)*dt)
     N=Na
        
    f=plt.figure()
    plt.scatter(X,A,marker=".")
    plt.scatter(X,B,marker=".")
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