from time import sleep
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# selenium 4
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    # Dorme por 10 segundos
    sleep(10)