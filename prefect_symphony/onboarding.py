"""
This is a module containing tasks for interacting with:
Symphony onboarding
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: community-connect-public-api.yaml
# Updated at: 2022-09-07T03:10:47.570996

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def get_user_onboarding_availability(
    email: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get user's pod and availability for onboarding.

    Args:
        email:
            The user email, e.g. `user@companyDomain.com`.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/onboarding/tenant`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Something was wrong about the request. |
    | 401 | Unauthorized request. |
    """  # noqa
    endpoint = "/v1/onboarding/tenant"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Something was wrong about the request.",  # noqa
        401: "Unauthorized request.",  # noqa
    }

    params = {
        "email": email,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
