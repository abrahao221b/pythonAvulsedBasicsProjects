from blackJackAssets import *
import random
import os

# Sum function for list
def sum(hand_list):
    '''
        Sum all the integers numbers inside a list. Only receives a list
    '''
    if not hand_list == []:
        result = 0
        for i in hand_list:
            result += i 
        return result

# Implementing the ace function, getting the best play
def ace(hand_list):
   '''
     Puts the ace card as the best value possible for the players. Only receives a list
   '''
   # Verifying the hand_list function and doing the best play possible
   for i in range(len(hand_list) - 1):
       if hand_list[i] == 1:
           result = sum(hand_list) - 1
           result += 11
           if result < 21:
               hand_list[i] = 11
       elif hand_list[i] == 11:
           result = sum(hand_list)
           if result > 21:
               hand_list[i] = 1
           
    
# Shuffle function
def shuffle(hand_list_player, hand_list_computer, player_play, game_round, player_points, computer_points):
    '''
        Implements the dealer's shuffle action, and returns the sum for the player and computer's points. 
        Receives: the computer's list (list), the player's list (list), 
        whether the player does want to play (boolean), game round (integer), 
        player's points (integer), computer's points (integer). 
        Returns: the player's points, computer's points and the whether is the computer endgame
        
    '''
    computer_end_no = False
    # If it is the first round
    if game_round == 1:
        hand_list_computer.append(random.choice(cards_list))
        hand_list_computer.append(random.choice(cards_list))
        hand_list_player.append(random.choice(cards_list))
        hand_list_player.append(random.choice(cards_list))
    else:
        # Verifying whether the player wants to play
        if player_play and player_points < 21:
            hand_list_player.append(random.choice(cards_list))
        else:
            while(player_points > computer_points and (21 - computer_points) > 4):
                hand_list_computer.append(random.choice(cards_list))
                ace(hand_list_computer)
                computer_points = sum(hand_list_computer)
                
            computer_end_no = True
            
    # Calling the ace function
    ace(hand_list_computer)
    ace(hand_list_player)        
    return (sum(hand_list_player), sum(hand_list_computer), computer_end_no)

# Game over function 
def game_over(player_points, computer_points, end_no, computer_end_no):
    ''' 
        Verifying if the game is over. Receives: player's points (integer), computer's points (integer), 
        whether is the player endgame (boolean) and if is the computer endgame (boolean).
        Returns nothing. 
    '''
    # Verifying whether the game is over
    if player_points > 21 or computer_points > 21:
        return True
    elif (end_no and computer_end_no) and (computer_points > player_points or player_points > computer_points 
                                           or computer_points == player_points):
        return True
    elif (not end_no and computer_end_no) and (computer_points > player_points or computer_points < player_points 
                                               or computer_points == player_points):
        return True
    return False

# Function that prints the game round
def game_print(over, player_cards, player_points, computer_cards, computer_points):
    '''
        Prints the game's round. Receives: over (boolean), player cards (list), 
        player's points (integer), computer's cards (list) and computer's points (integer). 
        Returns nothing.
    '''
    # Printing the game round. Depends on the result of the round
    if not over:
        print(f"Your cards: {player_cards}, current score: {player_points}")
        print(f"Computer's first card: {computer_cards[0]}")
    else:
        print(f"Your final hand: {player_cards}, current score: {player_points}")
        print(f"Computer's final hand: {computer_cards}, current score: {computer_points}")

# Function that prints the game final result
def game_result(over, end_no, computer_end_no, player_points, computer_points):
    '''
       Printing the game final result of the game. Receives: over (boolean), 
       whether is the player endgame (boolean), if is the computer endgame (boolean), 
       player's points (integer) and computer's points (integer). Returns nothing.
    '''
    
    # Verifying the game result that will be print
    if over and (end_no or computer_end_no) and player_points == computer_points:
        print('''Draw 🙃''')
    elif over and player_points < 21 and computer_points > 21:
        print('''Opponent went over. You win 😁''')
    elif over and (end_no or computer_end_no) and player_points < 21 and computer_points == 21:
        print('''Lose, opponent has Blackjack 😱''')
    elif over and player_points == 21 and ((computer_points > 21 or computer_points < 21) and computer_end_no):
        print('''Win with a Blackjack 😎''')
    elif over and player_points > 21:
        print('''You went over. You lose 😭''')
    elif over and (end_no or computer_end_no) and player_points < computer_points:
        print('''You lose 😤''')
    elif over and (end_no or computer_end_no) and computer_points < player_points:
        print('''You win 😃''')


# Game function
def game():
    ''' 
        Game function. Receives nothing and returns nothing.
    '''
    
    # Cleaning the console screen
    os.system("clear")
    # Printing the game logo 
    logo()
    
    # Variables
    game_round = 1
    player_points = 0
    computer_points = 0
    player_cards = []
    computer_cards = []
    over = False
    play = False
    end_no = False
    computer_end_no = False
    
    # Beginning of the game
    while(not over):
        if not over:
             # Calling the shuffle function
            player_points, computer_points, computer_end_no = shuffle(player_cards, computer_cards, play, game_round, 
                                                                      player_points, computer_points)
            game_round += 1
            # Verifying whether the game is over
            over = game_over(player_points, computer_points, end_no, computer_end_no)
        
        # Printing the game 
        game_print(over, player_cards, player_points, computer_cards, computer_points)
        
        # Printing the game final result
        game_result(over, end_no, computer_end_no, player_points, computer_points)

        if not over:
            # Asking if the player does want a card or not
            want_play = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            # Verifying whether is the final play of the player
            if want_play == "y" and not play and not end_no:
                play = True
            elif want_play == "n" and play:
                play = False
                end_no = True
            elif want_play == "n" and not play and computer_end_no:
                play = False
                end_no = True     
        
# Menu function
def menu():
    
    ''' Menu function. Receives nothing, returns nothing.'''
    
    # Initializing the game
    while True:
        choose = input("Do you want to play a game of Blackjack? Type \'y\' or \'n\': ").lower()
        if choose == "n":
            break
        else:
            game()
            
                        
# Calling the menu function         
menu()