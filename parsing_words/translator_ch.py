from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")

url = "https://translate.google.com/?hl=ru&sl=en&tl=ru&op=translate"
driver: webdriver = webdriver.Chrome(
    executable_path="/fierfoxdriver/geckodriver-0.33.0",
    options=options
)

try:
    driver.get(url=url)
    time.sleep(2)

    input_word = driver.find_element(By.CLASS_NAME, "er8xn")
    input_word.clear()
    input_word.send_keys("dog")
    time.sleep(2)

    get_word = driver.find_element(By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[2]/c-wiz/div/div/div[1]/div/div[1]/table/tbody[1]/tr[1]")
    print(get_word.text)
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
