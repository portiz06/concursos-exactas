import numpy as np
import matplotlib.pyplot as plt

def norma_matricial(A):
    n = np.shape(A[0])
    s = np.zeros(100)
    s[0] = 0 
    for i in range(1,100):
        x = np.random.random(3)
        norma_2x = np.linalg.norm(x)
        print(norma_2x)
        Ax = A @ x
        norma_2Ax = np.linalg.norm(Ax,2)
        s[i] = max(s[i-1],norma_2Ax/norma_2x)
    return s


A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

s = norma_matricial(A)

sol_exacta = np.linalg.norm(A,2)

plt.scatter(range(0,100),s)
plt.axhline(sol_exacta, c = "red")
plt.grid(True)
plt.show()

