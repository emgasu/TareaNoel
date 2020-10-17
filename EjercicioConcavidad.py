#Ejercicio Concavidad

import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    return (x*x*x*x)

def derivada1(x):
  return (4*x*x*x)
def derivada2(x):
  return (12*x*x)

x=np.linspace(-2, 2, 21)

for x_ in x:
  if x_==0:
      print(x_,"Cero")
  else:
      print(x_,"Concava hacia arriba")
y=funcion(x)
plt.plot(x, y) 

