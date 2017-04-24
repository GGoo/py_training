from selenium.webdriver.firefox.webdriver import WebDriver
#from session.py import SessionHelper
#from group import GroupHelper
#from fixture.group import Group

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        #inicjacja pomocników
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd= self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()



