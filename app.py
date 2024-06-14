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
    pokemon_random = random.randint(0, len(lista_pokemons))
    print(f"Te has encotrado con un {lista_pokemons[pokemon_random].nombre} salvaje!\nQuieres capturarlo? 1-Si 2-No")
    opt = int(input("Toma una decision: "))
    if opt == 1:
        if entrenadorPrincipal().capturarPokemon(lista_pokemons[pokemon_random]):
            print("Lo has logrado capturar!")   
        else:
            print(f"Oh no, el {lista_pokemons[pokemon_random].nombre} a huido!")
    elif opt == 2:
        print("Has logrado escapar.")
    else:
        print("No existe esta opcion!")
    

def retarLiderGimnasio():
    pass

def aplicarObjeto():
    pass

def comprarObjeto():
    pass

def verPokedex():
    pass








def menu():
    print(f'''
    1- Explorar
    2- Aplicar objeto a tu pokemon
    3- Comprar Objeto
    4- Ver tu pokedex
    5- Salir
          ''')

def subMenu():
    print(f''' 1- Salir a capturar pokemons
          2- Retar a lider de gimnasio
          
          ''')

while True:
    
    menu()
    
    opt = int(input("Ingrese una opcion: "))
    if opt == 1:
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