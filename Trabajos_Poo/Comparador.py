num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

mayor = num1
menor = num1

if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
