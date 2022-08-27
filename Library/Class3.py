import math
def LU(A):
 n=len(A)
 sum=0
 B=[[0 for x in range(n)] for y in range(n)]
 C=[[0 for x in range(n)] for y in range(n)]
 for i in range(n):
  for j in range(i,n):
      
   if j==i:
    for k in range(i):
     sum=sum+B[k][i]**2
    B[j][j]= round((A[j][j]-sum)**(0.5),4)
    
   else:
    for k in range(i): 
     sum=sum+B[k][i]*B[k][j]
    B[i][j]= round((A[i][j]-sum)/B[i][i],4)
        
   sum=0
   C[j][i]=B[i][j]
   
 for line in B:
   print ('  '.join(map(str, line)))
 
 print("\n")
 
 return B


def transpose(A):
  for i in range(len(A)):
    for j in range(i+1,len(A)):
      A[i][j],A[j][i]=A[j][i],A[i][j]
  return A
  
  
def sym(A):
  for i in range(len(A)):
    for j in range(len(A)):
      if A[i][j]!=A[j][i]:
        return 2
      
  return 1


def chel(A,B):
  if sym(A)>1:
    print("Matrix is not symmetric")
    return 0
  
  sum=0
  A=transpose(LU(A))
  n=len(A)
  
  
  for i in range(n):
    for k in range(i):
      sum=sum+B[k][0]*A[i][k]
    
    B[i][0]=round((B[i][0]-sum)/A[i][i],4)
    sum=0
  
  for line in B:
   print ('  '.join(map(str, line)))
  
  A=transpose(A) 
   
  for i in range(n-1,-1,-1):
    for k in range(i+1,n):
        sum=sum+B[k][0]*A[i][k]
    
    B[i][0]=round((B[i][0]-sum)/A[i][i],4)
    sum=0
  
  print("\n")
  for line in B:
   print ('  '.join(map(str, line)))  
  

       
          
          
      
  

      
      
      
   
   
    
    