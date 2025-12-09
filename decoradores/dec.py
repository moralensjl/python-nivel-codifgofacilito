def plantilla(func):
    # Antes de llamar a la función original, ejecutamos ( for...range() ) algo.
    def wrapper(a, b): # Esto invoca(llama) a la funcion suma. wrapper invoca a la funcion. wrapper(4, 2)
        # Wrapper es donde se ponen lo valores de la funcion.
        # ej: wrapper(3, 4)
        for i in range(0, 10): # Esto se ejecuta antes
            print(i)
        funcion = func(a, b) # Esto ejecuta la funcion suma. Llamamos a la funcion original que es suma()
        print('Despues de...') # Después de que se ejecuta la funcion suma se imprime este mensaje
        return funcion
    return wrapper


# Cuando escribes esto, realmente ocurre lo siguiente:
#
# suma(4, 2) → en realidad llama a wrapper(4, 2) (porque suma fue reemplazada por wrapper).
#
# Dentro de wrapper:
#
# Se ejecuta print('Antes de...')
# 👉 aparece en pantalla Antes de...
#
# Luego se ejecuta func(a, b) → esto es suma(4, 2) (la función original).
#
# Dentro de suma se imprime Dentro de la funcion suma
#
# Y retorna 4 + 2 = 6
#
# Después se imprime Despues de...
#
# Finalmente, wrapper devuelve el resultado 6.
#
# Ese 6 se pasa al print() externo, y por eso ves el número al final.


@plantilla
def suma(a, b):
    print('Dentro de la funcion suma')
    return a + b

print(suma(4, 2))
