"""
Lambda <parametros>: <body> # Siempre retornan un valor
"""
suma = lambda num1, num2: num1 + num2
print(suma(4, 6))

add = lambda *args: sum(args)
print(add(5, 6, 6, 8, 9, 11, 45))

deposit = lambda balance, amount=0: balance + amount


