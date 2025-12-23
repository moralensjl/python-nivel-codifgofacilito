# haciendo algunos ejemplos con funcion callback
def saludar():
    print('Hola, soy el callback')


def ejecutar_callback(callback):
    print("Haciendo algo antes")
    callback() # este callback ejecuta la funcion saludar
    print("Haciendo algo despues")


ejecutar_callback(saludar)
