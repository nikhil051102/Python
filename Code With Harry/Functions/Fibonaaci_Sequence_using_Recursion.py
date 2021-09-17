# Fibonaaci Series
number = int(input("Which term do you want, Enter its Place : "))

def fibonacci(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)

print(fibonacci(number))