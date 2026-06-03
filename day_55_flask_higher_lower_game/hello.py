from flask import Flask

app = Flask(__name__)


def logging_decorator(function):
    def wrapper(*args):
        print(f"You are about to call {function.__name__}")
        result = function(*args)
        print(f"The result was {result}")
    return wrapper

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center;">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
            '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWNuZDR3eDA3eTRsN2dpMDRta2c3bTBoMmpyMHpmbmk2a29kNmhhNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rdma0nDFZMR32/giphy.gif" width=500, height=500>'

@app.route("/bye")
@make_bold
@make_emphasis
def bye():
    return 'Bye!'

@app.route("/a_function/<int:a>/<int:b>")
@logging_decorator
def a_function(*args):
    return sum(args)

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)