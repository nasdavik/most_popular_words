import requests
from bs4 import BeautifulSoup

word = "hello"
url = "https://translate.yandex.ru/?source_lang=en&target_lang=ru&text=" + word

response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content, "html.parser")

answer = []
print(soup.find(class_="textinput"))

