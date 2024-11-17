import random

def game_result(computer, player):
    if computer == player:
        return "It's a tie!"
    
    elif (computer == "snake" and player == "water") or \
         (computer == "water" and player == "gun") or \
         (computer == "gun" and player == "snake"):
        return "Computer wins!"
    
    else:
        return "You win!"

def play_game():
    choices = ["snake", "water", "gun"]
    computer_choice = random.choice(choices)
    
    print("Welcome to Snake, Water, Gun Game!")
    print("Choose one: Snake, Water, or Gun")
    
    player_choice = input("Your choice: ").lower()
    
    if player_choice not in choices:
        print("Invalid choice! Please choose either Snake, Water, or Gun.")
        return
    
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")
    
    result = game_result(computer_choice, player_choice)
    print(result)

play_game()
