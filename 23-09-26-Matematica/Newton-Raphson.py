def newton_raphson(f,df,x_0,tol=1e-5,N=100):
    x = x_0
    iteraciones = 0
    while iteraciones < N:
        x_prox = x - f(x)/df(x)
        if abs(x-x_prox)< tol:
            return x_prox,iteraciones
        x = x_prox
        iteraciones += 1
    print("No se alcanzó la convergencia después de", N, "iteraciones.")
    return None, iteraciones

def f(x):
    return x**15 -2

def df(x):
    return 15*x**14

raiz,iteraciones = newton_raphson(f,df,1,tol=1e-3)

if raiz != None:
    print("Se alcanzo la convergencia, luego de", iteraciones, "iteraciones, hallando la raiz:",round(raiz,3))