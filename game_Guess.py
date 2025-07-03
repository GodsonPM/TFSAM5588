import random

def number_guessing_game():
    """
    A simple number guessing game where the player tries to guess
    a random number within a specified range.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")

    # Generate a random number between 1 and 100 (inclusive)
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7 # Give the player a limited number of tries

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))

            if not (1 <= guess <= 100):
                print("Please guess a number between 1 and 100.")
                continue # Ask for input again without incrementing attempts

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\nCongratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts.")
                break # Exit the loop, game won
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    else: # This block executes if the while loop completes without a 'break' (i.e., attempts ran out)
        print("\nGame Over! You ran out of attempts.")
        print(f"The number I was thinking of was: {secret_number}")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
