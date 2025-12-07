dates = dict(nombre= 'Moralens', apellido= 'Jean-Louis', edad= 23, is_active= True)

print(dates["apellido"])
print(dates.get("edad"))

# Keys, values, item
print(dates.keys()) # Nos muestra todas las llaves del dict
print(list(dates.keys())) # Una lista de llaves
print(tuple(dates.keys())) # Una tupla de llaves
print('----------------------------------------->')
print(dates.values())
print(list(dates.values()))
print(dates.items())