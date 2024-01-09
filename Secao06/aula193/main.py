# type: ignore
# Selenium - Automatizando tarefas no navegador
from time import sleep
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# selenium 4
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# ROOT_FOLDER = Path(__file__).parent
# CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver'

# chrome_options = webdriver.ChromeOptions()
# chrome_service = Service()
# chrome_browser = webdriver.Chrome(
#     service=chrome_service,
#     options=chrome_options,
# )

# chrome_browser.get('https://www.google.com.br/')
# time.sleep(30)


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service()

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )

    search_input.send_keys('Hello World!')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    print(results)

    links = results.find_elements(By.TAG_NAME, 'a')
    print(links[0])
    links[0].click()

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)