from habilidad import Habilidad

class Pokemon():

    def __init__(self, nombre:str, nivel:str, tipo:str, salud:int, ataque:int, defensa:int):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__tipo = tipo
        self.__salud = salud
        self.__ataque = ataque
        self.__defensa = defensa
        self.__habilidades:list = []

        @property
        def nombre(self) -> str:
            return self.__nombre
        
        @property
        def nivel(self) -> str:
            return self.__nivel

        @property
        def tipo(self) -> str:
            return self.__tipo

        @property
        def salud(self) -> str:
            return self.__salud
        
        @salud.setter
        def salud(self, value):
            self.__salud = value

        @property
        def ataque(self) -> str:
            return self.__ataque
        
        @ataque.setter
        def ataque(self, value):
            self.__ataque = value

        @property
        def defensa(self) -> str:
            return self.__defensa
        
        @defensa.setter
        def defensa(self, value):
            self.__defensa = value

        @property
        def habilidades(self) -> str:
            return self.__habilidades
        


        def atacar(self):
            pass

        def agregar_habilidad(self, habilidad: Habilidad):
            self.habilidades.append(habilidad)

        def subir_nivel(self):
            pass