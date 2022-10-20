import matplotlib.pyplot as plt
import math
import numpy as np



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
 plt.plot(x, func(x,D))
 plt.plot(A,B)
 plt.show()    

  