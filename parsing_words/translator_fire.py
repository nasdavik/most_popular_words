from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import random
import json
from multiprocessing import Pool, Manager

manager = Manager()
lock = manager.Lock()
translations = {}

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


def get_answer(word, translations, lock, attempt=0):
    ans = processing_translate(word)
    if len(ans) < 2 and attempt < 5:
        get_answer(word, translations, lock, attempt=attempt+1)
    else:
        lock.acquire()
        translations[word] = ans
        lock.release()
        print(f"{word} - Completed")


if __name__ == "__main__":
    with open("C:\\Users\\Данила\\PycharmProjects\\most_popular_words\\words_lib\\words100.json") as json_file:
        info = json.load(json_file)
        test = ['row', 'queen', 'king', 'pool']

        p = Pool(processes=2)
        p.map(get_answer, [(word, translations, lock) for word in test])
        print(translations)
