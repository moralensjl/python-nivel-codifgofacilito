"""
Escribe un programa que pida tu edad
luego le sume 50 anios
Imprima "Mi edad en 50 anios seria x"

"""

#datos_edad = input("Introducir la edad: ")
#datos_edad = int(datos_edad)
#datos_edad = datos_edad + 50
#print('Mi edad en 50 anios seria: ', datos_edad)

"""
Escribe un menu para un restuarante
                                    """

datos_cliente = input("Introduzca su nombre : ")
print("Hola", datos_cliente, "Bienvenido al restuarante Lana")

empanadas_de_queso = "Empanadas de queso"
pizzas_de_queso = "Pizzas de queso"
taco_mexicano = "Taco Mexicano"

print(f"El menu del dia de hoy es: \n{empanadas_de_queso}, \n{pizzas_de_queso}, \n{taco_mexicano}")

opciones = input("Que opcion del menu quiere: ")
if opciones == "1":
    print(f"Empanadas: {empanadas_de_queso}")
elif opciones == "2":
    print(f"Pizzas: {pizzas_de_queso}")
elif opciones == "3":
    print(f"Taco Mexicano: {taco_mexicano}")
else:
    print("Opcion no valida")

direccion_cliente =input("Introduzca su direccion de la cuenta: ")
print(f"Direccion de la cuenta: {direccion_cliente}")

tiempo_de_entrega = 50
print(f"Hola {datos_cliente} su pedido de plato sera llevado en {tiempo_de_entrega} minutos a: {direccion_cliente}")
