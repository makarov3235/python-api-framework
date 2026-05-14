from clients.base_client import BaseClient


class CartsClient(BaseClient):

    def add_cart(self, user_id, products):

        payload = {
            "userId": user_id,
            "products": products
        }

        return self.post(
            endpoint="/carts/add",
            json=payload
        )