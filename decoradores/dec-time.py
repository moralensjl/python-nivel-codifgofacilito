import time

def decorador_timer(a, b):
    time.sleep(1)
    return a + b


print(decorador_timer(5, 6))

