from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep

class Fit4LessBot():
    def __init__(self):
        self.driver = webdriver.Chrome('/mnt/c/webdrivers/chromedriver.exe')

    def login(self):
        self.driver.get('https://myfit4less.gymmanager.com/portal/login.asp')

        email_in = self.driver.find_element_by_id('emailaddress')
        email_in.send_keys('terrenjchan@gmail.com')

        pass_in = self.driver.find_element_by_id('password')
        pass_in.send_keys('Tc_1022916')

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        login_btn = bot.driver.find_element_by_id('loginButton')
        login_btn.click()

    def _find_date(self):
        select_date_btn = self.driver.find_element_by_id('btn_date_select')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        date_btn.click()

        date_btn = self.driver.find_element_by_id('date_2020-11-26')
        date_btn.click()
