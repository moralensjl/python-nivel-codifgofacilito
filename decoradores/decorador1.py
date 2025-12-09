
def decorator(func):
    def wrapper(*args, **kwargs): # wrapper es la nueva funcion que va a reempleza persona.
        # wrapper= persona
        print('Antes de ejecutar la funcion original')

        result = func(*args, **kwargs) # func es la funcion que va a decorar a persona.
        # func = persona
        print('Despues de llamar a la funcion original')
        return result
    return wrapper


@decorator
def persona(nombre, edad, cuidad):
    return f'Mi nombre es: {nombre}, tengo {edad} y vivo en {cuidad}'


mi_persona = persona('Moralens, jean-louis',edad= 23, cuidad= 'Mexico')
print(mi_persona)

