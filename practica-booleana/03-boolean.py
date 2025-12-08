
x = 5
y = 10
z = 15

print(x < y < z) # True
print(x == 5 and y > 8) # True
print(not z == 10 or x > 10) # True

edad = int(input("Ingresa tu edad: "))
respuesta = input("¿Tienes permiso para conducir? (si/no): ")

if respuesta.lower() == "si":
    tiene_permiso = True
else:
    tiene_permiso = False

    if edad >= 18:
        print("Puede conducir, tiene permiso.")
    else:
        print("No puede conducir.")