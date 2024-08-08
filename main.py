import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
print(soup.prettify())

movies = soup.find_all(name="h3", class_="title")
movies_text = [movie.getText() for movie in movies]
print(movies_text)
movies_text_reverse = [movie for movie in reversed(movies_text)]

with open("rating.text", "w", encoding="utf-8") as file:
    for movie in movies_text_reverse:
        file.write(movie + "\n")
