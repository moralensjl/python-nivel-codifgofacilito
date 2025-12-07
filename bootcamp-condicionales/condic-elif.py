

edad = int(input("Ingrese su edad por pantalla: "))
if edad < 18:
    categoria = "adolescente, niño"
elif 18 <= edad < 21:
    categoria = "Joven"
elif 21 <= edad < 30:
    categoria = "Joven adulto"
elif 30 <= edad < 40:
    categoria = "Adulto"
elif 40 <= edad < 50:
    categoria = "Adulto maduro"
elif 50 <= edad < 60:
    categoria = "Vejez temprana"
else:
    categoria = "Muy avanzado en la vejez"


nivel_de_edad = {
    "A": "adolescente, niño",
    "B": "joven",
    "C": "joven adulto",
    "D": "adulto",
    "E": "adulto maduro",
    "F": "vejez temprana",
    "G": "muy avanzado en la vejez",
}

print(f'Su categoria de edad es: {categoria} {nivel_de_edad.get(categoria) or ''}')