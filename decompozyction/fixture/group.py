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


    def return_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

