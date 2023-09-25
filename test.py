import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# options = Options()
# options.set_preference('permissions.default.image', 2)
# driver: webdriver = webdriver.Firefox(
#         executable_path="/fierfoxdriver/geckodriver-0.33.0",
#         options=options
#     )
#
# try:
#     driver.get(url="https://www.kreekly.com/lists/1000-naibolee-populyarnyh-angliyskih-slov/")
#     driver.implicitly_wait(10)
#     load = driver.find_element(By.CLASS_NAME, "load_more")
#     load.click()
#
#     time.sleep(10)
#
#     words = driver.find_elements(By.CLASS_NAME, "eng")
#     new_words = [x.text for x in words]
#     print(len(new_words))
#     print(new_words)
#     driver.implicitly_wait(10)
#
#
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
#
# ews = 1
# for i in new_words:
#     print(ews, i)
#     ews = ews + 1
#
# print(len(set(new_words)))


# with open("words_lib/words1000.json", "w", encoding="utf-8") as wr:
#     all_words = {}
#     for word in new_words:
#         all_words[word] = ""
#     ews = 1
#     for i in all_words:
#         print(ews, i)
#         ews = ews + 1
#     json.dump(all_words, wr, ensure_ascii=False)


with open("words_lib/words10000.json", "r", encoding="utf-8") as reading:
    answer = json.load(reading)
    ews = 1
    for i in answer:
        print(ews, i)
        ews = ews + 1