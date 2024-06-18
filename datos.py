from entrenador import *
from pokedex import *
from pokemon import *
from gimnasio import *
from medalla import *
from habilidad import *
from objeto import *
from calcular_probabilidad import calcular_probabilidad




lista_pokemons = [Pokemon("Pikachu", 25, "Eléctrico", 100, 40, "Impactrueno", 57),
    Pokemon("Charizard", 36, "Fuego", 150, 78, "Impactrueno", 88),
    Pokemon("Bulbasaur", 16, "Planta", 120, 49, "Impactrueno", 76),
    Pokemon("Squirtle", 10, "Agua", 90, 48, "Impactrueno", 23),
    Pokemon("Jigglypuff", 12, "Normal", 110, 20, "Impactrueno", 89),
    Pokemon("Gengar", 28, "Fantasma", 120, 60, "Impactrueno", 12),
    Pokemon("Eevee", 18, "Normal", 80, 50, "Impactrueno", 73),
    Pokemon("Snorlax", 50, "Normal", 300, 65, "Impactrueno", 22),
    Pokemon("Dragonite", 55, "Dragón", 200, 95, "Impactrueno", 87),
    Pokemon("Mewtwo", 70, "Psíquico", 200,  90, "Impactrueno", 56),
    Pokemon("Gyarados", 35, "Agua", 150, 79, "Impactrueno", 51),
    Pokemon("Arcanine", 40, "Fuego", 200,  80, "Impactrueno", 52),
    Pokemon("Machamp", 32, "Lucha", 160,  75, "Impactrueno", 56),
    Pokemon("Lapras", 45, "Agua/Hielo", 85, 80, "Impactrueno", 75),
    Pokemon("Alakazam", 38, "Psíquico", 105, 55, "Impactrueno", 91),
    Pokemon("Golem", 42, "Roca", 180,  130, "Impactrueno", 11),
    Pokemon("Blastoise", 36, "Agua", 170, 100, "Impactrueno", 54),
    Pokemon("Venusaur", 36, "Planta", 180, 83, "Impactrueno", 58),
    Pokemon("Jolteon", 30, "Eléctrico", 65, 60, "Impactrueno", 72),
    Pokemon("Flareon", 30, "Fuego", 130, 60, "Impactrueno", 82)]


lista_pokedex = [Pokedex(), Pokedex(), Pokedex()]
lista_pokedex[1].agregar_pokemon(lista_pokemons[5])
lista_pokedex[1].agregar_pokemon(lista_pokemons[2])
lista_pokedex[1].agregar_pokemon(lista_pokemons[3])
lista_pokedex[1].agregar_pokemon(lista_pokemons[6])
lista_pokedex[1].agregar_pokemon(lista_pokemons[8])
lista_pokedex[1].agregar_pokemon(lista_pokemons[7])


lista_entrenadores = [
    Entrenador("Maximus", lista_pokedex[0]), 
    Entrenador("Aurelio", lista_pokedex[1]), 
    Entrenador("Blackets", lista_pokedex[2])
    ]

lista_medallas = [
    Medalla("Medalla Roca"), 
    Medalla("Medalla Rayo")
    ]

lista_objetos = [
    Objeto("Pocion", "curativo", 20), 
    Objeto("Piedra Lunar", "evolutivo", 1),
    Objeto("Bayas", "defensivo", 10),
    Objeto('Pocion Superior', 'curativo', 50),
    Objeto("Chaleco asalto","defensivo", 30),
    Objeto("Armadura Maltida","evolutivo", 2)
    ]

lista_entrenadores[0].agregar_pokemon(lista_pokemons[0])
lista_entrenadores[0].agregar_pokemon(lista_pokemons[1])

lista_entrenadores[1].agregar_pokemon(lista_pokemons[15])
lista_entrenadores[1].agregar_pokemon(lista_pokemons[17])

lista_entrenadores[2].agregar_pokemon(lista_pokemons[18])
lista_entrenadores[2].agregar_pokemon(lista_pokemons[19])

#lista_entrenadores[0].elegirPokemon(0)
lista_entrenadores[1].elegir_pokemon(0)
lista_entrenadores[2].elegir_pokemon(0)

# lista_pokemons[0].agregar_habilidad(Habilidad("Chispa", 30))
# lista_pokemons[0].agregar_habilidad(Habilidad("Imapct Trueno", 50))

# lista_pokemons[1].agregar_habilidad(Habilidad("Garra Umbria", 70))
# lista_pokemons[1].agregar_habilidad(Habilidad("Garra Metal", 50))

# lista_pokemons[2].agregar_habilidad(Habilidad("Placaje", 30))
# lista_pokemons[2].agregar_habilidad(Habilidad("Latigo Cepa", 80))


lista_gimnasios = [
                Gimnasio("La Roca", lista_entrenadores[1], lista_medallas[0]),
                Gimnasio("El Rayo", lista_entrenadores[2], lista_medallas[1])
                ]


lista_entrenadores[0].agregar_objeto(lista_objetos[3])


