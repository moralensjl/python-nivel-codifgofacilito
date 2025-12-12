
def generador_simple():
    n = 1
    print("comenzando a general numeros")

    n += 1
    print(f"Nuevo valor {n}")
    yield n

    n += 1
    print(f"Otro valor {n}")
    yield n

    n += 1
    print(f"Ultimo valor {n}")
    yield n

    print("----Llamada----")


valores = generador_simple()
print(next(valores))
print(next(valores))
print(next(valores))
print(next(valores))