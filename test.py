import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
#
# options = Options()
# options.set_preference('permissions.default.image', 2)
# driver: webdriver = webdriver.Firefox(
#         executable_path="/fierfoxdriver/geckodriver-0.33.0",
#         options=options
#     )
#
# with open("words_lib/words20000.json", encoding="utf-8") as rd:
#     words = json.load(rd)
#     for word in words:
#         try:
#             driver.get(url="https://www.google.com/")
#
#             word_input = driver.find_element(By.ID, "APjFqb")
#             word_input.clear()
#             word_input.send_keys(f'\"{word}\"')
#             word_input.send_keys(Keys.ENTER)
#
#             time.sleep(3)
#
#             stat = driver.find_element(By.ID, "result-stats")
#             answer = stat.text.split()
#             answer = "".join(answer[2:-2])
#             print(answer)
#
#         except Exception as ex:
#             print(ex)
#
# driver.close()
# driver.quit()


with open("words_lib/words20000.json", "r", encoding="utf-8") as reading:
    standart = json.load(reading)
    with open("words_lib/words5000.json") as rd:
        instance = json.load(rd)
        for i in instance:
            try:
                standart[i]
            except Exception as ex:
                print(ex)
                print(i)
