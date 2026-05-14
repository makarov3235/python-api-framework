import pytest
import allure

from helpers.assertions import (
    assert_status_code
)


@pytest.mark.integration
@allure.feature("Search Edge Cases")
@pytest.mark.parametrize(
    "query",
    [
        "",
        "!@#$%^",
        "😀😀😀",
        "a" * 500,
        "' OR 1=1 --",
        "<script>alert(1)</script>"
    ]
)
def test_search_edge_cases(
    search_client,
    query
):

    response = search_client.search_products(
        query=query
    )

    assert response.status_code in [200, 400]