import pytest
import allure

from helpers.assertions import assert_status_code
from data.auth_data import INVALID_PASSWORD


@pytest.mark.regression
@allure.feature("Auth")
@allure.story("Invalid password")
def test_login_invalid_password(auth_client):

    response = auth_client.login(
        username=INVALID_PASSWORD["username"],
        password=INVALID_PASSWORD["password"]
    )

    assert_status_code(response, 400)



@pytest.mark.regression
@allure.feature("Auth")
@allure.story("Empty credentials")
def test_login_empty_credentials(auth_client):

    response = auth_client.login(
        username="",
        password=""
    )

    assert_status_code(response, 400)