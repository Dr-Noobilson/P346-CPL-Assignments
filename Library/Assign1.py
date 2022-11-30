import matplotlib.pyplot as plt
from math import sqrt

#Question 1: To print sum of first n odd numbers and factorial of n
def sum(n):
  s=0
  for i in range(n):
   s+=2*i+1
  return s

def fact(k):
  p=1
  for i in range(2,k+1):
   p*=i
  return p


#Question 2: Sum of N terms of an AP, GP and HP series for common difference 1.5 and common ratio 0.5
def ap(n):return 0 if n==1 else 1.5*(n-1)+ap(n-1)

def gp(n):return 1 if n==1 else 0.5**(n-1)+gp(n-1)

def hp(n):return 1 if n==1 else 1/(1.5*(n-1))+hp(n-1)


#Question 3: Sum of the series of general term: -(-0.5)^n (n=1,2,...). Plot the sum versus n.
def series(n):
  s=0
  x,y=[],[]
  for i in range(1,n+1):
   x.append(i)
   s-=(-0.5)**i
   y.append(s)
  plt.plot(x, y)
  plt.xlabel("n")
  plt.ylabel("Sum")
  

#Question 4: Matrix Multiplication 
def matpro(a,b):
  x=[[0 for x in range(len(b[0]))] for y in range(len(a))]
  s=0                    
  for i in range(len(a)):
    for j in range(len(b[0])):
      for k in range(len(b)):    
       s=round(s+a[i][k]*b[k][j],3)
      x[i][j],s=s,0    
  return x
 
    
#Question 5: Class to find sum, product and modulus of two complex numbers
class myComplex:
  def __init__(self, a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        
  def sum(self):
    print(self.a+self.c,"+",self.b+self.d,"i")
    
  def pro(self):
    print(self.a*self.c-self.b*self.d,"+",self.a*self.d+self.b*self.c,"i")
    
  def mod(self):
    print(round(sqrt(self.a**2+self.b**2),3),"\n",round(sqrt(self.c**2+self.d**2),3))

def truncate(f, n):
    return math.floor(f * 10 ** n) / 10 ** n