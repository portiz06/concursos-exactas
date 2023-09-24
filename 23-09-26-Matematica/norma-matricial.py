# Importamos la libreria necesaria para realizar las operaciones matematicas entre matrices o vectores , y la necesaria para poder graficar



import numpy as np
import matplotlib.pyplot as plt

"""
Se quiere estimar la norma 2 de una matriz A ∈ R3x3. Para eso generaremos la estimacion como el máximo del valor ∥Ax∥_2/∥x∥_2 entre varios vectores x ∈ R3 no nulos generados al azar.
Y veremos graficamente las sucesivas aproximaciones generadas en 100 vectores x distintos, eligiendo siempre el maximo del valor ∥Ax∥_2/∥x∥_2
"""


"""
   Requiere una matriz cuadrada de 3*3, 
   Retorna un grafico de la sucesion de aproximaciones a la norma 2 de la matriz ingresada, comparada con la norma exacta
"""

def norma2(A: np.array):
    # Generamos un vector donde iremos guardando nuestras sucesivas aproximaciones
    s = np.zeros(100)
    # Hacemos 100 iteraciones
    for i in range(1,100):
        # Generamos un vector de R^3 aleatorio con coordenadas en el intervalo [0,1]
        x = np.random.random(3)
        # Calculamos la norma 2 de x
        norma2_x = np.linalg.norm(x)
        # Calculamos Ax, recordando que el operador @ de numpy nos devuelve la multiplicacion entre matrices, o entre matriz y vector
        Ax = A @ x
        # Calculamos la norma 2 de Ax
        norma2_Ax = np.linalg.norm(Ax,2)
        # Nos quedamos con el maximo en cada iteracion
        s[i] = max(s[i-1], norma2_Ax/norma2_x)
    # Calculamos la norma 2 exacta de A, para comparar con nuestras aproximaciones
    norma_exacta = np.linalg.norm(A,2)

   # Graficamos para el rango 0 a 100 el vector s con aproximaciones de la norma 2, y agregamos con otro color el calculo de la norma exacta
    plt.scatter(range(0, 100), s, label="Aproximación de la Norma 2")
    plt.axhline(y=norma_exacta, color='r', linestyle='-', label="Norma 2 Exacta")
    plt.xlabel("Iteraciones")
    plt.ylabel("Valor de la Norma 2")
    plt.legend()
    plt.title("Estimación de la Norma 2 de la Matriz A")
    plt.show()
 
    
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
norma2(matriz) 