class Medalla:

    def __init__(self, nombre):
        self.__nombre = nombre
        

    @property
    def nombre(
        self,
    ):
        return self.__nombre


    def __str__(self) -> str:
        return f"Medalla: {self.nombre}"
