import math
from .Assign2 import rand
import matplotlib.pyplot as plt
import numpy as np


#Monte Carlo

def MonteC(funx,a,b,N,e):
    
    sum1=sum2=0
    r=LCG(N,a,b,e)
    
    for i in range(N):
        sum1+=funx(r[i])**2
        sum2+=funx(r[i])
    
    sum1= sum1/N + (sum2/N)**2
    sum2=(b-a)*sum2/N
    
    print("Fn:",sum2,"\nError:",math.sqrt(sum1))
    return sum2


def PlotMC(k,a,b,func):
 k=k/(b-a)
 y=[k,k,k]
 x = np.linspace(a, b)
 z=np.arange(a,b+(b-a)/2,0.5)
 plt.plot(x, func(x))
 plt.plot(z,y)
 plt.show()  
     
    
def MCarlo(N,a,b,funx,e):
    p=[]
    q=[]
    K=[]
    for i in range(N):
        r=int((i+1)*10)
        p.append(r)
        q.append(MonteC(funx,a,b,r,0.1))
        if abs(q[i]-3.14159265)<e:break
    print(p,"\n",q)    
    plt.plot(p,q)   
    



j=32768

def LCG(n,k):
  x=[]
  for i in range(n):
    k=rand(k)/j
    x.append(k)
  return x


def inverse_sampling(cpdf,N,seed,parameter):
    return [cpdf(i,parameter) for i in LCG(N,seed)]
   
   
def importance_sampling(integrand,pdf,guess_pdf,samples,parameter):
    
    weighted_sum = 0
    squared_weighted_sum = 0
    N = len(samples)
    solution_list = []
    
    for i in range(N):
        term = integrand(samples[i])*pdf(samples[i],parameter)/guess_pdf(samples[i],parameter)
        weighted_sum += term
        squared_weighted_sum += term**2
        
    solution_list.append(weighted_sum/N)
    solution_list.append(squared_weighted_sum/N - (weighted_sum/N)**2)
    
    return solution_list




def markov_sampling(N,a,b,guess_pdf,parameter,x0,step_size,seed):
    
    random_sample = []
    
    for i in range(N):
        
        random_sample.append(x0)
        
        l = r = step_size/2
        if x0 + step_size/2 > b: r = b - x0
        if x0 - step_size/2 < a: l= x0 - a
        
        trial = x0 - l + (r+l)*rand(x0)/j
        r = guess_pdf(trial,parameter)/guess_pdf(x0,parameter)
  
        if r >= 1: x0 = trial
            
        else:
            seed = rand(seed)/j 
            if seed<r: x0 = trial
            
    return random_sample



def markov_sample_plotter(pdf,samples,a,b,parameter):
    N=len(samples)
    f=plt.figure()
    x = np.linspace(a, b, 1000)
    plt.plot(x, pdf(x,parameter))
    plt.hist(samples)
    plt.show()  
              
               

  
