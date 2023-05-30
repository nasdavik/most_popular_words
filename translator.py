from selenium import webdriver
import time

url = "https://translate.google.com/"
driver: webdriver = webdriver.Chrome(executable_path=
                    "C:\\Users\\1\\PycharmProjects\\most_popular_words\\chromdriver\\oldversion\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
