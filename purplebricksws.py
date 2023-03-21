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

type = driver.find_element("xpath", "//input[@id='buyers-hero-property-search-input']")

location = "london"

type.send_keys(location)

search = driver.find_element(
    "xpath", "//button[@data-testid='buyers-hero-property-search-button']"
)
search.click()

# listings = driver.find_elements(
#     "xpath", "//ul[@class='search-resultsstyled__StyledSearchResults-krg5hu-2 iaLdgK']"
# )

# for listing in listings:
#     price = listing.find_element(
#         "xpath", "//strong[@data-testid='search-result-price']"
#     ).text
#     address = listing.find_element(
#         "xpath", "//span[@data-testid='search-result-address']"
#     ).text
#     bedrooms = listing.find_element(
#         "xpath", "//strong[@data-testid='search-result-bedrooms']"
#     ).text
#     print(price, address, bedrooms)


# //ul[@class="search-resultsstyled__StyledSearchResults-krg5hu-2 iaLdgK"]

# //ul[@data-testid="results-list"]

# //a[@class="property-cardstyled__StyledLink-sc-15g6092-1 eQIvCR"]

# listings = driver.find_elements("class", 'property-cardstyled__StyledLink-sc-15g6092-1 eQIvCR')

# for listing in listings:
#     desc = listing.find_element("xpath", "//a[@class='property-cardstyled__StyledLink-sc-15g6092-1 eQIvCR']")
