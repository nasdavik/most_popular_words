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

    input_world = driver.find_element(By.CLASS_NAME, "er8xn")
    input_world.clear()
    input_world.send_keys("dog")
    time.sleep(2)

    get_world = driver.find_element(By.CLASS_NAME, "j7bWb")
    print(get_world.text)
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
