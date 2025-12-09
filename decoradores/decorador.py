# un decorador es una funcion que recibe una funcion como argumento
# y retorna una nueva funcion que usualmente extiende el comportamiento
# de la funcion original.

def mi_decorador(func):
    def envoltura():
        print("Antes de llamar a la funcion ")
        func() # Esta funcion esta llamando a la funcion saludar(). por lo tanto,
        # func es saludar()
        print("Despues de llamar a la funcion")
    return envoltura

@mi_decorador
def saludar():
    print("Hola!")


if __name__ == "__main__":
    saludar()


