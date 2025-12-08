# Los numeros primos solo tienen dos divisores
# se dividen entre si mismos y entre uno

# numero = 3
# if numero % numero == numero and numero % 1 == 1:
#     print("Es numero primo")
# else:
#     print("No es numero primo")
#
numero = int(input("Ingrese un numero: "))
if numero > 1 and numero >= 2:
    print("Es primo")
else:
    print("No es primo")

numeros_primos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for numero in numeros_primos:
#     if numero % 2 == 0:
#         print(f"par {numero}")
#     else:
#         print(f"impar {numero}")


primo = [p for p in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if p ]