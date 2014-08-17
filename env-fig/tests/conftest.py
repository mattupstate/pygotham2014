# -*- coding: utf-8 -*-
"""
    conftest
    ~~~~~~~~
"""

import pytest

from myapp import app, db


@pytest.fixture(scope='session')
def client():
    with app.app_context():
        db.create_all()
    app.testing = True
    app.debug = True
    return app.test_client()
