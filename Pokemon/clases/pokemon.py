class Pokemon:
    cantidad_pokemons = 0

    def __init__(self, nombre, tipo, ataque, defensa, salud):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        Pokemon.cantidad_pokemons += 1
        print(f"{self.nombre} ha sido creado. Tipo: {self.tipo}, Nivel: {self.nivel}")

    def __del__(self):
        Pokemon.cantidad_pokemons -= 1
        print(f"{self.nombre} ha sido liberado.")

    def entrenar(self, *args):
        self.nivel += 1
        print(f"{self.nombre} sube al nivel {self.nivel}.")
        if not args:
            self.ataque += 5
            self.defensa += 3
            self.salud += 10
        else:
            if len(args) >= 1:
                self.ataque += args[0]
            if len(args) >= 2:
                self.defensa += args[1]
            if len(args) >= 3:
                self.salud += args[2]
        print(f"Nuevas estadísticas -> Ataque: {self.ataque}, Defensa: {self.defensa}, Salud: {self.salud}")

    def mostrar_info(self):
        print(f"\n--- Información del Pokémon ---")
        print(f"Nombre:  {self.nombre}")
        print(f"Tipo:    {self.tipo}")
        print(f"Nivel:   {self.nivel}")
        print(f"Ataque:  {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud:   {self.salud}")
        print("-------------------------------")

    def atacar(self, objetivo):
        if self == objetivo:
            print("No puedes atacarte a ti mismo.")
            return
        danio = max(self.ataque - (objetivo.defensa // 2), 0)
        objetivo.salud -= danio
        if objetivo.salud < 0:
            objetivo.salud = 0
        print(f"{self.nombre} atacó a {objetivo.nombre} causando {danio} de daño.")
        print(f"Salud restante de {objetivo.nombre}: {objetivo.salud}")

    @classmethod
    def total_pokemons(cls):
        print(f"Pokémon registrados: {cls.cantidad_pokemons}")
