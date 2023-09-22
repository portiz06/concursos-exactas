import numpy as np
import matplotlib.pyplot as plt

def metodo_euler(f,t_0,t_f,x_0,h):
    t = np.arange(t_0,t_f,h)
    n = len(t)
    x = np.zeros(n)
    x[0] = x_0
    for i in range(0,n-1):
        x[i+1] = x[i] + h*f(x[i])
    
    return t,x

def ejemplo(x):
    return 1/x

t,x = metodo_euler(ejemplo,0,5,1,0.1)


    
plt.plot(t, x, label='Aproximación de x(t)')
plt.xlabel('Tiempo (t)')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()