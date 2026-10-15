tienda = {
    "acción": ["Mono enojado I", "Mono enojado II: La venganza"],
    "ciencia ficción": ["RoboBob"],
    "terror": ["La maldición de la escuela técnica"]
}

biblioteca = {
    
}

condicion = True
menu1= ["1) Tienda", "2) Jugar un juego", "3) Salir"]
print("Bienvenido a la tienda de juegos")
print("Seleccione una opción del menú:")
for opcioni in menu1:
    print(opcioni)
while condicion:
    opcion = input("Ingrese una opción del menú: ")
    if opcion == "1":
        menu2 = ["1) Comprar juego", "2) Ingresar un juego", "3) Salir"]
        for opcion2 in menu2:
            print(opcion2)
        opcionvol2 = input("Ingrese una opción del menú: ")
        if opcionvol2 == "1":
            generos_disponibles = list(tienda.keys())
            print("Géneros disponibles en la tienda:")
            for genero in generos_disponibles:
                print(genero)
            genero = input("Ingrese el género del juego que desea comprar: ")
            if genero in tienda:
                print("Juegos disponibles en el género", genero, ":")
                for juego in tienda[genero]:
                    print(juego)
                juego_seleccionado = input("Ingrese el nombre del juego que desea comprar: ")
                if juego_seleccionado in tienda[genero]:
                    biblioteca[juego_seleccionado] = genero
                    print("Juego comprado y agregado a la biblioteca.")
                else:
                    print("El juego no está disponible en la tienda.")
        elif opcionvol2 == "2":
            generos_disponibles = list(tienda.keys())
            print("Géneros disponibles en la tienda:")
            for genero in generos_disponibles:
                print(genero)
            generoo = input("Ingrese el género del juego que desea ingresar: ")
            nombre_juego = input("Ingrese el nombre del juego: ")
            if generoo in tienda:
             tienda[generoo].append(nombre_juego)
             print("Juego ingresado en la tienda.")
            else:
                print("El género no está disponible en la tienda.")
        elif opcionvol2 == "3":
            print("Saliendo de la tienda...")
            print("Bienvenido a la tienda de juegos")
            print("Seleccione una opción del menú:")
            for opcioni in menu1:
                print(opcioni)

    elif opcion == "2":
        if biblioteca:
            print("Juegos en la biblioteca:")
            for juego in biblioteca:
                print(juego)
            juego_seleccionado = input("Ingrese el nombre del juego que desea jugar: ")
            if juego_seleccionado in biblioteca:
                print("Jugando a", juego_seleccionado, "...")
                input("Presione cualquier tecla para salir del juego.")
            elif juego_seleccionado not in biblioteca:
                print("El juego no está en la biblioteca.")
        else:
            print("No hay juegos en la biblioteca.")