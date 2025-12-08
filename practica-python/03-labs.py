
"""
Imagina que estamos validando si un usuario puede entrar al panel de
administración de tu Tienda Virtual.

"""
# rol_usuario = "admin"
# if rol_usuario == "admin":
#     print("Acceso total concedido. Bienvenido al panel.")
# elif rol_usuario == "vendedor":
#     print("Acceso parcial. Puedes ver tus ventas.")
# else:
#     print("Acceso denegado. Solo personal autorizado.")


# rol_usuario = input("Introduzca sus datos por pantalla: ")
#
# if rol_usuario == "admin".lower():
#     print("Acceso total concedido. Bienvenido al panel.")
# elif rol_usuario == "vendedor".lower():
#     print("Acceso parcial. Puedes ver tus ventas.")
# else:
#     print("Acceso denegado. Solo personal autorizado.")

usuario = "admin"
usuario_contrasena = "admin5450"

rol_usuario = input("Ingrese su nombre de usuario: ")

if rol_usuario.lower() == usuario.lower():
    print("Usuario registrado correctamente...")

    rol_usuario2 = input("Ingrese su contraseña: ")

    if rol_usuario2.lower() == usuario_contrasena.lower():
        print("Contraseña correcta. Acceso concedido.")
    else:
        print("Contraseña incorrecta")

else:
    print("Nombre de usuario incorrecto")
