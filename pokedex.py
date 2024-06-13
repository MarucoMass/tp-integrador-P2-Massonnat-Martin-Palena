from pokemon import Pokemon


class Pokedex:
    def __init__(
        self,
    ):
        self.__pokemons = []

    @property
    def pokemons(
        self,
    ):
        return self.__pokemons

    def agregar_pokemon(self, pokemon: Pokemon):
        self.pokemons.append(pokemon)

    def buscar_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return pokemon
        else:
            return "No se encontro ese pokemon"
