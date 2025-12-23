# practicando con callback function en python

def lista_estudiantes(datos):
    for key, values in datos.items():
        print(f'{key}: {values}')


def nombres_y_promedio(datos):
    print(f'nombres y promedio de los estudiantes: {datos.get("nombres_y_promedio")}')


def cursos(formaciones):
    print(f'cursos de programacion y computacion: {formaciones.get("cursos")}')



def main(datos, callback):

    callback(datos)


if __name__ == "__main__":
    estudiantes = {
        "nombres_y_promedio": [('ana', 'miguel', 'sara', 'noemi', 'james'),
                    (8.5, 6.4, 9.2, 7.3, 5.5)],
        "cursos": ['fronted', 'programacion python', 'análisis de datos', 'ciencia de datos', 'IA']
    }
    main(estudiantes, lista_estudiantes)
    main(estudiantes, nombres_y_promedio)
    main(estudiantes, cursos)
