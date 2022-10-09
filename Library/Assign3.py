import math
from .Assign1 import matpro

def transpose(A):
  for i in range(len(A)):
    for j in range(i+1,len(A)):
      A[i][j],A[j][i]=A[j][i],A[i][j]
  return A




#Guass-Jordan Elimination

#Function for returning the row number of the largest element of a column
def check(a,i):
    y=a[i][i]
    t=i
    for j in range(i,len(a)):         
     if abs(a[j][i])>abs(y):
      y=a[j][i]
      t=j
    if y==0:return -1               
    else:return t                    

#Swap is used to swap two rows k and i
def swap(a,k,i): 
 for t in range(0,len(a[0])):       
  a[k][t],a[i][t]=a[i][t],a[k][t]       

#Reduce is used to turn the diagonal element of a row to 1
def reduce(a,i,e):
 g=a[i][i]
 for t in range(i,len(a[0])):
  a[i][t]=round(a[i][t]/g,e)

#Convert is used to turn all non diagonal elements of a column to 0
def convert(a,i,e):
 g=0
 for m in range(len(a)):
  if m!=i:
   g=a[m][i]
   for z in range(i,len(a[0])):
    a[m][z]=round(a[m][z]-g*a[i][z],e)
 
#Solve turns one column into that of an identity matrix  
def solve(a,i,e):
 q=check(a,i)
 if q<0:
  print("No Unique Solution")
  return 0
 swap(a,q,i)                      
 reduce(a,i,e)
 convert(a,i,e)
 

#Guass performs solve() on every column of the matrix   
def Guass(a,e):
 for i in range(len(a)):
  solve(a,i,e)
 for line in a:
  print ('  '.join(map(str, line)))
 print("\n Solution matrix X: \n")
 for i in range(len(a)):
     print(a[i][len(a[0])-1])
     




  




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
    
    
   #Lower Triangle
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
        
        for j in range(i):
            sum=sum+A[i][j]*B[j][0]
        
        B[i][0]=B[i][0]-sum
        sum=0
        
    return B


#Backward Substitution
def back(A,B,e):
    n=len(A)
    sum=0
    for i in range(n-1,-1,-1):
        
        for j in range(i+1,n):
            sum=sum+A[i][j]*B[j][0]
            
        B[i][0]=round((B[i][0]-sum)/A[i][i],e)
        sum=0
    
    return B
    
    
#Calling each function
def LUC(A,B,e):
    A=LU(A)
    B= back(A,forw(A,B),e)
    print("\n Solution matrix X: \n")
    for line in B:
      print ('  '.join(map(str, line)))








#Chelosky Decomposition

#Function for checking whether matrix is symmetric or not 
def sym(A):
  for i in range(len(A)):
    for j in range(len(A)):
      if A[i][j]!=A[j][i]:
        return 2
      
  return 1


#Chelosky Decomposition function
def Dec(A):
 n=len(A)
 sum=0
 for i in range(n):
  for j in range(i,n):
    
   if j==i:
    for k in range(0,i):
     sum=sum+A[k][i]**2
    A[j][j]= (A[j][j]-sum)**(0.5)
    
   else:
    A[j][i]=0
    for k in range(0,i): 
     sum=sum+A[k][i]*A[k][j]
    A[i][j]= (A[i][j]-sum)/A[i][i]
        
   sum=0
 
 return A 


#Function for solving linear equations using Chelosky Decomposition     
def chelk(A,B,e):
  if sym(A)>1:
    print("Matrix is not symmetric")
    return 0
  
  #Forward Substitution
  sum=0
  A=transpose(Dec(A))
  n=len(A)
  
  
  for i in range(n):
    for k in range(i):
      sum=sum+B[k][0]*A[i][k]
    
    B[i][0]=round((B[i][0]-sum)/A[i][i],e)
    sum=0
  
  
  #Backward Substitution
  A=transpose(A) 
  
  for i in range(n-1,-1,-1):
    for k in range(i+1,n):
        sum=sum+B[k][0]*A[i][k]
    
    B[i][0]=round((B[i][0]-sum)/A[i][i],e)
    sum=0
  
  for line in B:
   print ('  '.join(map(str, line))) 
         
         
         
         
         



#Jacobi and Guass-Seidal

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
     
          
      
def Jacobi(A,B,e):
    
    A,B=pivot(A,B)
    
    n=len(A)
    C=[[1] for y in range(n)]
    D=[[0] for y in range(n)]
    m=2000
    sum=0
    y=1
    
    for k in range(m):
     for i in range(n):
        for j in range(n):
            if j!=i:
             sum=sum+A[i][j]*C[j][0]
            
            if abs(D[j][0]-C[j][0]) > (10**(-e)):y=1
                
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
                




def PosDef(A,C):
    K=matpro(matpro(transpose(C),A),C)
    for i in range(len(K)):
        for j in range(len(K[0])):
            if K[i][j]<=0:
                print("Not positive definite.")
                return 0
    return 1

    


def GS(A,B,e):
    n=len(A)
    X=[[0] for y in range(n)]
    m=200
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
        
        if abs(c-X[i][0])<(10**(-e)):y+=1
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
        
        
        


