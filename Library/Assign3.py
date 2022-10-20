import math
from .Assign1 import matpro


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
def Guass(a,e): #e is precision
 for i in range(len(a)):
  solve(a,i,e)
 for line in a:
  print ('  '.join(map(str, line)))
 print("\n Solution matrix X: \n")
 for i in range(len(a)):
     print(a[i][len(a[0])-1])
     












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
def LUD(A,B,e): #e is precision
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
#Upper triangle
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
  
  #Checking for symmetric matrix
  if sym(A)>1:
    print("Matrix is not symmetric")
    return 0
  
  sum=0
  A=Dec(A)
  n=len(A)
  
  #Forward Substitution
  
  for i in range(n):
    for k in range(i):
      sum=sum+B[k][0]*A[k][i]
    
    B[i][0]=round((B[i][0]-sum)/A[i][i],e)
    sum=0
  
  #Backward Substitution
  
  for i in range(n-1,-1,-1):
    for k in range(i+1,n):
        sum=sum+B[k][0]*A[i][k]
    
    B[i][0]=round((B[i][0]-sum)/A[i][i],e)
    sum=0
  
  for line in B:
   print ('  '.join(map(str, line))) 
  return B
         
         
         
         
         



















#Jacobi and Guass-Seidal

#Pivoting function for producing diagonally dominant matrix
def pivot(A):
 c=0
 t=0
 for i in range(len(A)): #Row pivot
     t=i                 #t stores largest element of a column
     c=abs(A[i][i])
     for j in range(len(A[0])):
         if abs(A[i][j])>c:
             c=abs(A[i][j])
             t=j 
         
     if t>i:
         for v in range(len(A)):
             A[v][i],A[v][t]=A[v][t],A[v][i] 
     elif t<i:
         print("Matrix is not diagonally dominant \n")
         return 0
     
 return A
     
          

#Jacobi function     
def Jacobi(A,B,e):

    if A==0:  #From pivot function
      print("Jacobi not possible")
      return 0
    
    n=len(A)
    C=[[1] for y in range(n)]       #C stores values after new iteration
    D=[[0] for y in range(n)]       #D stores the values after last iteration
    m=500000                        #m stores maximum number of iterations
    sum=0
    y=0
    
    for k in range(m):
      for i in range(n):
        for j in range(n):
            if j!=i:
             sum=sum+A[i][j]*C[j][0]
            
            if abs(D[j][0]-C[j][0]) < (10**(-e)):y+=1  #Checking for precision
                
        if y!=n:    
         D[i][0]=(B[i][0]-sum)/A[i][i]
         
        else:
          print("Number of iterations:",k+1,"\nSolution matrix X:\n")
          for line in C:
            print ('  '.join(map(str, line) ))   
          return    
     
        sum=0
          
      y=0    
      C,D=D,C
          
                


    
    
#Guass Seidal Function

def GS(A,B,e):
    n=len(A)
    
    if A==0: #From pivot function
      print("Guass-Seidal not possible")
      return 0
    
    X=[[0] for y in range(n)]       #X stores values after new iteration
    m=300
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
        
        if abs(c-X[i][0])<(10**(-e)):y+=1 #Precision condition
        X[i][0]=c
        
     
     if y==n:break #If all elements of X follow precision condition
  
    
    print("Number of iterations:", v+1,"\nSolution matrix X:\n") 
    for line in X:
       print ('  '.join(map(str, line) ))         
        
        
        


#Function for generating transpose of a matrix
def transpose(A):
  for i in range(len(A)):
    for j in range(i+1,len(A)):
      A[i][j],A[j][i]=A[j][i],A[i][j]
  return A


#For for checking whether matrix A is positive definite or not
def PosDef(A,C):
    K=matpro(matpro(transpose(C),A),C)
    for i in range(len(K)):
        for j in range(len(K[0])):
            if K[i][j]<=0:
                print("Not positive definite.")
                return 0
    return 1