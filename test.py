from selenium import webdriver 
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox_options = Options()
gecko_driver_path = "../geckodriver"
firefox_options.binary_location = gecko_driver_path
driver = webdriver.Firefox(options=firefox_options)


driver.get("https://www.amazon.fr")

driver.find_element(By.ID , "sp-cc-rejectall-link").click()

try:
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys("carte de jeux")
    search_box.send_keys(Keys.ENTER)
    open_element = driver.find_element(By.XPATH, "//span[text()='BIERDORF Jeux de Cartes Poker - Étanches en Plastique Diamond Noir Nouveauté Jeu de Cartes 54, Playing Cards']").click()

    price = driver.find_element(By.XPATH, "//*[@id=\"corePriceDisplay_desktop_feature_div\"]/div[1]/span[2]/span[2]")
    print(price.text)
except Exception as ex:
    assert False
