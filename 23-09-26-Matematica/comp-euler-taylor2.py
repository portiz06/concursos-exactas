import numpy as np
import matplotlib.pyplot as plt

def metodo_euler(f,t_0,t_f,x_0,h):
    t = np.arange(t_0,t_f,h)
    n = len(t)
    x = np.zeros(n)
    x[0] = x_0
    for i in range(0,n-1):
        x[i+1] = x[i] + h*f(t[i],x[i])
    
    return x

def taylor2(f,df_x,df_t,t_0,t_f,x_0,h):
    t = np.arange(t_0,t_f,h)
    n = len(t)
    x = np.zeros(n)
    x[0] = x_0
    for i in range(0,n-1):
        x[i+1] = x[i] + h*f(t[i],x[i]) + (h**2)/2*(f(t[i],x[i])*df_x(t[i],x[i])+df_t(t[i],x[i]))
    
    return x

def f(t,x):
    return x

def df_x(t,x):
    return x

def df_t(t,x):
    return x 

sol_en_tf = np.exp(1)

errores_euler = []
errores_taylor = []


t_0 = 0
t_f = 1
x_0 = 1

valores_h = [0.1,0.05,0.01,0.005,0.001,0.0005]

##
for h in valores_h:
    sol_euler = metodo_euler(f,t_0,t_f,x_0,h)
    sol_taylor = taylor2(f,df_x,df_t,t_0,t_f,x_0,h)

    error_en_tf_euler = np.abs(sol_euler[-1] - sol_en_tf)
    error_en_tf_taylor = np.abs(sol_taylor[-1] - sol_en_tf)

    errores_euler.append(error_en_tf_euler)
    errores_taylor.append(error_en_tf_taylor)

log_valores_h =  np.log(valores_h)
log_errores_euler = np.log(errores_euler)
log_errores_taylor = np.log(errores_taylor)


plt.figure()
plt.plot(log_valores_h, log_errores_euler, label='Euler')
plt.plot(log_valores_h, log_errores_taylor, label='Taylor (2do orden)')
plt.xlabel('log(h)')
plt.ylabel('log(EN)')
plt.legend()
plt.grid(True)
plt.title('Convergencia de Métodos Numéricos')
plt.show()
##