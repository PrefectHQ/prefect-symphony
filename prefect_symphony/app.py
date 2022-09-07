"""
This is a module containing tasks for interacting with:
Symphony app
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: authenticator-api-public.yaml
# Updated at: 2022-09-07T03:04:03.700737

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def get_v1_app_pod_certificate(
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieve the certificate that can be use to validate the JWT token obtain
    through the extension application authentication flow.

    Args:
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/app/pod/certificate`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 401 | Client is unauthorized to access this resource. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/app/pod/certificate"  # noqa

    responses = {
        200: "OK.",  # noqa
        401: "Client is unauthorized to access this resource.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.GET,
    )

    contents = _unpack_contents(response, responses)
    return contents
