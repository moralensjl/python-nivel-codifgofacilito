# 5) Realiza una función llamada agregar_sin_repetidos() que reciba una lista y un elemento.
# La función debe añadir el elemento al final de la
# lista con la condición de no repetir ningún elemento. Además si este elemento ya se encuentra en la
# lista se debe invocar un error de tipo
# ValueError que debes capturar y mostrar este mensaje en su lugar:
# Error: Imposible añadir elementos duplicados => [elemento].
# Prueba a agregar los elementos 7, "Python" y 5 a través de la función agregar_sin_repetidos() e
# imprime la lista completa al finalizar.
# Pista: Puedes utilizar la sintaxis: elemento in lista
# Datos de entrada:



def agregar_sin_repetidos(lista, elemento):
    try:
        # verificar si el elemento ya esta en la lista
        if elemento in lista:
            # si esta, lanzar el error con el mensaje especifico
            raise ValueError(f"Error: Imposible agregar elementos duplicados => {elemento}.")

        # si no esta agregarlo al final de la lista
        lista.append(elemento)
        return lista

    except ValueError as error:
        print(error)
        return lista

mi_lista = [7, "python", 5]
#print("Intentando agregar 7:")
#mi_lista = agregar_sin_repetidos(mi_lista, 7)
mi_lista = agregar_sin_repetidos(mi_lista, "JavaScript")
mi_lista = agregar_sin_repetidos(mi_lista, "TypeScript")
print(mi_lista)

