import random

MAX_ATTEMPTS = 10
SECRET_NUMBER = 98

print("Welcome to the Guess the Number game!")
print("You must guess a number between 1 and 100.")

while True:
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        attempts += 1
        try:
            guess = int(input(f"Attempt {attempts}/{MAX_ATTEMPTS} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            attempts -= 1
            continue

        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100.")
            attempts -= 1
            continue

        if guess == SECRET_NUMBER:
            print(f"Congratulations! You guessed the number in {attempts} attempt{'s' if attempts != 1 else ''}.")
            break
        elif guess < SECRET_NUMBER:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    else:
        print(f"Out of attempts! The secret number was {SECRET_NUMBER}.")

    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again not in {"yes", "y"}:
        print("Thanks for playing!")
        break
