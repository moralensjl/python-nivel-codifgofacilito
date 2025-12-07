# Crea una funcion que reciba un arreglo de numeros y devuelva la suma de todos sus
# elementos
def suma_elementos(arreglo):
    sumatoria = sum(arreglo)
    print(f"Sumatoria: {sumatoria}")

if __name__ == "__main__":
    suma_elementos([3, 5, 6, 7])
