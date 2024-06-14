import random


def calcular_probabilidad_captura(nivel_pokemon):

    dificultad = 0.5 + (nivel_pokemon / 100)
    probabilidad_captura = max(0.1, min(1.0, 1.0 - dificultad))

    valor = random.random()

    if valor <= probabilidad_captura:
        return True
    else:
        return False




