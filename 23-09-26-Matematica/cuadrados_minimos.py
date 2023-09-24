# Importamos la libreria necesaria para realizar las operaciones matematicas entre matrices o vectores , y la necesaria para poder graficar

import numpy as np
import matplotlib.pyplot as plt

"""
La siguiente función encuentra la mejor recta que se ajusta a un conjunto de datos ponderados.
Requiere tres parámetros:
   - x: un vector con las coordenadas x de los datos.
   - y: un vector con las coordenadas y de los datos.
   - w: un vector con los pesos asociados a cada observación.

Retorna dos coeficientes 'a' y 'b' de la ecuación de la recta f(x) = ax + b que mejor se ajusta a las observaciones,
minimizando el error ponderado definido como la suma de los cuadrados de las diferencias pesadas entre las observaciones y la recta ajustada.

"""


def encontrar_mejor_recta(x, y, w):
    # Calculamos las sumas necesarias para las fórmulas de mínimos cuadrados ponderados
    
    # Suma de los pesos
    suma_w = np.sum(w)
    
    # Suma pesada de x
    suma_wx = np.sum(w * x)
    
    # Suma ponderada de y
    suma_wy = np.sum(w * y)
    
    # Suma pesada de xy
    suma_wxy = np.sum(w * x * y)
    
    # Suma ponderada de x al cuadrado
    suma_wx_cuadrado = np.sum(w * x**2)

    # Calculamos los coeficientes 'a' y 'b' usando las fórmulas de mínimos cuadrados ponderados
    a = (suma_w * suma_wxy - suma_wx * suma_wy) / (suma_w * suma_wx_cuadrado - suma_wx**2)
    b = (suma_wy - a * suma_wx) / suma_w
    
    return a, b

# Veamos un ejemplo

# Datos de prueba
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5.01, 7.02, 9.1, 11.1])
w = np.array([1, 0.5, 1, 0.5, 0.5])

# Llama a la función para encontrar la mejor recta, en el sentido de aproximacion a los datos
a, b = encontrar_mejor_recta(x, y, w)

# Ploteamos los resultados 

plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Datos', color='blue')
plt.plot(x, a * x + b, label=f'Recta ajustada: {a:.2f}x + {b:.2f}', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Ajuste de Mínimos Cuadrados Ponderados')
plt.show()

# Imprime los resultados
print("La mejor recta es: {:.2f}x + {:.2f}".format(a, b))