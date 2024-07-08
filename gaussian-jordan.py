from numpy import linalg , matrix

def gaussian_jordan(A, B):
  size = len(A)
  
  for j in range(size):
    r = A[j][j]
    A[j] = [m / float(r)  for m in A[j]]
    B[j][0] /= float(r)
    
    for i in range(size):
      if i != j:
        zarib = A[i][j]
        B[i][0] -= abs(B[j][0] * zarib) 
        
        for k in range(size):
          A[i][k] -= abs(A[j][k] * zarib) 
          
  return B
        

def gaussian_jordan_inverse(A):
  size = len(A)
  
  inverse = [[0 for _ in range(size)] for _ in range(size)]
  
  for i in range(size):
    for j in range(size):
      if i == j :
        inverse[i][j] = 1
  
  for j in range(size):
    r = A[j][j]
    A[j] = [m / float(r)  for m in A[j]]
    inverse[j] = [x / float(r) for x in inverse[j]]
    for i in range(size):
      if i != j:
        zarib = A[i][j]
        
        for k in range(size):
          A[i][k] -= abs(A[j][k] * zarib)
          inverse[i][k] -= abs(inverse[j][k] * zarib)
          
  return inverse
        
        

size = int(input("enter A matrix size: "))

A = [[0] * size for i in range(size)]
for i in range(size):
  for j in range(size):
    A[i][j] = int(input(f"enter a{i}{j}: "))
    
B = [[0] for i in range(size)]
for i in range(size):
  B[i] = [int(input(f"enter b{i}: "))]
  

if linalg.det(A) == 0 :
  print("Your matrix doesn't have inverse!")
else :
  answer = gaussian_jordan(A, B)
  Inverse = gaussian_jordan_inverse(A)
  print("x = ","\n" ,matrix(answer))
  print("A Inverse = ", "\n", matrix(Inverse))

