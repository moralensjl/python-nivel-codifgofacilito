

users = ['user1', 'user2', 'user3']
courses = ('Python', 'Django', 'Rails')
scores = [10, 8, 7]

response = tuple(zip(users, courses, scores))
print(response)

# Funciones de tuplas
numbers = (1, 3, 7, 5, 0, 2, 7, 10)
print(sorted(numbers)) # Nos entrega una lista ordenada de elementos
print(sorted(numbers, reverse=True))
print(numbers.count(7)) # Cuantas veces se repite un elemento y si un elemento esta dentro de una tupla
