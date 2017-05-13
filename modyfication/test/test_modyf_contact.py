import pytest

from modyfication.model.contact import Contact


@pytest.fixture

def test_modyfing_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_contact_form()
    app.contact.modyfing_first_contact(Contact(name="Python8", middlename="Python8", lastname="Python8", nickname="none",
                                      company="none",
                                      address="ul. Gdańska 8, 83-135 Olsztyn", homephone="58 123456789",
                                     mobile="0607 173 894", mail="ola@olina.pl",
                                      birthyear="1999"))
    app.contact.submit_contact()



