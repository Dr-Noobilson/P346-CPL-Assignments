import matplotlib.pyplot as plt
import math


e=0.00001
f=0.0001
k=0
d=0.04
p=0


def Bracket(a,b,func,t):
    
    x=func(a)
    y=func(b)
    
    if t==10:return 0
    t+=1
    
    if x*y<0:
        print("a=",a,",b=",b,"\nIterations:",t,"\n")
        return a,b
     
    
    if x*y>0:
        
        if abs(x)<abs(y):   
          return Bracket(float(a-d*(b-a)),b,func,t) 
        elif abs(x)>abs(y):
          return Bracket(a,float(b+d*(b-a)),func,t) 
        


def Bisection(a,b,func,t):
    
    k=func((a+b)/2)
     
    if abs(b-a)<e and abs(k)<f:
        print ("Root: ", (a+b)/2,", Value: ", k)
        print("Iteration:",t+1,"\n")
        return 
    
    t+=1
        
    if k<0:
        Bisection((a+b)/2,b,func,t)
    elif k>0:
        Bisection(a,(a+b)/2,func,t)
    else:
        return "Incorrect-choice"
      
      
            
def Bisect(a,b,func,e):
 t=0
 k=1   
 condition=1
 
 while condition:    
     
    k=func((a+b)/2)
    if k<0: a= (a+b)/2
    elif k>0: b=(a+b)/2
    else: return "Incorrect-choice"    
    
    condition= abs(k)>e 
    t+=1
       
 print ("Root: ", (a+b)/2,", Value: ", k,"\nIteration:",t+1,"\n")
 return 
    
    
    
    
       
def Regula(a,b,func,e):
 t=m=1
 condition=1
 while condition:
    X=func(a)
    Y=func(b)
    m=b-(Y*(b-a)/(Y-X))
        
    if func(m)*X<0: b=m  
    else: a=m
    t+=1
    condition= abs(func(m))>e
    
 print("Root: ", m,", Value: ", k,"\n")
 print("Iteration:",t)
 return 
  
  
  
  
  

#Newton rapshon
def NewtonR(x,func,funx,e):
    l=t=0
    while abs(x-l)>e:
        l=x 
        x=l-(func(l)/funx(l))
        t+=1
    print("Root:",x,", Value:",func(x),"\nIteration:",t,"\n")
    return x
        





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
    for i in range(n-1):
        m.append(c[i]*(n-1-i))
    
    return m
        
      
#To deflation
 
def deflate(c,b):
    m=[]
    m.append(c[0])
    for i in range(1,len(c)-1):
        m.append(c[i]+b*m[i-1])

    return m  

    
#Laguerre   

def Lag(c,b,e):
    
    n=len(c)
    l=r=0
    j=0
    G,H=0,0
    
    if Makefunc(c,b)==0:
        return b
        
    while abs(b-l)>e:
        j=j+1
        l=b
        G=Makefunc(Diff(c),b)/Makefunc(c,b)
        H=G**2-Makefunc(Diff(Diff(c)),b)/Makefunc(c,b)
        r=math.sqrt((n-1)*(n*H-G**2))
      
        if abs(G-r)>abs(G+r):
            b=b-(n/(G-r))
        else:
            b=b-(n/(G+r))

    print("Root:",b,", Iteration: ",j,"\n")
    return b
            

   
def Solve(c,b,e):
    g=[]
    while len(c)>2:
        b=Lag(c,b,e)
        g.append(b)
        c=deflate(c,b)
        
    g.append(-c[1]/c[0]) 
    print(g)    
    


  

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
    print(r)
        
    
        
        
    
               
            
    
    
        













