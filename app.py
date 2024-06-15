from datos import *
import random

# Explorar(Aca es donde aleatoriamente selecciona un pokemon y lo muestra)
# Usar Objeto(Utilizar un objeto en un pokemon del equipo)
# Comprar objeto(Mostramos unos objetos y preguntamos si desea comprarlo tambien validamos si tiene mas de 5 objetos)
# Ver pokemons(Mostramos todos los pokemons que obtuvo en el juego)
# Ir a Gimnasio(Calculamos la probabilida de que gane basandonos en el nivel del pokemon del entrenador y el nivel del pokemon del lider de gimansio)
# Salir


#             ---> Logica para usar objeto <---
# while True:
#     if len(entrenador.objetos) > 0:
#         for i, x in enumerate(entrenador.objetos):
#             print(f"{i} {x}")

#         indice = int(input("Ingrese objeto: "))
#         # objeto = entrenador.usarObjeto(indice)
#         print(f"El objeto utilizado es: {entrenador.usarObjeto(indice)}")
#     else:
#         print("No tienes objetos")
#         break
# return f'''Nro: {self.nro_viaje} - {self.nombre}
#         Fecha Desde: {self.fecha_dede}
#         Fecha hasta: {self.fecha_hasta}
#         Días: [{self.cantidad_dias}]
#         Costo: $ {self.costo}'''

def entrenadorPrincipal():
    return lista_entrenadores[0]

def capturarPokemon():
    pokemon_random = random.randint(0, len(lista_pokemons)-1)
    print(f"Te has encontrado con un {lista_pokemons[pokemon_random].nombre} salvaje!\nQuieres capturarlo? 1-Si 2-No")
    opt = int(input("Toma una decision: "))
    if opt == 1:
        if entrenadorPrincipal().capturarPokemon(lista_pokemons[pokemon_random]):
            entrenadorPrincipal().default_pokemon.recibirAtaque(lista_pokemons[pokemon_random].ataque_base - entrenadorPrincipal().default_pokemon.defensa)
            print("Lo has logrado capturar!")   
        else:
            print(f"Oh no, el {lista_pokemons[pokemon_random].nombre} a huido!")
            entrenadorPrincipal().default_pokemon.recibirAtaque(lista_pokemons[pokemon_random].ataque_base)
                
    elif opt == 2:
        print("Has logrado escapar.")
    else:
        print("No existe esta opcion!")
    

def retarLiderGimnasio():
    if entrenadorPrincipal().default_pokemon != None:
        for index, gimnasio in enumerate(lista_gimnasios, 1):
            print(f"{index} - {gimnasio}")

        opt = int(input("Que gimnasio desea retar?"))

        gimnasio_seleccionado = lista_gimnasios[opt-1]

        if calcular_probabilidad(gimnasio_seleccionado.dueloPokemon(entrenadorPrincipal())):
            entrenadorPrincipal().agregarMedalla(lista_gimnasios[opt-1].medalla)
            print("Ganaste")
            entrenadorPrincipal().default_pokemon.recibirAtaque(gimnasio_seleccionado.entrenador.default_pokemon.ataque_base - entrenadorPrincipal().default_pokemon.defensa)
        else:
            print("Perdiste")
            entrenadorPrincipal().default_pokemon.salud = 0
    else:
        print("Antes de luchar debes elegir tu pokemon")

def aplicarObjeto():
    if len(entrenadorPrincipal().objetos) > 0:
        for i,objeto in enumerate(entrenadorPrincipal().objetos ,1):
            print(f"{i} {objeto}")
        
        objeto_elegido = int(input("Elija un objeto: "))
        
        for i,pokemon in enumerate(entrenadorPrincipal().equipo ,1):
            print(f"{i} {pokemon}")

        pokemon_elegido = int(input("En quien quiere usar el objeto: "))
        
        entrenadorPrincipal().usarObjeto(objeto_elegido - 1, pokemon_elegido - 1)
    else:
        print("No tienes objetos")
        
    #print(entrenadorPrincipal().equipo[0].salud)
        
def comprarObjeto():
    objetos_aleatorios = random.sample(range(len(lista_objetos)), 3)
    print(objetos_aleatorios)
    print("Estos objetos son los que tiene la tienda ahora mismo:")
    for i,objeto in enumerate(objetos_aleatorios, 1):
        print(f"{i} {lista_objetos[objeto]}")
    
    indice_objeto_comprado = int(input("Elija el objeto: "))
    if  indice_objeto_comprado > 3 or indice_objeto_comprado < 1:
        print("No valido")
    else:
        entrenadorPrincipal().agregarObjeto(lista_objetos[objetos_aleatorios[indice_objeto_comprado - 1]])
    
    

def verPokedex():
    for pokemon in entrenadorPrincipal().pokedex.pokemons:
        print(f"{pokemon.nombre} - Nivel: {pokemon.nivel}")


def elegirPokemonCompanero():
    for i,pokemon in enumerate(entrenadorPrincipal().equipo, 1):
            print(f"{i} {pokemon}")
        
        

    pokemon_elegido = int(input("Con quien deseas ir a explorar: "))
    
    if pokemon_elegido < 0 or pokemon_elegido > len(entrenadorPrincipal().equipo):
        print("Opcion no valida")
        return False
    else:
        if entrenadorPrincipal().equipo[pokemon_elegido - 1].salud == 0:
            print("Tienes que elegir un pokemon con vida!")
            return False
        entrenadorPrincipal().elegirPokemon(pokemon_elegido - 1)
        return True



def menu():
    print(f'''
    1- Explorar
    2- Aplicar objeto a tu pokemon
    3- Comprar Objeto
    4- Ver tu pokedex
    5- Salir
          ''')

def subMenu():
    print(f''' 
          1- Salir a capturar pokemons
          2- Retar a lider de gimnasio
          ''')

while True:
    
    menu()
    
    opt = int(input("Ingrese una opcion: "))
    if opt == 1:
        
        if elegirPokemonCompanero():
            subMenu()
            opt1 = int(input("Ingrese una opcion: "))
            if opt1 == 1:
                capturarPokemon()
                pass
            elif opt1 == 2:
                retarLiderGimnasio()
                pass
            else:
                print("Opcion no valida")
            
    elif opt == 2:
        aplicarObjeto()
        pass
    elif opt == 3:
        comprarObjeto()
        pass
    elif opt == 4:
        verPokedex()
        pass
    elif opt == 5:
        print("Chau aguante digimon")
        break
    else:
        print("Opcion incorrecta")