import pytest
import allure

from helpers.assertions import (
    assert_status_code,
    assert_response_time
)

from helpers.search_helpers import (
    extract_product_ids,
    has_duplicates
)


@pytest.mark.integration
@allure.feature("Search Integration")
def test_search_products_flow(
    search_client,
    products_client
):

    query = "phone"

    response = search_client.search_products(
        query=query
    )

    assert_status_code(response, 200)

    assert_response_time(response, 3)

    body = response.json()

    products = body["products"]

    # response not empty
    assert len(products) > 0

    # no duplicate ids
    product_ids = extract_product_ids(products)

    assert not has_duplicates(product_ids)

    # title contains search term
    matched_products = [
        product
        for product in products
        if query.lower() in product["title"].lower()
    ]

    assert len(matched_products) > 0

    # cross-service consistency
    for product in products:

        product_response = (
            products_client.get_product_by_id(
                product["id"]
            )
        )

        product_body = product_response.json()

        assert (
            product["price"] ==
            product_body["price"]
        )

        assert (
            product["category"] ==
            product_body["category"]
        )

        assert (
            product["rating"] ==
            product_body["rating"]
        )