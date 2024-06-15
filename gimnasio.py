from entrenador import Entrenador
from medalla import Medalla


class Gimnasio():
    
    def __init__(self, nombre, entrenador: Entrenador, medalla: Medalla) -> None:
        self.__nombre = nombre
        self.__entrenador = entrenador
        self.__medalla = medalla
        
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def entrenador(self):
        return self.__entrenador
    
    @property
    def medalla(self):
        return self.__medalla
    
    #METODOS
    
    def pokemonEntrenador(self):
        return self.entrenador.default_pokemon.nivel
    
    def dueloPokemon(self, entrenador: Entrenador):
        return self.entrenador.default_pokemon.nivel - entrenador.default_pokemon.nivel
    
    def __str__(self) -> str:
        return f"Gimnasio: {self.nombre}, El lider del gimnasio es: {self.entrenador.nombre}"
    
        
        
    