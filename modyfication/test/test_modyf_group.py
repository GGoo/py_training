from modyfication.model.group import Group

def test_modyfing_first_group(app):
    app.group.modyfing_first_group(Group(name="New group modyfication"))

def test_modyfing_first_header(app):
    app.group.modyfing_first_group(Group(header="New header modyfication"))




