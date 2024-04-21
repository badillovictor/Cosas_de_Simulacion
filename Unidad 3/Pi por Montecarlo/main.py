import math
import random


def distancia(a, b): return math.sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    # Asumiendo un circulo con radio = 1
    # Si generamos punto aleatorios con valores entre de A y B entre 0 y 1
    # Si la distancia a 0, 0 es menor que 1 estand dentro de circulo, si no, estan fuera
    # Si cubirmos todo un cuadrante de un mapa cartesiando del circulo, podemos aproximar Pi
    aciertos = 0
    intentos = 10000
    for i in range(0, intentos):
        a = random.random()
        b = random.random()
        if distancia(a, b) < 1: aciertos += 1

    # Termina la simulacion, calculamos Pi
    print('Pi Calculado: ' + str(aciertos / intentos * 4))
    # Comparamos con el valor de Python
    print('Diferencia con el valor de Python: ' + str(math.fabs(math.pi - (aciertos / intentos * 4))))
