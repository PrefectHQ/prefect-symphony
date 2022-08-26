from httpx import AsyncClient

from prefect_symphony import SymphonyCredentials


def test_symphony_credentials_get_client():
    client = SymphonyCredentials(
        pod_subdomain="pod_subdomain", token="token_value"
    ).get_client()
    assert isinstance(client, AsyncClient)
    if token is not None:
        assert client.headers["authorization"] == "Bearer token_value"
