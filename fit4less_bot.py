from selenium import webdriver
#from selenium.webdriver import ActionChains
from time import sleep

class Fit4LessBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/mnt/c/webdrivers/chromedriver.exe')

    def login(self, email, password):
        self.driver.get('https://myfit4less.gymmanager.com/portal/login.asp')

        email_in = self.driver.find_element_by_id('emailaddress')
        email_in.send_keys(email)

        pass_in = self.driver.find_element_by_id('password')
        pass_in.send_keys(password)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        login_btn = bot.driver.find_element_by_id('loginButton')
        login_btn.click()

    def _find_date(self, date):
        select_date_btn = self.driver.find_element_by_id('btn_date_select')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        select_date_btn.click()

        date_btn = self.driver.find_element_by_id('date_'+date)
        date_btn.click()


# Get login info from user

# Get booking date info from user

# Log in to booking site

# Try to access the date

    # If date does not show, catch exception, refresh page and try again

# Book requested time

    # Send error message if could not be booked
