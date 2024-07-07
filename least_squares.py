import numpy as np

def gram_schmidt(matrix):
    m, n = matrix.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for j in range(n):
        v = matrix[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i], matrix[:, j])
            v = v - R[i, j] * Q[:, i]
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = v / R[j, j]

    return Q, R

def least_squares_qr(A, b):
    Q, R = gram_schmidt(A)
    Qb = np.dot(Q.T, b)
    x = np.linalg.solve(R, Qb)
    r = b - np.dot(A, x)
    error_norm = np.linalg.norm(r)

    return x, error_norm, Q, R

size = int(input("enter A matrix size: "))

A = [[0] * size for i in range(size)]
for i in range(size):
  for j in range(size):
    A[i][j] = int(input(f"enter a{i}{j}: "))
    
B = [0 for _ in range(size)]
for i in range(size):
  B[i] = [int(input(f"enter b{i}: "))]

A = np.array(A)
B = np.array(B)

x, error_norm, Q, R = least_squares_qr(A, B)

print("the least squares answer:")
print(x)
print("error norm:")
print(error_norm)
print("Q matrix:")
print(Q)
print("R matrix:")
print(R)