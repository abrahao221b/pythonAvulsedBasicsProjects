
def sum(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1*number2

def division(number1, number2):
    return number1 / number2

def highfunction(number1, number2, func):
    return func(number1, number2)

print(highfunction(4, 5, division))