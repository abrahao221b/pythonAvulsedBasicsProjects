#Write your code below this line 👇


def eratosthenes_cipher(number):
    if number == 0 or number == 1:
        return False
    primes = []
    test = number + 1
    
    for i in range(test):
        primes.append(True)
    
    primes[0] = False
    primes[1] = False
    primes[2] = True
    for i in range(2, test):
        for j in range(i, test):
            if i*j < test:
                primes[i*j] = False
            else:
                break   
    return primes[number]
        

def prime_checker(number):
    if eratosthenes_cipher(number):
        print("It's a prime number.")
    else:
        print("It isn't a prime number.")
        



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
