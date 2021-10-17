import numpy as np
import matplotlib.pyplot as plt

#Solucion exacta de la funcion a)
"""
def y_solucion(t):
  return t*np.log(t) +2*t

def y_prima(t,y):
  return 1+(y/t)
"""
#Solucion exacta de la funcion b)
def y_solucion(t):
  return t-np.exp(-5*t)

def y_prima(t,y):
  return 5*np.exp(5*t)*(y-t)**(2)+1

def RungeKutta2(t0, y0,h,maximo,f_sol,f_p):
	t_anterior=t0
	y_anterior=y0
	t_posterior = t_anterior + h

	for i in range(maximo):
		k1=f_p(t_anterior, y_anterior)
		k2=f_p(t_posterior, y_anterior + h * k1)
		y_posterior= y_anterior + 0.5 * h *(k1+k2)

		#Calculo los errores
		error_local = np.abs(y_posterior-y_anterior)
		error_global = np.abs(y_posterior-f_sol(t_posterior))
		print(f"{i+1}: [t: {t_posterior}, y: {y_posterior}] , [EL: {error_local}, EG: {error_global}]")

		#Para la proxima iteraccion
		t_anterior=t_posterior
		y_anterior=y_posterior
		t_posterior = t_anterior + h
		#pass
	


#Intervalos
a=1
b=2
h=10**(-4)
#Valores iniciales
t0=a
y0=y_solucion(t0)
maximo=int((b-a)/h) #Numero de iteracciones

print(f"0: [t: {t0}, y: {y0}] ")
RungeKutta2(t0,y0,h,maximo,y_solucion,y_prima)