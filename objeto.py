class Objeto:

    def __init__(self, nombre, tipo, efecto) -> None:
        self.__nombre = nombre
        self.__tipo = tipo
        self.__efecto = efecto

    @property
    def nombre(
        self,
    ):
        return self.__nombre

    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @property
    def tipo(
        self,
    ):
        return self.__tipo

    @tipo.setter
    def tipo(self, new_tipo):
        self.__tipo = new_tipo

    @property
    def efecto(
        self,
    ):
        return self.__efecto

    @efecto.setter
    def efecto(self, new_efecto):
        self.__efecto = new_efecto

    def __str__(self) -> str:
        return f"|{self.nombre} \ Tipo: {self.tipo} \ Efecto: {self.efecto}|"
