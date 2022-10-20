import math
import matplotlib.pyplot as plt
from .Assign2 import rand


c=12345
a=1103515245
m=32768




#Question 1: To find the area of an ellipse upto 5% error
def ellipse(x,y,n):
 p=0
 for i in range(n):
#Finding the number of points within the ellipse
  if (x**2)/4+(y**2) <= 1: p+=1             
  x=4*rand(x)/m-2                                  
  y=2*rand(y)/m-1

 print("Area of ellispe:", p*8/n)
 print("Error:",round(abs(p*8/n-6.28318530718)*100/6.28318530718,2),"%\n")
 




def Wein(r,e):
 print("Wein's constant b:",math.floor((6.626*3*0.001/(1.381*r)*10000)*(10**e))/(10**e),"* 10^(-4)")
 
 



 
 
 
 
 