
"""
Instrucciones: Crear un archivo llamado desafio_1.py y escribir un programa con lo siguiente:
Una variable con el nombre de un proyecto (ej. "Tienda Virtual").
Una variable con el presupuesto inicial (ej. 5000).
Una variable con el costo del servidor (ej. 150.50).
Calcular el presupuesto restante restando el costo al presupuesto inicial.
Imprimir un mensaje usando f-strings (ej. "El proyecto X tiene un presupuesto restante de: Y").

"""

nombre_proyecto = 'Tienda Virtual'
presupuesto_inicial = 5000
costo_servidor = 150.50

presupuesto_restante = presupuesto_inicial - costo_servidor
print(f"El proyecto {nombre_proyecto} tiene un presupuesto restante de {presupuesto_restante:.2f}")