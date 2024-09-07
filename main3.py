import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, 'html.parser')
# print(soup.prettify())
anchor_tag = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in anchor_tag:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name='a').get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_upvotes)
# print(article_texts)
# print(article_links)

# max_upvotes = 0
# max_index = 0
# for i in range(len(article_upvotes)):
#     if max_upvotes < article_upvotes[i]:
#         max_upvotes = article_upvotes[i]
#         max_index = i
max_upvotes = max(article_upvotes)
max_index = article_upvotes.index(max_upvotes)
print(f"max upvotes articles is : {article_texts[max_index]} and the link is {article_links[max_index]} "
      f"and having upvotes: {article_upvotes[max_index]}")
