# ejemplos con callbacks para entender todo el procedimiento

def mostrar_todos_los_usuarios(usuarios):
    print("---- TODOS LOS USUARIOS DE LA BASE DE DATOS ----")
    for key, values in usuarios.items():
        print(f"{key}: {values}")


def mostrar_email_usuario(datos):
    print(f"Email del usuario: {datos.get('email')}")


def mostrar_nombre_usuario(datos):
    print(f"nombre de usuario: {datos.get('nombre_usuario')}")

# funcion principal
def usuarios_web(usuarios, callback):

    callback(usuarios)


if __name__ == "__main__":
    nombre_usuario = {
        "nombre": "moralens",
        "email": "moralens21@gmail.com",
        "nombre_usuario": "moralensj",
        "usuario_activo": True,
        "edad": 26
    }
    usuarios_web(nombre_usuario, mostrar_todos_los_usuarios)
    print("--- USUARIOS COMPLETOS DE LA BASE DE DATOS ----")
    usuarios_web(nombre_usuario, mostrar_email_usuario)
    usuarios_web(nombre_usuario, mostrar_nombre_usuario)






