from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import random

options = webdriver.FirefoxOptions()
useragent = UserAgent()
options.set_preference("general.useragent.override", useragent.random)
# options.headless = True
proxy = random.choice([None, "190.185.109.193:9417"])

if proxy:
    firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
    firefox_capabilities["marionette"] = True

    firefox_capabilities["proxy"] = {
        "proxyType": "MANUAL",
        "httpProxy": proxy,
        "sslProxy": proxy
    }

url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
driver: webdriver = webdriver.Firefox(
    executable_path="/fierfoxdriver/geckodriver-0.33.0",
    options=options, proxy=proxy
)

try:
    driver.get(url=url)
    time.sleep(2)

    input_word = driver.find_element(By.CLASS_NAME, "er8xn")
    input_word.clear()
    input_word.send_keys("world")
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

