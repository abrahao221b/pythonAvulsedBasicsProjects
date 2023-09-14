from blindAuctionAssets import logo
import os


def veredict(action_dictionary):
    biger_action = -99999
    biger_action_name = ""
    for person in action_dictionary:
        if action_dictionary.get(person) > biger_action:
            biger_action_name = person
            biger_action = action_dictionary.get(person)
            
    return (biger_action_name, biger_action)

    
def menu():
    logo()
    action_dictionary = {}
    biger_action = 0
    biger_action_name = ""
    while True:
        name = input("What is your name?: \n")
        action = float(input("What is your bid?: $"))
        more_people = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
        action_dictionary.update({name: action})
        if more_people == "no":
            break
        os.system('clear')
        
    biger_action_name, biger_action = veredict(action_dictionary)
    print(f"The winner is {biger_action_name} with a bid of ${biger_action}")
            
            
menu()