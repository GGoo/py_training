# -*- coding: utf-8 -*-
import exc4

from decompozyction.model.group import Group
#from group import Group

from decompozyction.fixture.application import Application
#from application import Application


@exc4.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group1", header="group1", footer="group1"))
    app.session.logout()

def test_add_empy_group(app):
    app.session.login(username="admin" , password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()