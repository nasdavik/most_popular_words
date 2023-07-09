from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import json
from multiprocessing import Pool, RLock

translations = {}
lock = RLock()


def processing_translate(wrd):

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
        proxy=proxy
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


def get_answer(word, attempt=0):
    ans = processing_translate(word)
    if len(ans) < 2 and attempt < 5:
        return get_answer(word, attempt=attempt+1)
    else:
        with lock:
            print(f"{word} - Completed")
            return {word: ans}


def end_func(response):
    global translations
    for x in response:
        translations.update(dict(x))


if __name__ == "__main__":
    with open("C:\\Users\\Данила\\PycharmProjects\\most_popular_words\\words_lib\\words100.json") as json_file:
        info = json.load(json_file)
        test = ['me', 'can', 'time', 'like', 'row', 'queen', 'king', 'pool']

        with Pool(4) as p:
            p.map_async(get_answer, info.keys(), callback=end_func)
            p.close()
            p.join()

    with open("C:\\Users\\Данила\\PycharmProjects\\most_popular_words\\words_lib\\test.json", "w", encoding='utf-8') as wr:
        json.dump(translations, wr, ensure_ascii=False)
