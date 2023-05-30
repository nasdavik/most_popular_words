from selenium import webdriver
import time

url = "https://translate.google.com/"
# driver: webdriver = webdriver.Chrome(executable_path=
#                     "C:\\Users\\1\\PycharmProjects\\most_popular_words\\chromdriver\\oldversion\\chromedriver.exe")

driver: webdriver = webdriver.Firefox(executable_path=
                                      "C:\\Пользователи\\Данила\\PycharmProjects\\most_popular_words\\fierfoxdriver\\geckodriver-0.33.0")

try:
    driver.get(url="https://youtube.com")
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
