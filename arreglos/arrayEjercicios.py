
# Crea un program que reciba numeros y lo añada a un arreglo, el programa debera dejar de solicitar
# numeros si recibe 0, luego de esto debera imprimir el arreglo y su tamaño

def main():
    numeros = []

    while True:
        try:
            numero = int(input("Ingrese un numero (Ingrese 0 para finalizar): "))
        except ValueError:
            print("Por favor, ingrese un numero válido")
            continue

        if numero == 0:
            break
        else:
            numeros.append(numero)
            print(f"Arreglo: {numeros}")
            print(f"Tamaño: {len(numeros)}")


if __name__ == "__main__":
    main()