"""
This is a module containing tasks for interacting with:
Symphony connection
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: pod-api-public.yaml
# Updated at: 2022-09-07T03:04:07.531298

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def post_v1_connection_accept(
    session_token: str,
    connection_request: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Accept the connection request for the requesting user.

    Args:
        session_token:
            Session authentication token.
        connection_request:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/connection/accept`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: Connection cannot be found. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/connection/accept"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: Connection cannot be found.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "connection_request": connection_request,
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
async def post_v1_connection_create(
    session_token: str,
    connection_request: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Sends an invitation to connect with another user.

    Args:
        session_token:
            Session authentication token.
        connection_request:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/connection/create`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: User cannot be found. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/connection/create"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: User cannot be found.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "connection_request": connection_request,
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
async def get_v1_connection_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    status: str = None,
    user_ids: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    This retrieves all connections of the requesting user. (i.e. both connections in
    which the requesting user is the sender and those in which the requesting
    user is the inivtee) By default, if you haven't specified the connection
    status to filter on, this call will only return results for both
    'pending_incoming' and 'pending_outgoing'. You can optionally filter by
    userIds to further restrict the results of a specific connection status. If
    the users are in the same private pod, the users have an implicit connection
    status of 'accepted'. Those users will not be returned in the response if
    you don't specify the connection status as 'accepted' (default is 'pending')
    and the explicit userIds in the request.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        status:
            Filter the connection list based on the connection status. The
            connection status can only be pending_incoming,
            pending_outgoing, accepted, rejected, or all (all of the
            above).
        user_ids:
            The userIds parameter should be specified as a comma delimited list of
            user ids and can be used to restrict the results of a
            specific connection. Note that this is particularly
            important if the caller intends to retrieve results for
            implicit connection (user within the same pod). Implicit
            connections will not be included in the response if userId
            is not provided.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/connection/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: Connection cannot be found. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/connection/list"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: Connection cannot be found.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "status": status,
        "user_ids": user_ids,
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
async def post_v1_connection_reject(
    session_token: str,
    connection_request: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Reject the connection between the requesting user and request sender. If both
    users are in the same private pod, an error will be returned because both
    users have an implicit connection which cannot be rejected.

    Args:
        session_token:
            Session authentication token.
        connection_request:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/connection/reject`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: Connection cannot be found. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/connection/reject"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: Connection cannot be found.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "connection_request": connection_request,
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
async def post_v1_connection_user_uid_remove(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Removes a connection with a user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/connection/user/{uid}/remove`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: Connection cannot be found. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/connection/user/{uid}/remove"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: Connection cannot be found.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "uid": uid,
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
async def get_v1_connection_user_user_id_info(
    session_token: str,
    user_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    The status of the connection invitation to another user.

    Args:
        session_token:
            Session authentication token.
        user_id:
            User id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/connection/user/{user_id}/info`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: Connection cannot be found. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/connection/user/{user_id}/info"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: Connection cannot be found.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "user_id": user_id,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
