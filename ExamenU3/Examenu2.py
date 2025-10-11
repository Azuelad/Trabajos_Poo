class Planeta:
    total_planetas = 0  # Variable de clase

    def __init__(self, nombre, distancia):
        self.nombre = nombre
        self.distancia = distancia  # distancia en millones de km
        Planeta.total_planetas += 1
        print(f"Planeta {self.nombre} registrado correctamente.")

    def __del__(self):
        print(f"El planeta {self.nombre} ha sido eliminado del registro.")

    @classmethod
    def contar_planetas(cls):
        print(f"Total de planetas registrados: {cls.total_planetas}")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} | Distancia: {self.distancia} millones de km")


class NaveEspacial:
    total_naves = 0  # Variable de clase

    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad  # velocidad en km/s
        self.destino = None
        NaveEspacial.total_naves += 1
        print(f"Nave {self.nombre} construida exitosamente.")

    def __del__(self):
        print(f"La nave {self.nombre} ha sido retirada del servicio.")

    @classmethod
    def contar_naves(cls):
        print(f"Total de naves registradas: {cls.total_naves}")

    def asignar_destino(self, planeta, *misiones, **recursos):
        self.destino = planeta
        print(f"La nave {self.nombre} se dirige a {planeta.nombre}.")
        if misiones:
            print("Misiones adicionales:", ", ".join(misiones))
        if recursos:
            print("Recursos cargados:")
            for k, v in recursos.items():
                print(f" - {k}: {v}")

    def calcular_tiempo_viaje(self):
        if self.destino is None:
            print(f"La nave {self.nombre} no tiene destino asignado.")
            return
        # Convertimos distancia a km y velocidad a km/s
        tiempo_segundos = (self.destino.distancia * 1_000_000_000) / self.velocidad
        tiempo_horas = tiempo_segundos / 3600
        print(f"Tiempo estimado de viaje de {self.nombre} a {self.destino.nombre}: {tiempo_horas:.2f} horas.")

    def mostrar_info(self):
        print(f"Nave: {self.nombre} | Velocidad: {self.velocidad} km/s | Destino: {self.destino.nombre if self.destino else 'No asignado'}")


# =============================
# Menú principal
# =============================

planetas = []
naves = []

def menu():
    while True:
        print("\n--- MENÚ INTERPLANETARIO ---")
        print("1. Registrar planeta")
        print("2. Registrar nave")
        print("3. Asignar destino a nave")
        print("4. Calcular tiempo de viaje")
        print("5. Mostrar información")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del planeta: ")
            distancia = float(input("Distancia desde la Tierra (en millones de km): "))
            planetas.append(Planeta(nombre, distancia))

        elif opcion == "2":
            nombre = input("Nombre de la nave: ")
            velocidad = float(input("Velocidad (en km/s): "))
            naves.append(NaveEspacial(nombre, velocidad))

        elif opcion == "3":
            if not naves or not planetas:
                print("Primero registra al menos una nave y un planeta.")
                continue
            print("\nNaves disponibles:")
            for i, nave in enumerate(naves):
                print(f"{i+1}. {nave.nombre}")
            idx_nave = int(input("Selecciona la nave: ")) - 1

            print("\nPlanetas disponibles:")
            for j, planeta in enumerate(planetas):
                print(f"{j+1}. {planeta.nombre}")
            idx_planeta = int(input("Selecciona el planeta destino: ")) - 1

            misiones = input("Misiones adicionales (separa con coma, opcional): ").split(",") if input("¿Agregar misiones? (s/n): ").lower() == "s" else []
            recursos = {}
            if input("¿Agregar recursos? (s/n): ").lower() == "s":
                while True:
                    clave = input("Nombre del recurso (o Enter para terminar): ")
                    if clave == "":
                        break
                    valor = input(f"Cantidad de {clave}: ")
                    recursos[clave] = valor

            naves[idx_nave].asignar_destino(planetas[idx_planeta], *misiones, **recursos)

        elif opcion == "4":
            if not naves:
                print("No hay naves registradas.")
                continue
            for nave in naves:
                nave.calcular_tiempo_viaje()

        elif opcion == "5":
            print("\n--- Información de planetas ---")
            for planeta in planetas:
                planeta.mostrar_info()
            Planeta.contar_planetas()

            print("\n--- Información de naves ---")
            for nave in naves:
                nave.mostrar_info()
            NaveEspacial.contar_naves()

        elif opcion == "6":
            print("Saliendo del sistema interplanetario...")
            break

        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
