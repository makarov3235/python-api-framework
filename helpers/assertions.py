def assert_status_code(response, expected_status):

    actual_status = response.status_code

    assert actual_status == expected_status, (
        f"Expected status code {expected_status}, "
        f"but got {actual_status}"
    )


def assert_response_time(response, max_seconds):

    response_time = response.elapsed.total_seconds()

    assert response_time < max_seconds, (
        f"Response time is too high: {response_time}"
    )