import pytest
import allure

from helpers.assertions import assert_status_code
from helpers.integration_helpers import calculate_total


@pytest.mark.integration
@allure.feature("Integration")
@allure.story("User cart flow")
def test_user_cart_flow(
    auth_client,
    carts_client,
    products_client,
    valid_user
):

    # STEP 1
    login_response = auth_client.login(
        username=valid_user["username"],
        password=valid_user["password"]
    )

    assert_status_code(login_response, 200)

    login_body = login_response.json()

    token = login_body["accessToken"]
    user_id = login_body["id"]

    # STEP 2
    me_response = auth_client.get_me(token)

    assert_status_code(me_response, 200)

    me_body = me_response.json()

    assert me_body["id"] == user_id

    # STEP 3
    cart_products = [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 2,
            "quantity": 1
        }
    ]

    cart_response = carts_client.add_cart(
        user_id=user_id,
        products=cart_products
    )

    assert_status_code(cart_response, 201)

    cart_body = cart_response.json()

    # STEP 4
    assert cart_body["userId"] == user_id

    # STEP 5
    assert (
        cart_body["totalProducts"] ==
        len(cart_products)
    )

    # STEP 6
    assert (
        cart_body["discountedTotal"] <=
        cart_body["total"]
    )

    # STEP 7
    expected_total = 0

    for item in cart_body["products"]:

        product_response = products_client.get_product_by_id(
            item["id"]
        )

        product_body = product_response.json()

        expected_total += (
            product_body["price"] *
            item["quantity"]
        )

    assert cart_body["total"] == expected_total