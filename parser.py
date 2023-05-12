from bs4 import BeautifulSoup
import requests

result = []
info = requests.get("https://www.kreekly.com/lists/100-samyh-populyarnyh-angliyskih-slov/")

soup = BeautifulSoup(info.content, "html.parser")
for word in soup.select('.list-words > .dict-word'):
    answer = word.select('.dict-word > .eng')
    result.append(answer[0].text)

for i in result:
    print(i)
