from clients.base_client import BaseClient


class AuthClient(BaseClient):

    def login(self, username, password):

        payload = {
            "username": username,
            "password": password
        }

        response = self.post(
            endpoint="/auth/login",
            json=payload
        )

        return response

    def get_me(self, token):

        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = self.get(
            endpoint="/auth/me",
            headers=headers
        )

        return response