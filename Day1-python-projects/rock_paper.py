import random


def play_game():
    try:
        users_input = input("Enter your choice (r, p, s): ").lower()
        if users_input not in ["r", "p", "s"]:
            raise ValueError("Invalid input. Please enter 'r', 'p', or 's'.")
        computer_choice = random.choice(["rock", "paper", "scissors"])
        if (users_input == "r" and computer_choice == "scissors"):
            print("You win!")
        elif (users_input == "p" and computer_choice == "rock"):
            print("You win!")
        elif (users_input == "s" and computer_choice == "paper"):
            print("You win!")
        elif (users_input == computer_choice):
            print("It's a tie!")
        else:
            print("You lose!")
           

    except ValueError:
        print("Invalid input. Please enter 'r', 'p', or 's'.")
        return

def main():
 game_running = True  
 while game_running:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        game_running = False
        print("Thanks for playing! Goodbye!")     

main()