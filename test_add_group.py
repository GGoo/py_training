# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.firefox.webdriver import WebDriver

from group import Group


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group(unittest.TestCase):
    # inicjalizacja
    def setUp(self):

        self.wd = WebDriver()
        # sterownik
        self.wd.implicitly_wait(60)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, password="secret", username="admin")
        self.open_group_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, Group(name="group1",header="group1", footer="group1"))
        self.submit_group_creation(wd)
        self.return_groups_page(wd)
        self.logout(wd)

    def test_add_empy_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, password="secret", username="admin")
        self.open_group_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, Group(name="", header="", footer=""))
        self.submit_group_creation(wd)
        self.return_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_groups_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def submit_group_creation(self, wd):
        wd.find_element_by_name("submit").click()


    def fill_group_form(self, wd, group):
        wd.find_element_by_name("group_name").click()
    #    wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
       # if not wd.find_element_by_xpath(
        #        "//div[@id='content']//select[normalize-space(.)='[none] abc']//option[1]").is_selected():
         #   wd.find_element_by_xpath("//div[@id='content']//select[normalize-space(.)='[none] abc']//option[1]").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)

    def init_group_creation(self, wd):
        wd.find_element_by_name("new").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, password, username):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("seckret")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/group.php")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()