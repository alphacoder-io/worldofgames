import Helpers
import random

difficulty = 1
secret_number = 0

def generate_number():
    global secret_number
    secret_number = random.randrange(1, difficulty + 1)

def get_guess_from_user():
    message = f"Guess a number between 1 and {difficulty}\n"
    guessed = input(message)
    guessed_number = Helpers.convert_to_int(guessed)
    while not Helpers.is_in_range_int(guessed_number, 1, difficulty):
        message = f"{guessed} is not a valid number between 1 and {difficulty}, try again\n"
        guessed_number = input(message)
    return guessed_number

def compare_results(guessed_number):
    return guessed_number == secret_number

def play(chosen_difficulty):
    try:
        if not Helpers.is_positive_int(chosen_difficulty):
            raise Exception("difficulty should be a positive int")
        global difficulty
        difficulty = chosen_difficulty
        generate_number()
        guessed_number = get_guess_from_user()
        return compare_results(guessed_number)
    except Exception as e:
        raise Exception(f"Error due to {e}")