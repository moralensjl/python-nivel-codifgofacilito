contrasena_actual = "123456789usda"
pin_de_recuperacion = 1721
usuario = input("Ingresa tu usuario: ")
contrasena = input("Ingresa tu contrasena: ")

if contrasena == contrasena_actual and len(contrasena) > 10:
    print("Bienvenido al sistema por primera vez")
    # Ejercicio de cambiar la contrasena
    nueva_contrasena = input("Ingresa tu nueva contrasena: ")
    if nueva_contrasena == contrasena_actual:
        print("No puede usar la misma contrasena")
    else:
        if len(nueva_contrasena) > 10:
            contrasena_actual = nueva_contrasena
            print(f"Su nueva contrasena es {contrasena_actual}")
        else:
            print("La contrasena debe tener al menos 10 caracteres")
else:
    print("Contrasena incorrecta")

    pin = int(input("Ingresa tu pin de recuperacion: "))
    if pin_de_recuperacion == pin:
        print(f"Su contrasena actual es: {contrasena_actual}")

    else:
        print("Pongase en contacto con soporte para recuperar tu cuenta")
