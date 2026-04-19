#%%
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(URL)
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]

# print(movie_titles)
movie_order = [int(movie.split(" ")[0].replace(':', '').replace(')','')) for movie in movie_titles]

movie_titles = [movie.split(maxsplit=1)[1] for movie in movie_titles]
# print(movie_order)
# print(movie_titles)
sorted_movie_titles = [x for _, x in sorted(zip(movie_order, movie_titles))]
# print(sorted_movie_titles)
# print(movie_titles)
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for enum, movie in enumerate(sorted_movie_titles, start=1):
        file.write(f"{enum}) {movie}\n")