"""
This is a module containing tasks for interacting with:
Symphony im
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: pod-api-public.yaml
# Updated at: 2022-09-07T03:04:07.533267

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def post_v1_im_create(
    uid_list: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    At least one user ID must be provided or an error response will be sent.  The
    caller is implicitly included in the members of the created chat.  Duplicate
    users will be included in the membership of the chat but the duplication
    will be silently ignored.  If there is an existing IM conversation with the
    same set of participants then the id of that existing stream will be
    returned.  This method was incorrectly specified to take a query parameter
    in version 1.0 of this specification but now expects a JSON array of user
    IDs in the body of the request.

    Args:
        uid_list:
            List of (integer) User IDs of participants.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/im/create`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/im/create"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "uid_list": uid_list,
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


@task
async def get_v1_im_id_info(
    id: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get information about a partcular IM.

    Args:
        id:
            Id used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/im/{id}/info`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/im/{id}/info"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "id": id,
        "session_token": session_token,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def post_v1_im_id_update(
    id: str,
    payload: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the attributes of an existing IM.

    Args:
        id:
            Id used in formatting the endpoint URL.
        payload:

        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/im/{id}/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 451 | Unavailable for Legal Reasons: Compliance Issues found in IM update request. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/im/{id}/update"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        451: (  # noqa
            "Unavailable for Legal Reasons: Compliance Issues found in IM update"
            " request."
        ),
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "id": id,
        "payload": payload,
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
