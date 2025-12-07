# import operations
from operations import resta


a = [1, 2, 3, 4]

# a.extend([5, 6, 7])
# a.pop()
# a.append(5)
# a.insert(1, 6)
# a.sort()
print(a)

b = (5, 6, 7, 8)

for i in a:
    print(i)

#    indice, excluyente, conteo
for i in range(0, 5, 1): # el tercer elemento no es necesario.
    print(f'range: {i}')

# aqui imprimimos los elementos de la lista
for i in range(0, len(a) ):
    print(f'>> {a[i]}')
    #print(a[i])


# El while se utiliza con expresiones booleanas

# mientras i sea menor que el tamano de la lista (que la longitud de la lista)
i = 0
while i < len(a):
    print(a[i])
    #i = i + 1
    i +=1


# El if se utiliza para hacer comparaciones
if a[0] == b[0]:
    print("El numero es igual")
else:
    print("El numero no es igual")


# Funciones
def imprimir(lista):
    for j in lista:
        print(j)

imprimir([1, 2, 3, 4])


def imprimir_nombre(nombre):
    print(nombre)

imprimir_nombre('Noticia: JDK 25. Java ha cambiado')
print(imprimir_nombre('Alexandre'))

c = resta(3, 2)
print(c)

