import requests
from bs4 import BeautifulSoup
import json
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
list_of_100_movies_tags = soup.find_all(name="h3",class_="title")
list_of_100_movies = [article.text for article in list_of_100_movies_tags]
list_of_100_movies.reverse()
print(list_of_100_movies)

with open("top-100-movies.txt", 'w',encoding="utf-8") as file:
    for item in list_of_100_movies:
        file.write(item + '\n') # Using f-string for a newline character

