import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
html_movies_data = soup.find_all("h3", class_="title")
# all_movies = []
# for movie in html_movies_data:
#     movies = movie.getText()
#     all_movies.append(movies)
movie_titles = [movies.getText() for movies in html_movies_data]
movies = movie_titles[::-1]
# for n in range(len(movie_titles)-1, 0, -1):
#     print(movie_titles[n])


with open(file="movies.txt", mode="w", encoding="utf8") as file:
    for movie in movies:
        file.write(f"{movie}\n")

