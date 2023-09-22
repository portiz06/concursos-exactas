import numpy as np

def integracion_numerica(f, a, b, n):
    particiones = np.linspace(a, b, n)  # Corregir "linespace" a "linspace"
    resultado = 0
    for i in range(len(particiones) - 1):  # Corregir "len" en lugar de "len(particiones)-1"
        a_i = particiones[i]
        b_i = particiones[i + 1]
        resultado += (b_i - a_i) / 2 * (f(a_i) + f(b_i))  # Corregir la llamada a la función f(a_i) y f(b_i)
    return resultado

def f(x):
    return 1 / np.sqrt(1 + x**2)

resultado = integracion_numerica(f, 0, 1, 4)
print(round(resultado,4))