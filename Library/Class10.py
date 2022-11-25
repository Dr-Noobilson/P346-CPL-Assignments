import math
from .Assign1 import matpro


def dot(A,B):
    sum=0
    for i in range(len(A[0])):
        sum+=A[0][i]*B[0][i]
    return sum

def powriter(A,x0,e):
    
    sum=2
    y=x0
    z=matpro(A,y)
    k0=dot(z,x0)/dot(y,x0)
    y=z
    z=matpro(A,y)
    k1=dot(z,x0)/dot(y,x0)
    
    while abs(k1-k0)>e:
      sum+=1
      k0=k1
      y=z
      z=matpro(A,y)  
      k1=dot(z,x0)/dot(y,x0)
    
    print("Eigenvalue:",k1,", Iterations: ",sum)
    print(y)
    
    sum=0 
    for i in range(len(y)):sum+=y[i][0]**2
    for i in range(len(y)):y[i][0]/=math.sqrt(sum)
    return y
    
    
      
      
      