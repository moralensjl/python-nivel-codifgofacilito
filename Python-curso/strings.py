# Strings
# Split: Genera una lista a partir de un String
# Join: Genera un String a partir de una lista

courses = "Python PHP Ruby Django MongoDB"
list_courses = courses.split(' ')
print(courses)
print(list_courses)

cursos = ["Python", "Django", "Flask", "PHP"]
message_cursos = ', '.join(cursos)
print(message_cursos)


# Generar nuevos strigs
name = 'Moralens'
last_name = 'Jean-Louis'
full_name = f'{name} {last_name}'
print(full_name)

full_name = ' * '.join([name, last_name])
print(full_name)