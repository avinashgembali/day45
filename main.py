import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
top_movies = soup.find_all(name="h3", class_="title")
top_list = []
for tag in top_movies:
    top_list.append(tag.getText())
reversed_list = top_list[::-1]
print(reversed_list)
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in reversed_list:
        file.write(movie + "\n")