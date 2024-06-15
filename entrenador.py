from pokemon import Pokemon
from pokedex import Pokedex
from calcular_probabilidad import calcular_probabilidad
from objeto import Objeto
from medalla import Medalla

class Entrenador:

    __id_entrenador_autoincrement = int(0)
    __validar_nombres = []

    def __init__(self, nombre: str, pokedex: Pokedex):
        self.__nombre = Entrenador.__validarNombre(nombre)
        self.__id_entrenador: int = Entrenador.__id_autoincrement()
        self.__equipo: list = []
        self.__objetos: list = []
        self.__medallas: list = []
        self.__default_pokemon = None # HAY QUE VER ESTO.ACA PUSIMOS ASI PORQUE CUANDO QUERIAMOS RETAR A OTRO SE QUEDABA ESTO EN NONE Y NO PODIA SEGUIR
        self.__pokedex = pokedex

    @property
    def default_pokemon(self):
        return self.__default_pokemon

    @default_pokemon.setter
    def default_pokemon(self, value):
        if value in self.equipo:
            self.__default_pokemon = value
        else:
            raise ValueError("El Pokémon debe estar en el equipo del entrenador.")

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
    def pokedex(self):
        return self.__pokedex

    @classmethod
    def __id_autoincrement(cls):
        cls.__id_entrenador_autoincrement += 1
        return cls.__id_entrenador_autoincrement

    @classmethod
    def __validarNombre(cls, nombre):
        if nombre in cls.__validar_nombres:
            return False
        cls.__validar_nombres.append(nombre)
        return nombre

    # METODOS
    
    @property
    def cant_pokemons_pokedex(self):
        return len(self.pokedex.pokemons)
        
    @property
    def cant_objetos(self):
        return len(self.objetos)
    
    def agregar_pokemon(self, pokemon: Pokemon)-> None:
        self.equipo.append(pokemon)
        
        #self.pokedex.agregar_pokemon(pokemon)

    def remover_pokemon(self, pokemon: Pokemon) -> None:
        self.equipo.remove(pokemon)

    def capturar_pokemon(self, pokemon: Pokemon) -> bool:
        if calcular_probabilidad(pokemon.nivel) and len(self.equipo) < 5 :
            self.agregar_pokemon(pokemon)    
                # self.pokedex.agregar_pokemon(pokemon)
            return True
        return False

    def elegir_pokemon(self, index: int):
        self.default_pokemon = self.equipo[index]

    def usar_objeto(self, indice_objeto: int, indice_pokemon: int) -> bool:
        objeto = self.objetos[indice_objeto]
        pokemon = self.equipo[indice_pokemon]

        if objeto.tipo == "curativo":
            if pokemon.salud < 100:
                pokemon.salud = min(100, pokemon.salud + objeto.efecto)
                objeto_usado = self.objetos.pop(indice_objeto)
                return objeto_usado

        elif objeto.tipo == "evolutivo":
            pokemon.subir_nivel(objeto.efecto)
            objeto_usado = self.objetos.pop(indice_objeto)
            return objeto_usado
        
        elif objeto.tipo == "defensivo":
            if pokemon.defensa < 50:
                pokemon.defensa = min(50, pokemon.defensa + objeto.efecto)
                objeto_usado = self.objetos.pop(indice_objeto)
                return objeto_usado
        
    def agregar_objeto(self, objeto: Objeto)->None:
        self.objetos.append(objeto)

    def agregar_medalla(self, medalla:Medalla)->None:
        self.medallas.append(medalla)

    def __str__(self) -> str:
        return f"Nombre{self.nombre} ID: {self.default_pokemon}"



