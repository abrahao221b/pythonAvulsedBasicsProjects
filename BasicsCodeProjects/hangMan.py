from hangManImg import *

# Date: 18/04/2023
# Version 1.0.0
# Words for the game
words = {"beekeeper", "helldog", "bubblesort", "mergesort", "quicksort", "selectionsort", "insertionsort", "computer", "hardware", "elefant"}

# Printing the logo game
logoImg()

# Displaying the word
def display_word(empty_word):
    empty_word_display = ""
    for i in empty_word:
        empty_word_display += i
    print(empty_word_display)

# Linear search to find the letters guessed by the player
def linear_search_letters(word, letter, letters_positions):
    for i in range(len(word)):
        if word[i] == letter:
            letters_positions.append(i)

# Verifying the player state in the game
def game_state(empty_word):
    if "_" not in empty_word:
        return True
    return False

# Game main function
def game():
    life = 6
    empty_word = []
    word = list(words.pop())
    win_state = False
   
    # Putting the symbol "_" inside the empty_word list
    for i in range(len(word)):
        empty_word.append("_")
    
    # Main loop in the game
    while life > 0:
        player_guess = input("Guess a letter: ")
        letters_positions = []
        
        # Verifying the player guess
        if player_guess in word:
            linear_search_letters(word, player_guess, letters_positions)
            for i in letters_positions:
                empty_word[i] = player_guess 
        else:
            print(f"You guessed {player_guess}, that's not in the word. You lose a life.")
            life -= 1
        
        # Displaying the body state    
        bodyHangMan(life)
        # Displaying the empty word
        display_word(empty_word)
        
        # Verifying the player's state in the game
        win_state = game_state(empty_word)
        
        # Win state
        if win_state:
            win_game()
            break
        
    # Loose state    
    if life == 0:
        loose_game()    

# Calling the game function 
game()    





