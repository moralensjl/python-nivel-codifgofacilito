
def resta(a, b):
    return a - b


# Hacer una funcion que se llame division_por_2

a = (5, 2, 100, -2, 30, 9999, -11111, 8, 6)

def division_por_2():
    for i in a:
        if i % 2 == 0:
            print(f' >> {i}')


def division_par():
    for i in range(0, len(a)):
        if a[i] % 2 == 0:
            print(a[i])


if __name__ == '__main__':
    division_por_2()
    #division_par()



# Ciclos
ciclos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#def numeros_primos(n):
#     primos = []
#    for i in range(1, n + 1):
#        if i % 2 == 0:
#            primos.append(i)

def numeros_primos():
    for i in range(0, len(ciclos)): # consultamos el tamano de la lista que es "ciclos"
        if ciclos[i] % 2 == 0:
            print(f'primos: {ciclos[i]}')
# la funcion len devuelve el numero de iterables que hay en un elemento.
numeros_primos()