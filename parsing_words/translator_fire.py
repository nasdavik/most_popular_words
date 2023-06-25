from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


proxy = random.choice([None, "190.185.109.193:9417"])

if proxy:
    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities["marionette"] = True

    firefox_capabilities["proxy"] = {
        "proxyType": "MANUAL",
        "httpProxy": proxy,
        "sslProxy": proxy
    }

url = "https://translate.google.com/?hl=ru&sl=en&tl=ru&op=translate"
driver: webdriver = webdriver.Firefox(
    executable_path="/fierfoxdriver/geckodriver-0.33.0",
    proxy=proxy
)

try:
    driver.get(url=url)
    time.sleep(2)

    input_world = driver.find_element(By.CLASS_NAME, "er8xn")
    input_world.clear()
    input_world.send_keys("world")
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

