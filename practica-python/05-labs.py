
"""

Vamos a aplicar esto a tu proyecto "Tienda Virtual". Las reglas de negocio han cambiado
y necesitamos calcular el costo de envío automáticamente según cuánto compre el cliente.

Instrucciones: Crea un archivo desafio_2.py y escribe un script que haga lo siguiente:
Define una variable total_compra con un monto (ej. 120.00).
Implementa la siguiente lógica de envíos usando if/elif/else:
Si la compra es menor a $50: El envío cuesta $10.
Si la compra es mayor o igual a $50 pero menor a $100: El envío cuesta $5.
Si la compra es **mayor o igual a $100**: El envío es GRATIS ($0).
Calcula el total_final (compra + envío).
Imprime un mensaje final que diga: "Para una compra de $[monto], el envío es
$[costo] y el total a pagar es $[total_final]".

"""
from copyreg import constructor

# total_compra = 150.00
#
# if total_compra < 50:
#     costo_envio = 10
# elif total_compra >= 50 and total_compra < 100:
#     costo_envio = 5
# else:
#     costo_envio = 0.0
#
# total_final = total_compra + costo_envio
# print(f"Para una compra de {total_compra} el envio es {costo_envio} y el total a pagar es {total_final}")

calificacion = 8
try:
    if calificacion >= 10:
        promedio = 4.0
    elif calificacion <= 7:
        promedio = 3.5
    elif calificacion <= 5:
        promedio = 2.5
    else:
        promedio = 1

    promedio_calificacion = calificacion / promedio
    print(f"El promedio final del estudiante es {promedio_calificacion}")

except ZeroDivisionError as e:
    print(e)





