from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import random
import json


def processing_translate(wrd):

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

    url = "https://translate.google.com/?hl=ru&sl=en&tl=ru&op=translate"
    driver: webdriver = webdriver.Firefox(
        executable_path="/fierfoxdriver/geckodriver-0.33.0",
        options=options, proxy=proxy
    )

    try:
        driver.maximize_window()
        driver.get(url=url)
        driver.implicitly_wait(10)

        input_word = driver.find_element(By.CLASS_NAME, "er8xn")
        input_word.clear()
        input_word.send_keys(wrd)
        driver.implicitly_wait(10)

        get_word = driver.find_elements(By.CLASS_NAME, "TKwHGb")
        all_translates = {}
        for word in get_word:
            if word.text:
                translator = word.find_element(By.CLASS_NAME, "kgnlhe")
                usage = word.find_element(By.CLASS_NAME, "YF3enc")
                if translator.text and usage.get_attribute('aria-label'):
                    all_translates[translator.text] = usage.get_attribute('aria-label')
        favorite = driver.find_element(By.CLASS_NAME, "ryNqvb")
        if favorite.text not in all_translates.keys():
            all_translates[favorite.text] = "Распространенный вариант"

        return all_translates

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    info = json.loads("C:\\Users\\Данила\\PycharmProjects\\most_popular_words\\words_lib\\words100.json")
    print(info)
    for i in info:
        info = info.loads()
        print(info)
        for i in info.keys():
            def get_answer():
                ans = processing_translate(i)
                if len(ans) < 2:
                    ans = get_answer()
                return ans
            answer = get_answer()
            print(answer)
            print("#" * 10)
            print(f"{i} - Completed")
            print("-" * 10)
