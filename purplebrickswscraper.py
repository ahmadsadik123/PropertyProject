from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time


class Scraper:
    def __init__(self) -> None:
        options = Options()

        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(
            "C:/Users/AhmadSadik/Desktop/PropertyProject/chromedriver",
            options=options,
        )

        url = "https://www.purplebricks.co.uk/buyers"

        self.driver.get(url)
        time.sleep(3)

    def __cookies(self) -> webdriver.Chrome:
        try:
            acceptcookies = self.driver.find_element(
                "xpath", "//button[@class='as-oil__btn-optin as-js-optin']"
            )

            acceptcookies.click()
            time.sleep(1)

        except:
            pass

    def __typelocation(self) -> webdriver.Chrome:
        try:
            location = "london"

            type.send_keys(location)

            search = self.driver.find_element(
                "xpath", "//button[@data-testid='buyers-hero-property-search-button']"
            )
            search.click()
            time.sleep(1)

        except:
            pass

    def __scraper(self) -> webdriver.Chrome:
        try:
            listings = self.driver.find_elements(
                "xpath",
                "//ul[@class='search-resultsstyled__StyledSearchResults-krg5hu-2 iaLdgK']",
            )

            propertyinfo = []

            for listing in listings:
                price = listing.find_element(
                    "xpath", "//strong[@data-testid='search-result-price']"
                ).text
                address = listing.find_element(
                    "xpath", "//span[@data-testid='search-result-address']"
                ).text
                bedrooms = listing.find_element(
                    "xpath", "//strong[@data-testid='search-result-bedrooms']"
                ).text
                # print(price, address, bedrooms)
                dict = {"Price": price, "Address": address, "Bedrooms": bedrooms}
                time.sleep(3)

                propertyinfo.append(dict)

            df = pd.DataFrame(propertyinfo)
            return df
        except:
            pass
