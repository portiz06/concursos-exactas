""""

Escribir un programa que implemente el método de Euler explícito para aproximar numéricamente la solución x(t) de la siguiente ecuación
diferencial en el intervalo [t0, tF ]:

"""
import numpy as np
import matplotlib.pyplot as plt

def metodo_euler(f,x_0,t_0,t_f,h):
    t = np.arange(t_0,t_f+0.0001,h)
    n = len(t)
    x = np.zeros(n)
    x[0] = x_0
    for i in range (1,n): 
        x[i] = x[i-1] + h*f(t[i-1],x[i-1])
    
    return t,x

def metodo_euler2(f,x_0,t_0,t_f,n):
    t = np.linspace(t_0,t_f,n)
    x = np.zeros(n)
    x[0] = x_0
    for i in range (1,n) :
        x[i] = x[i-1] + h*f(t[i-1],x[i-1])

    return t,x

def f(t,x):
    return x 

x_0 = 1
t_0 = 0
t_f = 5
h = 0.1
n = 51

t,x = metodo_euler(f,x_0,t_0,t_f,h)

sol_exacta = np.exp(t)


plt.plot(t,x)
plt.plot(t,sol_exacta)
plt.grid(True)
plt.show()

