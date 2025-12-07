# Sub-listas
course = ['Python', 'Django', 'Flask', 'Ruby', 'MongoDB']

new_list = [course[0], course[1], course[2]]
#print(new_list)

list_slicing = course[2:5]
print(list_slicing)

copy_course = course[::2] # Hace un salto en las listas
copy_courses = course[::-1] # invierte la lista
print(copy_courses)