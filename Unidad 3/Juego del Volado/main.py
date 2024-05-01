import random
def tiroMoneda():
    return True if random.random() > 0.5 else False

def apostar(cantidadActual, multiplicador):
    if cantidadActual >= 50:
        return 50
    elif cantidadActual <= 0:
        return 0
    else:
        apuestaActual = cantidadActual if cantidadActual < apuesta * multiplicador else apuesta * multiplicador
        if tiroMoneda():
            cantidadActual += apuestaActual
            return apostar(cantidadActual, 1)
        else:
            cantidadActual -= apuestaActual
            return apostar(cantidadActual, multiplicador * 2)




if __name__ == '__main__':
    cantidad = 30
    apuesta = 10
    loteria = 0
    quiebra = 0

    for i in range(0, 100000):
        if apostar(30, 1):
            loteria += 1
        else:
            quiebra += 1

    print('Ganadas: ' + str(loteria))
    print('Perdidas: ' + str(quiebra))
    print('Ratio: ' + str(loteria / 100000))
