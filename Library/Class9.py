import math
import matplotlib.pyplot as plt

def pardif(Lx,Lt,Nx,Nt,func,x0,xL,t,a):
    
  V = [[func((j+1)*0.1)] for j in range(Nx)]
  n=int(t/(Lt/Nt))
  
  for k in range(n):
   for i in range(Nx):
      
      if i==0:
          V[i][0]=V[i][0]*(1-2*a)+V[i+1][0]*a
      elif i==Nx-1:
          V[i][0]=V[i-1][0]*a+V[i][0]*(1-2*a)      
      else:
          V[i][0]=V[i-1][0]*a+V[i][0]*(1-2*a)+V[i+1][0]*a
    
  return V      
      
    
    