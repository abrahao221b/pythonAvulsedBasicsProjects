from calculatorAssets import *
import math

def subtration(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")
    return (num1 - num2)

def sum(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")
    return (num1 + num2)

def multiplication(num1, num2):
    print(f"{num1} * {num2} = {num1 * num2}")
    return (num1 * num2)

def division(num1, num2):
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
        return (num1 / num2)
    else:
        print("Indeterminacy!")
        return 0

def module(num1, num2):
    print(f"{num1} % {num2} = {num1 % num2}")
    return (num1 % num2)

def power(num1, pow):
    if pow == 0:
        print(f"{num1}^{pow} = {num1**pow}")
        return 1
    elif pow > 1:
        for i in range(1, pow):
            num1 *= num1
        print(f"{num1}^{pow} = {num1**pow}")
        return num1
    else:
        return root_any_number(num1, pow)

def root_any_number(num1, pow):
    if pow != 0:
        print(f"{num1}^{pow} = {num1**pow}")
        return num1**(1 / pow)
    else:
        print("Impossible!")
        return 0
    
def sin(num1):
    print(f"sin({num1}) = {math.sin(num1)}")
    return math.sin(num1)

def cos(num1):
    print(f"cos({num1}) = {math.cos(num1)}")
    return math.cos(num1)

def tan(num1):
    print(f"tan({num1}) = {math.tan(num1)}")
    return math.tan(num1)

def sec(num1):
    if num1 != 90 and num1 != 270:
        print(f"sec({num1}) = {1 / math.cos(num1)}")
        return (1 / math.cos(num1))
    else:
        print("Indeterminacy!")
        return 0

def cossec(num1):
    if num1 != 360 and num1 != 0:
        print(f"cossec({num1}) = {1 / math.sin(num1)}")
        return (1 / math.sin(num1))
    else:
        print("Indeterminacy!")
        return 0

def cotan(num1):
    if num1 != 90 and num1 != 270:
        print(f"tan({num1}) = {1 / math.tan(num1)}")
        return (1 / math.tan(num1))
    else:
        print("Indeterminacy!")
        return 0

def arcsin(num1):
    print(f"arcsin({num1}) = {math.asin(num1)}")
    return math.asin(num1)

def arccos(num1):
    print(f"arccos({num1}) = {math.acos(num1)}")
    return math.acos(num1)

def arctan(num1):
    print(f"arctan({num1}) = {math.atan(num1)}")
    return math.atan(num1)

def log(num1, base):
    if base > 0:
        print(f"log({num1}) = {math.log(num1, base)}")
        return math.log(num1, base)
    else:
        print("Impossible!")
        return 0

def permutation(number):
    if number == 0:
        return 1
    elif number > 1:
        number = int(number)
        result = 1
        for i in range(2, number+1):
            result *= i
        print(f"{number}! = {result}")
        return result

def menu():
    logo()
    num1 = 0
    num2 = 0
    while True:
        num1 = float(input("What's the first number?: "))
       
        while True:
            operations()
            picked_operation = input("Pick an operation: ").lower()
            num2 = float(input("What's the next number?: "))
            
            if picked_operation == "+":
                num1 = sum(num1, num2)
                print(num1)
            elif picked_operation == "-":
                num1 = subtration(num1, num2)
                print(num1)
            elif picked_operation == "*":
                num1 = multiplication(num1, num2)
                print(num1)
            elif picked_operation == "/":
                num1 = division(num1, num2)
                print(num1)
            elif picked_operation == "%":
                num1 = module(num1, num2)
                print(num1)
            elif picked_operation == "power":
                num1 = power(num1, num2)
                print(num1)
            elif picked_operation == "root":
                num1 = root_any_number(num1, num2)
                print(num1)
            elif picked_operation == "sin":
                choosen = int(input("What number do you want to test, 1 or 2: "))
                if choosen == 1:
                    num1 = sin(num1)
                else:
                    num1 = sin(num2)
                print(num1)
            elif picked_operation == "cos":
                choosen = int(input("What number do you want to test, 1 or 2: "))
                if choosen == 1:
                    num1 = cos(num1)
                else:
                    num1 = cos(num2)
                print(num1)
            elif picked_operation == "tan":
                choosen = int(input("What number do you want to test, 1 or 2: "))
                if choosen == 1:
                    num1 = tan(num1)
                else:
                    num1 = tan(num2)
                print(num1)
            elif picked_operation == "sec":
                choosen = int(input("What number do you want to test, 1 or 2: "))
                if choosen == 1:
                    num1 = sec(num1)
                else:
                    num1 = sec(num2)
                print(num1)
            elif picked_operation == "cossec":
                choosen = int(input("What number do you want to test, 1 or 2: "))
                if choosen == 1:
                    num1 = cossec(num1)
                else:
                    num1 = cossec(num2)
                print(num1)
            elif picked_operation == "cotan":
                choosen = int(input("What number do you want to test, 1 or 2: "))
                if choosen == 1:
                    num1 = cotan(num1)
                else:
                    num1 = cotan(num2)
                print(num1)
            elif picked_operation == "arcsin":
                choosen = int(input("What number do you want to test, 1 or 2: "))
                if choosen == 1:
                    num1 = arcsin(num1)
                else:
                    num1 = arcsin(num2)
                print(num1)
            elif picked_operation == "arccos":
                choosen = int(input("What number do you want to test, 1 or 2: "))
                if choosen == 1:
                    num1 = arccos(num1)
                else:
                    num1 = arccos(num2)
                print(num1)
            elif picked_operation == "arctan":
                choosen = int(input("What number do you want to test, 1 or 2: "))
                if choosen == 1:
                    num1 = arctan(num1)
                else:
                    num1 = arctan(num2)
                print(num1)
            elif picked_operation == "log":
                num1 = log(num1, num2)
                print(num1)
            elif picked_operation == "permutation":               
                choosen = int(input("What number do you want to test, 1 or 2: "))
                if choosen == 1:
                    num1 = permutation(num1)
                else:
                    num1 = permutation(num2)
                print(num1)
            else:
                print("Operation doesn't exist!")
                
            chosen_continue_same = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation: \n").lower()
            
            if chosen_continue_same == "n":
                break
                
        num1 = 0
        chosen_continue = input("You want to continue, if yes press \'y\' and enter, if no \'n\' and enter. \n").lower()
        
        if chosen_continue == "n":
            break
        
menu()