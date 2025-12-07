# Crea una expresion que determine si un numero es
# positivo, negativo, o igual a cero.

numero = int(input("Coloca un numero por pantalla: "))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")


es_par = int(input("Coloca un numero por pantalla: "))

if es_par % 2 == 0:
    print("El numeros es par")
else:
    print("El numero es impar")


cadena = input("Coloca una cadena por pantalla: ")
if len(cadena) < 10:
    print("El texto tiene menos de 10 caracteres")
elif len(cadena) > 10:
    print("El texto tiene mas de 10 caracteres")
else:
    print("El texto tiene exactemente 10 caracteres")

es_mayor_de_edad = int(input("Coloca su edad: "))
if es_mayor_de_edad >= 18:
    print("Es mayor de edad, puede votar")
else:
    print("Es menor de edad, no puede votar")


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad




