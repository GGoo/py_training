# -*- coding: utf-8 -*-
from decompozyction.model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="group1", header="group1", footer="group1"))
    app.session.logout()


def test_add_empy_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
