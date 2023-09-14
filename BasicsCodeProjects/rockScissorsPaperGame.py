import random
import rockScirssorsPaperImg

# Player
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_play = random.randrange(2)

if player_input == 0:
    rockScirssorsPaperImg.rock()
elif player_input == 1:
    rockScirssorsPaperImg.paper()
elif player_input == 2:
    rockScirssorsPaperImg.scirssors()
    
print("Computer chose:")

if computer_play == 0:
    rockScirssorsPaperImg.rock()
elif computer_play == 1:
    rockScirssorsPaperImg.paper()
elif computer_play == 2:
    rockScirssorsPaperImg.scirssors()
    
# Result code

if player_input == computer_play:
    print("It's a draw!")
else:
    if player_input == 0 and computer_play == 2 or player_input == 1 and computer_play == 0 or player_input == 2 and computer_play == 1:
        print("You Win!!!")
    else:
        print("You Loose!!")