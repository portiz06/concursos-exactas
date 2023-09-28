"""
Cuadrados mínimos.
(a) Implementar una función que reciba vectores de datos x, y y un vector de pesos
positivos w y devuelva la función f(x) = ax + b que minimiza el error
X
0≤i≤n
wi(yi − f(xi))2.
(b) Testear el programa para la siguiente tabla de datos
x 1 2 3 4 5
y 3 5.01 7.02 9.1 11.1
w 1 0.5 1 0.5 0.5
"""


import numpy as np
import matplotlib.pyplot as plt

def cuadrados_minimos(x,y,w):
    suma_w = np.sum(w)
    suma_wx = np.sum(x*w)
    suma_wy = np.sum(y*w)
    suma_wx2 = np.sum(w* x**2)
    suma_wxy = np.sum(w*x*y)

    a = (suma_wx * suma_wy - suma_w * suma_wxy)/ (suma_wx**2 - suma_w * suma_wx2)
    b = (suma_wy-a*suma_wx)/suma_w

    return a,b

x = np.array([1,2,3,4,5])
y = np.array([3,5.01,7.02,9.1,11.1])
w = np.array([1,0.5,1,0.5,0.5])

a,b = cuadrados_minimos(x,y,w)

def recta(a,b,x):
    return a*x+b

plt.scatter(x,y)
plt.plot(x,recta(a,b,x))
plt.grid(True)
plt.show()

