# un decorador es una funcion que recibe una funcion como argumento
# y retorna una nueva funcion que usualmente extiende el comportamiento
# de la funcion original.
def mi_decorador(func):
    def envoltura():
        print("Antes de llamar a la funcion")
        func()
        print("Despues de llamar a la funcion")
    return envoltura


def saludar():
    print("Hola")

if __name__ == "__main__":
    saludar_decorada = mi_decorador(saludar)
    saludar_decorada()

