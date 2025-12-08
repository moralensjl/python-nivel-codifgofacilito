
calificaciones = [10, 7, 9, 8, 7]

def promedio(numeros):
    total = 0
    suma = 0

    for numero in numeros:
        total = total + 1
        suma = suma + numero

    print(suma / total)

promedio(calificaciones)


def mas_diez_caracteres(mensaje):
    total = 0

    for caracter in mensaje:
        print(caracter, mensaje)
        total = total + 1

    print(total)

mas_diez_caracteres(mensaje= "Live CodigoFacilito")