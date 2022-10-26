import math
import matplotlib.pyplot as plt
import numpy as np

def ForEuler(x0,y,func,h,x):
    
    A=[]
    B=[]
    
    while x0<x:
        A.append(x0)
        B.append(y)
        y=y+h*func(x0)
        x0=x0+h
    
    print("Solution at",x, " is:", y)
    plt.plot(A,B)
    
    
def BackEuler():
    