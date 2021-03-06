from selenium.webdriver.firefox.webdriver import WebDriver
from decompozyction.fixture.session import SessionHelper
from decompozyction.fixture.group import GroupHelper
from decompozyction.fixture.contact import  ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

        #inicjacja pomocników
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()

