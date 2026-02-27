import random
# program runs
# User is asked to guess a number between 1 and 100
#  we use a while loop , if the entered number is not == to the generated number, we will ask the user to guess again until they get it right
# if the user's choice is greater than the generated number, we will print "too high, try again"
# if the user's choice is less than the generated number, we will print "too low, try again"
# if the user's choice is equal to the generated number, we will print "congratulations, you guessed the number in x attempts"

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low, try again.")
            elif user_guess > number_to_guess:
                print("Too high, try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

number_guessing_game()

