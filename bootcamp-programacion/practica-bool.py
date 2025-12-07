numero_par = int(input("Introduce un numero: "))
if numero_par % 2 == 0:
    print("El numero es par")
else:
    print("El numero no es par")


texto = input("Introduce un texto: ")
if len(texto) > 10:
    print("El texto tiene mas de 10 caracteres")
elif len(texto) < 10:
    print("El texto tiene menos de 10 caracteres")
else:
    print("EL texto tiene exactamente 10 caracteres")



