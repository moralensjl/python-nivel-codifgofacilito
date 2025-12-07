
#

for fizzbuzz in range(1, 101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print(f'FizzBuzz {fizzbuzz}')
    elif fizzbuzz % 3 == 0:
        print(f'Fizz {fizzbuzz}')
    elif fizzbuzz % 5 == 0:
        print(f'Buzz {fizzbuzz}')
    else:
        print(f'-> {fizzbuzz}')



game_fizzbuzz = int(input('Digite un numero: '))

if game_fizzbuzz % 3 == 0 and game_fizzbuzz % 5 == 0:
    print(f'FizzBuzz {game_fizzbuzz}')
elif game_fizzbuzz % 3 == 0:
    print(f'Fizz {game_fizzbuzz}')
elif game_fizzbuzz % 5 == 0:
    print(f'Buzz {game_fizzbuzz}')
else:
    print(f'-> {game_fizzbuzz}')















