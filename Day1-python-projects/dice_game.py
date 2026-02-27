import random

def generate_dice_values():
    a = random.randint(1, 7)
    b = random.randint(1, 7)
    value = (a,b)
    return value

def roll_dice():
    while True:
        choice = input("Do you want to roll the dice? (yes/no): ")
        if choice.lower() == "yes":
            dice_values = generate_dice_values()
            print(dice_values)
        elif choice.lower() == "no":
            print(" Thank you for playin!!")
            break
        else:
            print("Invalid choice. Please try again.")

roll_dice()

       


