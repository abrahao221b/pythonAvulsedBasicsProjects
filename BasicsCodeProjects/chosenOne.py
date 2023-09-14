# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
chosen_one = random.randint(0, len(names) - 1) 
print(f"{names[chosen_one]} is going to buy the meal today!")

# The code could be simplified with the choice function, but it couldn't be used in the answer!
chosen_one_simple = random.choice(names)
print(f"{chosen_one_simple} is going to buy the meal today!")