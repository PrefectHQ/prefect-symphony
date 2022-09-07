"""
This is a module containing tasks for interacting with:
Symphony util
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: agent-api-public.yaml
# Updated at: 2022-09-07T03:04:01.829506

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def post_v1_util_echo(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    message: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Test endpoint, returns input.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        message:


    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/util/echo`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Message sent. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/util/echo"  # noqa

    responses = {
        200: "Message sent.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    json_payload = {
        "message": message,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        json=json_payload,
    )

    contents = _unpack_contents(response, responses)
    return contents