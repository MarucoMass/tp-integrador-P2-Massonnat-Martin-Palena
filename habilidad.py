class Habilidad:
    def __init__(self, nombre, dano):
        self.__nombre = nombre
        self.__dano = dano

    @property
    def nombre(
        self,
    ):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @property
    def dano(
        self,
    ):
        return self.__dano

    @dano.setter
    def dano(self, new_dano):
        self.__dano = new_dano

    def __str__(self) -> str:
        return f"Habilidad: {self.nombre}/Daño: {self.dano}"
