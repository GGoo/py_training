import pytest
from modyfication.model.contact import Contact



def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_new_contact_form()
    app.contact.delete_first_contact()



