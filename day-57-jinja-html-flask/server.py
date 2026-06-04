from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", random_number=random_number, current_year=current_year)

@app.route("/guess/<string:name>")
def guess(name):
    gender_response = requests.get("https://api.genderize.io?name=" + name)
    age_response = requests.get("https://api.agify.io?name=" + name)
    return render_template("guess.html", name=name.title(), gender=gender_response.json().get("gender"), age=age_response.json().get("age"))


@app.route("/blog/<int:num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/5600349f4bb58c1cbfde"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)