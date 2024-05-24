# loop to play "rock", "paper", "scissors" game at the end 
# of each iteration, the user is asked if they want to play again
# if the user types "no", the loop stops

import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Enter rock, paper, or scissors: ")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"The computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
        else:
            print("You lose!")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again == "no":
            break


play_game()