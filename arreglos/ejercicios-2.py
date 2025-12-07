
# Dado un arreglo de numeros imprime el cuadrado de cada numero

def imprimir_cuadrados(arreglo):
    for numero in arreglo:
        cuadrado = numero ** 2
        print(f"El cuadrado de {numero} es {cuadrado}")


if __name__ == "__main__":
    numeros_ejemplo = [2, 5, 6, 7, 12]
    imprimir_cuadrados(numeros_ejemplo)
    # imprimir_cuadrados([2, 5, 6, 7, 12])
