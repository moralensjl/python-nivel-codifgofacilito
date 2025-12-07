#
# lista_compras = int(input("Agregue su lista de compras: "))
#
# compras = []
#
# for i in range(lista_compras):
#     agregar_al_carrito = input("Que quiere agregar al carrito de compras: ")
#     compras.append(agregar_al_carrito)
#
#     print(f"Usted ha agregado {compras} a su lista de compras")

#
# tienda = int(input("Que productos de nuestra tiende quiere comprar: "))
#
# productos = []
#
# for i in range(tienda):
#     agregar_al_carrito = input("Agregue los productos al carrito: ")
#
#     productos.append(agregar_al_carrito)
#
#     print(f"Usted ha agregado {productos} a su carrito de compras")

numeros = int(input("Ingresa la cantidad de numeros que quieres agregar a tu lista: "))

# lista_numeros = [numeros]
lista_numeros = []

for i in range(numeros):
    numeros_usuarios = int(input("Ingresa los numeros: "))
    lista_numeros.append(numeros_usuarios)

    print(f"Usted ha agregado {lista_numeros} a su lista")

