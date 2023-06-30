from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from multiprocessing import Pool


def processing_translate(wrd):

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")

    url = "https://translate.google.com/?hl=ru&sl=en&tl=ru&op=translate"
    driver: webdriver = webdriver.Chrome(
        executable_path="/chromdriver/oldversion/chromedriver.exe",
        options=options
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
        for point in get_word:
            if point.text:
                translator = point.find_element(By.CLASS_NAME, "kgnlhe")
                usage = point.find_element(By.CLASS_NAME, "YF3enc")
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
    with open("C:\\Users\\1\\PycharmProjects\\most_popular_words\\words_lib\\words100.json", "r") as json_file:
        info = json.load(json_file)

        def get_answer(word, attempt=0):
            ans = processing_translate(word)
            if attempt == 5:
                return ans
            if len(ans) < 2:
                ans = get_answer(word, attempt=attempt+1)
            global info
            info[word] = ans
            print(info)
            print(f"{word} - Completed")

        p = Pool(processes=2)
        p.map(get_answer, info.keys())

# AttributeError: Can't get attribute 'get_answer'
