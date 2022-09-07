"""
This is a module containing tasks for interacting with:
Symphony room
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: pod-api-public.yaml
# Updated at: 2022-09-07T03:04:07.536626

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def post_v1_room_id_membership_add(
    id: str,
    payload: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Adds new member to an existing room.

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
    `/v1/room/{id}/membership/add`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/room/{id}/membership/add"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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


@task
async def post_v1_room_id_membership_demote_owner(
    id: str,
    payload: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Demotes room owner.

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
    `/v1/room/{id}/membership/demoteOwner`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/room/{id}/membership/demoteOwner"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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


@task
async def post_v1_room_id_membership_promote_owner(
    id: str,
    payload: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Promotes user to owner.

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
    `/v1/room/{id}/membership/promoteOwner`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/room/{id}/membership/promoteOwner"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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


@task
async def post_v1_room_id_membership_remove(
    id: str,
    payload: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Removes member from an existing room.

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
    `/v1/room/{id}/membership/remove`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/room/{id}/membership/remove"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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


@task
async def post_v1_room_id_set_active(
    id: str,
    active: bool,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deactivate or reactivate a chatroom. At creation, a new chatroom is active.

    Args:
        id:
            Id used in formatting the endpoint URL.
        active:

        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/room/{id}/setActive`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/room/{id}/setActive"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "id": id,
        "active": active,
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
async def get_v2_room_id_membership_list(
    id: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Lists current members of an existing room.

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
    `/v2/room/{id}/membership/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v2/room/{id}/membership/list"  # noqa
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
async def post_v3_room_create(
    payload: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create a new chatroom.  If no  attributes are specified, the room is created as
    a private chatroom.

    Args:
        payload:

        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/room/create`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 451 | Unavailable for Legal Reasons: Compliance Issues found in room creation request. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v3/room/create"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        451: (  # noqa
            "Unavailable for Legal Reasons: Compliance Issues found in room creation"
            " request."
        ),
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
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


@task
async def post_v3_room_search(
    session_token: str,
    query: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Search rooms according to the specified criteria.

    Args:
        session_token:
            Session authentication token.
        query:
            The search query object.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            No. of results to skip.
        limit:
            Max no. of results to return. If no value is provided, 50 is the
            default. Must be a positive integer and must not exceed 100.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/room/search`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v3/room/search"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "skip": skip,
        "limit": limit,
        "query": query,
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
async def get_v3_room_id_info(
    id: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get information about a partcular chatroom.

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
    `/v3/room/{id}/info`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v3/room/{id}/info"  # noqa
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
async def post_v3_room_id_update(
    id: str,
    payload: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the attributes of an existing chatroom.

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
    `/v3/room/{id}/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 451 | Unavailable for Legal Reasons: Compliance Issues found in room update request. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v3/room/{id}/update"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        451: (  # noqa
            "Unavailable for Legal Reasons: Compliance Issues found in room update"
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
