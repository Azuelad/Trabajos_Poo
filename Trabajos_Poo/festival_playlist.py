# Listas para almacenar datos
nombres = []
artistas = []
duraciones = []
popularidades = []

def agregar_canciones():
    """Pregunta cuántas canciones agregar y captura sus datos."""
    print("\n--- 1. AGREGAR CANCIONES ---")
    while True:
        try:
            num_canciones = int(input("¿Cuántas canciones desea agregar? "))
            if num_canciones > 0:
                break
            else:
                print("Debe ingresar un número positivo.")
        except ValueError:
            print("Entrada no válida. Ingrese un número entero.")

    for i in range(num_canciones):
        print(f"\nCanción {len(nombres) + 1} de {len(nombres) + num_canciones}:")
        
        while True:
            try:
                nombre = input("Nombre de la canción: ")
                artista = input("Artista: ")
                duracion = float(input("Duración en minutos (ej. 3.5): "))
                if duracion > 0:
                    break
                else:
                    print("La duración debe ser positiva.")
            except ValueError:
                print("Duración no válida. Ingrese un número flotante.")

        while True:
            try:
                popularidad = int(input("Popularidad (1-100): "))
                if 1 <= popularidad <= 100:
                    break
                else:
                    print("La popularidad debe estar entre 1 y 100.")
            except ValueError:
                print("Popularidad no válida. Ingrese un número entero.")

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)
        
    print(f"\n{num_canciones} canción(es) agregada(s) correctamente.")

def ver_reportes():
    """Genera y muestra estadísticas sobre la playlist."""
    if not nombres:
        print("\nNo hay canciones registradas para generar reportes.")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    
    # Cálculos usando funciones nativas de Python
    suma_popularidad = sum(popularidades)
    promedio_popularidad = suma_popularidad / total_canciones
    
    max_pop = max(popularidades)
    min_pop = min(popularidades)
    
    # Encontrar los índices de las canciones más/menos populares
    idx_max = popularidades.index(max_pop)
    idx_min = popularidades.index(min_pop)

    print("\n" + "="*45)
    print("REPORTE DE LA PLAYLIST DEL FESTIVAL")
    print("="*45)
    print(f"Número total de canciones: {total_canciones}")
    print(f"Duración total de la playlist: {duracion_total:.2f} minutos")
    print("-" * 45)
    print(f"Promedio de popularidad: {promedio_popularidad:.2f}")
    print("-" * 45)
    print(f"Canción más popular ({max_pop}):")
    print(f"   {nombres[idx_max]} por {artistas[idx_max]}")
    print(f"Canción menos popular ({min_pop}):")
    print(f"   {nombres[idx_min]} por {artistas[idx_min]}")
    print("="*45)

def buscar_canciones():
    """Permite al usuario buscar canciones por artista o rango de popularidad."""
    if not nombres:
        print("\nNo hay canciones registradas para buscar.")
        return
        
    print("\n--- 3. BUSCAR CANCIONES ---")
    print("a. Buscar por artista")
    print("b. Buscar por rango de popularidad")
    opcion = input("Seleccione una opción (a/b): ").lower()

    resultados = []

    if opcion == 'a':
        artista_buscado = input("Ingrese el nombre del artista a buscar: ").strip().lower()
        for i, artista in enumerate(artistas):
            if artista.lower() == artista_buscado:
                resultados.append(i)
        
        print(f"\nResultados para el artista '{artista_buscado.capitalize()}':")
        
    elif opcion == 'b':
        while True:
            try:
                min_pop = int(input("Popularidad mínima: "))
                max_pop = int(input("Popularidad máxima: "))
                if 1 <= min_pop <= max_pop <= 100:
                    break
                else:
                    print("El rango debe estar entre 1 y 100, y el mínimo no debe ser mayor al máximo.")
            except ValueError:
                print("Popularidad no válida. Ingrese números enteros.")
                
        for i, pop in enumerate(popularidades):
            if min_pop <= pop <= max_pop:
                resultados.append(i)

        print(f"\nResultados para popularidad entre {min_pop} y {max_pop}:")
        
    else:
        print("Opción no válida.")
        return

    # Imprimir resultados
    if resultados:
        print("-" * 30)
        for i in resultados:
            print(f"   {nombres[i]} - {artistas[i]} ({popularidades[i]} pop, {duraciones[i]:.2f} min)")
        print("-" * 30)
    else:
        print("No se encontraron canciones que coincidan con el criterio.")


def playlist_recomendada():
    """Genera una playlist con canciones de popularidad superior al promedio."""
    if not nombres:
        print("\nNo hay canciones registradas.")
        return

    total_canciones = len(nombres)
    suma_popularidad = sum(popularidades)
    promedio_popularidad = suma_popularidad / total_canciones
    
    print("\n--- 4. PLAYLIST RECOMENDADA ---")
    print(f"El promedio de popularidad actual es: {promedio_popularidad:.2f}")
    print(f"Incluyendo solo canciones con popularidad > {promedio_popularidad:.2f}:")
    
    recomendadas = []
    
    for i, pop in enumerate(popularidades):
        if pop > promedio_popularidad:
            recomendadas.append(i)

    if recomendadas:
        print("-" * 45)
        for i in recomendadas:
            print(f"{nombres[i]} - {artistas[i]} (Popularidad: {popularidades[i]})")
        print("-" * 45)
    else:
        print("No hay canciones cuya popularidad sea superior al promedio.")

def menu_principal():
    """Muestra el menú de opciones y maneja la interacción principal."""
    while True:
        print("\n" + "="*45)
        print("FESTIVAL DE MÚSICA - PLAYLIST MANAGER")
        print("="*45)
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")
        print("-" * 45)

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            agregar_canciones()
        elif opcion == '2':
            ver_reportes()
        elif opcion == '3':
            buscar_canciones()
        elif opcion == '4':
            playlist_recomendada()
        elif opcion == '5':
            print("\n¡Gracias por usar el sistema! Programa finalizado.")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

# Iniciar el programa
if __name__ == "__main__":
    menu_principal()