# Aprendiendo list comprenhension

# Estructura basica
# [nuevo_elemento for elemento in lista]
var = [num for num in [1, 2, 3, 4] ]
print(var)

# Con condicion
# [nuevo_elemento for elemento in lista if condicion]
condicion = [ num for num in [1, 2, 3, 4] if num % 2 == 0 ]
print(condicion)

# Con transformacion
# [ Transformacion for elemento in lista ]
transformacion = [ num * 2 for num in [1, 2, 3, 4] ]
print(transformacion)

# Crear una lista de cuadrados
cuadrados = [ n*n for n in range(1, 6) ]
print(cuadrados)

# Filtrar numeros pares
pares = [ n for n in range(10) if n % 2 == 0 ]
print(pares)

# Convertir todos los textos en mayuscula
nombres = ["juan", "pedro", "santiago", "maria"]
nombre_mayus = [nombre.upper() for nombre in nombres]
print(nombre_mayus)

# Doble condicion
nums = [n for n in range(20) if n % 2 == 0 and n > 10]
print(nums)

# Reemplazar valores (if-else-dentro)
resultado = ["PAR" if n % 2 == 0 else "IMPAR" for n in range(6)]
print(resultado)

# Comparación: Código normal vs List Comprehension
pares = []

for n in range(10):
    if n % 2 == 0:
        pares.append(n)
        print(pares)


pares = [n for n in range(10) if n % 2 == 0]
print(f"List comprehension: {pares}")


"""

📝 Tu primer ejercicio
Quiero que hagas este:
👉 Crear una lista con los números del 1 al 20, pero solo los múltiplos de 3.
Usa list comprehension.
Envíame tu código y yo te doy feedback como tu tutor. ¡Vamos! 🧑‍🏫🔥

"""

multiplos = [m for m in range(20) if m % 3 == 0]
print(f"Multiplos: {multiplos}")

# 👉 Crea una lista con los cuadrados de los números del 1 al 10, pero solo de los números impares.

square = [s*s for s in range(1, 10) if s % 2 == 1]
#print(square)


# 👉 Crea una list comprehension que devuelva una lista con la longitud de cada palabra.
palabras = ["python", "chatgpt", "curso", "teologia", "web"]
longitud_palabras = [len(p) for p in palabras]
print(longitud_palabras)

# 👉 Crea una list comprehension que genere una nueva lista con cada número multiplicado por 10.

number = [n* 10 for n in [1, 2, 3, 4, 5]]
print(f"x 10: {number}")


