
a = True
b = False
print(a and b) # False. Es false porque ambas expresiones tienen que ser true
print(a or b) # True. es true porque una de las expresiones es true.
print(not a) # False. porque niega la expresion. si es true, sera lo contrario y viceversa.

# Evalúa las siguientes expresiones y escribe qué valor booleano (True o False) devolverá cada una:
valor = 5 > 2
print(valor) # True

valor1 = 10 == 2 * 5
print(valor1) # True

valor2 = 7 != 7
print(valor2) # false

valor3 = not (4 < 6) # false
print(valor3)

# Escribe un programa que pida un número y diga si es mayor o igual que 18.
numero_usuario = int(input("Ingresa un numero: "))
if numero_usuario > 18:
    print("El numero es mayor de 18")
elif numero_usuario == 18:
    print("El numero es igual a 18")
else:
    print("El numero es menor de 18")


# Crea un programa que pida dos números y diga si:
# Ambos son positivos.
# Al menos uno es mayor que 10.
# Ninguno es cero
try:
    num1 = int(input("Ingresa un numero por pantalla: "))
    num2 = int(input("Ingresa el segundo numero por pantalla: "))

    if (num1 > 0) and (num2 > 0):
        print("Ambos numeros son positivos")
    elif (num1 > 10) or (num2 > 10):
        print("Por lo menos uno es mayor a 10")
    elif (num1 != 0) and (num2 != 0):
        print("Ninguno es cero")
    else:
        print("Opcion no valida")

except ValueError as error:
    print(f"{error}")


