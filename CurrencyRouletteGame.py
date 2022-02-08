import Helpers
import random

difficulty = 1

def get_guess_from_user(amount_to_convert):
    message = f"Please guess how much {amount_to_convert} $ are in ILS with an interval of {5-difficulty}\n"
    guess = input(message)
    return Helpers.convert_to_float(guess)

def get_money_interval(amount_to_convert):
    usd_to_ils_rate = Helpers.get_current_USD_to_ILS_rate()
    t = usd_to_ils_rate * amount_to_convert
    return t-(5-difficulty),t+(5-difficulty)

def play(chosen_difficulty):
    try:
        if not Helpers.is_positive_int(chosen_difficulty):
            raise Exception("difficulty should be a positive int")
        global difficulty
        difficulty = chosen_difficulty
        amount_to_convert = random.randrange(1, 101)
        money_interval = get_money_interval(amount_to_convert)
        guess = get_guess_from_user(amount_to_convert)
        return money_interval[0] <= guess <= money_interval[1]
    except Exception as e:
        raise Exception(f"Error due to {e}")