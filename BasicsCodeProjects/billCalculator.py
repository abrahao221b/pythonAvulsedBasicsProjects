print("Welcome to the tip calculator.")
bill = input("What was the total bill? ")
people = float(input("How many people to split the bill? "))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))

# Calculator code

# Taking off the "$" symbol
bill = [i for i in bill if i != "$"]

# Finding the bill's power in the 10 base 
power = 0
for i in bill:
    if i == ".":
        break
    power += 1

# Taking off the "." symbol    
bill = [i for i in bill if i != "."]

# Creating a new variable for the bill
new_bill = 0

# Decreasing the variable power by 1
power -= 1

# Making the bill's number
for i in bill:
    new_bill += float(i) * (10**power)
    power -= 1
    
# Calculating the bill split and printing 
split = (new_bill / people) + ((new_bill * (percentage_tip / 100)/people))
split_format = "{:.2f}".format(split) 
print(f"Each person should pay: ${split_format}")