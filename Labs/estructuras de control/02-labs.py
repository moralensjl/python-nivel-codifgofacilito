

numero = 6

if numero % 2 == 0:
    print("Es un numero par")
else:
    print("No es par")


total = 4000

if total >= 2000:
    print("Tiene un descuento del 10%")
else:
    print("Sin descuento")




edad = 18

if 1 <= edad <= 3:
    print("Bebe")
elif 4 <= edad <= 12:
    print("Infante")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 60:
    print("Adulto")
elif 61 <= edad <= 100:
    print("Anciano")
else:
    print("No se encontro la etapa")


for saludo in range(5):
    print("Hola mundo!")


for numero in range(10):
    if numero % 2 == 0:
        print(numero, " es par")
    else:
        print(numero, " es impar")




# password = input("Ingresa la contraseña: ")
# while password != "admin1234":
#     print("Password incorrecto")
#     password = input("Ingresa la contraseña: ")
# print("Bienvenido al sistema")
#
#


while True:
    try:
        numero = int(input("Ingrese un numero: "))
        break
    except ValueError:
        print("No se puede operar con str")



