import math
import matplotlib.pyplot as plt

def pardif(x0,xL,Lt,Nx,Nt,func,t):
    
  hx = (xL - x0)/Nx  
  ht = Lt/Nt
  a = ht/hx**2
  V = [ [func(x0+j*hx)] for j in range(Nx+1)]
  n = int(t/ht)
  
  
  for k in range(n):
   for i in range(Nx+1):
      
      if i==0:
          V[i][0]=V[i][0]*(1-2*a)+V[i+1][0]*a
      elif i==Nx-1:
          V[i][0]=V[i-1][0]*a+V[i][0]*(1-2*a)      
      else:
          V[i][0]=V[i-1][0]*a+V[i][0]*(1-2*a)+V[i+1][0]*a
    
  return V      
      
    
    