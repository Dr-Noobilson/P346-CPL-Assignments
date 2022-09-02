import math


def pivot(A,B):
 c=0
 t=0
 for i in range(len(A[0])):
     t=i
     c=abs(A[i][i])
     for j in range(len(A)):
         if abs(A[j][i])>c:
             c=abs(A[j][i])
             t=j
         
     if j>i:
         for v in range(len(A[0])):
             A[i][v],A[t][v]=A[t][v],A[i][v]
             B[i][0],B[t][0]=B[t][0],B[i][0]
     elif j<i:
         print("Jacobi not possible \n")
         return 0
     
     
 return A,B
     
     
     
      
def Jacobi(A,B):
    
    A,B=pivot(A,B)
    
    n=len(A)
    C=[[1] for y in range(n)]
    D=[[0] for y in range(n)]
    m=2000
    sum=0
    e=0.001
    y=1
    
    for k in range(m):
     for i in range(n):
        for j in range(n):
            if j!=i:
             sum=sum+A[i][j]*C[j][0]
            
            if abs(D[j][0]-C[j][0]) > e:y=1
                
        if y==1:    
         D[i][0]=(B[i][0]-sum)/A[i][i]
        else:
            
         print(k)
         for line in C:
          print ('  '.join(map(str, line)))
         return C
     
        sum=0
        
     y=0    
     
     C,D=D,C
     

    for line in C:
      print ('  '.join(map(str, line) ))         
                




def matpro(a,b):
  x=[[0 for x in range(len(b[0]))] for y in range(len(a))]
  s=0                    
  for i in range(len(a)):
    for j in range(len(b[0])):
      for k in range(len(b)):    
       s=round(s+a[i][k]*b[k][j],3)
      x[i][j],s=s,0    
  return x
    
    
    
def transpose(A):
  for i in range(len(A)):
    for j in range(i+1,len(A)):
      A[i][j],A[j][i]=A[j][i],A[i][j]
  return A



def PosDef(A,C):
    K=matpro(matpro(transpose(C),A),C)
    for i in range(len(K)):
        for j in range(len(K[0])):
            if K[i][j]<=0:
                print("Not positive definite.")
                return 0
    return 1

    
    
    


def GS(A,B):
    n=len(A)
    X=[[0] for y in range(n)]
    m=200
    e=0.00001
    y,sum=0,0
    
    for v in range(m):
     y=0
     for i in range(n):
        sum=0
        for j in range(i): 
            sum+=A[i][j]*X[j][0]
        
        for k in range(i+1,n):
            sum+=A[i][k]*X[k][0]
        
        c=(B[i][0]-sum)/A[i][i]
        
        if abs(c-X[i][0])<e:y+=1
        X[i][0]=c
        
     if y==n:
      print(v,"\n")
      for line in X:
       print ('  '.join(map(str, line) )) 
      return X
    
    print("\n") 
    for line in X:
       print ('  '.join(map(str, line) )) 
    return X          
        
            
        
            
                               

 