#Ejercicio punto de inflexion
import numpy as np
import matplotlib.pyplot as plt
def funcion(x):
    return ((x*x*x*x)/12)-((x*x*x)/2)+(x*x)+10
def derivada1(x):
  return ((x*x*x)/3)-((3(x*x))/2)+(2*x)
def derivada2(x):
  return (x*x) - 3*x +2
#Paso I. f"(x) se iguala a 0 a fin de calcular las posiciones candidatas:
# x*x - 3x + 2 = 0  o  bien ( x - 1)(x - 2) = 0
#Por lo tanto, f"(x) = 0 cuando x = 1 y x = 2  
#Paso II. Para x = 1, f"(x) se evalúa a la izquierda y a la derecha de x = 1 
# cuando x = 0.9 y x =1.1
x1=derivada2(0.9)
print(" Derivada2(0.9)= ",x1)
x2=derivada2(1.1)
print(" Derivada2(1.1)= ",x2)
if x1>0:
    if x2<0:
        print("Un Punto de inflexion existe cuando x=1")
elif x1<0:
    if x2>0:
        print("Un Punto de inflexion existe cuando x=1")
else:
    print("x=1 NO es un Punto de inflexion")

#  Para x = 2, f"(x) se evalúa a la izquierda y a la derecha de x = 2 
# cuando x = 1.9 y x =2.1


x3=derivada2(1.9)
print(" derivada2(1.9)= ",x3)
x4=derivada2(2.1)
print(" derivada2(2.1)= ",x4)

if x3>0:
    if x4<0:
        print("Un Punto de inflexion existe cuando x=2")
elif x3<0:
    if x4>0:
        print("Un Punto de inflexion existe cuando x=2")
else:
    print("x=2 NO es un Punto de inflexion")     
    
# Grafica
x = np.linspace(-2.5, 2.5, 10)

y = funcion(x)
y1=funcion(1)
y2=funcion(2)
plt.plot(x, y) 
plt.plot(1,y1, marker="o", color="red")
plt.plot(2,y2, marker="o", color="red")
