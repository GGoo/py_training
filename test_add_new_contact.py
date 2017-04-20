# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.firefox.webdriver import WebDriver

from contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_new_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_new_contact(self):

        wd = self.wd
        self.open_home_page(wd)
        self.login_in_admin(wd, username="admin", password="secret")
        self.fill_new_contact_form(wd, Contact(name="Aleksandra", middlename="Zofia", lastname="Zosińska", nickname="none", company="none",
                                 address=  "ul. Gdańska 8, 83-135 Olsztyn", homephone="58 123456789", mobile="0607 173 894", mail="ola@olina.pl",
                                   birthyear="1999"))
        self.submit_contact(wd)
        self.return_home_page(wd)
        self.logout(self,wd)

    def submit_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, success, wd):
        wd.find_element_by_link_text("Logout").click()
        self.assertTrue(success)

    def fill_new_contact_form(self, wd, contact):
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % contact.name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys()
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("%s" % contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.mail)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").send_keys("\\9")
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").send_keys("\\9")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").send_keys("\\9")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[1]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birthyear)
        wd.find_element_by_css_selector("body").click()

    def login_in_admin(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")
        wd.find_element_by_name("user").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
