from selenium import webdriver
import time
from fake_useragent import UserAgent


useragent: UserAgent = UserAgent()
options: webdriver = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
driver: webdriver = webdriver.Chrome(executable_path="/chromdriver/oldversion/chromedriver.exe",
                                     options=options)

try:
    driver.get(url=url)
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
