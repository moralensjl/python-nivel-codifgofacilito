import random

player_choice = int(input('Digite un numero del 1 al 5 -> (1 -> 5): ' ))

random_number = random.randint(1, 5)

if  player_choice < 1 or player_choice > 5:
    print('El numero debe estar entre 1 y 5')
elif player_choice == random_number:
    print(f'Adivinaste el numero ({random_number}).')
elif player_choice > random_number:
    print(f'El numero elegido es muy alto. El número era {random_number}')
elif player_choice < random_number:
    print(f'El numero elegido es muy bajo. El número era {random_number} ')

