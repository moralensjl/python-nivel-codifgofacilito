# num = int(input("Ingresa un numero: "))
# if num > 5:
#     print("El numero ingresado es mayor a 5")


num = int(input("Ingresa un numero par: "))
if num % 2 != 0:
    print("ERROR: el numero ingresado no es par")
print(f"El numero ingresado fue: {num}")


# numero = int(input("Ingresa un numero: "))
# if numero % 2 != 0:
#     print(f"{numero} es un numero par")
# else:
#     print(f"{numero} no es un numero par")

# IS: es para comparar si los dos objetos son iguales en memoria
# if type(numero) is int:
#     print("Es un numero entero")
# else:
#     print("No es un numero entero")

lloviendo = False
action = 'playa' if not lloviendo else "biblioteca"
print("Vamos a la", action)