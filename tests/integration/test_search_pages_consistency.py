import pytest
import allure

from helpers.search_helpers import (
    extract_product_ids
)


@pytest.mark.integration
@allure.feature("Search Pagination")
def test_search_pages_do_not_overlap(
    search_client
):

    response_page_1 = (
        search_client.search_products(
            query="phone",
            limit=5,
            skip=0
        )
    )

    response_page_2 = (
        search_client.search_products(
            query="phone",
            limit=5,
            skip=5
        )
    )

    page_1_products = (
        response_page_1.json()["products"]
    )

    page_2_products = (
        response_page_2.json()["products"]
    )

    ids_1 = set(
        extract_product_ids(page_1_products)
    )

    ids_2 = set(
        extract_product_ids(page_2_products)
    )

    assert ids_1.isdisjoint(ids_2)