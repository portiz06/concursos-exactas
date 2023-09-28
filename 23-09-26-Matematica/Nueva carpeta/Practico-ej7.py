"""
Sea a = x0, . . . , xn = b una partición regular de [a, b]. Implementar un programa
que reciba una función f, los límites del intervalo [a, b] y un parámetro
n y que mediante la regla de trapecios devuelva un valor aproximado de
la integral entre a y b de f,partiendo [a, b] en n intervalos.
"""
import numpy as np

def regla_trapecio(f,a,b,n):
    intervalos = np.linspace(a,b,n)
    resultado = 0
    for i in range(1,len(intervalos)):
        a_i = intervalos[i-1]
        b_i = intervalos[i]
        resultado += (b_i-a_i)/2 *(f(b_i)+f(a_i)) 
    return resultado

def f(x):
    return 1/ np.sqrt(1+x**2)

print(round(regla_trapecio(f,0,1,4),4))