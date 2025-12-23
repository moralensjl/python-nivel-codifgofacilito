# quiero hacer un programa donde haya una funcion que tenga una lista de nombres
# en otra funcion quiero recorrer esa lista de nombres
# y finalmente mediante un callback llamar a esas funciones

def mostrar_nombres(nombre):
    for name in nombre:
        print(f"nombres: {name}")


def elementos(nombre):
    print(f"accediendo al ultimo nombre: {nombre[5]}")


def mostrar(nombre, callback):
    callback(nombre)


if __name__ == '__main__':
    nombres = ['ana', 'fernando', 'pepe', 'lidia', 'marco', 'sara']
    mostrar(nombres, mostrar_nombres)
    mostrar(nombres, elementos)