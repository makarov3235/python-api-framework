from clients.base_client import BaseClient


class SearchClient(BaseClient):

    def search_products(
        self,
        query,
        limit=None,
        skip=None
    ):

        params = {
            "q": query
        }

        if limit:
            params["limit"] = limit

        if skip:
            params["skip"] = skip

        return self.get(
            endpoint="/products/search",
            params=params
        )