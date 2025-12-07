# Ejemplos de ciclos for
# range( start, stop, step )
# Start, es opcional porque toma por defecto a 0
# Stop, debemos indicarle el final porque se puede volver infinito
# Step, si queremos ir de uno en uno o de dos en dos etc.
# for i in range(1, 11):
#     print(i)
#
#
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers[::2]:
    print(number**2)

fruits = {
    'fresa': 'roja',
    'limon': 'verde',
    'papaya': 'amarilla',
    'guayaba': 'rosado'
}

for name, color in fruits.items():
    print(f'{name} es de color: {color}')

print(fruits['fresa'])