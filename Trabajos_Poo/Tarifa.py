edad = int(input("Ingresa tu edad: "))
if edad < 0:
    print("La edad no puede ser negativa.")
elif edad < 12:
    print("La tarifa de entrada es: $50")
elif edad <= 17:
    print("La tarifa de entrada es: $80")
else:
    print("La tarifa de entrada es: $120")
