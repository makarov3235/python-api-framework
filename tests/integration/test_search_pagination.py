import pytest
import allure

from helpers.assertions import assert_status_code
from helpers.search_helpers import (
    extract_product_ids
)


@pytest.mark.integration
@allure.feature("Search Pagination")
@pytest.mark.parametrize(
    "limit,skip",
    [
        (5, 0),
        (5, 5),
        (10, 10)
    ]
)
def test_search_pagination(
    search_client,
    limit,
    skip
):

    response = search_client.search_products(
        query="phone",
        limit=limit,
        skip=skip
    )

    assert_status_code(response, 200)

    body = response.json()

    assert body["limit"] == limit
    assert body["skip"] == skip

    assert len(body["products"]) <= limit