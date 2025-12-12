# diccionarios

usuario = dict()

#agregando nuevo llave valor
usuario['nombre'] = 'moralens'
usuario['edad'] = 23
usuario['activo'] = True
usuario['nombre_usuario'] = 'moralens06'
print(usuario)

# actualizar valor mediante una llave
usuario['nombre_usuario'] = 'moralens_j6'
print(usuario)

# obtener valor mediante una llave
print(usuario['nombre_usuario'])

# obtenemos las llaves del diccionario mediante keys
print(usuario.keys()) # dict_keys(['nombre', 'edad', 'activo', 'nombre_usuario'])

# obtenemos las llaves del diccionario mediante values
print(usuario.values()) # dict_values(['moralens', 23, True, 'moralens_j6'])

# para obtener clave valor lo podemos hacer mediante un for
for keys, values in usuario.items():
    print(f'{keys}: {values}')


calificacion = usuario.get('calificacion', [])
print(calificacion)