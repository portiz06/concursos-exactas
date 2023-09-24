# Importamos la libreria necesaria para realizar operaciones matematicas
import numpy as np

"""
La regla del trapecio nos brinda una apoximacion del area bajo la curva f, que se obtiene si se reemplaza en el intervalo [a, b] la integral de
la funcion f por la de la recta que une los puntos (a, f(a)) con (b, f(b)). En este caso, particionamos el intervalo en n particiones regulares, 
aproximando mejor este resultado, a= x_0 , ..., x_n = b . 
Al aproximar la integral f por la de la recta que une los puntos (x_k, f(x_k)) con (x_(k+1), f(x_(k+1))), podemos calcular esta ultima expresion mediante la formula de area 
de un trapecio, es decir, en este caso (x_(k+1) - x_k) / 2 * (f(x_k) + f(x_(k+1))). Y asi para cada particion regular en el intervalo [a,b], sumando sus resultados, hasta
obtener la aproximacion de la integral deseada.
"""

"""
Recibe una funcion f, un segmento [a,b], dado por su punto inicial a, y su punto final b, y un n, indicando en cuantas particiones regulares se divide el intevalo
Retorna una aproximacion numerica mediante regla del trapecio de la integral de f entre a y b
"""

def integracion_numerica(f, a, b, n):
    # Mediante np.linspace, generamos las particiones del intervalo. (Dados dos puntos a y b, y un numero n, genera n puntos equiespaciados, entre a y b)
    particiones = np.linspace(a, b, n)  
    # Iniciamos el contador para el resultado
    resultado = 0
    # Para cada particion
    for i in range(len(particiones) - 1): 
        a_i = particiones[i]
        b_i = particiones[i + 1]
        # Generamos la aproximacion del area bajo la curva de esa particion, y la sumamos al resultado
        resultado += (b_i - a_i) / 2 * (f(a_i) + f(b_i))  
    return resultado


# Veamos un ejemplo

# Definimos nuestra funcion f
def f(x):
    return 1 / np.sqrt(1 + x**2)

# Llamamos a la integracion numerica, con los parametros deseados, e imprimimos el resultado, redondeado a 4 decimales
resultado = integracion_numerica(f, 0, 1, 4)
print(round(resultado,4))
