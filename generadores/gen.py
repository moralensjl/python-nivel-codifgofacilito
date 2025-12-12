
lista_generadora = ['ana', 'luisa', 'omar', 'omara', 'zoe', 'tamar', 'marc', 'james']

def lista_nombres():
    for i in lista_generadora:
        yield i
        #print(f'nombres: {i}')

gen = lista_nombres()
print(next(gen))

def mi_generador_simple():
    n = 1
    print("Empezandon a generar el valor 1...")

    n += 1
    print("Continuando para generar el valor 2")
    yield n

    n += 1
    print("Finalizando para generar el valor 3...")
    yield n

    print("----Llamada----")

# creamos la instancia del generador
gen = mi_generador_simple()
print(next(gen))
print(next(gen))
#print(next(gen))
