from re import M, X
from secrets import choice
import matplotlib.pyplot as plt
import math


e=0.00001
f=0.00001
k=0
d=0.04
p=0


def Bracket(a,b,func,t):
    
    x=func(a)
    y=func(b)
    
    if t==10:return 0
    t+=1
    
    if x*y<0:
        print(a,b,t)
        return a,b
     
    
    if x*y>0:
        
        if abs(x)<abs(y):   
          return Bracket(float(a-d*(b-a)),b,func,t) 
        elif abs(x)>abs(y):
          return Bracket(a,float(b+d*(b-a)),func,t) 
        


def Bisection(a,b,func,t):
    
    k=func((a+b)/2)
     
    if abs(b-a)<e and abs(k)<f:
        print ("Root: ", (a+b)/2,", Value: ", k,"\n")
        print("Iteration:",t)
        return 0
    
    t+=1
        
    if k<0:
        Bisection((a+b)/2,b,func,t)
    elif k>0:
        Bisection(a,(a+b)/2,func,t)
    else:
        return "Incorrect-choice"
            
        
        
def Regula(a,b,func,t):
    
    m=float(a-(func(a)*(b-a)/(func(b)-func(a))))
    print(m,t)
    k=func(m)
    
    if abs(b-a)<e:
        print("Root: ", m,", Value: ", k,"\n")
        print("Iteration:",t)
        return 0
    
    t+=1
    
    if k<0:
        Regula(m,b,func,t)
    elif k>0:
        Regula(a,m,func,t)
    else:
        return "Incorrect-choice or function"
    
  
v=0.00001  

def NewtonR(x,func,funx):
    l=0
    t=0
    while abs(x-l)>v:
        l=x 
        x=l-(func(l)/funx(l))
        t+=1
    return x,t
        


#To create fucntion

def Makefunc(c,j):
    n=len(c)
    y=0
    for i in range(n):
        y=y+c[i]*(j**(n-i-1))
    
    return y

               
#For Differentiation
 
def Diff(c):
    n=len(c)
    m=[]
    for i in range(n):
        m.append(c[i]*(n-1-i))
    m.pop()
    
    return m
        
      
#To deflation
 
def deflate(c,b):
    m=[]
    m.append(c[0])
    for i in range(1,len(c)-1):
        m.append(c[i]+b*m[i-1])

    return m  

    
#Laguerre   

v=0.001
def Lag(b,c):
    
    n=len(c)
    l=0
    j=0
    G,H=0,0
    
    #X= lambda x : Makefunc(x)
    #Y= lambda y : X(Diff(y))
    #Z= lambda z : Y(Diff(z))
    
    
    if Makefunc(c,b)==0:
        return b
        
    while abs(b-l)>v:
        j=j+1
        l=b
        G=Makefunc(Diff(c),b)/Makefunc(c,b)
        H=G**2-Makefunc(Diff(Diff(c)),b)/Makefunc(c,b)

        if G>0:
            b=b-(n/(G-math.sqrt((n-1)*(n*H-G**2))))
        else:
            b=b-(n/(G+math.sqrt((n-1)*(n*H-G**2))))
          
    
    if Makefunc(c,b)<v:
        print(j)
        return b
            

   
def Solve(b,c):
    g=[]
    t=0
    while len(c)>2:
        b=Lag(b,c)
        g.append(b)
        c=deflate(c,b)
    
    print(g)
    
    
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
    print(r)
    
        
    
        
        
    
               
            
    
    
        













