from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from dotenv import load_dotenv
import os
from time import sleep

from githubpages import GitHubPages


load_dotenv()
url_Github = os.getenv("url_Github")
username = os.getenv("username")
password= os.getenv("password")

firefox_options = Options()
gecko_driver_path = "../geckodriver"
firefox_options.binary_location = gecko_driver_path
driver = webdriver.Firefox(options=firefox_options)

get_page_GitHub = GitHubPages(driver)
get_page_GitHub.load(url_Github)
get_page_GitHub.login(username, password)
get_page_GitHub.load_repository()
get_page_GitHub.dashbord()
sleep(5)
get_page_GitHub.logout()
get_page_GitHub.quit()