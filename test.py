import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

options = Options()
options.set_preference('permissions.default.image', 2)
driver: webdriver = webdriver.Firefox(
        executable_path="/fierfoxdriver/geckodriver-0.33.0",
        options=options
    )

try:
    driver.get(url="https://www.kreekly.com/lists/1000-naibolee-populyarnyh-angliyskih-slov/")
    driver.implicitly_wait(10)

    button = driver.find_element(By.CLASS_NAME, "load_more ")
    print(button.text)
    button.click()

    words = driver.find_elements(By.CLASS_NAME, "eng")
    print(len(words))
    driver.implicitly_wait(10)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


with open("words_lib/words1000.json", "r", encoding="utf-8") as read:
    answer = json.load(read)
    print(len(answer))
