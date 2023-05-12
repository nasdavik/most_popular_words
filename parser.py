from bs4 import BeautifulSoup
import requests

info = requests.get("https://www.kreekly.com/lists/100-samyh-populyarnyh-angliyskih-slov/")

soup = BeautifulSoup(info.content, "html.parser")

for word in soup.select(".container > ")