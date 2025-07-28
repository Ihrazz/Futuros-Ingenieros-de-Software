from tabulate import tabulate
from lectura_productos import leer_productos

def mostrar_menu():
    while True:
        print("\n=== Menú de Productos ===")
        print("1. Ver productos")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            productos = leer_productos()
            print(tabulate(productos, headers="keys", tablefmt="fancy_grid"))
        elif opcion == "2":
            print("Adiós :)")
            break
        else:
            print("Opción no válida, intenta de nuevo.")