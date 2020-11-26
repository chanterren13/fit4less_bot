from selenium import webdriver
#from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
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

    def _find_time(self, time):
        # //div[@class='available-slots']/div[@data-slottime='at time']
        time_btn = self.driver.find_element_by_xpath("//div[@class='available-slots'/div[@data-slottime='at "+time+"']")
        time_btn_location = str(time_btn.location['y']+100)
        self.driver.execute_script("window.scrollTo(0, "+btn_location+");")
        time_btn.click()

        confirm_btn = self.driver.find_element_by_id('dialog_book_yes')
        confirm_location = str(confirm_btn['y']+34)
        self.driver.execute_script("window.scrollTo(0, "+confirm_location+");")
        confirm_btn.click()


    def book(self, date, time):
        while True:
            # Try to find the date 
            try:
                self._find_date(date)
            except NoSuchElementException:
                # If not available, refresh until it is
                self.driver.refresh()
                continue
            
            # Try to find the time
            try:
                self._find_time(time)
            except NoSuchElementException:
                # If not available, likely already full
                print("Time not available.")
                break
            
            print("Successfully booked "+date+" at "+time)
            break
        

# Get login info from user
print("If using Python2 or older, please wrap the info in single quotes (eg 'john@email.com').")
email = input("Enter your email: ")
password = input("Enter your password: ")
# Get booking date info from user
date = input("Enter the date you want to book (YYYY-MM-DD): ")
time = input("Enter the time you want to book (eg 8:00 PM): ")
# Log in to booking site
#bot = Fit4LessBot()
#bot.login(email, password)

#bot.book(date, time)
