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



j=32768

def LCG(n,a,b,k):
  x=[]
  for i in range(n):
    k=rand(k)/j
    x.append(a+(b-a)*k)
  return x

#Monte Carlo

def MonteC(funx,a,b,N,e):
    
    sum1=sum2=0
    r=LCG(N,a,b,e)
    
    for i in range(N):
        sum1+=funx(r[i])**2
        sum2+=funx(r[i])
    
    sum1= sum1/N + (sum2/N)**2
    sum2=(b-a)*sum2/N
    
    print("Fn:",sum2,"\nError:",math.sqrt(sum1))
    return sum2


def PlotMC(k,a,b,func):
 k=k/(b-a)
 y=[k,k,k]
 x = np.linspace(a, b)
 z=np.arange(a,b+(b-a)/2,0.5)
 plt.plot(x, func(x))
 plt.plot(z,y)
 plt.show()  
     
    
def MCarlo(N,a,b,funx,e):
    p=[]
    q=[]
    K=[]
    for i in range(N):
        r=int((i+1)*10)
        p.append(r)
        q.append(MonteC(funx,a,b,r,0.1))
        if abs(q[i]-3.14159265)<e:break
    print(p,"\n",q)    
    plt.plot(p,q)   



