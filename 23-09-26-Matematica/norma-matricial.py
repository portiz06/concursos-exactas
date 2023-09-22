import numpy as np
import matplotlib.pyplot as plt

def norma2(A: np.array):
    s = np.zeros(100)
    for i in range(1,100):
        x = np.random.rand(3)
        norma2_x = np.linalg.norm(x)
        Ax = np.dot(A, x)
        norma2_Ax = np.linalg.norm(Ax,2)
        s[i] = max(s[i-1], norma2_Ax/norma2_x)
    norma_exacta = np.linalg.norm(A,2)
    plt.plot(range(0,100),s)
    plt.axhline(y = norma_exacta, color = 'r', linestyle = '-')
    plt.show()   
    
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
norma2(matriz) 