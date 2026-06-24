def mostar_menu():
    print(f"==MENU PRINCIPAL===\n1. Agregar consola\n2. Buscar consola por sigla\n3. Eliminar consola\n4. Mostrar todas las consolas\n5. Salir")

def leer_op():
    opcion = input("Ingrese una opcion: ").strip()
    return opcion

def dicion():
    dicc_consolas = {}
    dicc_ventas = {}
        
    while True:
        mostar_menu()
        op = leer_op()
        
        if op == "1":
            pass
        elif op == "2":
            pass
        elif op == "3":
            pass
        elif op == "4":
            pass
        elif op == "5":
            print("\nSaliendo del sistema\n¡Esperamos que vulva pronto!")
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 5.")
if __name__ == "__main__":
    dicion()