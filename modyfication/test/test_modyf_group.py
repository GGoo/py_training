import pytest
#from modyfication.model.group import Group
from modyfication.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_modyfing_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modyfing_first_group()
    app.session.logout()




