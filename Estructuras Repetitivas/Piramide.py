n = int(input("Ingresa la altura de la pirámide: "))

i = 1
while i <= n:
    espacios = " " * (n - i)         
    estrellas = "*" * (2 * i - 1)    
    print(espacios + estrellas)
    i += 1
