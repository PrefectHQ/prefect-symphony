"""
This is a module containing tasks for interacting with:
Symphony idm
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: login-api-public.yaml
# Updated at: 2022-09-07T03:04:05.677882

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def get_idm_keys(
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    This is a public endpoint, no authentication is required. The JWKS can be used
    to verify JWT issued by the idm/tokens endpoint. Since SBE 20.14.

    Args:
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/idm/keys`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/idm/keys"  # noqa

    responses = {
        200: "OK.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.GET,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def post_idm_tokens(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    scope: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Returns a valid OAuth2 access token from a given session token to be used for
    authentication.

    Args:
        session_token:
            User session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        scope:
            Optional field used to get access with specific entitlements, use space
            separated list to define more that one.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/idm/tokens`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 401 | Client is unauthorized to access this resource. |
    | 403 | Forbidden to access this endpoint . |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/idm/tokens"  # noqa

    responses = {
        200: "OK.",  # noqa
        401: "Client is unauthorized to access this resource.",  # noqa
        403: "Forbidden to access this endpoint .",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "scope": scope,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.POST,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
