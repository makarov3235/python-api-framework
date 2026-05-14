import pytest
import allure

from helpers.assertions import (
    assert_status_code,
    assert_response_time
)

from helpers.schema_validator import validate_schema


@pytest.mark.smoke
@allure.feature("Auth")
@allure.story("Positive login")
def test_success_login(auth_client):

    response = auth_client.login(
        username="emilys",
        password="emilyspass"
    )

    assert_status_code(response, 200)

    assert_response_time(response, 3)

    validate_schema(
        data=response.json(),
        schema_path="schemas/login_schema.json"
    )

@pytest.mark.regression
@allure.feature("Auth")
@allure.story("Check response time")
def test_login_response_time(auth_client, valid_user):

    response = auth_client.login(
        username=valid_user["username"],
        password=valid_user["password"]
    )

    response_time = response.elapsed.total_seconds()

    assert response_time < 3