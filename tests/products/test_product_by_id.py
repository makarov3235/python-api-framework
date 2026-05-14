import pytest
import allure

from helpers.assertions import assert_status_code


@pytest.mark.smoke
@allure.feature("Products")
def test_get_product_by_valid_id(products_client):

    response = products_client.get_product_by_id(1)

    assert_status_code(response, 200)

    body = response.json()

    assert body["id"] == 1


@pytest.mark.regression
@allure.feature("Products")
def test_get_product_by_invalid_id(products_client):

    response = products_client.get_product_by_id(999999)

    assert_status_code(response, 404)