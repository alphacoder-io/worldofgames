import Utils
import Helpers

def add_score(difficulty):
    try:
        scoreFromFile = get_score_from_file()
        if scoreFromFile is None:
            scoreFromFile = 0
        print(f"former score is {scoreFromFile}")
        newScore = get_new_score(scoreFromFile, difficulty)
        print(f"New score is {newScore}")
        write_score_to_file(newScore)
    except Exception as e:
        print(f"Error adding score to file due to {e}")

def get_score_from_file():
    scoreFromFile = None
    content = None
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as f:
            content = f.read()
        if content:
            scoreFromFile = Helpers.convert_to_int(content)

        if scoreFromFile < 0:
            scoreFromFile = None
    except Exception as e:
        scoreFromFile = None

    return scoreFromFile

def get_new_score(oldScore, difficulty):
    return (difficulty*3) + 5 + oldScore

def write_score_to_file(newScore):
    try:
        with open(Utils.SCORES_FILE_NAME, "w") as f:
            f.write(str(newScore))
    except Exception as e:
        raise e






