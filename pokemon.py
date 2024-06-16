from habilidad import Habilidad


class Pokemon:

    def __init__(self, nombre: str, nivel: int, tipo: str, salud_base: int, ataque_base: int, defensa_base: int):
        self.__nombre = nombre
        self.__nivel = nivel
        self.__tipo = tipo
        self.__salud_base = salud_base
        self.__salud_actual = salud_base
        self.__defensa_base = defensa_base
        self.__defensa_actual = defensa_base
        self.__ataque_base = ataque_base
        self.__habilidades = []


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
    def salud_base(self):
        return self.__salud_base
        
    @property
    def salud_actual(self,):
        return self.__salud_actual
        
    @salud_actual.setter
    def salud_actual(self, new_salud):
        self.__salud_actual = new_salud
        
    @property
    def defensa_base(self):
        return self.__defensa_base
    
    @property
    def defensa_actual(self):
        return self.__defensa_actual
    
    @defensa_actual.setter
    def defensa_actual(self, new_defensa):
        self.__defensa_actual = new_defensa
        
    @property
    def ataque_base(self):
        return self.__ataque_base
    
    @ataque_base.setter 
    def ataque_base(self, new_ataque_base):
        self.__ataque_base = new_ataque_base
        
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
        self.salud_actual -= dano
        if self.salud_actual < 0:
            self.salud_actual = 0

    def agregar_habilidad(self, habilidad: Habilidad):
        self.habilidades.append(habilidad)

    def subir_nivel(self, niveles):
        self.nivel += niveles
        
    def __str__(self) -> str:
        return f"|{self.nombre} \ Vida: {self.salud_actual} \ Defensa: {self.defensa_actual}|"
