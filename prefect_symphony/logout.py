"""
This is a module containing tasks for interacting with:
Symphony logout
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: authenticator-api-public.yaml
# Updated at: 2022-09-07T03:04:03.701680

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def post_v1_logout(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Logout a users session.

    Args:
        session_token:
            the session token to logout.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/logout`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 403 | Forbidden: Certificate authentication is not allowed for the requested user. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/logout"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        403: (  # noqa
            "Forbidden: Certificate authentication is not allowed for the requested"
            " user."
        ),
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.POST,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents