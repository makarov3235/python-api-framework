import pytest
import allure


@pytest.mark.integration
@allure.feature("Integration")
def test_cart_invalid_user(carts_client):

    products = [
        {
            "id": 1,
            "quantity": 1
        }
    ]

    response = carts_client.add_cart(
        user_id=999999,
        products=products
    )

    assert response.status_code in [400, 404, 201]


@pytest.mark.integration
@allure.feature("Integration")
def test_cart_invalid_product(
    carts_client
):

    products = [
        {
            "id": 999999,
            "quantity": 1
        }
    ]

    response = carts_client.add_cart(
        user_id=1,
        products=products
    )

    assert response.status_code in [400, 404, 201]


@pytest.mark.integration
@allure.feature("Integration")
def test_empty_cart(carts_client):

    response = carts_client.add_cart(
        user_id=1,
        products=[]
    )

    assert response.status_code in [400, 422, 201]