from modyfication.model.group import Group
#
#@pytest.fixture
#def app(request):
 #   fixture = Application()
  #  request.addfinalizer(fixture.destroy)
   # return fixture


def test_modyfing_first_group(app):
    app.group.modyfing_first_group(Group(name="New group"))

def test_modyfing_first_header(app):
    app.group.modyfing_first_group(Group(header="New header"))




