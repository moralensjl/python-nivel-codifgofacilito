try:
    edad = int(input("Coloque su edad por pantalla: "))


    if type(edad) != int:
        raise TypeError("El dato introducido no es un numero")
    elif edad >= 18:
        print("Puede ver la pelicula en el cine")
    else:
        print(" No puede ver la pelicula en el cine")

except Exception as error:
    print(f"Error : {error}")