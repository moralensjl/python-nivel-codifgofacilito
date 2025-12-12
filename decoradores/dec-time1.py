import time

def decorador(func):
    def wrapper(*args, **kwargs): # esta funcion, wrapper, envuelve a la funcion operacion. lo reemplaza.
        start = time.time()
        time.sleep(4)
        print(f'El tiempo trascurrido fue {time.time() - start:.4f}')
        result = func(*args, **kwargs) # func, va decorar a la funcion operacion
        print('Despues de la ejecucion')
        return result
    return wrapper

@decorador
def operacion(*args, **kwargs):
    return f'{args} {kwargs}'


print(operacion('Madrid', 'Mexico', nombre= 'Moralens', edad= 23, altura= 1.78))


