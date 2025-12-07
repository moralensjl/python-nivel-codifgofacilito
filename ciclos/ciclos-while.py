

# want_greet = 'S'
#
# while want_greet == 'S':
#     print('Hola, que tal!')
#     want_greet = input('Quiere otro saludo? (S/N): ')
# print('Que tengas un buen dia!')

day = 0
week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

while day < 7:
    print(f'Hoy es {week[day]}')
    day += 1
