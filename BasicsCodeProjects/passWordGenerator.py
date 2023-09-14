import random

# Lists
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol_list = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "§", "Ø", "<", ">", "/", "?", "¿", "¡", "°", "[", "]", "|", "Ñ"]

# Print
print("Welcome to the PyPassword Generator!")

# Varaibles
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

# Password size
size = letters + symbols + numbers

pass_word = ""
letters_size = len(letter_list) - 1
symbols_size = len(symbol_list) - 1
numbers_size = len(number_list) - 1

how_many_letters = 0
how_many_symbols = 0
how_many_numbers = 0
i = 0

# Password algorithm
while i < size:
    element_position = random.randint(0, 2)
    if element_position == 0 and how_many_letters <= letters - 1:
        how_many_letters += 1
        upper_or_lower = random.randint(0, 1)
        position = random.randint(0, letters_size)
        if upper_or_lower == 1:
            pass_word += letter_list[position].lower()
        else:
            pass_word += letter_list[position]
        i += 1
    elif element_position == 1 and how_many_symbols <= symbols - 1:
        how_many_symbols += 1
        pass_word += symbol_list[random.randint(0, symbols_size)]
        i += 1
    elif element_position == 2 and how_many_numbers <= numbers - 1:
        how_many_numbers += 1
        pass_word += number_list[random.randint(0, numbers_size)]
        i += 1
    
print(list(pass_word))
print(f"You password is: {pass_word}")

