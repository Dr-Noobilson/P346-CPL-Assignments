import math
from .Assign2 import rand
import matplotlib.pyplot as plt
import numpy as np
import random


#Random Number Generators
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





#Crude Monte Carlo Integration Functions
def montec(integrand,a,b,N,samples):
    
    mean = 0
    variance = 0
    solution_list = []
    
    for i in range(N):
        variance += integrand(samples[i],0)**2
        mean += integrand(samples[i],0)
    
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







#Importance Sampling Monte Carlo method

#Inverse transform sampler
def inverse_sampling(cpdf,N,seed,parameter):
    return [cpdf(i,parameter) for i in LCG(N,seed)]
   
#Importance sampling Integration   
def importance_sampling(integrand,pdf,guess_pdf,samples,parameter):
    
    weighted_sum = 0
    squared_weighted_sum = 0
    N = len(samples)
    solution_list = []
    
    for i in range(N):
        term = integrand(samples[i],parameter)*pdf(samples[i],parameter)/guess_pdf(samples[i],parameter)
        weighted_sum += term
        squared_weighted_sum += term**2
        
    solution_list.append(weighted_sum/N)
    solution_list.append(squared_weighted_sum/N - (weighted_sum/N)**2)
    
    return solution_list


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


#Variance vs parameter plotter
def minimizer(P1,P2,integrand,pdf,guess_pdf,cpdf,N,seed,step_size):
    variance = []
    parameters = []
    
    while P1 < P2:
        samples = inverse_sampling(cpdf,N,seed,P1)
        variance.append(importance_sampling(integrand,pdf,guess_pdf,samples,P1)[1])
        parameters.append(P1)
        P1 += step_size
    
    plt.scatter(parameters,variance,marker='.')
    plt.xlabel("Parameter (β)")
    plt.ylabel("Variance (σ^2)")
    plt.grid()
    plt.show()










#Variation Monte Carlo technique

#Metropolis sampler
def metropolis_sampling(N,a,b,guess_pdf,parameter,x0,step_size):
    
    random_sample = []
    accepted = 0
    burn_in = int(N*0.5)
    normalizer = 0
    
    for i in range(N):
        
        random_sample.append(x0)
        normalizer += guess_pdf(x0,parameter)
        
        l = r = step_size/2
        if x0 + step_size/2 > b: r = b - x0
        if x0 - step_size/2 < a: l= x0 - a
        
        trial = x0 - l + (r+l)*random.random()
        acceptance = guess_pdf(trial,parameter)/guess_pdf(x0,parameter)
  
        if acceptance >= 1: 
            x0 = trial
            accepted += 1
            
        else: 
            if random.random() < acceptance: 
                x0 = trial
                accepted  += 1
    
    normalizer /= N  
    return random_sample[burn_in:], normalizer 




def metropolis_sample_plotter(pdf,samples,a,b,parameter,k):
            
    y, x, _ = plt.hist(samples, bins=75)
    plt.xlabel("x")
    plt.ylabel("Frequency")
    plt.grid()
    fig = plt.figure()
    weights = np.ones_like(samples)/(y.max()*k)
    plt.hist(samples,  weights=weights, bins=75,label="Samples")
    x = np.linspace(a, b, 1000)
    plt.plot(x, pdf(x,parameter),label="PDF ρ(x))")
    plt.xlabel("x")
    plt.ylabel("Relative Frequency")
    plt.grid()
    plt.legend()
    plt.show()  
              

               
#Variance vs parameter plotter
def metropolis_solution_plotter(integrand,pdf,guess_pdf,para1,para2,N,x,y,x0,h):
    
    x_values = []
    mean_values = []
    variance_values =[]
    step_size = 0.05
    l = 0
    
    while para1 <= para2:
        
        samples,l = metropolis_sampling(N,x,y,guess_pdf,para1,x0,h)
        
        x_values.append(para1)
        a,b = importance_sampling(integrand,pdf,pdf,samples,para1)
        mean_values.append(a)
        variance_values.append(b)
        
        para1 += step_size
        h *= 1.2
    
    figure1 = plt.figure()
    plt.scatter(x_values,mean_values,marker='.')
    plt.xlabel("Parameter (β)")
    plt.ylabel("Ground state energy (E_T)")
    plt.grid()

    figure2 = plt.figure()
    plt.scatter(x_values,variance_values,marker='.')
    plt.xlabel("Parameter (β)")
    plt.ylabel("Variance (σ^2)")
    plt.grid()




def generic_plotter(a,b,f1,f2,f3,L1,L2):
    x = np.arange(a,b,0.01)
    plt.plot(x,f1(x,L1),label="Integrand",color='black')
    plt.plot(x,f2(x,L1),label="Importance Distribution 1",color='green',linestyle='--'
             ,linewidth=1) 
    plt.plot(x,f3(x,L2),label="Importance Distribution 2",color='blue',linestyle='--'
             ,linewidth=1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid()