# Diagramas de flujo
nombre = input("Escribe tu nombre: ")
if nombre.capitalize() == "Moralens":
    print(f"{nombre} es mi nombre.")
else:
    print(f"{nombre} no es mi nombre.")


num1 = int(input("Escribe un numero: "))
num2 = int(input("Escribe el segundo numero: "))
num3 = int(input("Escribe el tercer numero: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} es mayor a {num2} y mayor a {num3}.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} es mayor a {num1} y mayor a {num3}.")
elif num3 > num1 and num3 > num2:
    print(f"{num3} es mayor a {num2} y mayor a {num1}.")


a = [1,2,3,4,5]
for i in a:
    print(i)

    if i % 2 == 0:
        print(f"{i} es par.")



for j in range(0, len(a)):
    print(a[j])

    if a[j] % 2 == 0:
        print(f"{a[j]} es par.")