import pytest

from clients.auth_client import AuthClient


@pytest.fixture
def auth_client():

    return AuthClient()
