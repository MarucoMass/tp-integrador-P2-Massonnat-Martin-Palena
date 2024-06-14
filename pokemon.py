from habilidad import Habilidad


class Pokemon:

    def __init__(self, nombre: str, nivel: str, tipo: str):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__tipo = tipo
        self.__habilidades = []
        self.__ataque_con_habilidad = None 

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
    def habilidades(self) -> list:
        return self.__habilidades

    
    def salud():
    
    def ataque_base():
        
    def defensa():
        
    
    
    # Metodos
    
    def recibir_ataque(self, dano: int):
        self.salud -= dano

    def agregar_habilidad(self, habilidad: Habilidad):
        self.habilidades.append(habilidad)

    def subir_nivel(self):
        self.nivel += 1
