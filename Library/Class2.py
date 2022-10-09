#Function for returning the row number of the largest element of a column
def check(a,i):
    y=a[i][i]
    t=i
    for j in range(i,len(a)):         
     if abs(a[j][i])>abs(y):
      y=a[j][i]
      t=j
    if y==0:return -1               
    else:return t                    

#Swap is used to swap two rows k and i
def swap(a,k,i): 
 for t in range(0,len(a[0])):       
  a[k][t],a[i][t]=a[i][t],a[k][t]       

#Reduce is used to turn the diagonal element of a row to 1
def reduce(a,i):
 g=a[i][i]
 for t in range(i,len(a[0])):
  a[i][t]=round(a[i][t]/g,3)

#Convert is used to turn all non diagonal elements of a column to 0
def convert(a,i):
 g=0
 for m in range(len(a)):
  if m!=i:
   g=a[m][i]
   for z in range(i,len(a[0])):
    a[m][z]=round(a[m][z]-g*a[i][z],3)
 
#Solve turns one column into that of an identity matrix  
def solve(a,i):
 q=check(a,i)
 if q<0:
  print("No Unique Solution")
  return 0
 swap(a,q,i)                      
 reduce(a,i)
 convert(a,i)
 

#Guass performs solve() on every column of the matrix   
def Guass(a):
 for i in range(len(a)):
  solve(a,i)
 for line in a:
  print ('  '.join(map(str, line)))
 print()
