import pytest
import allure

from helpers.assertions import assert_status_code


@pytest.mark.regression
@allure.feature("Search")
def test_search_products(products_client):

    response = products_client.search_products("phone")

    assert_status_code(response, 200)

    body = response.json()

    assert len(body["products"]) > 0


@pytest.mark.regression
@allure.feature("Pagination")
@pytest.mark.parametrize(
    "limit,skip",
    [
        (5, 0),
        (10, 5),
        (20, 10)
    ]
)
def test_products_pagination(products_client, limit, skip):

    response = products_client.get_all_products(
        limit=limit,
        skip=skip
    )

    assert_status_code(response, 200)

    body = response.json()

    assert body["limit"] == limit
    assert body["skip"] == skip