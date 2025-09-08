numero = int(input("Ingresa un número entero: "))

n = abs(numero)
contador = 0

if n == 0:
    contador = 1
else:
    while n > 0:
        n //= 10   
        contador += 1

print(f"El número {numero} tiene {contador} dígitos.")
