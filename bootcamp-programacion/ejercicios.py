

nota_1 = 3
nota_2 = 6
nota_3 = 8

suma = nota_1 + nota_2 + nota_3
print(suma/3)

RUTA_IMAGEN = "imagenes/imagen.jpg"
print(RUTA_IMAGEN)

"""
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo
introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario
haya introducido.
"""

nombre_usuario = input("Introduzca el nombre del usuario: ")
print(f"Hola {nombre_usuario}!")

"""
Crear una aplicación que le permita al usuario ingresar 2 números y luego mostrar en pantalla la suma de
ambos.
"""

ingresar_numero = int(input("Ingresa un numero por pantalla: "))
ingresar_numero2 = int(input("Ingresa un segundo numero por pantalla: "))

resultado = ingresar_numero + ingresar_numero2
print(f"Resultado: {resultado}")

"""
Crear una aplicación que le permita al usuario ingresar (base, altura) calcular 
y mostrar en pantalla el área
de un triángulo.
"""

base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))

area = base * altura / 2
print(f"Area es igual a -> {area}")


"""
Crear una aplicación que le permita al usuario ingresar dos edades y mostrar en pantalla True si las dos
edades son iguales o False sino.
"""

age1 = int(input("Ingresa la edad: "))
age2 = int(input("Ingresa la edad: "))

son_iguales = age1 == age2
print(f"Las dos edades son iguales? {son_iguales}")


def area(base, altura):
    result = base * altura / 2
    return result

buscar_area = area(10, 7)
print(buscar_area)

