import random

logo = r"""
   /$$$$$$                                               /$$$$$$$$ /$$                       /$$   /$$                         /$$                          
 /$$__  $$                                             |__  $$__/| $$                      | $$$ | $$                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$         | $$   | $$$$$$$   /$$$$$$       | $$$$| $$ /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/         | $$   | $$__  $$ /$$__  $$      | $$ $$ $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$          | $$   | $$  \ $$| $$$$$$$$      | $$  $$$$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$         | $$   | $$  | $$| $$_____/      | $$\  $$$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/         | $$   | $$  | $$|  $$$$$$$      | $$ \  $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          |__/   |__/  |__/ \_______/      |__/  \__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      



"""


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)

    difficulty = input("Choose a difficulty: Easy or Hard: ").lower()
    if difficulty == "easy":
        guesses = 10
    elif difficulty == "hard":
        guesses = 5
    else:
        print("Invalid choice! Defaulting to hard mode.")
        guesses = 5

    while guesses > 0:
        print(f"\nYou have {guesses} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print(f"You got it! The answer was {number}. 🎉")
            return  # function se bahar nikal jao (game win ho gaya)
        elif guess > number:
            print("Too High!")
        else:
            print("Too Low!")

        guesses -= 1

    print(f"\nYou lose! The number was {number}. 😭")


# Main loop for play again
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break
