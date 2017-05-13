# -*- coding: utf-8 -*-
from modyfication.model.group import Group


def test_add_group(app):
    app.group.create(Group(name="ex8", header="ex8 header", footer="ex8 footer"))

def test_add_empy_group(app):
    app.group.create(Group(name="", header="", footer=""))
