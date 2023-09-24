# Importamos la libreria necesaria para realizar las operaciones matematicas entre matrices o vectores 

import numpy as np

"""
El método de Jacobi es un algoritmo iterativo utilizado para resolver sistemas de ecuaciones lineales Ax = b , con A matriz cuadrada.
Encuentra una aproximación a la solución del sistema mediante iteraciones sucesivas.
Sigue el paso iterativo  x^(k+1) = D^-1(b-Rx^k). Donde D es la diagonal de A, y R es L + U, siendo L la matriz triangular inferior, y U la matriz triangular superior.
Requiere que el radio espectral sea menor a 1, (donde el radio espectral es el mayor modulo de sus autovalores)
El algoritmo propuesto se detiene cuando se alcanza una tolerancia deseada o se llega al número máximo de iteraciones.
"""

def Jacobi(A, b, tol=1e-10, m=100, x0=[]): 
    """"
   Args:
        A : Matriz de coeficientes del sistema.
        b : Vector de términos constantes.
        tol : Tolerancia para el error deseado, si no se le pasa un valor esta fijada en 1e-10.
        m : Número máximo de iteraciones permitidas, si no se le pasa un valor esta fijado en 100.
        x0 : Vector inicial (opcional), se le puede no pasar un valor.

    Returns:
        x: Vector de la solución aproximada.
        i-1: Número de iteraciones realizadas.
    """

    # Obtener el tamaño de la matriz A
    n = A.shape[0]

    # Obtener la diagonal de A
    d = np.diag(A)

    # Calcular la inversa de la diagonal de A
    invD = np.diag(1 / d)

    # Descomponer A en su parte triangular inferior (L) y superior (U)
    N = np.tril(A, -1) + np.triu(A, 1)

    # Calcula el termino D^-1 @ R donde recordemos que el @  multiplica entre matrices
    T = -invD @ N

    # Calcular el termino D^-1 @ b
    c = invD @ b

    # Calcular el radio espectral de T
    radio_espectral = np.max(np.abs(np.linalg.eigvals(T)))

    # Comprobar si el método de Jacobi convergerá
    if radio_espectral >= 1:
        # Si no converge en x retornamos un mensaje indicandolo
         print("No se encontro solución, no cumple la condicion del radio espectral")

    # Inicializar el vector x con valores aleatorios si no se proporciona uno, o si se proporciona uno con dimensiones no compatibles
    if len(x0) != n:
        x = np.random.random(n)
    else:
        x = x0

    # Inicializar un vector auxiliar para almacenar el valor anterior de x
    xold = np.zeros(n)

    # Inicializar el contador de iteraciones
    i = 0

    # Realizar iteraciones hasta que se alcance la tolerancia o el número máximo de iteraciones
    while np.linalg.norm(x - xold) > tol and i < m:
        xold = x.copy()

        # Calculamos D^-1(b+Rx)
        x = T @ x + c
        i += 1
        if i == m:
            # Si se alcanzo el numero maximo de iteraciones devolvemos el ultimo vector solucion encontrado, y el numero de iteraciones
            return x, i 

    return x, i 


# Veamos como funciona el algoritmo en dos ejemplos de uso:

A = np.array([[3, 1, 1],
              [2, 6, 1],
              [1, 1, 4]])
b = np.array([5, 9, 6])
x, iteraciones = Jacobi(A, b)

if x is not None:
    print("Solución encontrada:", x)
    print("Iteraciones realizadas:", iteraciones)

A2 = np.array([[5, 7, 6, 5],
               [7, 10, 8, 7],
               [6, 8, 10, 9],
               [5, 7, 9, 10]])
b2 = np.array([23, 32, 33, 31])

x2, iteraciones2 = Jacobi(A2, b2)
