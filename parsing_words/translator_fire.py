from selenium import webdriver
import time
from fake_useragent import UserAgent

useragent: UserAgent = UserAgent()
options: webdriver = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", useragent.random)
url = "https://translate.google.com/"
driver: webdriver = webdriver.Firefox(executable_path=
                                      "C:\\Пользователи\\Данила\\PycharmProjects\\most_popular_words\\fierfoxdriver\\geckodriver-0.33.0")

try:
    driver.get(url=url)
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
