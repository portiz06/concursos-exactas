"""
Implementar un programa que reciba como input una función f, su derivada
f′, un punto inicial x0, una tolerancia ε y un entero N y aplique el método de
Newton-Raphson para buscar una raíz de f a partir de x0. El programa debe
finalizar cuando |xn − xn−1| < ε o cuando llega al paso N. Si no se alcanza la
convergencia luego de N pasos, imprimir un mensaje de error.
(b) Para f(x) = x15 − 2 implementando el programa del item anterior, hallar
una aproximación del cero de la función comenzando con x0 = 1, usando una
tolerancia de 10−3.

"""

import numpy as np
import matplotlib.pyplot as plt

def newtonraphson(f,df,x_0,tol=1e-6,N=100):
    x = x_0+10
    x_new = x_0
    iteraciones = 0
    while abs(x_new -x) >= tol and iteraciones < N:
        x = x_new
        x_new = x - f(x)/df(x)
        iteraciones += 1
    
    if iteraciones == N and np.abs(x_new -x) >= tol:
        print("No se alcanzo la convergencia luego de",N,"pasos")
        return None
    
    return x_new

def f(x):
    return x**15-2

def df(x):
    return 15*x**14

raiz = newtonraphson(f,df,1,1e-3)

x = np.linspace(-5,5,500)
plt.plot(x,f(x))
plt.scatter(raiz,0)
plt.grid(True)
plt.show()
print(raiz)
