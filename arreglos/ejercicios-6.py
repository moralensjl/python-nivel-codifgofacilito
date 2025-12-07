# Crea un funcion que reciba un arrreglo y devuelva un nuevo arreglo in elementos duplicados
def eliminar_duplicados(arreglo):
    return list(set(arreglo))

if __name__ == "__main__":
    numeros = [1, 2, 5, 5, 5, 5, 7]
    numeros_sin_duplicados = eliminar_duplicados(numeros)
    print(f"El arreglo sin duplicados es: {numeros_sin_duplicados}")


nombre = ['James']
print(nombre)
