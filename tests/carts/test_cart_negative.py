import pytest
import allure


@pytest.mark.regression
@pytest.mark.xfail(
    reason="DummyJSON mock API accepts negative quantity"
)
@allure.feature("Cart")
def test_cart_negative_quantity(carts_client):

    products = [
        {
            "id": 1,
            "quantity": -1
        }
    ]

    response = carts_client.add_cart(products)

    assert response.status_code in [400, 422]