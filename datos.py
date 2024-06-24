from entrenador import *
from pokedex import *
from pokemon import *
from gimnasio import *
from medalla import *
from habilidad import *
from objeto import *
from calcular_probabilidad import calcular_probabilidad




lista_pokemons = [ Pokemon("Pikachu", 25, "Eléctrico", 100, 50, "Impactrueno", 40),
    Pokemon("Charmander", 15, "Fuego", 80, 40, "Llamarada", 60),
    Pokemon("Bulbasaur", 20, "Planta", 90, 45, "Rayo Solar", 55),
    Pokemon("Squirtle", 18, "Agua", 85, 48, "Hidrobomba", 70),
    Pokemon("Jigglypuff", 22, "Normal", 120, 35, "Canto", 25),
    Pokemon("Meowth", 17, "Normal", 75, 40, "Golpe Furia", 45),
    Pokemon("Psyduck", 23, "Agua", 95, 50, "Confusión", 50),
    Pokemon("Machop", 19, "Lucha", 100, 55, "Golpe Karate", 60),
    Pokemon("Geodude", 21, "Roca", 110, 60, "Avalancha", 65),
    Pokemon("Gastly", 24, "Fantasma", 70, 30, "Bola Sombra", 80),
    Pokemon("Eevee", 16, "Normal", 85, 45, "Rapidez", 50),
    Pokemon("Snorlax", 30, "Normal", 160, 70, "Hiperrayo", 100),
    Pokemon("Gengar", 28, "Fantasma", 85, 50, "Puño Sombra", 85),
    Pokemon("Onix", 26, "Roca", 120, 70, "Terremoto", 75),
    Pokemon("Arcanine", 29, "Fuego", 105, 55, "Llamarada", 90),
    Pokemon("Gyarados", 32, "Agua", 115, 60, "Hidrobomba", 100),
    Pokemon("Lapras", 27, "Agua", 130, 65, "Surf", 85),
    Pokemon("Ditto", 20, "Normal", 70, 40, "Transformación", 0),
    Pokemon("Vulpix", 15, "Fuego", 75, 38, "Lanzallamas", 55),
    Pokemon("Alakazam", 35, "Psíquico", 80, 45, "Psíquico", 95)]


lista_pokedex = [Pokedex(), Pokedex(), Pokedex(), Pokedex,  Pokedex(), Pokedex()]
lista_pokedex[1].agregar_pokemon(lista_pokemons[5])
lista_pokedex[1].agregar_pokemon(lista_pokemons[2])
lista_pokedex[1].agregar_pokemon(lista_pokemons[3])
lista_pokedex[1].agregar_pokemon(lista_pokemons[6])
lista_pokedex[1].agregar_pokemon(lista_pokemons[8])
lista_pokedex[1].agregar_pokemon(lista_pokemons[7])


lista_entrenadores = [
    Entrenador("Maximus", lista_pokedex[0]), 
    Entrenador("Aurelio", lista_pokedex[1]), 
    Entrenador("Blackets", lista_pokedex[2]),
    Entrenador("Zephyr", lista_pokedex[3]),
    Entrenador("Pyro", lista_pokedex[4]),
    Entrenador("Aquarius", lista_pokedex[5])
    ]

lista_medallas = [
    Medalla("Medalla Roca"), 
    Medalla("Medalla Rayo"),
    Medalla("Medalla Viento"),
    Medalla("Medalla Fuego"),
    Medalla("Medalla Agua")
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

lista_entrenadores[3].agregar_pokemon(lista_pokemons[7])  

lista_entrenadores[4].agregar_pokemon(lista_pokemons[14]) 

lista_entrenadores[5].agregar_pokemon(lista_pokemons[16]) 

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
                Gimnasio("El Rayo", lista_entrenadores[2], lista_medallas[1]),
                Gimnasio("El Viento", lista_entrenadores[3], lista_medallas[2]),
                Gimnasio("El Fuego", lista_entrenadores[4], lista_medallas[3]),
                Gimnasio("El Agua", lista_entrenadores[5], lista_medallas[4])
                ]


lista_entrenadores[0].agregar_objeto(lista_objetos[3])


