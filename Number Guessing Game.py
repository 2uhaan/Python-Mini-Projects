from curses.ascii import isdigit
import random

number = random.randint(1,10)
guess = 0

while True:
    guess += 1
    user_guess = input("Guess a Number between 1-10 : ")
    if user_guess.isdigit:      #to avoid Error message we check if its a int or not
        user_guess = int(user_guess)
    else:
        print("Invalid")
        continue                             #this will continue the infinte loop insted of moving to condition below


    if user_guess == number:
        print("You got it !")
        break
    elif user_guess > number:
        print("Too High")
    else:
        print("Too Low")

print("Congradulations You Guessed it write in " + str(guess) + " Guesses")

