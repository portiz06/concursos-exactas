"""
Escribir un programa que implemente el método de Jacobi para la resolución
de un sistema lineal Ax = b, con las siguientes condiciones:
• que al inicio calcule el radio espectral del método y que termine si es mayor
o igual a 1,
• que finalice si el método se estaciona,
• que finalice si se excede cierto tope de iteraciones.

"""

import numpy as np

def jacobi(A,b,x_0=[],it=100,tol=1e-10):
    n = np.shape(A[0])

   
    
    D = np.diag(A)
    L = np.tril(A,-1)
    U = np.triu(A,1)

    inv_D = np.diag(1/D)

    c = inv_D @ b

    T = -inv_D @ (L+U)

    if max(np.abs(np.linalg.eigvals(T))) >= 1:
        print("Radio espectral mayor a 1")
        return None,0

    cont = 0 

    if len(x_0) != n :
        x = np.random.random(n)
    else :
        x = x_0

    x_old = np.zeros(n)

    while cont < it and  np.linalg.norm(x_old - x) > tol:
        x_old = x
        x = T @ x + c 
        cont += 1
    if cont == it:
        print("Se alcanzaron las iteraciones propuestas")
    
    
    return x,cont

A = np.array([[3,1,1],
              [2,6,1],
              [1,1,4]])
b = np.array([5,9,6])

A2 = np.array([[5,7,6,5],
              [7,10,8,7],
              [6,8,10,9],
              [5,7,9,10]])
b2 = np.array([23,32,33,31])
print(jacobi(A2,b2))
