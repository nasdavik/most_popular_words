import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random


with open("words_lib/test.json", encoding="utf-8") as rd:
    words = json.load(rd)
    for word in words:

        proxy = "38.170.104.137:9144"

        if proxy:
            firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
            firefox_capabilities["marionette"] = True

            firefox_capabilities["proxy"] = {
                "proxyType": "MANUAL",
                "httpProxy": proxy,
                "sslProxy": proxy
            }

        options = Options()
        options.set_preference('permissions.default.image', 2)
        driver: webdriver = webdriver.Firefox(
            executable_path="/fierfoxdriver/geckodriver-0.33.0",
            options=options, proxy=proxy
        )

        try:
            driver.get(url="https://www.google.com/")

            word_input = driver.find_element(By.ID, "APjFqb")
            word_input.clear()
            word_input.send_keys(f'\"{word}\"')
            word_input.send_keys(Keys.ENTER)

            time.sleep(3)

            stat = driver.find_element(By.ID, "result-stats")
            answer = stat.text.split()
            answer = "".join(answer[2:-2])
            words[word] = answer
            print(f'{word} - complete')

        except Exception as ex:
            print(ex)

        finally:
            driver.close()
            driver.quit()

    with open("words_lib/test.json", "w", encoding="utf-8") as wr:
        json.dump(words, wr, ensure_ascii=False)


# with open("words_lib/all_words.json", encoding="utf-8") as rd:
#     standart = json.load(rd)
#     with open("words_lib/test.json", "w", encoding="utf-8") as wr:
#         json.dump(standart, wr, ensure_ascii=False)
#
