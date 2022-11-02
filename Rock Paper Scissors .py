import random

user_win = 0
pc_win = 0

options = ["rock", "paper", "scissors"]

while True:
    choice = input("Enter Rock/Paper/Scissors or end to quit : ").lower()
    if choice == "end":
        break

    if choice not in options:
        print("Invalid -- Retry")
        continue

    choice_index = random.randint(0,2)
    pc_pick = options[choice_index]

    print("The Computer Picked ", pc_pick)

    if choice == "rock" and pc_pick == "scissors":
        print("You win!")
        user_win += 1
    
    elif choice == "scissor" and pc_pick == "paper":
        print("You win!")
        user_win += 1

    elif choice == "paper" and pc_pick == "rock":
        print("You won!")
        user_win += 1

    elif choice == pc_pick:
       print("its a Draw")

    else:
        print("You Lost :( ")
        pc_win += 1

print("You won ", user_win, " times.")
print("The Computer won ", pc_win, " times.")


