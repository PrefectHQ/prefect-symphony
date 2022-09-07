"""
This is a module containing tasks for interacting with:
Symphony user
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: pod-api-public.yaml
# Updated at: 2022-09-07T03:10:50.392289

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def post_v1_user_presence_register(
    session_token: str,
    uid_list: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Register interest in a user's presence status.

    Args:
        session_token:
            Session authentication token.
        uid_list:
            List of (integer) User IDs of users whose presence to query.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/user/presence/register`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: user id cannot be located. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/user/presence/register"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: user id cannot be located.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "uid_list": uid_list,
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
async def post_v1_user_search(
    session_token: str,
    search_request: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
    local: bool = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Search for users by name or email address.

    Args:
        session_token:
            Session authentication token.
        search_request:
            search criteria.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            number of records to skip.
        limit:
            Max number of records to return. If no value is provided, 50 is the
            default.
        local:
            If true then a local DB search will be performed and only local pod
            users will be returned. If absent or false then a directory
            search will be performed and users from other pods who are
            visible to the calling user will also be returned.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/user/search`

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
    endpoint = "/v1/user/search"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "No user found.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "skip": skip,
        "limit": limit,
        "local": local,
        "session_token": session_token,
        "search_request": search_request,
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
async def post_v1_user_uid_follow(
    session_token: str,
    uid: str,
    uid_list: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Make a list of users start following a specific user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        uid_list:
            List of (integer) User IDs of the followers.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/user/{uid}/follow`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/user/{uid}/follow"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "uid": uid,
        "uid_list": uid_list,
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
async def get_v1_user_uid_followers(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
    limit: int = None,
    before: str = None,
    after: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Returns the list of followers for a specific user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        limit:
            This is the maximum number of objects that may be returned.
        before:
            Returns results from an opaque “before” cursor value as presented via a
            response cursor.
        after:
            Returns results from an opaque “after” cursor value as presented via a
            response cursor.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/user/{uid}/followers`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/user/{uid}/followers"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "uid": uid,
        "limit": limit,
        "before": before,
        "after": after,
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
async def get_v1_user_uid_following(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
    limit: int = None,
    before: str = None,
    after: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Returns the list of users that a specific user is following.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        limit:
            This is the maximum number of objects that may be returned.
        before:
            Returns results from an opaque “before” cursor value as presented via a
            response cursor.
        after:
            Returns results from an opaque “after” cursor value as presented via a
            response cursor.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/user/{uid}/following`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/user/{uid}/following"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "uid": uid,
        "limit": limit,
        "before": before,
        "after": after,
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
async def post_v1_user_uid_unfollow(
    session_token: str,
    uid: str,
    uid_list: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Make a list of users unfollowing a specific user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        uid_list:
            List of (integer) User IDs of the followers.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/user/{uid}/unfollow`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/user/{uid}/unfollow"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "uid": uid,
        "uid_list": uid_list,
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
async def get_v2_user(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    uid: int = None,
    email: str = None,
    username: str = None,
    local: bool = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get user information.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        uid:
            User ID as a decimal integer.
        email:
            Email address.
        username:
            login user name.
        local:
            If true then a local DB search will be performed and only local pod
            users will be returned. If absent or false then a directory
            search will be performed and users from other pods who are
            visible to the calling user will also be returned. Note: for
            username search, the local flag must be true.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v2/user`

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
    endpoint = "/v2/user"  # noqa

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
async def get_v2_user_presence(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get presence information about the requesting user.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v2/user/presence`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Invalid session token. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v2/user/presence"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Invalid session token.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
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
async def post_v2_user_presence(
    session_token: str,
    presence: str,
    symphony_credentials: "SymphonyCredentials",
    soft: bool = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set the presence of the requesting user.

    Args:
        session_token:
            Session authentication token.
        presence:

        symphony_credentials:
            Credentials to use for authentication with Symphony.
        soft:
            If true, the user's current status is taken into consideration. If the
            user is currently OFFLINE, the user's presence will still be
            OFFLINE, but the new presence will take effect when the user
            comes online. If the user is currently online, the user's
            activity state will be applied to the presence if
            applicable. (e.g. if you are setting their presence to
            AVAILABLE, but the user is currently idle, their status will
            be represented as AWAY).

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v2/user/presence`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Invalid session token. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v2/user/presence"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Invalid session token.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "soft": soft,
        "presence": presence,
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
async def post_v3_user_presence(
    session_token: str,
    presence: str,
    symphony_credentials: "SymphonyCredentials",
    soft: bool = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Set presence information for a particular user.

    Args:
        session_token:
            Session authentication token.
        presence:

        symphony_credentials:
            Credentials to use for authentication with Symphony.
        soft:
            If true, the user's current status is taken into consideration. If the
            user is currently OFFLINE, the user's presence will still be
            OFFLINE, but the new presence will take effect when the user
            comes online. If the user is currently online, the user's
            activity state will be applied to the presence if
            applicable. (e.g. if you are setting their presence to
            AVAILABLE, but the user is currently idle, their status will
            be represented as AWAY).

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/user/presence`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized. |
    | 403 | Forbidden. |
    | 404 | Not Found: user id cannot be located. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v3/user/presence"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized.",  # noqa
        403: "Forbidden.",  # noqa
        404: "Not Found: user id cannot be located.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "soft": soft,
        "presence": presence,
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
async def get_v3_user_uid_presence(
    uid: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    local: bool = False,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get presence information about a particular user.

    Args:
        uid:
            Uid used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        local:
            If true, a local query will be performed and the presence will be set to
            OFFLINE for users who are not local to the calling user's
            pod. If false or absent, then the presence of all local
            users and the presence of all external users to whom the
            calling user is connected will be queried.  For external
            users, a 'presence interest' should be registered through
            /v1/user/presence/register before querying for presence.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/user/{uid}/presence`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: user id cannot be located. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v3/user/{uid}/presence"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: user id cannot be located.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "uid": uid,
        "local": local,
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
