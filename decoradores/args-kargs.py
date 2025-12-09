# funcion designada a variable
def saludar(nombre):
    return f"Hola {nombre}"

# podemos definir una funcion dentro de una funcion
def exterior():
    def interior():
        return "Hola desde la funcion interior"
    return interior()

# podemos pasar una funcion como argumento a otra funcion
def funcion_exterior(funcion):
    return funcion()

def saludo():
    return "Hola"

# una funcion puede retornar otra funcion
def exterior1():
    def interior():
        return "Hola desde interior"
    return interior # retorna la funcion, no la ejecuta.




if __name__ == "__main__":
    mi_funcion = saludar
    print(mi_funcion("Ana"))

    print(exterior())

    print(funcion_exterior(saludo))

    mi_funcion1 = exterior1() # mi funcion ahora es la funcion interior
    print(mi_funcion1()) # imprime 'hola desde el interior'