#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

coin_face = random.randint(0, 1)

if coin_face == 0:
    print("Heads")
else:
    print("Tails")