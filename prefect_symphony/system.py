"""
This is a module containing tasks for interacting with:
Symphony system
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: pod-api-public.yaml
# Updated at: 2022-08-26T18:55:04.228236

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def get_v2_system_protocols(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get a list of URI protocols supported by the company (pod).

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            Number of items to skip. Default is 0.
        limit:
            Maximum number of items to return. Default is 100 and not to exceed
            1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v2/system/protocols`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v2/system/protocols"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "skip": skip,
        "limit": limit,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
