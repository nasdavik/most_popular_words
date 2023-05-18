import requests
from bs4 import BeautifulSoup

word = "hello"
url = "https://translate.yandex.ru/?source_lang=en&target_lang=ru&text=" + word

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

answer = []
print(soup.select(".trnslator-container > .translation-word > .translation-chunk"))

