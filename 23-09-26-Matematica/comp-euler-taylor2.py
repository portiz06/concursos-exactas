# Importamos las librerias necesarias para realizar calculos matematicos, y graficar
import numpy as np
import matplotlib.pyplot as plt

"""
Se quiere verificar numéricamente el orden de convergencia de los métodos de Euler y Taylor de orden 2.
Para eso estudiaremos sus errores
Recordemos que ambos metodos resuelven ecuaciones diferenciales ordinarias de manera numerica, mediante aproximaciones sucesivas desde un tiempo inicial, donde se encuentra el dato inicial, 
hasta llegar a un tiempo final desdeado, con pasos muy pequeños.
Las iteraciones del metodo de Euler estan dadas por x(t_i + h) = x(t_i) + h*f(t_i,x_i)
Las iteraciones en el metodo de Taylor de 2do orden estan dadas por x(t_i + h) = x(t_i) + h*f(t_i,x_i) + (h^2)/2 * (f(t_i, x_i) * f_x(t_i, x_i) + f_t(t_i, x_i))
"""

# Definición de la función que implementa el método de Euler para resolver una Ecuación Diferencial Ordinaria (EDO).
"""
Requiere una funcion f(tal que x'(t) = f(t,x)), un tiempo inicial t_0, un tiempo final t_f, un dato inicial x_0, es decir x(t_0) = x_0, y un paso h
Retorna un vector con la aproximacion numerica de la solucion  de la EDO con tiempos entre t_0 y t_f, con pasos h

"""
def metodo_euler(f, t_0, t_f, x_0, h):
    # Generamos un arreglo de tiempo desde t_0 hasta t_f con pasos de tamaño h.
    t = np.arange(t_0, t_f, h)
    n = len(t)
    x = np.zeros(n)  # Vector para almacenar las soluciones
    x[0] = x_0  # La condición inicial.
    
    # Implementación del método de Euler. 
    for i in range(0, n - 1):
        x[i + 1] = x[i] + h * f(t[i], x[i])
    
    return x

# Definición de la función que implementa el método de Taylor de segundo orden para resolver una EDO.

"""
Requiere una funcion f(tal que x'(t) = f(t,x)), df_x (la derivada de f respecto de x), df_t (la derivada de f respecto de t),
un tiempo inicial t_0, un tiempo final t_f, un dato inicial x_0, es decir x(t_0) = x_0, y un paso h
Retorna un vector con la aproximacion numerica de la solucion  de la EDO con tiempos entre t_0 y t_f, con pasos h

"""
def taylor2(f, df_x, df_t, t_0, t_f, x_0, h):
    # Generamos un arreglo de tiempo desde t_0 hasta t_f con pasos de tamaño h.
    t = np.arange(t_0, t_f, h)
    n = len(t)
    x = np.zeros(n) # Vector para almacenar las soluciones
    x[0] = x_0 # Condicion inicial

    
    # Implementación del método de Taylor de segundo orden.
    for i in range(0, n - 1):
        x[i + 1] = x[i] + h * f(t[i], x[i]) + (h**2) / 2 * (f(t[i], x[i]) * df_x(t[i], x[i]) + df_t(t[i], x[i]))
    
    return x

"""
 Veamos un ejemplo de uso con la ecuacion x' = x // x(0) = 1. 
 Analiticamente se puede comprobar claramente que la solucion a la ecuacion diferencial es e^t.
 Lo que haremos sera resolverla con ambos metodos, y comparar las soluciones aproximadas, con la solucion analitica exacta, viendo sus errores en forma logaritmica, asi los podemos apreciar
 linealmente, lo que nos facilita la comparacion.
"""
# Definición de la ecuacion diferencial a resolver: dx/dt = f(t,x) = x
def f(t, x):
    return x

# Derivada de f(t,x) con respecto a x , que es simplemente 1.
def df_x(t, x):
    return 1

# Derivada de f(t,x) con respecto a t , que en este caso es 0 ya que no depende de t.
def df_t(t, x):
    return 0

# Valor de la solución exacta en t_f = 1.
sol_en_tf = np.exp(1)

# Listas para almacenar los errores en la estimación de la solución.
errores_euler = []
errores_taylor = []

# Condiciones iniciales y valores de h (los pasos de tiempo) que vamos a probar.
t_0 = 0
t_f = 1
x_0 = 1
valores_h = [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005]

# Ciclo para iterar a través de diferentes valores de h y calcular los errores.
for h in valores_h:
    # Resolver la EDO usando el método de Euler.
    sol_euler = metodo_euler(f, t_0, t_f, x_0, h)
    
    # Resolver la EDO usando el método de Taylor de segundo orden.
    sol_taylor = taylor2(f, df_x, df_t, t_0, t_f, x_0, h)

    # Calcular el error en t_f para cada método.
    error_en_tf_euler = np.abs(sol_euler[-1] - sol_en_tf)
    error_en_tf_taylor = np.abs(sol_taylor[-1] - sol_en_tf)

    # Almacenamos los errores.
    errores_euler.append(error_en_tf_euler)
    errores_taylor.append(error_en_tf_taylor)

# Tomar el logaritmo de los valores de h y los errores para realizar una gráfica log-log.
log_valores_h = np.log(valores_h)
log_errores_euler = np.log(errores_euler)
log_errores_taylor = np.log(errores_taylor)

"""
Lo que se espera ver en la gráfica log-log es una representación de la convergencia de los métodos numéricos en función del tamaño del paso de tiempo elegido (h).
En general, se espera observar que a medida que h disminuye (es decir, se utilizan más pequeños), los errores en la estimación de la solución se reducen, lo que indica una mayor precisión. 
Además, tambien se espera que el método de Taylor de segundo orden sea más preciso que el método de Euler, 
ya que el método de Taylor de segundo orden tiene un error de truncamiento de orden superior.

"""

# Graficar los resultados.
plt.figure()
plt.plot(log_valores_h, log_errores_euler, label='Euler')
plt.plot(log_valores_h, log_errores_taylor, label='Taylor (2do orden)')
plt.xlabel('log(h)')
plt.ylabel('log(error en tiempo final)') 
plt.legend()
plt.grid(True)
plt.title('Convergencia de Métodos Numéricos')
plt.show()

"""
El resultado es consistente, se observa que a medida que h disminuye (se mueve hacia la izquierda en el gráfico), los errores tienden a disminuir 
Y ademas, lo hacen de manera mas pronunciada para el metodo de Taylor de segundo orden en comparación con el método de Euler, 
lo que demuestra que el método de Taylor es más preciso en este contexto.
Además, las líneas de ambas aproximaciones son aproximadamente rectas en el gráfico log-log, esto indica que los métodos convergen, lo cual es el resultado esperado.
"""