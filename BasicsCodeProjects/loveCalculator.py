# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
ocurs_true = 0
ocurs_love = 0
#Joining the names makes the problem a lot easier way 
full_name = name1 + name2
full_name = full_name.upper()

for i in "TRUE":
    for a in full_name:
       if a == i:
           ocurs_true += 1

for i in "LOVE":
    for a in full_name:
        if a == i:
            ocurs_love += 1

total = f"{ocurs_true}{ocurs_love}"
total = int(total)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total < 50 and total > 40:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

