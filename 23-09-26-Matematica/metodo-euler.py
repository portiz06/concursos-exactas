# Importamos la libreria necesaria para realizar las operaciones matematicas entre matrices o vectores , y la necesaria para poder graficar


import numpy as np
import matplotlib.pyplot as plt

"""
El metodo de Euler sirve para aproximar numericamente las soluciones de una ecuacion diferencial, utilizando un dato inicial x_0 en t_0, y la ecuacion, podemos generar el valor de la
pendiente de la recta tangente en (t_0,x(t_0)). Y suponiendo un paso h, muy chico, donde la recta tangente aproxime bien a la funcion, podemos determinar que 
x(t_1) = x(t_0+h) = x(t_0) + h*f(t_0,x(t_0)), y asi prosiguiendo hasta llegar a t_f, tiempo final esperado para la solucion de la ecuacion diferencial, siguiendo la sucesion dada por 
x(t_n+1) = x(t_n) + h*f(t_n,x(t_n))
"""

"""
Requiere una funcion f (donde x' = f(t,x(t))) , un tiempo inicial t_0, un tiempo final t_f, un valor x_0 tal que f(t_0) = x_0, y un paso h (por defecto, si no se agrega tiene valor 0.1)
Devuelve un vector de tiempos T, con comienzo en t_0 y final en t_f, y un vector x, con las soluciones x(t), para todo t perteneciente al vector T, ambos necesarios para graficar la
solucion aproximada 
"""

def metodo_euler(f,t_0,t_f,x_0,h=0.1):
    # Genera una vector que tiene comienzo en t_0, fin en t_f, con pasos de h unidades
    t = np.arange(t_0,t_f,h)
    n = len(t)
    # Generamos un vector para guardar las soluciones en todo los tiempos de t
    x = np.zeros(n)
    # Definimos el x en tiempo t_0 como el x_0 (por condicion inicial) 
    x[0] = x_0
    # Hacemos las iteraciones del metodo, aproximando en cada paso por la tangente, guardando los resultados en el vector
    for i in range(0,n-1):
        # x(t_n+1) = x(t_n) + h*f(t_n,x(t_n))
        x[i+1] = x[i] + h*f(t[i],x[i])
    # Retornamos los vectores de tiempo, y de soluciones aproximadas, para poder graficar la solucion
    return t,x

# Vemos un ejemplo de uso 

# Definimos la funcion x´
def ejemplo(t,x):
    return x
# Llamamos al metodo de euler

t,x = metodo_euler(ejemplo,0,5,1,0.1)

# Calculamos la solución real
x_real =  np.exp(t)

# Graficamos ambas soluciones y vemos como aproxima el metodo, a la solucion real
plt.plot(t, x, label='Aproximación de x(t)')
plt.plot(t, x_real, label='Solución Real')
plt.xlabel('Tiempo (t)')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()