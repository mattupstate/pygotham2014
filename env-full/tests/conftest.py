# -*- coding: utf-8 -*-
"""
    conftest
    ~~~~~~~~
"""

import pytest

from myapp import app


@pytest.fixture(scope='session')
def client():
    app.testing = True
    app.debug = True
    return app.test_client()
