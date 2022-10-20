import matplotlib.pyplot as plt
import math
from .Assign3 import chelk
import numpy as np


#Bracket function
def Bracket(a,b,func,t,d):
    
    x=func(a)
    y=func(b)
    if t==10:return 0
    
    if x*y<0:
        print("a=",a,",b=",b,"\nIterations:",t,"\n")
        return a,b
     
    t+=1
    
    if x*y>0:
        
        if abs(x)<abs(y):   
          return Bracket(float(a-d*(b-a)),b,func,t) 
        elif abs(x)>abs(y):
          return Bracket(a,float(b+d*(b-a)),func,t) 
        
        
#Bisection function       
def Bisect(a,b,func,t,e):
 k=1   
 condition=1
 print ("Steps ", (a+b)/2,", Value: ", k,"\nIteration:",t+1,"\n")
 
 while condition:    
     
    k=func((a+b)/2)
    if k<0: a= (a+b)/2
    elif k>0: b=(a+b)/2
    else: return "Incorrect-choice"    
    
    condition= abs(k)>e 
    print ("Root: ", (a+b)/2,", Value: ", k,"\nIteration:",t+1,"\n")
    t+=1
       
 print ("Root: ", (a+b)/2,", Value: ", k,"\nIteration:",t+1,"\n")
 return 
    
    

 
#Regula Falsi  
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
    
 print("Root: ", m,", Value: ", func(m),"\nIteration:",t,"\n")
 return 





#Newton rapshon
def NewtonR(x,func,funx,e):
    l=t=0
    while abs(x-l) > 10**(-e):
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
    






#Fit function

def Fit(A,B,n):
 sum1=0
 sum2=0
 C=[[0 for x in range(n)] for y in range(n)]
 D=[[0] for y in range(n)]
 
 for i in range(n):
    for j in range(i+1):    
       
      for k in range(len(A)):
       sum1=sum1+(A[k][0]**(i+j))
      
      
      C[i][j]=C[j][i]=sum1
      sum1=0
    for k in range(len(A)):
      sum2=sum2+((A[k][0]**(i))*B[k][0])
        
    D[i][0]=sum2
    sum2=0
 

 for line in C:
   print ('  '.join(map(str, line))) 
 print()
 for line in D:
   print ('  '.join(map(str, line))) 
   
 if n==2:
   S=len(A)*C[1][1]-(C[0][1]**2)
   print("Error (a1):",C[1][1]/S,"\nError (a2):",len(A)/S)
   for i in range(len(B)):
     sum2=sum2+(B[i][0]**2)
   print("r^2:",(D[1][0]**2)/(C[1][1]*sum2))
   
 print()
 return C,D



def my_formula(x,D): 
    k=0
    for i in range(len(D)):
        k+=D[i][0]*(x**i)
    return k  



def FitPlot(A,B,a,b,func,D):
 f = plt.figure()
 x = np.linspace(a, b, 1000)
 plt.plot(x, func(x,D))
 plt.plot(A,B)
 plt.show()






    
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
    