import numpy as np #Libreria numerica de python
import random #Libreria de aleatoriedad
from matplotlib import pyplot as plt #Libreria de graficas

#Variables
niveles = 12 #Niveles de obstaculos
canicas = 3000 #Cantidad de canicas
contenedores = [1,2,3,4,5,6,7,8,9,10,11,12,13] #Contenedores de canicas
probabilidad = 0.5 #Probabilidad de cada nivel de obstaculos

def simulacion_maquina(n, p): #Hace la simulacion
    conteo = np.arange(13) #Para llevar el conteo de canicas por cada contenedor

    for i in range(1, n): #Comienza a tirar las 3000 canicas
        posicion_canica = 6 #Las canicas comienzan cayendo desde el centro
        for j in range(1, niveles): #Por cada nivel se determina la posicion actual de la canica
            
            #Tira un numero al azar
            rand = random.random()

            if rand >= p: #Si el numero es mayor que 0.5 moverá la canica hacia la derecha
                posicion_canica += 0.5
            else: #De lo contrario moverá la canica hacia la izquierda
                posicion_canica -= 0.5
        #Una vez que la canica haya pasado por todos los niveles se registra la posicion del contenedor donde ha caido
        conteo[int(posicion_canica)] += 1
    #Al terminar arroja el conteo de canicas por contenedor
    return conteo
    

def graficacion(conteo): #Hace la graficacion de la simulacion y la muestra en pantalla
    
    #Se coloca el titulo de la grafica y los nombres de los ejes
    plt.title("Simulacion de la Máquina de Galton")
    plt.xlabel('Distribucion de canicas')
    plt.ylabel('Cantidad de canicas')
    #Genera una grafica de barras mostrando la distribucion y la cantidad de canicas
    plt.bar(contenedores, conteo)
    #Muestra la grafica en pantalla
    plt.show()

#Se guarda en una variable el resultado de la simulacion
calculo = simulacion_maquina(canicas, probabilidad)
#Con el resultado de la simulacion se hace su graficacion para mostrarse en pantalla
graficacion(calculo)