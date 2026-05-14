from clients.base_client import BaseClient


class ProductsClient(BaseClient):

    def get_all_products(self, limit=None, skip=None):

        endpoint = "/products"

        params = {}

        if limit:
            params["limit"] = limit

        if skip:
            params["skip"] = skip

        return self.get(
            endpoint=endpoint,
            params=params
        )

    def get_product_by_id(self, product_id):

        return self.get(
            endpoint=f"/products/{product_id}"
        )

    def search_products(self, query):

        return self.get(
            endpoint=f"/products/search?q={query}"
        )