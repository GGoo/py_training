import pytest
from modyfication.model.contact import Contact
from modyfication.fixture.application import  Application


def test_add_new_contact(app):
    app.contact.fill_new_contact_form(Contact(name="Exer9", middlename="Zofia", lastname="Zosińska", nickname="none",
                                      company="none",
                                      address="ul. Gdańska 8, 83-135 Olsztyn", homephone="58 123456789",
                                      mobile="0607 173 894", mail="ola@olina.pl",
                                      birthyear="1999"))
    app.contact.submit_contact()


