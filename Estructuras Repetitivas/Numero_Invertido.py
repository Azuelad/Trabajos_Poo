numero = int(input("Ingresa un número entero: "))

n = abs(numero)
invertido = 0

while n > 0:
    digito = n % 10          
    invertido = invertido * 10 + digito
    n //= 10                 

if numero < 0:
    invertido = -invertido

print(f"Número original: {numero}")
print(f"Número invertido: {invertido}")
