from pokemon import Pokemon
from pokedex import Pokedex
from probabilidad_captura import calcular_probabilidad_captura
from objeto import Objeto
from medalla import Medalla

class Entrenador:

    __id_entrenador_autoincrement = int(0)
    __validar_nombres = []

    def __init__(self, nombre: str, pokedex: Pokedex, default_pokemon:Pokemon):
        self.__nombre = Entrenador.validarNombre(nombre)
        self.__id_entrenador: int = Entrenador.id_autoincrement()
        self.__equipo: list = []
        self.__objetos: list = []
        self.__medallas: list = []
        self.__default_pokemon = default_pokemon # HAY QUE VER ESTO.ACA PUSIMOS ASI PORQUE CUANDO QUERIAMOS RETAR A OTRO SE QUEDABA ESTO EN NONE Y NO PODIA SEGUIR
        self.__pokedex = pokedex

    @property
    def default_pokemon(self):
        return self.__default_pokemon

    @default_pokemon.setter
    def default_pokemon(self, value):
        if value in self.equipo:
            self._default_pokemon = value
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
    def id_autoincrement(cls):
        cls.__id_entrenador_autoincrement += 1
        return cls.__id_entrenador_autoincrement

    @classmethod
    def validarNombre(cls, nombre):
        if nombre in cls.__validar_nombres:
            return False
        cls.__validar_nombres.append(nombre)
        return nombre

    # METODOS

    def agregarPokemon(self, pokemon: Pokemon)-> None:
        if len(self.equipo) < 5:
            self.equipo.append(pokemon)
        self.pokedex.agregar_pokemon(pokemon)

    def removerPokemon(self, pokemon: Pokemon) -> None:
        self.equipo.remove(pokemon)

    def capturarPokemon(self, pokemon: Pokemon) -> bool:
        if calcular_probabilidad_captura(pokemon.nivel):
            self.agregarPokemon(pokemon)
            # self.pokedex.agregar_pokemon(pokemon)
            return True
        return False

    def elegirPokemon(self, index: int):
        self.default_pokemon = self.equipo[index]

    def usarObjeto(self, indice_objeto: int, indice_pokemon: int) -> bool:
        objeto = self.objetos[indice_objeto]
        pokemon = self.equipo[indice_pokemon]

        if objeto.nombre == "Pocion":
            if pokemon.salud < 100:
                pokemon.salud = min(100, pokemon.salud + 10)
                objeto_usado = self.objetos.pop(indice_objeto)
                return objeto_usado

        elif objeto.nombre == "Piedra Evolutiva":
            pokemon.subirNivel()
            objeto_usado = self.objetos.pop(indice_objeto)
            return objeto_usado
        
    def agregarObjeto(self, objeto: Objeto)->None:
        self.objeto.append(objeto)

    def agregarMedalla(self, medalla:Medalla)->None:
        self.medallas.append(medalla)

    def __str__(self) -> str:
        return f"Nombre{self.nombre} ID: {self.default_pokemon}"



