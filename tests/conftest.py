import pytest

from clients.auth_client import AuthClient
from data.auth_data import VALID_USER


@pytest.fixture
def auth_client():

    return AuthClient()


@pytest.fixture
def valid_user():

    return VALID_USER


@pytest.fixture
def auth_token(auth_client, valid_user):

    response = auth_client.login(
        username=valid_user["username"],
        password=valid_user["password"]
    )

    body = response.json()

    return body["accessToken"]