"""
A simple game where the user has to guess a randomly generated 4-digit number.
The user receives hints based on the accuracy of their guess.
"""
import random


def generate_number():
    """Generate a random 4-digit number."""
    return random.randint(1000, 9999)


def generate_hints(target, guess):
    """
    Generate hints based on the user's guess.

    Parameters:
    - target (str): The correct 4-digit number.
    - guess (str): The number guessed by the user.

    Returns:
    - str: A string of hints where:
        'o' indicates the digit is correct and in the right position,
        'x' indicates the digit is correct but in the wrong position,
        '#' indicates the digit is incorrect.
    """
    hints = []
    for i in range(4):
        if guess[i] == target[i]:
            hints.append('o')
        elif guess[i] in target:
            hints.append('x')
        else:
            hints.append('#')
    return ' '.join(hints)


def guess_the_number_game():
    """The main game loop where the user is prompted to guess the number. """
    target_number = str(generate_number())
    attempts = 0

    while True:
        guess = input("Guess the four-digit number (or type 'quit' to exit): ")
        attempts += 1

        if guess == 'quit':
            print("Thanks for playing! The number was:", target_number)
            break
        if guess == target_number:
            print("Congratulations! You've guessed the correct number.")
            print("Number of attempts:", attempts)

            replay_choice = input("Do you want to play again? (yes/no): ")
            if replay_choice.lower() == 'yes':
                guess_the_number_game()
                break

            print("Thanks for playing!")
            break

        hints = generate_hints(target_number, guess)
        print("Hints:", hints)


guess_the_number_game()
