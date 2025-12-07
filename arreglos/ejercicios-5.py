# Crea una funcion que reciba un arreglo de numeros y devuelve un nuevo arreglo con
# solo los numeros pares.
#
# arreglo = [1, 3, 4, 6, 7, 8, 9]
# def numeros_pares():
#     for arreglos in range(0, len(arreglo)):
#         if arreglo[arreglos] % 2 == 0:
#             print(arreglo[arreglos])
#
# if __name__ == "__main__":
#     numeros_pares()
#
#
#
#
# arreglo = [1, 3, 4, 6, 7, 8, 9]
#
# def numeros_pares():
#     for i in range(len(arreglo)):
#         if arreglo[i] % 2 == 0:
#             print(f"Par encontrado en el índice {i}: {arreglo[i]}")
#
# numeros_pares()


def numeros_pares(arreglo):
    return [num for num in arreglo if num % 2 == 0]

if __name__ == "__main__":
    numeros =  [1, 3, 4, 6, 7, 8, 9]

    resultado = numeros_pares(numeros)
    print(f"Los numeros pares del arreglo son: {resultado}")

#
# pares = []
#
# for num in range(10):
#     if num % 2 == 0:
#         pares.append(num)
#         print(pares)


# Crea una funcion que reciba un arreglo de numeros y devuelve un nuevo arreglo con
# solo los numeros pares.

def numeros_pares(arreglo):
    arreglo = [num for num in arreglo if num % 2 == 0]
    return arreglo

if __name__ == "__main__":
    nuevos_pares = [1, 2, 3, 4, 5, 6, 7]
    print(numeros_pares(nuevos_pares))