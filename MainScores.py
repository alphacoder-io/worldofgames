from flask import Flask, render_template
import Score
import Utils

app = Flask(__name__)

@app.route('/')
def score_server():
    scoreFromFile = Score.get_score_from_file()
    if scoreFromFile is None:
        return render_template('scores_error.html', error=f"error {Utils.BAD_RETURN_CODE}, could not read score from file")
    else:
        return render_template('scores.html', score=scoreFromFile)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,port=80)

