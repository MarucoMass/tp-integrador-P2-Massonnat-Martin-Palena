import random


def calcular_probabilidad(nivel_pokemon):

    dificultad = 0.3 + (nivel_pokemon / 100)
    probabilidad = max(0.2, min(1.0, 1.0 - dificultad))

    valor = random.random()

    if valor <= probabilidad:
        return True
    else:
        return False




