from guessNumberGameAssets import *
import random

player_life = 0

def fill_number_list():
    number_list = []
    for i in range(1, 101):
        number_list.append(i)
    
    return number_list

def show_player_life(life):
    print(f"You have {life} attempts remaining to guess the number.")

def game(player_life):
    number_list = fill_number_list()
    choosen_number = 0
    player_number = 0
    player_guess = False
    
    choosen_number = random.choice(number_list)
    
    while((not player_guess) and player_life > 0):
        player_number = int(input("Make a guess: "))
        if player_number == choosen_number:
            player_guess = True
            print(f"You got it! The answer was {choosen_number}.")
        elif player_number > choosen_number:
            if (player_number - choosen_number) < 10:
                print("High, but almost there.\nGuess again.")
            else:
                print("Too high.\n Guess again.")
            player_life -= 1
            show_player_life(player_life)         
        elif player_number < choosen_number:
            if (choosen_number - player_number) < 10:
                print("Low, but almost there.\nGuess again.")
            else:
                print("Too low.\n Guess again.")
            player_life -= 1
            show_player_life(player_life)
        
    if not player_guess:
        print(f"You've run out of guesses, you lose. The correct number was {choosen_number}!")
        
def menu():
    logo()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    global player_life
    
    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if game_difficulty == "easy":
        player_life = 10
    elif game_difficulty == "hard":
        player_life = 5
    else:
        player_life = 3
        print("Error, error, error!!!!")
        
    show_player_life(player_life)
        
    game(player_life)
    

menu()
        
    