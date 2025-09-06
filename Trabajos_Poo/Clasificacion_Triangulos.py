# Clasificación de triángulos según sus lados

# Solicitar longitudes al usuario
lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))

# Verificar si las longitudes forman un triángulo válido
if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    # Clasificación
    if lado1 == lado2 == lado3:
        print("El triángulo es EQUILÁTERO.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("El triángulo es ISÓSCELES.")
    else:
        print("El triángulo es ESCALENO.")
else:
    print("Las longitudes no forman un triángulo válido.")
