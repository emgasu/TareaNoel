#Ejercicio puntos criticos

import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
   return pow(x,4) /4 - 9 * pow(x,2)  /2
def derivada1(x):
  return (x*x*x)-(9(x))
def derivada2(x):
  return 3*(x*x) -9

# Grafica
x=np.linspace(-5, 5, 51)

for x_ in x:
  if x_<3:
      if x_<-3:
          print(x_,"Concava hacia arriba")
      if x_>-3:
          print(x_,"Concava hacia abajo")
  else:
      print(x_,"Concava hacia arriba")
y=funcion(x)
plt.plot(x, y) 
y1=funcion(-3)
y2=funcion(3)
plt.plot(3,y1, marker="o", color="red")
plt.plot(-3,y2, marker="o", color="red")

print("Los mínimos relativos ocurren en f en los puntos (-3,-20.25) y (3,-20.25); y un máximo relativo se presenta en (0, 0). ")