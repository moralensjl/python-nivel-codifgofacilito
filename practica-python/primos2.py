# Realizar un programa donde podamos saber si un numero es primo
# Para que sea un numero primo tengo que verificar que el numero sea un numero entero y
# mayor a 1. si no es mayor a uno entonces no es primo. los numeros primos comienzan a partir
# de 2, por eso en nuestro bucle for el numero ingresado por el usuario debe ser mayor a 1 para
# que sea numero primo.

# Luego usamos un bucle for para iterar los numeros. en el bucle comenzamos los numeros en 2.
# en la variable num se guardará el numero ingresado por el usuario. si el usuario ingresa el numero 10
# este sera el limete que usará el bucle para imprimir todos los numeros primos. se le suma + 1 porque
# si el usuario ingresa el numero 10 la iteracion llegará hasta el 9, con el + 1 se le suma un numero
# mas.

limite = int(input("Ingrese un numero: "))

print("Numeros positivos")
for num in range(2, limite + 1):
    es_primo = True

    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        print(num)

print(6 % 2)
