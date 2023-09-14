from highrLowerAssets import *
import os
import random

def fight_choose(data):
    return random.choice(data)

def person_features_print(person, up):
    if up:
        print(f"Compare A: {person['name']}, a {person['description']}, from {person['country']}.")
    else:
        print(f"Compare B: {person['name']}, a {person['description']}, from {person['country']}.")

def game():
    wrong_answer = False
    score = 0
    endgame = False
    
    second_person = {}
    first_person = fight_choose(data)
    
    while(not endgame):
        logo()
        second_person = fight_choose(data)
        person_features_print(first_person, True)
        vs_symbol()
        person_features_print(second_person, False)
        choose = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if choose == "a":
            if first_person['follewer_count'] < second_person['follewer_count']:
                wrong_answer = True
            else:
                score += 1
        elif choose == "b":
            if second_person['follewer_count'] < first_person['follewer_count']:
                wrong_answer = True
            else:
                score += 1
        else:
            wrong_answer = True
        
        os.system("clear")
        if not wrong_answer:
            first_person = second_person
        else:
            endgame = True
    
    return score

def menu():
    final_score = game()
    print(f"Sorry, that's wrong. Final score: {final_score}")
    
menu()