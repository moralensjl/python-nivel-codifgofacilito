course: list[str] = ['Python', 'Django', 'Flask', 'Ruby', 'MongoDB']

copy_list = course.copy()
print(copy_list)

course.reverse()
print(course)

course.sort() # Ordena los elementos
print(course)

course.sort(reverse=True)
print(course)