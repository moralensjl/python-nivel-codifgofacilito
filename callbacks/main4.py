
def nombres_estudiantes(info):
    estudiantes = ['ana', 'cristian', 'abel', 'noemi']
    print(info)
    print(f'nombre del primer estudiante: {estudiantes[0]}')

def calificaciones(info):
    notas = [10, 8, 7, 6]
    print(info)
    print(f'calificacion del primer estudiante: {notas[0]}')


def centro_educativo(callback):
    mostrar = "detalles"
    callback(mostrar)



centro_educativo(nombres_estudiantes)
centro_educativo(calificaciones)

