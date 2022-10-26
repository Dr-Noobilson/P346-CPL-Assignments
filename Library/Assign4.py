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
        print("a=",a,", b=",b,"\nIterations:",t,"\n")
        return a,b
     
    t+=1
    
    if x*y>0:
        
        if abs(x)<abs(y):   
          return Bracket(float(a-d*(b-a)),b,func,t,d) 
        elif abs(x)>abs(y):
          return Bracket(a,float(b+d*(b-a)),func,t,d) 
        



        
#Bisection function       
def Bisect(a,b,func,e): 
 condition=1
 k=1
 x=[]
 
 while condition:    
     
    k=func((a+b)/2)
    if k*func(a)>0: a= (a+b)/2
    elif k*func(b)>0: b=(a+b)/2
    else: return "Incorrect-choice"      
    
    condition= abs(k)>10**(-e) 
    x.append(round(((a+b)/2),7))
       
 return x
 
 
 

 
#Regula Falsi  
def Regula(a,b,func,e):
 m=0
 condition=1
 x=[]
 
 while condition:
    X=func(a)
    Y=func(b)
    m=b-(Y*(b-a)/(Y-X))
        
    if func(m)*X<0: b=m  
    else: a=m
    condition= abs(func(m))>10**(-e)
    x.append(round(m,7))
    
 return x



#Newton rapshon
def NewtonR(x,func,funx,e):
    r=[]
    l=0
    while abs(x-l) > 10**(-e):
        l=x 
        x=l-(func(l)/funx(l))
        r.append(round(x,7))
    return r
    




#Table1 is used for comparing solutions from Bisection and Regula-Falsi in a table
def Table1(a,b,func,e):
    
    print("Iteration     Bisection     Regula-Falsi")
    x=Bisect(a,b,func,e)
    y=Regula(a,b,func,e)
    z=max(len(x),len(y))
    w=min(len(x),len(y))
    for i in range(z):
     if i<w:
      print("     ",i+1,"      ",x[i],"      ",y[i]) 
     else:
        if z==len(x):
            print("     ",i+1,"      ",x[i])
        else:
            print("      ",i+1,"         ",y[i])
 
 

 
#Table2 is used for comparing solutions from Bisection, Regula-Falsi and Newton-Raphson in a table   
def Table2(a,b,func,funx,j,e):
    
    x=Bisect(a,b,func,e)
    y=Regula(a,b,func,e)
    r=NewtonR(j,func,funx,e)
    z=max(len(x),len(y),len(r))
    
    M = [ [ "" for i in range(4) ] for j in range(z) ]

    print("Iteration     Bisection       Regula-Falsi        Newton-Raphson")
    
    
    for i in range(z):
        M[i][0]=i+1
        if i<len(x):M[i][1]=x[i]
        if i<len(y):M[i][2]=y[i]
        if i<len(r):M[i][3]=r[i]
        
    for line in M:
      print ('           '.join(map(str, line)))
        
        
    
 
     
    

#To create function

def Makefunc(c,j):
    n=len(c)
    y=0.0
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
        
    while abs(b-l)>10**(-e):
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
            

#LagSolve calls both Laguerre and deflation function   
def LagSolve(c,b,e):
    g=[]
    while len(c)>2:
        b=Lag(c,b,e)
        g.append(b)
        c=deflate(c,b)
        
    g.append(-c[1]/c[0]) 
    print("Roots are:",g)    
    







#Function for fitting data from A, B to a polynomial of degree n-1

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

  
 #Printing errors in a1 and a2 and r^2 
 if n==2:
   S=len(A)*C[1][1]-(C[0][1]**2)
   print("\nError (a1):",C[1][1]/S,"\nError (a2):",len(A)/S)
   for i in range(len(B)):
     sum2=sum2+(B[i][0]**2)
   print("r^2:",(D[1][0]**2)/(C[1][1]*sum2))
   
 print()
 return C,D

 
 
#Function for plot B vs A and func
def FitPlot(A,B,a,b,func,D):
 f = plt.figure()
 x = np.linspace(a, b, 1000) 
 plt.plot(x, func(x,D)) #Plotting the obtained best fit function
 plt.plot(A,B) #Plotting the given data points
 plt.show()    





