nfl = int(input("Coloque un numero por pantalla para el grito de su equipo NFL: "))
if nfl == 1:
    team = "49ers"
elif nfl == 2:
    team = "Colts"
elif nfl == 3:
    team = "Raven"
elif nfl == 4:
    team = "Rams"
elif nfl == 5:
    team = "Falcons"
else:
    team = "Opcion no valida"


battle_cries = {
    "49ers" : "Faithful to The Bay",
    "Colts" : "For the Shoe 🐎👟",
    "Raven" : "Play Like a Raven",
    "Rams" : "Whose House? Rams House! 🐏💥",
    "Falcons" : "Rise Up 🦅",
    "Opcion no valida" : "No valida",
}

print(f"NFL Team Battle Cries: {team} => {battle_cries.get(team)}")