class Medalla:

    def __init__(self, nombre, gimnasio) -> None:
        self.__nombre = nombre
        self.__gimnasio = gimnasio

    @property
    def nombre(
        self,
    ):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @property
    def gimnasio(
        self,
    ):
        return self.__gimnasio

    @gimnasio.setter
    def gimnasio(self, new_gimnasio):
        self.__gimnasio = new_gimnasio

    def __str__(self) -> str:
        return f"Medalla: {self.nombre} del Gimnasio: {self.gimnasio}"
