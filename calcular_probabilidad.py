import random


def calcular_probabilidad(nivel_pokemon):

    dificultad = 0.5 + (nivel_pokemon / 110)
    probabilidad = max(0.1, min(1.0, 1.0 - dificultad))

    valor = random.random()

    if valor <= probabilidad:
        return True
    else:
        return False




