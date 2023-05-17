import requests
from bs4 import BeautifulSoup

req = requests.get("https://translate.yandex.ru/?source_lang=en&target_lang=ru")
print(req.text)
