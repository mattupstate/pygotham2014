# -*- coding: utf-8 -*-
"""
    test_app
    ~~~~~~~~
"""

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
