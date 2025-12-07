def outer_function():
    message = 'Estamos dentro de una funcion'

    def inner_function():
        print(message)

    inner_function()

outer_function()

