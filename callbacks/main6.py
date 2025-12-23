
def mostrar_datos(usuario):
    print("Datos mostrados por pantalla:")
    for key, value in usuario.items():
        print(f"{key}: {value}")


def guardar_datos(usuario):
    print("Datos guardados en diccionario interno")
    base_datos = {}
    base_datos["usuario"] = usuario
    print(base_datos)


def usuarios(usuario, callbacks):
    for callback in callbacks:
        callback(usuario)


if __name__ == '__main__':
    datos = {
        "nombre": input("Ingrese su nombre: "),
        "email": input("Ingrese su email: "),
        "nombre_usuario": input("Cree su nombre de usuario: ")
    }

    usuarios(datos, [guardar_datos, mostrar_datos])

