import pytest

from modyfication.fixture.application import Application
from modyfication.model.contact import Contact


@pytest.fixture
#def app(request):
 #   fixture = Application()
  #  request.addfinalizer(fixture.destroy)
   # return fixture

#
#def test_modyfing_first_contact(app):
   # app.session.login(username="admin", password="secret")
 #   app.contact.modyfing_first_contact()
   # app.session.logout()

def test_modyfing_first_contact(app):
    app.contact.modyfing_first_contact(Contact(name="new contact"))

