def deposit(balance, amount=0):
    return balance + amount


def withdraw(balance, amount=0):
    if amount > balance:
        return None

    return balance - amount


def handle_operation(callback, *args, **kwargs):
    result = callback(args, kwargs)
    print(result)


default = lambda *args, **kwargs: '>>> Lo sentimos, opcion NO valida'


# func1 = deposit
# func2 = withdraw
#
# print(func1(100, 23))
# print(func2(200, 45))

options = {
    'a': deposit,
    'b': withdraw
}


option = input('Ingresa una opcion (a/b): ')
balance = int(input('Ingresa tu balance: '))
amount = int(input('Ingresa la cantidad: '))

function = options.get(option, default)
total = function(balance, amount)
print(total)







