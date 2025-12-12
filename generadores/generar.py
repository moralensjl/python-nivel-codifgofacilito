
# los generadores en python son una forma de crear iteradores
# se usan cuando no queremos usar todos los elementos de una
# secuencia en memoria de una sola vez.
def contador():
    n = 1
    while n <= 3:
        yield n # pausa aqui y devuelve n
        n += 1

for numero in contador():
    print(numero)


def num_impar(limite):
    num = 1
    while num <= limite:
        yield num
        num += 2

for number in num_impar(20):
    print(f'Numeros impares: {number}')