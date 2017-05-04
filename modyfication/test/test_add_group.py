# -*- coding: utf-8 -*-
from modyfication.model.group import Group


def test_add_group(app):
    app.group.create(Group(name="group1", header="group1", footer="group1"))

def test_add_empy_group(app):
    app.group.create(Group(name="", header="", footer=""))
