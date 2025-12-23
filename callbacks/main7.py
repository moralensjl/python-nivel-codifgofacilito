
def mostrar_usuarios(usuario):
    """
    :param usuario: usuario es un diccionario que será recorrido por un bucle for
    donde mostrara los datos del usuario usando las estructuras de datos: clave, valor.
    :return: el valor que retorna es un diccionario.
    """
    print("Datos mostrados por pantalla")
    for key, value in usuario.items():
        print(f"{key}: {value}")



def guardar_datos(usuario):
    print("Datos guardados en diccionario interno")
    base_datos = {}
    base_datos["usuario"] = usuario
    print(base_datos)


def usuarios(usuario, callbacks):
    """ usuario es un diccionario con los datos del usuario
    callbacks es una lista de funciones ej: callbacks = [guardar_datos, mostrar_datos]
    cada elemento de la lista es una funcion
    acepta un solo argumento, (usuario)

    """
    for callback in callbacks:
        callback(usuario)


if __name__ == '__main__':
    datos = {
        "nombre": input("Ingrese su nombre: "),
        "email": input("Ingrese su email: "),
        "nombre_usuario": input("Cree su nombre de usuario: ")
    }

    usuarios(datos, [guardar_datos, mostrar_usuarios])


ejemplo = {
    "nombres": {
        "isaac": "alm",
        "james": "ar",
        "alens": "sarx"
    }
}

print(ejemplo)