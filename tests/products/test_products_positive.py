import pytest
import allure

from helpers.assertions import assert_status_code
from helpers.schema_validator import validate_schema


@pytest.mark.smoke
@allure.feature("Products")
def test_get_products(products_client):

    response = products_client.get_all_products()

    assert_status_code(response, 200)

    body = response.json()

    validate_schema(
        body,
        "schemas/products_list_schema.json"
    )

    assert len(body["products"]) > 0


@pytest.mark.regression
@allure.feature("Products")
def test_products_validation(products_client):

    response = products_client.get_all_products()

    products = response.json()["products"]

    for product in products:

        assert product["price"] > 0
        assert product["stock"] >= 0
        assert 0 <= product["rating"] <= 5
        assert product["title"] != ""
        assert product["category"] != ""