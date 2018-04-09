from logzero import logger
from my_restful.app import app

import pytest


"""
import unittest
from unittest import TestCase


class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_root(self):
        response = self.app.get('/')
        assert response

if __name__ == "__main__":
    unittest.main()
"""

@pytest.fixture()
def flask_test_app():
    test_app = app.test_client()
    return test_app


@pytest.mark.parametrize("expected, uri", [
    (200, "/"),
    (200, "/todos"),
    (200, "/todo/1"),
    (200, "/todo/2"),
    (404, "/todo/xxx"),  # 存在しないtodo_idを指定した場合はエラー
])
def test_get(flask_test_app, expected, uri):
    res = flask_test_app.get(uri)
    logger.debug("status: %s" % res.status)
    logger.debug("data: %s" % res.data)
    assert res.status_code == expected


@pytest.mark.parametrize("expected,uri,payload", [
    (200, "/todo", {"data": "xxx"}),
])
def test_post(flask_test_app, expected, uri, payload):
    res = flask_test_app.post(uri, data=payload)
    logger.debug("status: %s" % res.status)
    logger.debug("data: %s" % res.data)
    assert res.status_code == expected


@pytest.mark.parametrize("expected,uri,payload", [
    (201, "/todo/1", {"data": "yyy"}),
    (404, "/todo/xxx", {"data": "fail"}),  # 存在しないtodo_idを指定した場合はエラー
])
def test_put(flask_test_app, expected, uri, payload):
    res = flask_test_app.put(uri, data=payload)
    logger.debug("status: %s" % res.status)
    logger.debug("data: %s" % res.data)
    assert res.status_code == expected
