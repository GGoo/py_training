import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.fill_new_contact_form(Contact(name="Aleksandra", middlename="Zofia", lastname="Zosińska", nickname="none",
                                      company="none",
                                      address="ul. Gdańska 8, 83-135 Olsztyn", homephone="58 123456789",
                                      mobile="0607 173 894", mail="ola@olina.pl",
                                      birthyear="1999"))
    app.submit_contact()
    app.logout()











