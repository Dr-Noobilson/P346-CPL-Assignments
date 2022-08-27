def check(a,i):
    y=a[i][i]
    t=i
    for j in range(i,len(a)):         
     if a[j][i]>y:
      y=a[j][i]
      t=j
    if y==0:return -1
    else:return t 

def swap(a,k,i): 
 for t in range(0,len(a[0])):       
  a[k][t],a[i][t]=a[i][t],a[k][t]       

def reduce(a,i):
 g=a[i][i]
 for t in range(i,len(a[0])):
  a[i][t]=round(a[i][t]/g,3)

def convert(a,i):
 g=0
 for m in range(len(a)):
  if m!=i:
   g=a[m][i]
   for z in range(i,len(a[0])):
    a[m][z]=round(a[m][z]-g*a[i][z],3)
    
def solve(a,i):
 q=check(a,i)
 if q<0:
  print("No Unique Solution")
  return 0
 swap(a,q,i)                      
 reduce(a,i)
 convert(a,i)
 for line in a:
    print ('  '.join(map(str, line)))
    
def Guass(a):
 for i in range(len(a)):
  solve(a,i)
  print()
