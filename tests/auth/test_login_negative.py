import pytest


@pytest.mark.parametrize(
    "username,password",
    [
        ("wrong_user", "wrong_pass"),
        ("emilys", "wrong_pass"),
        ("", ""),
        ("emilys", ""),
        ("", "emilyspass")
    ]
)
def test_login_negative(auth_client, username, password):

    response = auth_client.login(
        username=username,
        password=password
    )

    assert response.status_code == 400