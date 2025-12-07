contrasena_actual = "123456789usda"
pin_de_recuperacion = 1721
usuario = input("Ingresa tu usuario: ")
contrasena = input("Ingresa tu contrasena: ")

if contrasena == contrasena_actual and len(contrasena) > 10:
    print("Bienvenido al sistema por primera vez")
    # Ejercicio de cambiar la contrasena
    cambiar_contrasena = input("Digite su nueva contrasena: ")
    if cambiar_contrasena == contrasena_actual:
        print("Es la misma contrasena que la anterior")
    elif len(cambiar_contrasena)<= 10:
        print("La nueva contrasena es menor de 10 caracteres")
    else:
        contrasena_actual = cambiar_contrasena
        print("Su contrasena ha sido cambiada a: ", cambiar_contrasena)

else:
    print("Contrasena incorrecta")

    pin = input("Ingresa tu pin de recuperacion: ")
    if pin_de_recuperacion == pin:
        print(f"Su contrasena actual es: {contrasena_actual}")

    else:
        print("Pongase en contacto con soporte")