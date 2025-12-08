
# print("PROVOCANDO ERRORES")
# try:
#     numero = float(input("Introduce un numero: "))
#     mitad = 4
#     resultado = numero + mitad
#     print(f"{numero} + {mitad} = {resultado}")
# except ValueError:
#     print("No puedes convertir una letra a numero decimal")


# while True:
#     try:
#         n = float(input("Introduce un numero:"))
#         m = 5
#         resultado = n ** m # Si el programa sale bien rompe la iteracion
#         print(f"{n} ** {m} = {resultado}")
#         # break
#     except ValueError:
#      print("No puedes convertir una letra a numero decimal")
#     else:
#         print("Todo ha funcionado correctamente")
#         break
#     finally:
#         print("Fin de la iteracion") # siempre de ejecuta

#
# try:
#     n = int(input("Introduce un numero: "))
#     print(5/n)
# except Exception as e:
#     print(e)
    # print(type(e).__name__)


try:
    n = int(input("Introduce tu asiento: "))
    if n == 13:
        raise TypeError
    else:
        print(f"Tu asiento es el: {n}")
except TypeError:
    print("El numero 13 esta prohibido")
except Exception as e:
    print(e)


