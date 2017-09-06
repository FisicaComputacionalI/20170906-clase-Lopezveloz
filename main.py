import numpy as np 
import pylab as pl
x=[7000,8000,9000,10000,11000]
y=[73,80,85,87,89]
pl.plot(x,y)
#Crea un vector (arreglo) con los valores del eje x
x1=[7000,8000,9000,10000,11000]
#crea un vector (areglo) con los valores en el eje Y para cada valor en el eje X 
y2=[80,83,85,86,88]
#Grafica el vector x contra el vector y 
pl.plot(x1,y2)
pl.xlabel('Voltaje [V]')
pl.ylabel('Eficiencia[%]')
pl.grid(True)
pl.savefig('graph.png')