"""Credential classes used to perform authenticated interactions with Symphony"""

from typing import Any, Dict, Optional

from httpx import AsyncClient
from prefect.blocks.core import Block
from pydantic import SecretStr


class SymphonyCredentials(Block):
    """
    Block used to manage Symphony authentication.

    Attributes:
        pod_subdomain:
            Pod subdomain used in formatting the endpoint URL.
        token: The token to authenticate with Symphony.


    Examples:
        Load stored Symphony credentials:
        ```python
        from prefect_symphony import SymphonyCredentials
        symphony_credentials_block = SymphonyCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Symphony Credentials"
    # _logo_url = "<LOGO_URL_HERE>"  # noqa

    pod_subdomain: str
    token: SecretStr
    client_kwargs: Optional[Dict[str, Any]] = None

    def get_client(self) -> AsyncClient:
        """
        Gets an Symphony REST AsyncClient.

        Returns:
            An Symphony REST AsyncClient.

        Example:
            Gets a Symphony REST AsyncClient.
            ```python
            from prefect import flow
            from prefect_symphony import SymphonyCredentials

            @flow
            def example_get_client_flow():
                token = "consumer_key"
                symphony_credentials = SymphonyCredentials(token=token)
                client = symphony_credentials.get_client()
                return client

            example_get_client_flow()
            ```
        """
        base_url = (
            f"https://{self.pod_subdomain}.symphony.com/login/pubkey/authenticate"
        )

        client_kwargs = self.client_kwargs or {}
        client_kwargs["header"] = {
            "Authorization": f"Bearer {self.token.get_secret_value()}"
        }
        client = AsyncClient(base_url=base_url, **client_kwargs)
        return client
