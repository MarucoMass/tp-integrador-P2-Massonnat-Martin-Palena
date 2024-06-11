

class Entrenador():

    __id_autoincrement = int(0)
    __nombres_unicos = []

    def __init__(self, nombre:str):
        self.__nombre = Entrenador.nombres_unicos(nombre)
        self.__id:int = Entrenador.id_autoincrement()
        self.__equipos:list = []
        self.__objetos:list= []
        self.__medallas:list = []

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def id(self):
        return self.__id
    
    @property
    def equipos(self):
        return self.__equipos
   
    @property
    def objetos(self):
        return self.__objetos

    @property
    def medallas(self):
        return self.__medallas

    def __str__(self) -> str:
        return f"Nombre{self.nombre} ID: {self.id}"

    @classmethod
    def id_autoincrement(cls):
        cls.__id_autoincrement += 1
        return cls.__id_autoincrement
    
    @classmethod
    def nombres_unicos(cls, nombre):
        if nombre in cls.__nombres_unicos:
            return False
        cls.__nombres_unicos.append(nombre)
        return nombre
    
    

ent1 = Entrenador("pale")
ent2 = Entrenador("pale")
print(ent1)
if ent2.nombre:
    print(ent2)
    