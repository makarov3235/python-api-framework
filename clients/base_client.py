import requests

from config.settings import BASE_URL, TIMEOUT
from helpers.logger import logger
from utils.retry import retry


class BaseClient:

    def __init__(self):
        self.base_url = BASE_URL

    @retry(times=3, delay=2)
    def get(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}{endpoint}"

        response = requests.get(
            url=url,
            headers=headers,
            params=params,
            timeout=TIMEOUT
        )

        return response

    @retry(times=3, delay=2)
    def post(self, endpoint, json=None, headers=None):

        url = f"{self.base_url}{endpoint}"

        logger.info(f"POST request: {url}")
        logger.info(f"Request body: {json}")

        response = requests.post(
            url=url,
            json=json,
            headers=headers,
            timeout=TIMEOUT
        )

        logger.info(f"Response status: {response.status_code}")
        logger.info(f"Response body: {response.text}")

        return response