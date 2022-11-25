import math
from .Assign2 import rand
import matplotlib.pyplot as plt
import numpy as np


j=32768

def LCG(n,k):
  x=[]
  for i in range(n):
    k=rand(k)/j
    x.append(k)
  return x

def LCG2(n,a,b,k):
  x=[]
  for i in range(n):
    k=rand(k)/j
    x.append(a+(b-a)*k)
  return x


#Monte Carlo  
def montec(integrand,a,b,N,samples):
    
    mean = 0
    variance = 0
    solution_list = []
    
    for i in range(N):
        variance += integrand(samples[i])**2
        mean += integrand(samples[i])
    
    solution_list.append((b-a)*mean/N)
    solution_list.append(variance/N - (mean/N)**2)
    
    return solution_list


def crude_montec_plotter(integrand,a,b,N,seed):
    
    x_values = []
    mean_values = []
    variance_values =[]
    samples = []
    N1 = 10
    step_size = int((N-N1)/50)
    
    while N1 <= N:
        
        x_values.append(N1)
        samples = LCG2(N1,a,b,seed)
        x,y = montec(integrand,a,b,N1,samples)
        mean_values.append(x)
        variance_values.append(y)
        
        N1 += step_size
        seed += step_size/N1

    return x_values, mean_values, variance_values






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


def minimizer(P1,P2,integrand,pdf,guess_pdf,cpdf,N,seed,step_size):
    variance = []
    parameters = []
    
    while P1 < P2:
        samples = inverse_sampling(cpdf,N,seed,P1)
        variance.append(importance_sampling(integrand,pdf,guess_pdf,samples,P1)[1])
        parameters.append(P1)
        P1 += step_size
    
    plt.scatter(parameters,variance,marker='.')
    plt.show()


def solution_plotter(integrand,pdf,guess_pdf,parameter,cpdf,N,seed):
    
    x_values = []
    mean_values = []
    variance_values =[]
    N1 = 10
    step_size = int((N-N1)/30)
    
    while N1 <= N:
        
        x_values.append(N1)
        
        samples = inverse_sampling(cpdf,N1,seed,parameter)
        a,b = importance_sampling(integrand,pdf,guess_pdf,samples,parameter)
        mean_values.append(a)
        variance_values.append(b)
        
        N1 += step_size
        seed += step_size/N1

    return x_values, mean_values, variance_values



def markov_sampling(N,a,b,guess_pdf,parameter,x0,step_size,seed):
    
    random_sample = []
    accepted = 0
    burn_in = int(N*0.5)
    
    for i in range(N):
        
        random_sample.append(x0)
        
        l = r = step_size/2
        if x0 + step_size/2 > b: r = b - x0
        if x0 - step_size/2 < a: l= x0 - a
        
        trial = x0 - l + (r+l)*rand(x0)/j
        acceptance = guess_pdf(trial,parameter)/guess_pdf(x0,parameter)
  
        if acceptance >= 1: 
            x0 = trial
            accepted += 1
            
        else:
            seed = rand(seed)/j 
            if seed < acceptance: 
                x0 = trial
                accepted  += 1
    
    print(accepted/N)    
    return random_sample[burn_in:]



def markov_sample_plotter(pdf,samples,a,b,parameter):
    N=len(samples)
    new_sample = []
    
    for i in range(N):
        if i % 10 == 0:
            new_sample.append(samples[i])
            
            
    f1=plt.figure()
    plt.hist(samples,bins=20)
    f2=plt.figure()
    plt.hist(new_sample,bins=20)
    f3=plt.figure()
    x = np.linspace(a, b, 1000)
    plt.plot(x, pdf(x,parameter))
    plt.show()  
              
               

  
