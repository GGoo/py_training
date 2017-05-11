class ContactHelper:
    def __init__(self,app):
        self.app = app

#RELATED TO CONTACT
    def open_edit_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_new_contact_form(self, contact):
        wd = self.app.wd
        self.open_edit_page()
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

    def delete_first_contact(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php/")
        wd.find_element_by_name("selected[]")
        wd.find_element_by_xpath("//*[@id ='content']/form[2]/div[2]/input")
        return("http://localhost/addressbook/index.php")

    def modyfing_first_contact(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")
        wd.find_element_by_xpath("// *[ @ id = 'maintable'] / tbody / tr[2] / td[8] / a / img").click()
        wd.find_element_by_xpath("// *[ @ id = 'content'] / form[1] / input[3]").clear()
        wd.find_element_by_name("firstname").send_keys("Marysia")
        wd.find_element_by_name("update").click()
        return("http://localhost/addressbook/index.php")
#
 #   def modyfing_first_group(self, new_group_data):
  #      wd = self.app.wd
   #     self.open_group_page()
    #    self.select_first_group()
     #   # open modyfication form
      #  wd.find_element_by_name("edit").click()
       # self.fill_group_form(new_group_data)
        #  fill group form
        #wd.find_element_by_name("update").click()
        #self.return_groups_page()

    def submit_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


