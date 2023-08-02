# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# images = [rock, paper, scissors]
# print(images)

#Write your code below this line 👇

# print(rock)
# print(paper)
# print(scissors)

## import random module
import random

############################## define the game logic  ##################################
## game logic
## Rock Paper Scissors, commonly abbreviated as RPS, goes beyond the simple interactions of 
## scissors cutting paper, 
## paper covering rock, 
## and rock crushing scissors

## function to determine the winner
def determine_winner(player_choice, computer_choice):
    ## if the player choice and computer choice are the same, then its a tie
    if player_choice == computer_choice:
        return "ITS A TIE"
    
    ## elif
    ## player choice = rock and computer choice = scissors or
    ## player choice = paper and computer choice = rock or
    ## player choice = scissors and computer choice = paper
    ## player wins in any of these situation comes.
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        return "YOU WIN"
    
    ## any other condition happens
    ## computer wins
    else:
        return "COMPUTER WIN"
    
    
    
    
    
############################## getting the players choice  ############################
## getting the player choice
## develop a function to get the players choice
## 
def get_player_choice():
    
    # Create a dictionary to map choices to their corresponding images
    choices_images = {
                        "rock": rock,
                        "paper": paper,
                        "scissors": scissors
    }
    
    while True:
        ## player choice is an input
        ## it will choose from three different varieties
        ## rock, paper, scissor.
        ## so this loop will run until it gets a return value from the listed three,
        ## if any user type with mixed caps and small letter texts.
        ## we have to lower the player choice to get the standard output.
        player_choice = input("Enter the Choice from (rock/paper/scissors) : ").lower()
        ## above step will get the players choice.
        ## need to check whether it is correct or not
        if player_choice in choices_images:
            print("Your Choice : \n",choices_images[player_choice])
            return player_choice
        
        else:
            print("Invalid Choice, Please Choose Again")

############################## getting the computer choice ############################

## getting the computer choice
## randomly choose between three elements
## from rock, paper and scissor
## it cann be done using random module and choice function.

def get_computer_choice():
    
    # Create a dictionary to map choices to their corresponding images
    choices_images = {
                        "rock": rock,
                        "paper": paper,
                        "scissors": scissors
    }
    choices = ["rock","paper","scissors"]
    computer_choice = random.choice(choices)
    
    if computer_choice in choices_images:
        print("Computer Chose : ", choices_images[computer_choice])
    return computer_choice

############################### create the main loop of the game  #####################
## main function
## this will play the game

def main():
    ## welcome the player to the game
    print("Let's Play the Rock Paper Scissor Game:---------")
    
    while True:
        
        ## get the player choice using get_player_choice function
        player_choice = get_player_choice()
        ## get the computer choice similarly
        computer_choice = get_computer_choice()
        
        print(f"You Chose : {player_choice}")
        print(f"Computer Chose : {computer_choice}")
        
        ## check the result using the game defining function
        ## determine the winner
        result = determine_winner(player_choice, computer_choice)
        print(f"The Result is {result}")
        
        
        ## so if you want to play again
        ## you will havr to choose the guess again
        ## confirm whether the player needs to play the game again.
        play_again = input("Do you want to play the game again (yes/no) ??").lower()
        
        ## if the player dont want to play
        ## break out of the loop
        
        if play_again != "yes":
            print("Thanks for playing the Game !!!")
            break
        
############################### run the main function. ################################
if __name__ == "__main__":
    main()