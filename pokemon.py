from habilidad import Habilidad


class Pokemon:

    def __init__(self, nombre: str, nivel: int, tipo: str, salud: int, ataque_base: int, defensa: int):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__tipo = tipo
        self.__salud = salud
        self.__ataque_base = ataque_base
        self.__defensa = defensa
        self.__habilidades = []
        self.__ataque_con_habilidad = None

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def tipo(self) -> str:
        return self.__tipo

    @property
    def nivel(self) -> int:
        return self.__nivel
    
    @nivel.setter
    def nivel(self, new_nivel):
        self.__nivel = new_nivel

    @property
    def salud(self):
        return self.__salud
    
    @salud.setter
    def salud(self, new_salud):
        self.__salud = new_salud
        
    @property
    def ataque_base(self):
        return self.__ataque_base
    
    @ataque_base.setter 
    def ataque_base(self, new_ataque_base):
        self.__ataque_base = new_ataque_base
        
    @property
    def defensa(self):
        return self.__defensa
    
    @defensa.setter
    def defensa(self, new_defensa):
        self.__defensa = new_defensa
    
    @property
    def habilidades(self) -> list:
        return self.__habilidades

    """def ataque_base():
        pass"""

    # def salud(self, salud_base, danio):
    #     self.salud = self.salud - danio
    #     pass
    # Metodos

    def recibir_ataque(self, dano: int):
        self.salud -= dano
        if self.salud < 0:
            self.salud = 0

    def agregar_habilidad(self, habilidad: Habilidad):
        self.habilidades.append(habilidad)

    def subir_nivel(self, niveles):
        self.nivel += niveles
        
    def __str__(self) -> str:
        return f"{self.nombre} Vida: {self.salud}"
