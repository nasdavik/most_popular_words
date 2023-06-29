from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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
        time.sleep(3)

        input_word = driver.find_element(By.CLASS_NAME, "er8xn")
        input_word.clear()
        input_word.send_keys(wrd)
        time.sleep(2)

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
    info = ["answer", "country", "smile", "bold", "string"]
    for i in info:
        def get_answer():
            return processing_translate(i)
        answer = get_answer()
        while len(answer) < 2:
            answer = get_answer()
        print(answer)
        print("#" * 10)
        print(f"{i} - Completed")
        print("-" * 10)
