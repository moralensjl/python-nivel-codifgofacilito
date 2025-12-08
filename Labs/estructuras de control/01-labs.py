

generacion = int(input("Coloque su anio de naciemiento para saber cual es su generacion: "))

if 1946 <= generacion <= 1964:
    print("Eres Baby Boomers!")
elif 1965 <= generacion <= 1980:
    print("Eres de la generacion X!")
elif 1981 <= generacion <= 1996:
    print("Eres un Milenials!")
elif 1997 <= generacion <= 2003:
    print("Eres de la generacion Z!")
else:
    print("No esta en el rango establecido")

ever = (1, 3, 4, 5, 6, 8)
for w in ever:
    print(ever)