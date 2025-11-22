def crear_matriz():
    """Pregunta por las dimensiones y crea la matriz inicial de asientos libres ('L')."""
    while True:
        try:
            filas = int(input("Ingrese el número de filas del cine: "))
            columnas = int(input("Ingrese el número de columnas (asientos por fila): "))
            if filas > 0 and columnas > 0:
                break
            else:
                print("El número de filas y columnas debe ser mayor que cero.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese números enteros.")
    
    # Crea la matriz inicializada con 'L' (Libre)
    matriz = [['L' for _ in range(columnas)] for _ in range(filas)]
    print(f"\n✅ Matriz de {filas}x{columnas} creada. Todos los asientos están libres.")
    return matriz

def mostrar_sala(matriz):
    """Imprime la matriz de asientos con un formato legible."""
    if not matriz:
        print("La sala de cine no ha sido configurada.")
        return

    filas = len(matriz)
    columnas = len(matriz[0])

    print("\n" + "=" * (columnas * 4 + 8))
    print("🎬 ESTADO ACTUAL DE LA SALA")
    print("=" * (columnas * 4 + 8))
    
    # Encabezado de columnas
    header = "    " + " ".join([f"C{c+1: <2}" for c in range(columnas)])
    print(header)
    print("  " + "-" * (columnas * 4 + 2))
    
    # Contenido de la matriz
    for i in range(filas):
        # Muestra el número de fila
        fila_str = f"F{i+1:<2}| "
        for j in range(columnas):
            asiento = matriz[i][j]
            if asiento == 'L':
                # Asiento libre en azul/verde
                fila_str += f"\033[92m{asiento: <3}\033[0m"
            else:
                # Asiento ocupado en rojo
                fila_str += f"\033[91m{asiento: <3}\033[0m"
        print(fila_str)
    
    print("-" * (columnas * 4 + 8))
    print("L = Libre | X = Ocupado")

def obtener_posicion(matriz):
    """Solicita la fila y columna al usuario y valida si existen."""
    filas = len(matriz)
    columnas = len(matriz[0])
    
    while True:
        try:
            fila = int(input(f"Ingrese la Fila (1 a {filas}): "))
            columna = int(input(f"Ingrese la Columna (1 a {columnas}): "))
            
            # Convertir a índices basados en 0
            idx_fila = fila - 1
            idx_columna = columna - 1
            
            # 🟦 C) Verificar que el asiento exista
            if 0 <= idx_fila < filas and 0 <= idx_columna < columnas:
                return idx_fila, idx_columna
            else:
                print("❌ ERROR: La fila o columna ingresada no existe en esta sala.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese números enteros.")

def reservar_asiento(matriz):
    """Reserva un asiento libre ('L' -> 'X')."""
    print("\n--- RESERVAR ASIENTO ---")
    idx_fila, idx_columna = obtener_posicion(matriz)
    
    if matriz[idx_fila][idx_columna] == 'L':
        matriz[idx_fila][idx_columna] = 'X'
        print(f"✅ ÉXITO: Asiento F{idx_fila+1}, C{idx_columna+1} ha sido reservado.")
    else:
        # 🟦 C) No permitir reservar asientos ya ocupados
        print("⛔ Asiento ocupado. No se puede reservar.")

def liberar_asiento(matriz):
    """Libera un asiento ocupado ('X' -> 'L')."""
    print("\n--- LIBERAR ASIENTO ---")
    idx_fila, idx_columna = obtener_posicion(matriz)
    
    if matriz[idx_fila][idx_columna] == 'X':
        matriz[idx_fila][idx_columna] = 'L'
        print(f"✅ ÉXITO: Asiento F{idx_fila+1}, C{idx_columna+1} ha sido liberado.")
    else:
        print("⛔ Asiento ya está libre. No hay nada que liberar.")

def contar_asientos(matriz):
    """Cuenta y muestra el total de asientos libres y ocupados."""
    if not matriz:
        print("La sala de cine no ha sido configurada.")
        return
        
    libres = 0
    ocupados = 0
    
    for fila in matriz:
        for asiento in fila:
            if asiento == 'L':
                libres += 1
            else:
                ocupados += 1
                
    total = libres + ocupados
    
    print("\n--- ESTADÍSTICAS DE OCUPACIÓN ---")
    print(f"Capacidad total: {total} asientos")
    print(f"🪑 Asientos Libres (L): \033[92m{libres}\033[0m")
    print(f"🚫 Asientos Ocupados (X): \033[91m{ocupados}\033[0m")
    
    if total > 0:
        porcentaje_ocupacion = (ocupados / total) * 100
        print(f"Tasa de ocupación: {porcentaje_ocupacion:.2f}%")

def menu_principal():
    """Ejecuta el menú principal del sistema."""
    
    # 🟦 A) Crear la matriz de asientos al inicio
    matriz_asientos = crear_matriz()
    
    while True:
        print("\n" + "="*30)
        print("🍿 SISTEMA DE ASIENTOS DE CINE")
        print("="*30)
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos ocupados y libres")
        print("5. Salir")
        print("-" * 30)

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            mostrar_sala(matriz_asientos)
        elif opcion == '2':
            reservar_asiento(matriz_asientos)
        elif opcion == '3':
            liberar_asiento(matriz_asientos)
        elif opcion == '4':
            contar_asientos(matriz_asientos)
        elif opcion == '5':
            print("\n👋 ¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("⚠️ Opción no válida. Por favor, ingrese un número del 1 al 5.")

# Iniciar el programa
if __name__ == "__main__":
    menu_principal()