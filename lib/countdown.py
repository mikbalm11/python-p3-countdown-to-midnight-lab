import time

def countdown(timer):
    while timer > 0:
        print(f"{timer} SECOND(S)!")
        timer -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(timer):
    while timer > 0:
        print(f"{timer} SECOND(S)!")
        timer -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")