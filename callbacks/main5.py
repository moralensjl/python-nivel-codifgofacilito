# haciendo varios ejemplos con callbacks
def guardar_datos(datos):
    """
    :param datos: Esta funcion guarda los datos de los usuarios
    :return: y retorna los datos guardados
    """
    print("Datos guardados: ")
    print(datos)


def mostrar_datos(datos):
    print("datos del usuario")
    for keys, values in datos.items():
        print(f"{keys}: {values}")



def datos_personales(callback):
    datos = dict()
    datos["nombre"] = input("Ingrese su nombre: ")
    datos["email"] = input("Ingrese su email: ")
    callback(datos)




if __name__ == '__main__':
   datos_personales(guardar_datos)
   datos_personales(mostrar_datos)