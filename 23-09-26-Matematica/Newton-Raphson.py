
"""
El metodo de Newton-Raphson es un metodo utilizado para encontrar alguna raiz de una funcion f, para esto la idea del metodo es “ir por la tangente”.
Se empieza con x_0. Se traza la tangente en x_0 y se define x_1 como la interseccion de la tangente con el eje x. 
Luego se traza la tangente por x_1 y se toma x_2 la interseccion de la tangente con el eje x, y asi sucesivamente, 
hasta llegar a que esta sucesion converja para algun x_n, con alguna tolerancia, teniendo en cuenta posibles errores numericos , o raices irracionales por ejemplo
donde no se logre la igualdad exacta entre dos valores sucesivos.
Definimos f(x_n) + (x_(n+1)-x_n)*df(x_n) = 0, y a partir de alli despejamos x_(n+1) como 
x_(n+1) = x_n - f(x_n)/df(x_n)

Requiere una funcion f, su derivada df, un x_0 punto inicial, un valor de tolerancia (si no esta dado, por defecto es 1e-5),
y un numero de iteraciones maximas a realizar (si no esta dado,por defecto es 100)

Retorna una raiz de la funcion f original, y la cantidad de iteraciones realizadas hasta hallarla
"""

def newton_raphson(f,df,x_0,tol=1e-5,N=100):
    # Fijamos como x inicial el x_0
    x = x_0
    # Iniciamos el contador de iteraciones
    iteraciones = 0
    # Hasta llegar al tope de iteraciones
    while iteraciones < N:
        # Generamos el paso x_(n+1) = x_(n) - f(x_n)/df(x_n)
        x_prox = x - f(x)/df(x)
        # Si ya pase mi umbral de tolerancia, retorno la solucion encontrada
        if abs(x-x_prox)< tol:
            return x_prox,iteraciones
        x = x_prox
        iteraciones += 1
    # Si luego de las N iteraciones, no logre superar la tolerancia deseada, retorno que no se logro la convergencia
    print("No se alcanzó la convergencia después de", N, "iteraciones.")
    return None, iteraciones


# Ejemplo de uso 

# Definimos la funcion f, y su derivada df
def f(x):
    return x**15 -2

def df(x):
    return 15*x**14

# Llamamos a la funcion
raiz,iteraciones = newton_raphson(f,df,1,tol=1e-3)

if raiz != None:
    print("Se alcanzo la convergencia, luego de", iteraciones, "iteraciones, hallando la raiz:",round(raiz,3))