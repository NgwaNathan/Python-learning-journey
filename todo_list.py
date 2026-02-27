#  MY TO-DO LIST APP

tasks = []

def addtask():
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f"Task: {task} added successfully")


def removetask():
    return

def showtask():
    if not tasks:
        print("No task in list")
    else:
        for task in tasks:
            print(task)

    

def exitapp():
    print("Exiting app... bye!!!")
    



def main():
    while True:
        print("\n Options: 1. Add task 2. Remove task 3. Show tasks 4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            addtask()
        elif choice == "2":
            removetask()
        elif choice == "3":
            showtask()
        elif choice == "4":
            exitapp()
            break
        else:
            print("Invalid choice. Please try again.")


main()
