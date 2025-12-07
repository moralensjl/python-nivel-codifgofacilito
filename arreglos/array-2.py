#
# tienda = int(input("Ingrese la cantidad de productos que quiere comprar: "))
#
# carrito_compras = []
#
# for i in range(tienda):
#     pedidos_usuario = input("Seleccione los productos que desea comprar: ")
#
#     carrito_compras.append(pedidos_usuario)
#     print(f"Usted a seleccionado {carrito_compras} en su carrito de compras")


numeros = int(input("Ingrese la cantidad de numeros que quiere ver en la lista: "))

numeros_usuario = []

for i in range(numeros):
    numero = int(input("Ingrese los numeros por pantalla: "))
    if numero == 0:
        print("No se puede introducir el numero 0. Terminando programa....")
        break
    else:
        numeros_usuario.append(numero)
        print(f"Lista actual: {numeros_usuario} | Cantidad: {len(numeros_usuario)}")
