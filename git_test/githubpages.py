from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class GitHubPages: 
    def __init__(self, driver):
        self.driver = driver 
        
    def load(self, url):
        self.driver.get(url)
    
    def login(self, username, password):
        ##send username
        find_sign_in = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div/div[2]/div/div/div/a")
        find_sign_in.click()
        username_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "login_field")))
        username_box.clear()
        username_box.send_keys(username)

        ##send password
        password_box = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        password_box.clear()
        password_box.send_keys(password)

        ##send request
        send_button= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "commit")))
        send_button.click()
        
    def load_repository(self):
        button_repository = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[6]/div/div/aside/div/div/loading-context/div/div[1]/div/ul/li[1]/div/div/a")))
        button_repository.click()
        
    def dashbord(self):
        button_dashboard = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/header/div/div[1]/div/div[2]/nav/ul/li/a")))
        button_dashboard.click()
        
    def logout(self):
        button_label = self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/header/div[1]/div[2]/div[3]/deferred-side-panel/include-fragment/user-drawer-side-panel/button/span/span")
        button_label.click()
        signout_button = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/header/div[1]/div[2]/div[3]/deferred-side-panel/include-fragment/user-drawer-side-panel/dialog-helper/dialog/scrollable-region/div/div/nav/nav-list/ul/li[22]/a/span")))
        signout_button.click()
        signout_all_account_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[5]/main/div/form/input[4]")))
        signout_all_account_button.click()
        
    def quit(self):
        self.driver.quit()