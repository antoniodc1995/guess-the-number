name = input(f"Hi! Please type your name here: ")
print(f"Hi {name}! Try to guess the number. The range goes from 1 to 100. \n")
print("You have 10 attempts. \nEvery time you try, the script will tell you how many attempts you still have and if the guess is too high or too low.")
print(input("\nPress enter to start the game. Good luck! \n"))
import random
secret = random.randrange(1,100)
i = 0
while i < 10:
    inp = int(input("Enter a number: "))
    if inp < secret:
        print(f"The number you have to guess is higher. You still have {10-1-i} attempt(s).")
        if i == (10-1):
            print("Oh nooo! You lose, restart the program to play again.")    
    elif inp > secret:
        print(f"The number you have to guess is lower. You still have {10-1-i} attempt(s).")
        if i == (10-1):
            print("Oh nooo! You lose, restart the program to play again.")
    elif inp == secret:
        print(f"Congratulations, you guessed the number! Restart the program if you want to play again.")
        break
    i = i + 1