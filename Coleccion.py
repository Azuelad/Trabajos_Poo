import os
import struct

# --- CONFIGURACIÓN DE ARCHIVOS ---
ARCHIVO_TEXTO = "coleccion_anime.txt"
ARCHIVO_BINARIO = "datos_poder.bin"

TAMANO_REGISTRO_BINARIO = struct.calcsize('15sii') 

# --- FUNCIONES AUXILIARES DE ARCHIVO Y EXCEPCIONES ---

def crear_archivos_si_no_existen():
    try:
        if not os.path.exists(ARCHIVO_TEXTO):
            with open(ARCHIVO_TEXTO, 'w', encoding='utf-8') as f:
                f.write("Nombre | Serie | Categoría\n")
            print(f"Archivo de texto creado: {ARCHIVO_TEXTO}")

        if not os.path.exists(ARCHIVO_BINARIO):
            with open(ARCHIVO_BINARIO, 'wb') as f:
                pass
            print(f"Archivo binario creado: {ARCHIVO_BINARIO}")
            
    except IOError as e:
        print(f"Error de I/O al crear archivos: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado al inicializar: {e}")

def guardar_datos_binarios(nombre, poder, rareza):
    try:
        if not isinstance(poder, int) or not isinstance(rareza, int) or poder < 0 or rareza not in range(1, 101):
            raise ValueError("El Nivel de Poder debe ser entero positivo y la Rareza (1-100).")

        with open(ARCHIVO_BINARIO, 'ab') as f:
            nombre_bytes = nombre[:15].encode('utf-8')
            registro_binario = struct.pack('15sii', nombre_bytes, poder, rareza)
            f.write(registro_binario)
        
        print(f"Datos binarios guardados para {nombre}.")
    
    except ValueError as e:
        print(f"Error de Validación Binaria: {e}")
    except IOError as e:
        print(f"Error al escribir en el archivo binario: {e}")

# --- FUNCIONES DEL MENÚ INTERACTIVO ---

def agregar_elemento():
    print("\n--- AGREGAR NUEVO PERSONAJE ---")
    
    try:
        nombre = input("Nombre del Personaje: ").strip()
        
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")

        serie = input("Serie/Anime: ").strip()
        categoria = input("Categoría (Héroe/Villano/Sidekick): ").strip()
        
        try:
            poder = int(input("Nivel de Poder (entero): "))
            rareza = int(input("Rareza (1-100, entero): "))
        except ValueError:
            print("Error: El poder y la rareza deben ser números enteros válidos. No se guardará el registro.")
            return

    except ValueError as e:
        print(f"Error de entrada: {e}")
        return

    try:
        with open(ARCHIVO_TEXTO, 'a', encoding='utf-8') as f:
            linea = f"{nombre} | {serie} | {categoria}\n"
            f.write(linea)
        print(f"\nPersonaje {nombre} guardado en {ARCHIVO_TEXTO}.")
    except IOError as e:
        print(f"Error al escribir en el archivo de texto: {e}")
        
    guardar_datos_binarios(nombre, poder, rareza)

def mostrar_coleccion():
    print("\n--- COLECCIÓN COMPLETA DE PERSONAJES ---")
    
    try:
        with open(ARCHIVO_TEXTO, 'r', encoding='utf-8') as f:
            contenido = f.read()
            if not contenido.strip() or len(contenido.split('\n')) <= 1:
                print("La colección está vacía o solo contiene la cabecera.")
            else:
                print(contenido)
    except FileNotFoundError:
        print(f"Error: El archivo {ARCHIVO_TEXTO} no existe. Agrega un elemento primero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer: {e}")

def buscar_elemento():
    print("\n--- BUSCAR PERSONAJE ---")
    
    try:
        busqueda = input("Ingresa el nombre del personaje a buscar: ").strip()
        if not busqueda:
            raise ValueError("El término de búsqueda no puede estar vacío.")

        encontrado = False
        
        with open(ARCHIVO_TEXTO, 'r', encoding='utf-8') as f:
            f.readline()
            for linea in f:
                if busqueda.lower() in linea.lower():
                    print("¡Personaje Encontrado!")
                    print(linea.strip())
                    encontrado = True
                    break

        if not encontrado:
            print(f"Personaje '{busqueda}' no encontrado en la colección.")

    except FileNotFoundError:
        print(f"Error: El archivo {ARCHIVO_TEXTO} no existe.")
    except ValueError as e:
        print(f"Error de búsqueda: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado al buscar: {e}")

def mostrar_datos_binarios():
    print("\n--- DATOS BINARIOS (Poder y Rareza) ---")
    
    archivo_abierto = None
    try:
        archivo_abierto = open(ARCHIVO_BINARIO, 'rb')
        
        while True:
            registro_bytes = archivo_abierto.read(TAMANO_REGISTRO_BINARIO) 
            
            if not registro_bytes:
                break
            
            nombre_bytes, poder, rareza = struct.unpack('15sii', registro_bytes)
            
            nombre = nombre_bytes.decode('utf-8').split('\x00', 1)[0]
            
            print(f"-> {nombre:<15} | Poder: {poder:<5} | Rareza: {rareza}/100")

    except FileNotFoundError:
        print(f"Error: El archivo binario {ARCHIVO_BINARIO} no se ha encontrado.")
    except struct.error:
        print("Error de lectura binaria: El archivo puede estar corrupto o incompleto.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        
    finally:
        if archivo_abierto:
            archivo_abierto.close()
            print("\nArchivo binario cerrado con éxito (finally).")
        else:
            print("\nFin del proceso de lectura binaria.")

# --- FUNCIÓN PRINCIPAL (Menú) ---

def menu_principal():
    
    print("Iniciando Colección Digital...")
    crear_archivos_si_no_existen()

    while True:
        print("\n" + "="*35)
        print("===== MI COLECCIÓN ANIME 2.0 =====")
        print("1. Agregar personaje")
        print("2. Mostrar colección completa (Texto)")
        print("3. Buscar personaje por nombre")
        print("4. Mostrar datos binarios (Poder/Rareza)")
        print("5. Salir")
        print("="*35)
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == '1':
            agregar_elemento()
        elif opcion == '2':
            mostrar_coleccion()
        elif opcion == '3':
            buscar_elemento()
        elif opcion == '4':
            mostrar_datos_binarios()
        elif opcion == '5':
            print("Saliendo del sistema de Colección Digital. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# --- EJECUCIÓN DEL PROGRAMA ---

if __name__ == "__main__":
    menu_principal()