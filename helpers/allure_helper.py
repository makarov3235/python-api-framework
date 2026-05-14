import allure
import json


def attach_response(response):

    allure.attach(
        body=response.text,
        name="response",
        attachment_type=allure.attachment_type.JSON
    )


def attach_request(data):

    allure.attach(
        body=json.dumps(data, indent=4),
        name="request",
        attachment_type=allure.attachment_type.JSON
    )