def say_hello():
    print('Hola, desde una funcion')


say_hello()

def say_goodbye():
    print('Finalizando el script')

for _ in range(10):
    say_hello()
say_goodbye()


# funciones con parametro sin retorno
def count_to(number):
    for n in range(1, number + 1):
        print(n)


count_to(10)


def full_name(firt_name, last_name, prefix):
    full_data = f'{prefix} {firt_name} {last_name}'
    print(full_data)

full_name('Moralens','Jean-Louis','Mr.')


# funciones con retorno y parametro
def nombre_completo(nombre, apellido, edad):
    data = f'{nombre} {apellido} {edad}'
    return data

print(nombre_completo('Arya', 'Fonteccino', 32))


# Args
def suma(*numbers):
    return sum(numbers)

print(suma(2,  3, 4, 5, 7, 9, 6, 9, 5, 7))


def show_info(username, email, *scores): # Args: argumentos por posicion
    print(username)
    print(email)

    average = sum(scores) / len(scores)
    print(average)

show_info(
    'Cody',
    'cody@codigofacilito@gmail.com',
    10, 10, 8, 9, 9, 5 # Esto es una tupla
)

# Kwargs: Pasamos argumentos por nombres
def mostrar_info(**user):
    print(user)
    for key, values in user.items():
        print(key, '-', values)


mostrar_info(
    username= 'Cody',
    email= 'cody@codicofacilito.com',
    password= '1234',
    active=True,
    courses= ['Python', 'Django', 'Flask']
)

# Args y kwargs

