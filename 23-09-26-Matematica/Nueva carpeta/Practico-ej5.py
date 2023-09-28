"""
Se quiere verificar numéricamente el orden de convergencia
de los métodos de Euler y Taylor de orden 2. Para ello: resolver numéricamente
el problema

en el intervalo [0, 1] con ambos métodos, tomando h = 0.1, 0.05, 0.01, 0.005, 0.001
y 0.0005.
Obtener la solución exacta y para cada h, calcular el error que se comete al aproximar
x(1): EN = |x(1) − xN| . Graficar log(EN) en función de log(h). ¿Qué se espera
ver? ¿El resultado es consistente con el esperado?

"""
import numpy as np
import matplotlib.pyplot as plt

def euler(f,x_0,t_0,t_f,h):
    t = np.arange(t_0,t_f+0.00001,h)
    x= np.zeros(len(t))
    x[0] = x_0
    for i in range(1,len(t)):
        x[i] = x[i-1] + h*f(t[i-1],x[i-1])
    
    return x

def taylor2(f,fx,ft,x_0,t_0,t_f,h):
    t = np.arange(t_0,t_f+0.00001,h)
    x= np.zeros(len(t))
    x[0] = x_0
    for i in range(1,len(t)):
        x[i] = x[i-1]  + h*f(t[i-1],x[i-1]) + ((h**2)/2)* (f(t[i-1],x[i-1]) * fx(t[i-1],x[i-1]) + ft(t[i-1],x[i-1]))
    
    return x

def f(t,x):
    return x

def ft(t,x):
    return x

def fx(t,x):
    return 0
sol_exacta = np.exp(1)
    


valores_h = [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005]
errores_euler = np.zeros(len(valores_h))
errores_taylor2 = np.zeros(len(valores_h))

for i in range(0,len(valores_h)):
    errores_euler[i] = abs(euler(f,1,0,1,valores_h[i])[-1] - sol_exacta)
    errores_taylor2[i] = abs(taylor2(f,fx,ft,1,0,1,valores_h[i])[-1] - sol_exacta)

log_valores_h = np.log(valores_h)
log_errores_euler = np.log(errores_euler)
log_errores_taylor2 = np.log(errores_taylor2)

plt.plot(log_valores_h,log_errores_euler,c = "red",label = "Euler")
plt.plot(log_valores_h,log_errores_taylor2,c = "blue",label = "Taylor(orden 2)")
plt.xlabel("Logaritmo de valores de h")
plt.ylabel("Logaritmo de errores en t = 1")
plt.grid(True)
plt.legend()
plt.show()