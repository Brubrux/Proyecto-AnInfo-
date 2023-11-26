def main_menu():
    """
    Muestra el menu principal del juego del Ahorcado y maneja las opciones seleccionadas por el usuario.

    El bucle se ejecuta continuamente hasta que el usuario elige salir.

    Entrada:
    - Elige una opción ingresando el número correspondiente.

    Salida:
    - Mensajes de la opcion elegida.
    """
    while True:
        print_main_menu()
        opcion = input("Elige una opcion: ")
        if opcion == "1":
            print("Empezamos!")
        elif opcion == "2":
            print("Dificultad")
        elif opcion == "3":
            print("Reglas")
        elif opcion == "4":
            print("Adios!")
            break
        else:
            print("Opcion incorrecta")


def print_main_menu():
    """
    Imprime el menú principal del juego del Ahorcado.

    Opciones:
        1 - Empezar!!!!!!
        2 - Dificultad
        3 - Reglas
        4 - Salir :(
    """
    print("Opciones:")
    print("\t1 - Empezar!!!!!!")
    print("\t2 - Dificultad")
    print("\t3 - Reglas")
    print("\t4 - Salir :(")