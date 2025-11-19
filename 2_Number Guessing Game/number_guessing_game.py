import random

print("Welcome to the Number Guessing Game")

top_range = input("Enter the number of Range: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range<=0:
        print("Please enter a number that is larger than 0 next time.")
        quit()
else:
    print("Enter a number next time.")
    quit()

random_number = random.randint(0,top_range)
guess=0

while True:
    guess +=1
    user_guess = input("Enter a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Enter a number again")
        continue
    if(user_guess==random_number):
        print("You guessed the correct number ✅.")
        break
    elif(user_guess<random_number):
        print("You entered a smaller num")
    else:
        print("You entered a bigger num")

print(f"You got it in {guess} guesses.")

