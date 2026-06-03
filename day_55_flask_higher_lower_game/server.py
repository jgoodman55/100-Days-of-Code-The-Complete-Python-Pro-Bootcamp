from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)

def check_guess(guess):
    if guess < random_number:
        return '<h1 style="color: red;">Too low, try again!</h1>' \
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=500, height=500>'
    elif guess > random_number:
        return '<h1 style="color: purple;">Too high, try again!</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=500, height=500>'
    else:
        return '<h1 style="color: green;">You found me!</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=500, height=500>'

@app.route("/")
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=500, height=500>'


@app.route("/<int:number>")
def guess(number):
    return check_guess(number)

if __name__ == "__main__":
    app.run(debug=True)