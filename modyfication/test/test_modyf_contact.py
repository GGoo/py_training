import pytest

from modyfication.model.contact import Contact


@pytest.fixture

def test_modyfing_first_contact(app):
    app.contact.modyfing_first_contact(Contact())


