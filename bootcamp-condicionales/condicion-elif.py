import random


# score = float(input("Ingresa tu puntaje en numeros: "))
# if 4.5 <= score < 5:
#     grade = "E" # Estas son las llaves del diccionario.
# elif 4 <= score < 4.5:
#     grade = "S"
# elif 3 <= score < 4:
#     grade = "A"
# elif 2 <= score < 3:
#     grade = "I"
# elif 0 <= score < 2:
#     grade = "D"
# else:
#     grade = "Puntaje invalido"
#
# grades = {
#     "E": "Excelente",
#     "S": "Sobresaliente",
#     "A": "Aceptable",
#     "I": "Insuficiente",
#     "D": "Deficiente",
# }
#
# print(f"Tu puntaje es -> {grade}: {grades.get(grade) or '' }")
# print(grades[grade])

# Juego de piedra, papel, tijera

try:
# aca lo que selecciona el usuario
    player_choice_input = input("Piedra(Rock), Papel(Paper) Tijera(Scissor)? (r/p/s): ")

    player_choice = player_choice_input.lower()

    if player_choice not in ['r', 'p', 's']:
        raise Exception("Opcion invalida")

    computer_choice = random.choice(["r", "p", "s"])

    print(f"Eleccion del computador: {computer_choice}")

    if player_choice == computer_choice:
        print("Empate (Tie)")
    elif player_choice == "r" and computer_choice == "s":
        print("Human win!")
    elif player_choice == "s" and computer_choice == "p":
        print("Human win!")
    elif player_choice == "p" and computer_choice == "r":
        print("Human win!")
    else:
        print("Computer wins!")
except Exception as error:
    print(f"Error en la condicion: {error}")

