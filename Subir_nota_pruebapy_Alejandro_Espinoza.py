def validar_sigla(sigla, consolas):
    if not (2 <= len(sigla) <= 5):
        return False
    if not sigla.isupper() or not sigla.isalpha():
        return False
    if sigla in consolas:
        return False
    return True

def validar_nombre(nombre):
    return 3 <= len(nombre) <= 40

def validar_fabricante(fabricante):
    return 2 <= len(fabricante) <= 30

def validar_anio(anio_str):
    if not anio_str.isdigit():
        return False
    anio = int(anio_str)
    return 1972 <= anio <= 2025

def validar_precio(precio_str):
    try:
        precio = float(precio_str)
        return precio > 0
    except ValueError:
        return False
    
def validar_stock(stock_str):
    if not stock_str.isdigit():
        return False
    stock = int(stock_str)
    return stock >= 0

def buscar_consola(sigla, consolas):
    return sigla in consolas

def agregar_consola(consolas, ventas):
    print("\n--- Opción 1: Agregar Consola ---")
    
    sigla = input("Ingrese la sigla de la consola (2-5 letras mayúsculas): ").strip()
    
    if not validar_sigla(sigla, consolas):
        print("Error: Sigla inválida (debe ser mayúscula, de 2 a 5 letras y no estar repetida).")
        return
    
    nombre = input("Ingrese el nombre de la consola (3-40 caracteres): ").strip()
    
    if not validar_nombre(nombre):
        print("Error: Nombre inválido (debe tener entre 3 y 40 caracteres).")
        return
    fabricante = input("Ingrese el fabricante (2-30 caracteres): ").strip()
    
    if not validar_fabricante(fabricante):
        print("Error: Fabricante inválido (debe tener entre 2 y 30 caracteres).")
        return
    anio_str = input("Ingrese el año de lanzamiento (1972-2025): ").strip()
    
    if not validar_anio(anio_str):
        print("Error: Año inválido (debe ser un número entero entre 1972 y 2025).")
        return
    precio_str = input("Ingrese el precio (mayor a 0): ").strip()
    
    if not validar_precio(precio_str):
        print("Error: Precio inválido (debe ser un número decimal mayor a 0).")
        return
    stock_str = input("Ingrese el stock (mayor o igual a 0): ").strip()
    
    if not validar_stock(stock_str):
        print("Error: Stock inválido (debe ser un número entero mayor o igual a 0).")
        return

    consolas[sigla] = [nombre, fabricante, int(anio_str)]
    ventas[sigla] = [float(precio_str), int(stock_str)]
    print(f"Consola {sigla} agregada exitosamente al sistema")

def buscar_y_mostrar_consola(consolas, ventas):
    print("\n--- Opción 2: Buscar Consola por Sigla ---")
    sigla = input("Ingrese la sigla a buscar: ").strip().upper()
    
    if buscar_consola(sigla, consolas):
        datos = consolas[sigla]
        comercial = ventas[sigla]
        print("\n=== Consola Encontrada ===")
        print(f"Sigla       : {sigla}")
        print(f"Nombre      : {datos[0]}")
        print(f"Fabricante  : {datos[1]}")
        print(f"Año lanz.   : {datos[2]}")
        print(f"Precio      : ${comercial[0]:,.2f}")
        print(f"Stock       : {comercial[1]} unidades")
    else:
        print(f"No se encontró ninguna consola con la sigla '{sigla}'.")

def eliminar_consola(consolas, ventas):
    print("\n--- Opción 3: Eliminar Consola ---")
    sigla = input("Ingrese la sigla de la consola a eliminar: ").strip().upper()
    
    if buscar_consola(sigla, consolas):
        del consolas[sigla]
        del ventas[sigla]
        print(f"La consola '{sigla}' ha sido eliminada con éxito de ambos registros.")
    else:
        print(f"Error: No existe la consola con la sigla '{sigla}'.")


def mostrar_todas_las_consolas(consolas, ventas):
    print("==============================")
    print("LISTADO COMPLETO DE CONSOLAS")
    print("==============================")
    
    if not consolas:
        print("El sistema está vacío. No hay consolas registradas.")
        print("==============================")
        print("Total de consolas: 0")
        return

    for sigla in consolas.keys():
        nombre, fabricante, anio = consolas[sigla]
        precio, stock = ventas[sigla]
        print(f"Sigla: {sigla} | {nombre} | {fabricante} | {anio} | ${precio:,.2f} | Stock: {stock}")
        
    print("==============================")
    print(f"Total de consolas: {len(consolas)}")

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
            agregar_consola(dicc_consolas, dicc_ventas)
        elif op == "2":
            buscar_y_mostrar_consola(dicc_consolas, dicc_ventas)
        elif op == "3":
            eliminar_consola(dicc_consolas, dicc_ventas)
        elif op == "4":
            mostrar_todas_las_consolas(dicc_consolas, dicc_ventas)
        elif op == "5":
            print("\nSaliendo del sistema\n¡Esperamos que vulva pronto!")
            break
        else:
            print("Opción inválida. Ingrese un número del 1 al 5.")
if __name__ == "__main__":
    dicion()