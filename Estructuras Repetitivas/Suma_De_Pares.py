n = int(input("Ingresa un número entero: "))

i = 1
suma_pares = 0
suma_impares = 0

while i <= n:
    if i % 2 == 0:
        suma_pares += i
    else:
        suma_impares += i
    i += 1

print(f"Suma de pares hasta {n}: {suma_pares}")
print(f"Suma de impares hasta {n}: {suma_impares}")
