from selenium import webdriver
import time


proxy = "41.76.145.18:3128"
firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities["proxy"] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "sslProxy": proxy
}

url = "https://2ip.ru"
driver: webdriver = webdriver.Firefox(
    executable_path="/fierfoxdriver/geckodriver-0.33.0",
    proxy=proxy
)

try:
    driver.get(url=url)
    time.sleep(10)
except Exception as ex:
    print(ex)
