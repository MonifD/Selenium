from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


import os
from time import sleep
from dotenv import load_dotenv

def time():
    sleep(5)

load_dotenv()
url_Portforlio = os.getenv("url_Portforlio")

firefox_options = Options()
gecko_driver_path = "../geckodriver"
firefox_options.binary_location = gecko_driver_path
driver = webdriver.Firefox(options=firefox_options)

driver.get(url_Portforlio)
time()
driver.find_element(By.XPATH, "/html/body/section[1]/div/a").click()
time()
driver.find_element(By.XPATH, "/html/body/header/nav/a[1]").click()
time()
driver.find_element(By.XPATH, "/html/body/header/nav/a[3]").click()
time()
driver.find_element(By.XPATH, "/html/body/header/nav/a[4]").click()
time()
driver.find_element(By.XPATH, "/html/body/header/nav/a[2]").click()
time()
driver.find_element(By.XPATH, "/html/body/section[3]/div/div[1]/div[2]/strong/a").click()
time()
driver.find_element(By.XPATH, "/html/body/section[4]/div/div/strong/a").click()
time()
driver.quit()