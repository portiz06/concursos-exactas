import numpy as np

def Jacobi(A,b,tol=1e-10,m=100,x0=[]): # Elegimos una tolerancia para nuestro error y un máximo de 100 iteraciones
    n    = A.shape[0]
    d    = np.diag(A)
    invD = np.diag(1/d)     # Es la inversa de D
    N    = np.tril(A,-1)+np.triu(A,1)
    T   = -invD@N           # Matriz de iteraciones de Jacobi
    c    = invD@b
     # Calcular el radio espectral de T
    radio_espectral = np.max(np.abs(np.linalg.eigvals(T)))

    if radio_espectral >= 1:
        print("El método de Jacobi no converge debido al radio espectral >= 1.")
        return None, 0
    if len(x0) == 0:        # Si no se ingresa un vector inicial, le damos un vector inicial aleatorio  
        x = np.random.random(n)
    else:
        x = x0

    xold = np.zeros(n)       
    i=0
    while np.linalg.norm(x-xold)>tol and i<m: 
        xold=x.copy()      #### SIEMPRE USAR COPY PARA VECTORES Y MATRICES
        x = T@x + c
        i=i+1
        if i==m:
            print('ATENCIÓN: se alcanzó el número máximo de iteraciones')
    return x,i-1           ### pido el vector solución y la cantidad de iteraciones realizadas


# Ejemplos de usos:
A = np.array([[3, 1, 1],
              [2, 6, 1],
              [1, 1, 4]])
b = np.array([5, 9, 6])
x, iteraciones = Jacobi(A, b)

if x is not None:
    print("Solución encontrada:", x)
    print("Iteraciones realizadas:", iteraciones)

A2 = np.array([[5,7,6,5],
               [7,10,8,7],
               [6,8,10,9],
               [5,7,9,10]])
b2 = np.array([23,32,33,31])
x2,iteraciones2 = Jacobi(A2,b2)
if x2 is not None:
    print("Solución encontrada:", x2)
    print("Iteraciones realizadas:", iteraciones2)
