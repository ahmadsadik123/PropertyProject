from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pandas as pd


options = Options()

options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(
    "C:/Users/AhmadSadik/Desktop/PropertyProject/chromedriver",
    options=options,
)

url = "https://www.purplebricks.co.uk/buyers"

driver.get(url)


acceptcookies = driver.find_element(
    "xpath", "//button[@class='as-oil__btn-optin as-js-optin']"
)

acceptcookies.click()


# closenewsletter = driver.find_element("xpath", "//button[@id='button3']")

# closenewsletter.click()

type = driver.find_element("xpath", "//input[@id='buyers-hero-property-search-input']")


location = "london"

type.send_keys(location)

search = driver.find_element(
    "xpath", "//button[@data-testid='buyers-hero-property-search-button']"
)
search.click()

listings = driver.find_elements(
    "xpath",
    "//div[@class='property-cardstyled__StyledPrimaryInfo-sc-15g6092-6 focoAE']",
)

propertyinfo = []

for listing in listings:
    price = listing.find_element(
        "xpath", ".//strong[@data-testid='search-result-price']"
    ).text
    address = listing.find_element(
        "xpath", ".//span[@data-testid='search-result-address']"
    ).text
    bedrooms = listing.find_element(
        "xpath", ".//strong[@data-testid='search-result-bedrooms']"
    ).text

    dict = {"Price": price, "Address": address, "Bedrooms": bedrooms}

    propertyinfo.append(dict)

df = pd.DataFrame(propertyinfo)
print(df)

driver.quit()
