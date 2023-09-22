import numpy as np
import matplotlib.pyplot as plt

def encontrar_mejor_recta(x, y, w):
    # Calcula las sumas necesarias
    suma_w = np.sum(w)
    suma_wx = np.sum(w * x)
    suma_wy = np.sum(w * y)
    suma_wxy = np.sum(w * x * y)
    suma_wx_cuadrado = np.sum(w * x**2)

    # Calcula los coeficientes 'a' y 'b' usando las fórmulas de mínimos cuadrados ponderados
    a = (suma_w * suma_wxy - suma_wx * suma_wy) / (suma_w * suma_wx_cuadrado - suma_wx**2)
    b = (suma_wy - a * suma_wx) / suma_w
    return a, b

# Datos de prueba
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5.01, 7.02, 9.1, 11.1])
w = np.array([1, 0.5, 1, 0.5, 0.5])

# Llama a la función para encontrar la mejor recta
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