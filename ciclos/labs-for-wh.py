

animals = ['Cat', 'Dog', 'Rabbit', 'Horse', 'Dolphin']
for animal in animals:
    if 'o' in animal:
        break
    print(f'Break: {animal}')


names = ['carlos', 'jim', 'elian', 'wenz']
for name in names:
    if 'e' in name:
        break
    print(name)


animals = ['Cat', 'Dog', 'Rabbit', 'Horse', 'Dolphin']
for animal in animals:
    if 'o' in animal:
        continue
    print(f'continue: {animal}')

# intentos = 0
# while intentos < 5:
#     name = input('Introduce su nombre correctamente: ').lower()
#
#     if name == "james":
#         print('Bienvenido al sistema')
#         break
#     else:
#         print('Ha alcanzado el limite de intentos')
# else:
#     print('Inténtelo mas tarde')




