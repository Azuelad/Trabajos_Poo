class Candidato:
    def __init__(self, nombre, partido):
        self.nombre = nombre
        self.partido = partido
        self.votos = 0

    def sumar_voto(self):
        self.votos += 1

    def info(self):
        return f"{self.nombre} ({self.partido}) - Votos: {self.votos}"


class Eleccion:
    def __init__(self, nombre_eleccion):
        self.nombre_eleccion = nombre_eleccion
        self.candidatos = []

    def agregar_candidato(self, candidato):
        # Validar duplicados
        if any(c.nombre.lower() == candidato.nombre.lower() for c in self.candidatos):
            print("Ya existe un candidato con ese nombre.")
        else:
            self.candidatos.append(candidato)
            print(f"Candidato {candidato.nombre} agregado.")

    def votar(self, nombre_candidato):
        for c in self.candidatos:
            if c.nombre.lower() == nombre_candidato.lower():
                c.sumar_voto()
                print(f"Voto registrado para {c.nombre}.")
                return
        print("Ese candidato no existe.")

    def mostrar_resultados(self):
        if not self.candidatos:
            print("No hay candidatos registrados.")
        else:
            print("\n Resultados actuales:")
            for c in self.candidatos:
                print(c.info())

    def ganador(self):
        if not self.candidatos:
            print("No hay candidatos en la elección.")
        else:
            mayor = max(self.candidatos, key=lambda c: c.votos)
            print(f"\n Ganador provisional: {mayor.nombre} ({mayor.partido}) con {mayor.votos} votos.")


# Programa principal con menú
def ejecutar_menu():
    eleccion = Eleccion("Elección Estudiantil")

    salir = False
    while not salir:
        print("\n===== SISTEMA DE VOTACIÓN =====")
        print("1. Agregar candidato")
        print("2. Votar")
        print("3. Mostrar resultados")
        print("4. Consultar ganador")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre del candidato: ")
            partido = input("Partido del candidato: ")
            eleccion.agregar_candidato(Candidato(nombre, partido))

        elif opcion == "2":
            if not eleccion.candidatos:
                print(" No se puede votar, no hay candidatos.")
            else:
                nombre = input("¿Por quién deseas votar?: ")
                eleccion.votar(nombre)

        elif opcion == "3":
            eleccion.mostrar_resultados()

        elif opcion == "4":
            eleccion.ganador()

        elif opcion == "5":
            print(" Fin del programa, gracias por participar.")
            salir = True

        else:
            print(" Opción inválida, intenta de nuevo.")


# Ejecutar
if __name__ == "__main__":
    ejecutar_menu()
