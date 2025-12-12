
def info_personal(*datos, **carrera):
    print('Datos personales')
    return f"{datos}, {carrera}"


print(info_personal('Moralens', 'Jean-Louis', '23', 'Mexico',
                    universidad= 'UNAD',
                    carrera='Teologia',
                    cursos= 'Python'))


def suma(*numeros):
   total = 0
   for num in numeros:
       total += num
   return total

print(suma(1, 2, 3, 10, 11, 45, 90))

