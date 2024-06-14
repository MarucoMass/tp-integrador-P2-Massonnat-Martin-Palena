from entrenador import *
from pokedex import *
from pokemon import *
from gimnasio import *
from medalla import *
from habilidad import *
from objeto import *
from probabilidad_captura import calcular_probabilidad_captura






lista_pokemons = [Pokemon("Pikachu", "25", "Eléctrico", 100, 55, 40),
    Pokemon("Charizard", "36", "Fuego", 150, 84, 78),
    Pokemon("Bulbasaur", "16", "Planta", 120, 49, 49),
    Pokemon("Squirtle", "10", "Agua", 90, 48, 65),
    Pokemon("Jigglypuff", "12", "Normal", 110, 45, 20),
    Pokemon("Gengar", "28", "Fantasma", 120, 65, 60),
    Pokemon("Eevee", "18", "Normal", 80, 55, 50),
    Pokemon("Snorlax", "50", "Normal", 300, 110, 65),
    Pokemon("Dragonite", "55", "Dragón", 200, 134, 95),
    Pokemon("Mewtwo", "70", "Psíquico", 200, 150, 90),
    Pokemon("Gyarados", "35", "Agua", 150, 125, 79),
    Pokemon("Arcanine", "40", "Fuego", 200, 110, 80),
    Pokemon("Machamp", "32", "Lucha", 160, 130, 75),
    Pokemon("Lapras", "45", "Agua/Hielo", 250, 85, 80),
    Pokemon("Alakazam", "38", "Psíquico", 120, 105, 55),
    Pokemon("Golem", "42", "Roca", 180, 120, 130),
    Pokemon("Blastoise", "36", "Agua", 170, 83, 100),
    Pokemon("Venusaur", "36", "Planta", 180, 82, 83),
    Pokemon("Jolteon", "30", "Eléctrico", 130, 65, 60),
    Pokemon("Flareon", "30", "Fuego", 130, 95, 60)]


lista_pokedex = [Pokedex(), Pokedex(), Pokedex()]
lista_pokedex[1].agregar_pokemon(lista_pokemons[5])
lista_pokedex[1].agregar_pokemon(lista_pokemons[2])
lista_pokedex[1].agregar_pokemon(lista_pokemons[3])
lista_pokedex[1].agregar_pokemon(lista_pokemons[6])
lista_pokedex[1].agregar_pokemon(lista_pokemons[8])
lista_pokedex[1].agregar_pokemon(lista_pokemons[7])


lista_entrenadores = [Entrenador("Maximus", lista_pokedex[0]), Entrenador("Aurelio", lista_pokedex[1]), Entrenador("Blackets", lista_pokedex[2])]

lista_medallas = [Medalla("Medalla Roca"), Medalla("Medalla Rayo")]

lista_objetos = [Objeto("Pocion", "Curativo", "+20HP"), Objeto("Piedra Lunar", "Objeto Evolutivo", "+50XP" ), Objeto("Bayas", "Defensivo", "+30DEF")]



lista_pokemons[0].agregar_habilidad(Habilidad("Chispa", 30))
lista_pokemons[0].agregar_habilidad(Habilidad("Imapct Trueno", 50))

lista_pokemons[1].agregar_habilidad(Habilidad("Garra Umbria", 70))
lista_pokemons[1].agregar_habilidad(Habilidad("Garra Metal", 50))

lista_pokemons[2].agregar_habilidad(Habilidad("Placaje", 30))
lista_pokemons[2].agregar_habilidad(Habilidad("Latigo Cepa", 80))


lista_gimnasios = [Gimnasio("La Roca", lista_entrenadores[1], lista_medallas[0]),Gimnasio("El Rayo", lista_entrenadores[2], lista_medallas[1])]





