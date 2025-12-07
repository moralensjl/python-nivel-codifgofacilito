# Metodos para agregar elementos a una lista
course: list[str] = ['Python', 'Django', 'Flask', 'Ruby', 'MongoDB']
new_courses: list[str] = ['React', 'Next']
print()

course.append('Ruby on Rails') # Nos permite agregar un nuevo elemento a la lista
course.append('PHP')
course.append('Laravel')

course.insert(0, 'Rust')
course.insert(4, 'C#')
course.insert(2, 'MySQL')

course.extend(new_courses) # Nos permite agregar nuevo elementos a la lista. Incrementamos la lista.
print(course)

print('Vue' in course) # Para saber si un elemento esta dentro de la lista
print(course.index('MySQL'))

if 'Python' in course:
    print('Dicho elemento esta en la lista')
else:
    print('No se encuentra en la lista')


# Metodos para eliminar elementos
course.remove('Python')
course.remove('Django')
remove = course.pop()
print(remove)
print(course)

course.clear() # Vacia la lista
print(course)