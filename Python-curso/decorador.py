def decorator(func):

    def wrapper():
        print('>>> Antes del llamado')
        func()
        print('>>> Despues del llamado')

    return wrapper


@decorator
def hello_world():
    print('Hello world')

hello_world()
