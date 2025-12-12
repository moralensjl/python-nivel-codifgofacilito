# funciones generadoras
def generador():
    lista_valores = ['ana', 'antonio', 'francisco', 'cristian', 'crital']
    for lista in lista_valores:
        yield lista


# Iterar sobre el generador para obtener los valores
# for valor in generador():
#     print(valor)

# Convertir el generador a una lista
# print(list(generador()))

# usuando next
gen = generador()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def generadora():
    valores_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for valores in valores_numeros:
        yield valores


# for i in generadora():
#     print(i)

generadores = generadora()
print(next(generadores))
print(next(generadores))
print(next(generadores))
print(next(generadores))