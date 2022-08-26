"""
This is a module containing tasks for interacting with:
Symphony users
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: pod-api-public.yaml
# Updated at: 2022-08-26T18:55:04.229360

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def get_v2_users_presence(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    last_user_id: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    The returned data is taken from the in-memory cache for performance reasons
    which means inactive users may be omitted from the response.  All non-
    inactive users WILL be returned and some inactive users MAY be included. Any
    omitted user IS inactive.  Returned records are sorted by user ID,
    ascending.  This method is expensive. It pulls ALL records from the cache,
    sorts them and then only uses a subset. For large numbers of users, this can
    be very inefficient both due to sorting and due to the cache being
    distributed across many nodes.  Addiionally, there is the potential to miss
    users if they become active after the page in which their user ID falls has
    already been read by the client. To avoid this situation, a presence feed
    should be created (and optionally read from) first to capture presence
    changes of users who get reactivated during a paged call to this endpoint.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        last_user_id:
            Last user ID retrieved. Used for paging; if provided, results will skip
            users with IDs less than this parameter.
        limit:
            Max number of records to return. If no value is provided, 1000 is the
            default. The maximum supported value is 5000.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v2/users/presence`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v2/users/presence"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "last_user_id": last_user_id,
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


@task
async def get_v3_users(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    uid: str = None,
    email: str = None,
    username: str = None,
    local: bool = None,
    active: bool = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Search users by emails or ids. Only one of the search lists should be informed
    at a time. Search lists may containt up to 100 elements.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        uid:
            User IDs as a list of decimal integers separated by comma.
        email:
            List of email addresses separated by comma.
        username:
            List of username separated by comma.
        local:
            If true then a local DB search will be performed and only local pod
            users will be returned. If absent or false then a directory
            search will be performed and users from other pods who are
            visible to the calling user will also be returned.
        active:
            If not set all user status will be returned, if true all active users
            will be returned, if false all inactive users will be
            returned.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/users`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 204 | No user found. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v3/users"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "No user found.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "uid": uid,
        "email": email,
        "username": username,
        "local": local,
        "active": active,
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
