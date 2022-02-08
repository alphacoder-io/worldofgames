import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def open_chrome():
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-using")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.headless = True
        browser = webdriver.Chrome(options=chrome_options)
        return browser
    except Exception as e:
        print(e)
        return null

def test_scores_service(url):
    result = False
    chrome_browser = open_chrome()
    try:
        chrome_browser.get(url)
        scoreText = chrome_browser.find_element(By.ID,'score').text
        score = int(scoreText)
        if score >= 1 and score <= 1000:
            result = True
    except Exception as e:
        print(e)
        return False
    finally:
        chrome_browser.quit()
        return result

def main_function():
    try:
        result = test_scores_service('http://localhost:80')
        if result:
            print('success')
            return os._exit(0)
        else:
            print('failed')
            return os._exit(-1)
    except Exception as e:
        print(e)
        return os._exit(-1)

if __name__ == '__main__':
    main_function()



