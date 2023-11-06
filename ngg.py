import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Guess the number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            player_guess = int(input("Enter your guess: "))
            attempts += 1

            if player_guess < secret_number:
                print("Too low! Try again.")
            elif player_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts!")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    play_game()


# # # # # # # # # # # # #
# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Your guess: 50
# That's too high. Try again.
# Your guess: 25
# That's too high. Try again.
# Your guess: 12
# That's too low. Try again.
# Your guess: 18
# That's too high. Try again.
# Your guess: 15
# That's too low. Try again.
# Your guess: 16
# Congratulations! You guessed the secret number 16 in 6 attempts!
