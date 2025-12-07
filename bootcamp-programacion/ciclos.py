
a = [1, 2, 4, 5]

for i in range(0, len(a)): # consultamos el tamano de la lista que es "a"
    # la funcion len devuelve el numero de iterables que hay en un elemento.
    print(a[i]) # imprimimos a en la posicion i

i = 0
while i < len(a):
    print(a[i])
    i += 1


b = (1, 5, 33, 60, 30, 99, 50, 53, 42, 44)

def divisibles_por_2():
    for j in range(0, len(b)):
        if b[j] % 2 == 0:
            print(f'par -> {b[j]}')

if __name__ == "__main__":
    divisibles_por_2()



# Desarrollar una funcion que retorne todos los numeros primos
# entre 1 y un numero x que debe recibir por parametro
# y luego imprimir esos numeros.

