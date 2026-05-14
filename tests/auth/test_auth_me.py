import pytest
import allure

from helpers.assertions import assert_status_code


@pytest.mark.smoke
@allure.feature("Auth")
@allure.story("Get current user")
def test_get_current_user(auth_client, auth_token):

    response = auth_client.get_me(auth_token)

    assert_status_code(response, 200)

    body = response.json()

    assert body["username"] == "emilys"
    assert "email" in body