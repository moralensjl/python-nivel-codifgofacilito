
try:
    edad = int(input("Ingresa tu edad: "))
    mayoria_edad = 18
    if edad == mayoria_edad or edad >= mayoria_edad:
        print("Puede ejercer su derecho al voto")
    else:
        print("Es menor de edad, no puede ejercer su derecho al voto")
except ValueError:
    print("ValueError: invalid literal for int() with base 10: 'g'")
