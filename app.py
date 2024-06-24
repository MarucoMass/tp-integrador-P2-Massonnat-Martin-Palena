from datos import *
import random
from os import system

# Explorar(Aca es donde aleatoriamente selecciona un pokemon y lo muestra)
# Usar Objeto(Utilizar un objeto en un pokemon del equipo)
# Comprar objeto(Mostramos unos objetos y preguntamos si desea comprarlo tambien validamos si tiene mas de 5 objetos)
# Ver pokemons(Mostramos todos los pokemons que obtuvo en el juego)
# Ir a Gimnasio(Calculamos la probabilida de que gane basandonos en el nivel del pokemon del entrenador y el nivel del pokemon del lider de gimansio)
# Salir


def entrenador_principal():
    return lista_entrenadores[0]


def capturar_pokemon():
    system("cls")
    pokemon_random = random.randint(0, len(lista_pokemons) - 1)
    if lista_pokemons[pokemon_random] not in entrenador_principal().pokedex.pokemons:
        entrenador_principal().pokedex.agregar_pokemon(lista_pokemons[pokemon_random])

    print(
        f"Te has encontrado con un {lista_pokemons[pokemon_random].nombre} salvaje!\nQuieres capturarlo? 1-Si 2-No"
    )
    opt = int(input("Toma una decision: "))
    if opt == 1:
        if entrenador_principal().capturar_pokemon(lista_pokemons[pokemon_random]):
            entrenador_principal().default_pokemon.recibir_ataque(
                lista_pokemons[pokemon_random].ataque_base
                - entrenador_principal().default_pokemon.defensa_actual
            )
            print("Lo has logrado capturar!")
        else:
            print(f"Oh no, el {lista_pokemons[pokemon_random].nombre} a huido!")
            entrenador_principal().default_pokemon.recibir_ataque(
                lista_pokemons[pokemon_random].ataque_base
            )

    elif opt == 2:
        print("Has logrado escapar.")
    else:
        print("No existe esta opcion!")


def retar_lider_gimnasio():
    system("cls")
    if entrenador_principal().default_pokemon != None:
        if len(lista_gimnasios) > 0:
            print("Gimnasios:")
            for index, gimnasio in enumerate(lista_gimnasios, 1):
                print(f"\t║{index} - {gimnasio} - {gimnasio.medalla}║")

            opt = int(input("Que gimnasio desea retar?: "))

            gimnasio_seleccionado = lista_gimnasios[opt - 1]

            if calcular_probabilidad(
                gimnasio_seleccionado.duelo_pokemon(entrenador_principal())
            ):
                entrenador_principal().agregar_medalla(lista_gimnasios[opt - 1].medalla)
                gimnasio_seleccionado.remover_medalla()
                lista_gimnasios.pop(opt - 1)
                print("Ganaste")
                entrenador_principal().default_pokemon.recibir_ataque(
                    gimnasio_seleccionado.entrenador.default_pokemon.ataque_base
                    - entrenador_principal().default_pokemon.defensa_actual
                )
            else:
                entrenador_principal().default_pokemon.salud_actual = 0
                print("Perdiste")
        else:
            print("Ya has conseguido derrotar a todos los lideres de gimnasio!")
    else:
        print("Antes de luchar debes elegir tu pokemon")


def aplicar_objeto():
    system("cls")
    print("Tus Objetos:")
    if (entrenador_principal().cant_objetos) > 0:
        for i, objeto in enumerate(entrenador_principal().objetos, 1):
            print(f"\t║{i}- {objeto}║")

        objeto_elegido = int(input("Elija un objeto: "))

        print("Tus Pokemons:")
        for i, pokemon in enumerate(entrenador_principal().equipo, 1):
            print(f"\t║{i}- {pokemon}║")

        pokemon_elegido = int(input("En quien quiere usar el objeto: "))

        entrenador_principal().usar_objeto(objeto_elegido - 1, pokemon_elegido - 1)
    else:
        print("No tienes objetos")

    # print(entrenador_principal().equipo[0].salud)


def comprar_objeto():
    system("cls")
    objetos_aleatorios = random.sample(range(len(lista_objetos)), 3)
    print("Estos objetos son los que tiene la tienda ahora mismo:")
    for i, objeto in enumerate(objetos_aleatorios, 1):
        print(f"║{i} {lista_objetos[objeto]}║")

    indice_objeto_comprado = int(input("Elija el objeto: "))
    if indice_objeto_comprado > 3 or indice_objeto_comprado < 1:
        print("No valido")
    else:
        entrenador_principal().agregar_objeto(
            lista_objetos[objetos_aleatorios[indice_objeto_comprado - 1]]
        )


def ver_pokedex():
    system("cls")
    print("Pokedex: ")
    if len(entrenador_principal().pokedex) > 0:
        for pokemon in entrenador_principal().pokedex.pokemons:
            print(f"\t║{pokemon.nombre} - Nivel: {pokemon.nivel}║")
    else:
        print("Tienes que salir a explorar para ver tu pokedex.")


def ver_equipo():
    system("cls")
    print("Tu equipo: ")
    for i, pokemon in enumerate(entrenador_principal().equipo, 1):
        print(
            f"\t║{i} ➔ {pokemon.nombre} - Nivel: {pokemon.nivel} - Salud: {pokemon.salud_actual}║"
        )


def ver_inventario():
    system("cls")
    if len(entrenador_principal().objetos) > 0:
        print("Tus objetos: ")
        for i, objeto in enumerate(entrenador_principal().objetos, 1):
            print(f"\t║{i} ➔ {objeto}║")
    else:
        print("Tu inventario esta vacio.")


def ver_medallas():
    system("cls")
    if len(entrenador_principal().medallas) > 0:
        print("Tus medallas son:")
        for i, medalla in enumerate(entrenador_principal().medallas, 1):
            print(f"\t║{i} ➔ {medalla}║")
    else:
        print("No tienes medallas por el momento.")


def elegir_pokemon_companero():
    system("cls")
    for i, pokemon in enumerate(entrenador_principal().equipo, 1):
        print(f"{i} {pokemon}")

    pokemon_elegido = int(input("Con quien deseas ir a explorar: "))

    if pokemon_elegido < 0 or pokemon_elegido > len(entrenador_principal().equipo):
        print("Opcion no valida")
        return False
    else:
        if entrenador_principal().equipo[pokemon_elegido - 1].salud_actual == 0:
            print("Tienes que elegir un pokemon con vida!")
            return False
        entrenador_principal().elegir_pokemon(pokemon_elegido - 1)
        return True


def menu():
    print(
        r"""
        ╔════════════════════════════════╗
        ║              MENU              ║
        ╠════════════════════════════════╣
        ║ 1- Explorar                    ║
        ║ 2- Aplicar objeto a tu pokemon ║
        ║ 3- Comprar Objeto              ║
        ║ 4- Ver tu pokedex              ║
        ║ 5- Ver equipo                  ║
        ║ 6- Ver inventario              ║
        ║ 7- Ver medallas                ║
        ║ 8- Salir                       ║
        ╚════════════════════════════════╝"""
    )


def sub_menu():
    print(
        """ 
        ╔════════════════════════════════╗
        ║  1- Salir a capturar pokemons  ║
        ║  2- Retar a lider de gimnasio  ║
        ╚════════════════════════════════╝
          """
    )


while True:

    menu()

    opt = int(input("➔ Ingrese una opcion: "))
    if opt == 1:

        if elegir_pokemon_companero():
            sub_menu()
            opt1 = int(input("➔ Ingrese una opcion: "))
            if opt1 == 1:
                capturar_pokemon()
                pass
            elif opt1 == 2:
                retar_lider_gimnasio()
                pass
            else:
                print("Opcion no valida")

    elif opt == 2:
        aplicar_objeto()
        pass
    elif opt == 3:
        comprar_objeto()
        pass
    elif opt == 4:
        ver_pokedex()
        pass
    elif opt == 5:
        ver_equipo()
        pass
    elif opt == 6:
        ver_inventario()
        pass
    elif opt == 7:
        ver_medallas()
    elif opt == 8:
        print("Chau aguante digimon")
        break
    else:
        print("Opcion incorrecta")
