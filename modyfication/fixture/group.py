class GroupHelper:
    # konstruktor - w ktorym bedzie przekazywac sie  odsyłacz do application na glowna klase fixtury
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
         wd = self.app.wd
         wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys( group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        #select first group and submit delete
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_groups_page()

    def modyfing_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath("//*[@id='content']/form/span[1]/input").click()
        wd.find_element_by_xpath("//*[@id='content']/form/input[6]").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("group11")
       # wd.find_element_by_xpath("//*[@id='content']/form/label[3]").clear()
        wd.find_element_by_xpath("//*[@id='content']/form/label[3]").send_keys("groupchanged11")
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("changed")
        wd.find_element_by_name("update").click()
        self.return_groups_page()



    def return_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

