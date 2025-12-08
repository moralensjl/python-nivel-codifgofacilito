
# nombre_usuario = "admin"
# usuario_contrasena = "admin123"
#
# rol_usuario = input("Ingrese su nombre de usuario: ")
#
# if rol_usuario.lower() == nombre_usuario:
#     print("Nombre de usuario correcto.")
#
#     rol_usuario2 = input("Ingrese su contraseña: ")
#
#     if rol_usuario2 == usuario_contrasena:
#         print("Permitido el acceso.")
#     else:
#         print("Contraseña incorrecta")
#
# else:
#     print("Nombre de usuario incorrecto. vuelva a intentarlo. ")


# usuario = "admin"
# usuario_c = "admin123"
# intentos = 0
#
# rol_usuario = input("Ingrese su nombre de usuario: ")
#
# if rol_usuario == usuario:
#     print("S registro se completo exitosamente...")
#
#     rol_usuario2 = input("Ingrese su password por pantalla: ")
#
#     if rol_usuario2 == usuario_c:
#         print("Registro completado exitosamente")
#
#     else:
#         print("Password incorrecto")
#
# else:
#     print("Nombre de usuario incorrecto")


# usuario = "admin"
# usuario_c = "admin123"
# intentos = 0
#
# while intentos < 5:
#
#     rol_usuario = input("Ingrese su nombre de usuario por pantalla: ")
#
#     if rol_usuario == usuario:
#         print("Su nombre de usuario es correcto")
#         break
#     else:
#         intentos += 1
#         print("Nombre de usuario incorrecto. Vuelva a intentarlo.")

# usuario = "moralensj06_"
# usuario_c = "admin123"
# intentos = 0
# total_intentos = 5
#
# while intentos <= total_intentos:
#
#     rol_usuario = input("Ingrese su nombre de usuario: ")
#
#     if rol_usuario == usuario:
#         mensaje = "Su registro ha sido completado."
#         print(f"Bienvenido. {mensaje}")
#
#         rol_usuario2 = input("Ingresa su password: ")
#         if rol_usuario2 == usuario_c:
#             mensaje = "Bienvenido a su cuenta de usuario"
#             print(f"{mensaje} {usuario}")
#             break
#         else:
#             print("Password incorrecto, intentelo de nuevo")
#     else:
#         intentos += 1
#         print("Nombre de usuario incorrecto, Intentalo de nuevo")


usuario = "admin"
usuario_c = "admin123"
intentos = 0
total_itentos = 5

while intentos <= total_itentos:

    rol_usuario = input("Ingrese su usuario: ")

    if rol_usuario == usuario:
        print("Bienvenido a su cuenta:", usuario)

        rol_usuario2 = input("Ingrese su contrasena: ")

        if rol_usuario2 == usuario_c:
            print("Password correcto")
            break
        else:
            print("Password incorrecto. intentalo de nuevo")

    else:
        intentos += 1
        print("Nombre de usuario incorrecto")

    print("Vuevla mas tarde. Has agotado el total de intentos")
