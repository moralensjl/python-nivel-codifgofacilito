

rango = 0
while rango < 101:
    rango += 1

    if rango % 3 == 0 and rango % 5 == 0:
        print(f"fizzbuzz -> {rango}")
    elif rango % 3 == 0:
        print(f"fizz -> {rango}")
    elif rango % 5 == 0:
        print(f"buzz -> {rango}")
    else:
        print(rango)



