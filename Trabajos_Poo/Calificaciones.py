calificacion = int(input("Ingresa la calificación (0 - 100): "))

if calificacion < 0 or calificacion > 100:
    print("Calificación fuera de rango. Debe estar entre 0 y 100.")
else:
    
    if calificacion >= 90:
        print("La calificación en letra es: A")
    elif calificacion >= 80:
        print("La calificación en letra es: B")
    elif calificacion >= 70:
        print("La calificación en letra es: C")
    elif calificacion >= 60:
        print("La calificación en letra es: D")
    else:
        print("La calificación en letra es: F")
