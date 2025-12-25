from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

articles = soup.find_all("a",class_="storylink")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.text)
    article_links.append(article.get("href"))

article_upvotes = [int(upvotes.text.split(" ")[0]) for upvotes in soup.find_all(name="span",class_="score")]

max_upvotes_index = 0
max_upvotes = 0
for index in range(len(article_upvotes)):
    if article_upvotes[index] > max_upvotes:
        max_upvotes = article_upvotes[index]
        max_upvotes_index = index

print("The most upvoted article is: ", article_texts.__getitem__(max_upvotes_index))
print(article_links.__getitem__(max_upvotes_index))
print(article_upvotes)
print(article_upvotes[max_upvotes_index])