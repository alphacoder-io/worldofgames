import Helpers
import random
import time
import Utils

difficulty = 1
delay_seconds = 0.7


def generate_sequence():
    random_list = random.sample(range(1, 102), difficulty)
    return random_list

def get_list_from_user():
    lst = []
    print("Please enter the numbers you remember one by one\n")
    for i in range(difficulty):
        lst.append(Helpers.convert_to_int(input()))
    return lst

def is_list_equal(lst1, lst2):
    return lst1 == lst2

def play(chosen_difficulty):
    try:
        if not Helpers.is_positive_int(chosen_difficulty):
            raise Exception("difficulty should be a positive int")
        global difficulty
        difficulty = chosen_difficulty
        random_list = generate_sequence()
        print(f"We are going to show you a sequence of numbers for {delay_seconds} seconds, please memorize them")
        time.sleep(5)
        print(random_list)
        time.sleep(0.7)
        Utils.screen_cleaner()
        user_list = get_list_from_user()
        return is_list_equal(random_list, user_list)
    except Exception as e:
        raise Exception(f"Error due to {e}")