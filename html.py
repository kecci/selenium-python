from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# old way
# PATH = "/usr/local/bin/chromedriver"
# driver = webdriver.Chrome(PATH)

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("https://quotes.toscrape.com/page/1/")

# LOGIN
quotes = driver.find_elements(by=By.CLASS_NAME, value="quote")

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text

    print(text + " -- " + author)

driver.quit()