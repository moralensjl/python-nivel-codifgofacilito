dates = dict(nombre= 'Moralens', apellido= 'Jean-Louis', edad= 23, is_active= True)

class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def saludar(self):
        print(f"El nombre del usuario es: {self.nombre}")




u1 = Usuario('Anabel', '20')

usuario = {
    'nombre': u1.nombre,
    'edad': u1.edad,
    'saludo': u1.saludar
}

usuarios = (usuario,)
print(usuarios)

user = [u1.nombre, u1.edad, usuario, usuarios]
print(user)



print(usuario)
print(u1.__dict__)