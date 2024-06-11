from pokemon import Pokemon

class Entrenador():

    __id_entrenador_autoincrement = int(0)
    __nombres_unicos = []

    def __init__(self, nombre:str, pokemon_elegido = None):
        self.__nombre = Entrenador.nombres_unicos(nombre)
        self.__id_entrenador:int = Entrenador.id_autoincrement()
        self.__equipo:list = []
        self.__objetos:list= []
        self.__medallas:list = []
        self.__pokemon_elegido = pokemon_elegido

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def id_entrenador(self):
        return self.__id_entrenador
    
    @property
    def equipo(self):
        return self.__equipo
   
    @property
    def objetos(self):
        return self.__objetos

    @property
    def medallas(self):
        return self.__medallas

    @property
    def pokemon_elegido(self):
        return self.__pokemon_elegido
    
    def __str__(self) -> str:
        return f"Nombre{self.nombre} ID: {self.pokemon_elegido}"

    @classmethod
    def id_autoincrement(cls):
        cls.__id_entrenador_autoincrement += 1
        return cls.__id_entrenador_autoincrement
    
    @classmethod
    def nombres_unicos(cls, nombre):
        if nombre in cls.__nombres_unicos:
            return False
        cls.__nombres_unicos.append(nombre)
        return nombre
    
    def capturar_pokemon(self, pokemon) -> None:
        self.equipo.append(pokemon)

    def pokemon_elegido(self, pokemon:int):
        self.pokemon_elegido = self.equipo[pokemon]


    

ent1 = Entrenador("maruco")
ent2 = Entrenador("pale")

ent1.capturar_pokemon("pale")
ent1.capturar_pokemon("will")

ent1.pokemon_elegido(0)

print(ent1)

if ent2.nombre:
    print(ent2)
    