import math
from .Assign2 import rand
import matplotlib.pyplot as plt
import numpy as np



#Midpoint
def intMid(funx,a,b,N):
    sum=0
    h=(b-a)/N
    
    for i in range(N):
        sum= sum + (h*funx(a+((i+0.5)*h)))
        
    sum=round(sum,8)
    print("sum for N (",N,") =",sum)
    return sum
    
    
    
#Trapezoid

def intTrap(funx,a,b,N):
    sum=0
    h=(b-a)/N
    k=2
    
    for i in range(N):
        if i==0 and i==N-1:k=1
        else:k=2
        sum= sum + k*funx(a+i*h)
    
    sum=round(sum*h/2, 8)
    print("sum for N (",N,") =",sum)
    return sum



#Simpson
def Simp(funx,a,b,N):
    k=1
    sum=0
    h=(b-a)/N
    
    for i in range(N):
        if i==0 and i==N-1:k=1
        elif i%2==0:k=2
        else:k=4
        sum= sum + k*funx(a+i*h)

    sum=round(sum*h/3, 8)
    print("sum for N (",N,") =",sum)
    return sum


