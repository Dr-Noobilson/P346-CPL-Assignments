import matplotlib.pyplot as plt
import math
import numpy as np
from .Assign2 import rand
m=32768

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n



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
    plt.plot(np.arange(0,X[-1]*1.5,(X[-1]*1.5)/3),[y,y,y],label="Equilibrium line",color='black',linestyle='--'
             ,linewidth=0.8) 
    plt.plot(X,A,label='Left Side')
    plt.plot(X,B,label='Right Side')
    plt.xlabel("Time")
    plt.ylabel("Number of particles")
    plt.legend() 
    plt.grid()
    plt.show()
    







def NewtonR(x,func,funx,e):
    l=t=0
    while abs(x-l)>e:
        l=x 
        x=l-(func(l)/funx(l))
        t+=1
    return truncate(x,3),t

def RK4(x0,y,func,h,x,e): 
    
    A=[]
    B=[]
    k1=k2=k3=k4=0
    
    while x0<=x:
        
        A.append(x0)
        B.append(y)
        
        if x0+h>x and x0!=x: h=x-x0 
        
        k1=h*func(y,x0)
        k2=h*func(y+k1/2,x0+h/2)
        k3=h*func(y+k2/2,x0+h/2)
        k4=h*func(y+k3,x0+h)
        
        y += (k1+2*k2+2*k3+k4)/6
        x0=x0+h
        if y > 0 and y < e:
            A.append(x0)
            B.append(y)
            print("Maximum height reached is:",truncate(x0,4),"units\nVelocity at maximum height:",truncate(y,4),"units")      
            return A,B
    
    print("Maximum height reached is:",truncate(x0,4),"units\nVelocity at maximum height:",truncate(y,4),"units")     
    return A,B





#LU Decomposition

#The subsequent functions are used for row pivoting and checking if matrix A can be LU decomposed
#Function for returning cofactor
def cof(A, i, j): return [row[:j] + row[j+1:] for row in (A[:i] + A[i+1:])]

#Function for returning determinant
def det(A):
  n=len(A) 
  if n==1:
    return A[0][0]
    
  if n==2:
    return A[0][0]*A[1][1]-A[1][0]*A[0][1]
  sum = 0
 
  for i in range(n):
    sign= (-1)**i
    subdet = det(cof(A,0,i))
    sum= sum+ (sign * A[0][i] * subdet)
 
  return sum


#Function for returning the largest element of a column below the diagonal element for swapping
def check2(a,i):
   y=a[i][i]
   t=i
   for j in range(i,len(a)):         
    if abs(a[j][i])>abs(y):
      y=a[j][i]
      t=j
   if t==i:return -1               
   else:return t          

#Function swap2 is used swapping the kth and ith element for pivoting   
def swap2(a,b,k,i): 
  for t in range(0,len(a[0])):       
   a[k][t],a[i][t]=a[i][t],a[k][t]          
  b[k][0],b[i][0]=b[i][0],b[k][0]
  return a,b

#Arrange is used for row pivoting in case the LU Decomposition condition is not satisfied
def arrange(A,B):
  n=len(A)
  for i in range(n):
    C=[row[:i+1] for row in A[:i+1]] #C stores the leading submatrices
    if det(C)==0:
      q=check2(A,i)
      if q<0:
        print("LU not possible")
        return 0
      A,B=swap2(A,B,q,i)             #Partial row pivoting if det(C) is 0
    C=[row[:i+1] for row in A[:i+1]]
    if det(C)==0:
      print("LU not possible")
      return 0
  
  return A,B
    
    
    
#LU Decomposition
def LU(A):
 n=len(A)
 sum=0

 
 for i in range(n):
  for j in range(n):
   
   #Lower Triangle   
   if i<=j:
    for k in range(i):
     sum=sum+A[i][k]*A[k][j]
    A[i][j]= A[i][j]-sum
    
    
   #Upper Triangle
   else:
    for k in range(j): 
     sum=sum+A[i][k]*A[k][j]
    A[i][j]= (A[i][j]-sum)/A[j][j]
        
   sum=0
 
 return A


#Forward Substitution
def forw(A,B):
    n=len(A)
    sum=0
    for i in range(n):
      for k in range(n): 
        for j in range(i):
            
            sum=sum+A[i][j]*B[j][k]
        
        B[i][k]=(B[i][k]-sum)
        sum=0
        
    return B


#Backward Substitution
def back(A,B,e):
    n=len(A)
    sum=0
 
    for i in range(n-1,-1,-1):
       for k in range(n): 
        for j in range(i+1,n):
            sum=sum+A[i][j]*B[j][k]
            
        B[i][k]=truncate((B[i][k]-sum)/A[i][i],e)
        sum=0
    
    return B
    
    
#Calling each function
def LUD(A,B,e): #e is precision
    A=LU(A)
    B= back(A,forw(A,B),e)
    print("\n Solution matrix X: \n")
    for line in B:
      print ('  '.join(map(str, line)))
    return B