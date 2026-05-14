import pytest
import allure

from helpers.assertions import assert_status_code
from helpers.schema_validator import validate_schema

@pytest.mark.regression
@pytest.mark.xfail(
    reason="DummyJSON mock API accepts invalid product id"
)
@allure.feature("Cart")
def test_cart_invalid_product(carts_client):

    products = [
        {
            "id": 999999,
            "quantity": 1
        }
    ]

    response = carts_client.add_cart(products)

    assert response.status_code in [400, 404]