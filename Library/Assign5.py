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
    return sum



#Simpson
def simp(funx,a,b,N):
    k=1
    sum=0
    h=(b-a)/N
    
    for i in range(N):
        if i==0 and i==N-1:k=1
        elif i%2==0:k=2
        else:k=4
        sum= sum + k*funx(a+i*h)

    sum=round(sum*h/3, 8)
    return sum


#Function to print all three in table form
def numInt(funx,a,b,N):
    print(N,"   ",intMid(funx,a,b,N),"   ",intTrap(funx,a,b,N),"   ",simp(funx,a,b,N))
    
 

#Random number generator between two numbers a and b
j=32768

def LCG(n,a,b,k):
  x=[]
  for i in range(n):
    k=rand(k)/j
    x.append(a+(b-a)*k)
  return x


#Monte Carlo  
def monteC(funx,a,b,N,e):
    
    sum1=sum2=0
    r=LCG(N,a,b,e)
    
    for i in range(N):
        sum1+=funx(r[i])**2
        sum2+=funx(r[i])
    
    sum1= sum1/N + (sum2/N)**2
    sum2=(b-a)*sum2/N
    
    return sum2,math.sqrt(sum1)
    

#Function to plot the convergence of integral using Monte Carlo for different N   
def mcPlot(funx,a,b,N,y):
    p=[]
    q=[]
    r=10
    for i in range(N+1):
        p.append(r)
        q.append(monteC(funx,a,b,r,0.1)[0])
        r=int((i+1)*10000)
        
    f=plt.figure()
    plt.xlabel("N")
    plt.ylabel("Fn")   
    plt.plot(p,q)   
    plt.plot(np.arange(10,r*1.5,(r*1.5-10)/3),[y,y,y]) 

