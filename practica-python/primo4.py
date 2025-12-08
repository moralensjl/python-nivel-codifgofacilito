
def es_par(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for num in range(1, 101):
    if es_par(num):
        print(num)