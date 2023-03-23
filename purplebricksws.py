from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime


options = Options()

options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Locating the driver in the directory
driver = webdriver.Chrome(
    "chromedriver.exe",
    options=options,
)

# URL we will be using
url = "https://www.purplebricks.co.uk/buyers"

driver.get(url)

time.sleep(2)

# Accepting cookies popup, a try condition is used as the popup may not not appear
acceptcookies = driver.find_element(
    "xpath", "//button[@class='as-oil__btn-optin as-js-optin']"
)

try:
    acceptcookies.click()
    time.sleep(20)
except:
    pass

# After about 20seconds, a pesky newsletter window pops up which exists in a different frame,
# so the frame is changed to close it then changed back
iframe = driver.find_element(
    "xpath", "//*[@id='lightbox-iframe-46569678-6bbc-44b3-a785-cf2ad930b39f']"
)
driver.switch_to.frame(iframe)

close_button = driver.find_element("xpath", "//button[@id='button3']")
close_button.click()

driver.switch_to.default_content()

# Typing the desired location in the search bar (in this instance it's london)
type = driver.find_element("xpath", "//input[@id='buyers-hero-property-search-input']")

location = "london"

type.send_keys(location)

# Clicking the search button
search = driver.find_element(
    "xpath", "//button[@data-testid='buyers-hero-property-search-button']"
)
search.click()

propertyinfo = []
page_count = 0

# Using a while loop to loop through the pages
while True:
    listings = driver.find_elements(
        "xpath",
        "//div[@class='property-cardstyled__StyledPropertyCard-sc-15g6092-0 fwvNIe']",
    )

    # For loop to loop through the listings on a page,
    # the exception is used as the scraper kept crashing due to a "NoSuchElementException".
    # If this occurs the value will be stored as N/A
    for listing in listings:
        try:
            price = listing.find_element(
                "xpath", ".//strong[@data-testid='search-result-price']"
            ).text
        except NoSuchElementException:
            price = "N/A"

        try:
            address = listing.find_element(
                "xpath", ".//span[@data-testid='search-result-address']"
            ).text
        except NoSuchElementException:
            address = "N/A"

        try:
            bedrooms = listing.find_element(
                "xpath", ".//strong[@data-testid='search-result-bedrooms']"
            ).text
        except NoSuchElementException:
            bedrooms = "N/A"

        try:
            description = listing.find_element(
                "xpath", ".//span[@data-testid='search-result-description']"
            ).text
        except NoSuchElementException:
            description = "N/A"

        dict = {
            "Price": price,
            "Address": address,
            "Bedrooms": bedrooms,
            "Description": description,
        }

        propertyinfo.append(dict)

    # Initially, this looped through all pages however this took forever so I limited it to 20 - can easily be removed or adjusted
    page_count += 1
    if page_count == 20:
        break

    # Try except used in the event there is no next button (if it was looping through all pages)
    try:
        nextbutton = driver.find_elements(
            "xpath", "//button[@aria-label='Go to next page']"
        )
    except:
        pass

    # The below is used as there was a conflict in the XPaths for the next buttons, so indexing is used to select the second one
    if len(nextbutton) > 1 and nextbutton[1].is_enabled():
        nextbutton[1].click()
        time.sleep(2)
    else:
        break

# Data is stored in a DataFrame and then exported as a csv file
df = pd.DataFrame(propertyinfo)
print(df)

df.to_csv("raw_data.csv", index=False)

# Used to quit the Selenium driver
driver.quit()
