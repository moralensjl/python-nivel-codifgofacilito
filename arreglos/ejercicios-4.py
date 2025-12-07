# Crea una funcion que reciba un arreglo y un numero, y devuelva True si el numero esta en
# el arreglo, o False en caso contrario.

# def buscar_numero(arreglo, numero):
#     return numero in arreglo
#
# if __name__ == "__main__":
#     numeros = [1, 3, 5, 7, 9]
#     numero_buscar = 7
#
#     if buscar_numero(numeros, numero_buscar):
#         print(f"{numero_buscar} esta en el arreglo")
#     else:
#         print(f"{numero_buscar} no esta en el arreglo")


def buscar_numero(arreglo, numero):
    return numero in arreglo


lista = [1, 3, 5, 7, 9]
print(buscar_numero(lista, 3))   # True
print(buscar_numero(lista, 4))   # False





