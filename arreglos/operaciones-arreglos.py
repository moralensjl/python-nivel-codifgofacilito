
arreglo = [1, 3, 5, 7, 8]

# Metodo insert
arreglo.insert(2,5)
print(arreglo)

# Metodos pop/ para eleminar el ultimo elemento
arreglo.pop() # Sin parametros elimina el ultimo. con parametros elimina la posicion
arreglo.pop(2)
print(arreglo)

# Metodo append
arreglo.append("Perro")
print(arreglo)

# Metodo sort
# Sort no ordena si hay datos diferentes
arreglo_desordenado = [9, 5, 7, 2, 0]
print(arreglo_desordenado)
arreglo_desordenado.sort()
print(arreglo_desordenado)

# Reverse
arreglo_desordenado.reverse() # Invierte el orden
print(arreglo_desordenado)

# Count
arreglo_number = [3, 3, 3, 5, 7, 7, 9]
print(arreglo_number.count(3)) # Cuenta la cantidad de elementos que hay en una lista

# Remove
arreglo_number.remove(3)
print(arreglo_number) # Elimina la primera coicidencia

# Extend
# Clear
arreglo_number.clear()
print(arreglo_number)

# Copy
granja = ["Vaca", "Conejo", "Caballo", "Perro", "Gallina"]
granja2 = granja.copy()
print(granja2)
print(granja)

