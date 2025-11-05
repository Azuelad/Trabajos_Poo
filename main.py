import sys

# ==============================================================================
# 1. CLASE BASE: Artista
# ==============================================================================

class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad
        
    def presentarse(self):
        print("\n¡Bienvenidos al espectáculo de", self.nombre + "!")
        print("   (Género:", self.genero, "| Popularidad:", str(self.popularidad) + "/100)")

    def actuar(self):
        raise NotImplementedError("El método 'actuar()' debe ser sobrescrito por la subclase.")

    def despedirse(self):
        print("Gracias por la energía,", self.nombre, "se despide.")
        print("---------------------------------------------------------")


# ==============================================================================
# 2. SUBCLASES DE Artista
# ==============================================================================

class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(self.nombre, "canta su éxito", self.cancion_mas_popular, "con gran energía.")

class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print("El DJ", self.nombre, "mezcla temas de estilo", self.estilo + ", haciendo vibrar al público.")

class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = int(integrantes) 

    def actuar(self):
        print("La banda", self.nombre, "con", self.integrantes, "integrantes toca un poderoso solo de guitarra.")


# ==============================================================================
# 3. FUNCIÓN PRINCIPAL DEL FESTIVAL
# ==============================================================================

def iniciar_festival(lista_artistas):
    print("\n=========================================================")
    print("           INICIO DEL FESTIVAL MUSICAL")
    print("=========================================================")
    
    if not lista_artistas:
        print("¡No hay artistas programados para actuar!")
        return

    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuación\n")

    print("=========================================================")
    print("            FIN DEL FESTIVAL. ¡VUELVAN PRONTO!")
    print("=========================================================")


# ==============================================================================
# 4. PROGRAMA PRINCIPAL
# ==============================================================================

if __name__ == "__main__":
    lista_artistas = []
    
    try:
        num_artistas = int(input("¿Cuántos artistas se presentarán en el festival? "))
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
        sys.exit(1)

    for i in range(num_artistas):
        print("\n--- Creando Artista", str(i+1), "de", num_artistas, "---")
        
        while True:
            tipo_artista = input("Tipo de artista (Cantante, DJ o Banda): ").strip().capitalize()
            if tipo_artista in ["Cantante", "Dj", "Banda"]:
                break
            print("Tipo inválido. Por favor, escriba 'Cantante', 'DJ' o 'Banda'.")

        nombre = input("Nombre del artista/banda: ")
        genero = input("Género musical: ")
        
        while True:
            try:
                popularidad = int(input("Popularidad (1 a 100): "))
                if 1 <= popularidad <= 100:
                    break
                print("La popularidad debe ser un número entre 1 y 100.")
            except ValueError:
                print("Entrada inválida. Debe ser un número.")

        if tipo_artista == "Cantante":
            cancion = input("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)
        
        elif tipo_artista == "Dj":
            estilo = input("Estilo de mezcla (e.g., House, Techno): ")
            artista = DJ(nombre, genero, popularidad, estilo)
            
        elif tipo_artista == "Banda":
            while True:
                try:
                    integrantes = int(input("Número de integrantes: "))
                    break
                except ValueError:
                    print("Entrada inválida. Debe ser un número entero.")
            artista = Banda(nombre, genero, popularidad, integrantes)

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)