import CurrencyRouletteGame
import GuessGame
import MemoryGame
import Helpers
import Score

def welcome(name):
    return f"Hello {name} and welcome to the World of Games (Wog).\nHere you can find many cool games to play."

def load_game():
    game_input_valid = False
    message = "Please choose a game to play:\n"
    message += "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
    message += "2. Guess Game - guess a number and see if you chose like the computer\n"
    message += "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
    game = input(message)
    # using char value:
    while not game.isdigit() or int(game) < 1 or int(game) > 3:
        message = f"'{game}' is not valid game number, please choose a valid game number (1-3):\n"
        game = input(message)

    message = "Please choose game difficulty from 1 to 5:\n"

    difficulty = input(message)
    difficulty_number = Helpers.convert_to_int(difficulty)

    while not Helpers.is_in_range_int(difficulty_number,1,5):
            message = f"'{difficulty}' is not valid difficulty level, please choose game difficulty from 1 to 5:\n"
            difficulty = input(message)
            difficulty_number = Helpers.convert_to_int(difficulty)

    game_result = False
    if game == "1":
        game_result = MemoryGame.play(difficulty_number)
    elif game == "2":
        game_result = GuessGame.play(difficulty_number)
    elif game == "3":
        game_result = CurrencyRouletteGame.play(difficulty_number)
    else:
        print(f"game {game} does not exist")
        return

    if game_result:
        Score.add_score(difficulty_number)
        print("you have won the game :-) !!!")
    else:
        print("you have lost the game :-( ")