from pokemon import Pokemon
from pokedex import Pokedex
from probabilidad_captura import calcular_probabilidad_captura
from objeto import Objeto


class Entrenador():

    __id_entrenador_autoincrement = int(0)
    __validar_nombres = []

    def __init__(self, nombre:str, pokedex: Pokedex):
        self.__nombre = Entrenador.validarNombre(nombre)
        self.__id_entrenador:int = Entrenador.id_autoincrement()
        self.__equipo:list = []
        self.__objetos:list= []
        self.__medallas:set = ()
        self.__default_pokemon = None
        self.__pokedex = pokedex

    
    @property
    def pokedex(self):
        return self.__pokedex
    
    @property
    def default_pokemon(self):
        return self.__default_pokemon
    
    @default_pokemon.setter
    def default_pokemon(self, new_default_pokemon):
        self.default_pokemon = new_default_pokemon
    
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
    def default_pokemon(self):
        return self.__default_pokemon
    
    def __str__(self) -> str:
        return f"Nombre{self.nombre} ID: {self.pokemon_elegido}"

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
    
    
    
    #METODOS
    
    

    def agregarPokemon(self, pokemon: Pokemon):
        self.equipo.append(pokemon)
        
    def removerPokemon(self, pokemon: Pokemon):
        self.equipo.remove(pokemon)
        
    def capturarPokemon(self, pokemon: Pokemon):
        if calcular_probabilidad_captura(pokemon.nivel):
            self.agregarPokemon(pokemon)
            self.pokedex.agregar_pokemon(pokemon)
            return True
        return False 
        
    def elegirPokemon(self, index:int):
        self.default_pokemon = self.equipo[index]

    def usarObjeto(self, objeto: Objeto, indice_pokemon: int):
        if objeto.nombre == "Pocion" :
            if self.equipo[indice_pokemon].salud < 100:
                self.equipo[indice_pokemon].salud += 10    
        elif objeto.nombre == "Piedra Evolutiva":
            self.equipo[indice_pokemon].subirNivel()
            
         
    
    

ent1 = Entrenador("maruco")
ent2 = Entrenador("pale")

ent1.capturar_pokemon("pale")
ent1.capturar_pokemon("will")

ent1.pokemon_elegido(0)

print(ent1)

if ent2.nombre:
    print(ent2)
    