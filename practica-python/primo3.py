
# Funcion para determinar si un numero es primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Imprimir los numeros del 1 al 100
for num in range(1, 101):
    if es_primo(num):
        print(num)

