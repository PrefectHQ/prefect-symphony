"""
This is a module containing tasks for interacting with:
Symphony pubkey
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: login-api-public.yaml
# Updated at: 2022-09-07T03:10:48.513335

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def post_pubkey_app_authenticate(
    authenticate_request: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Based on an authentication request token signed by the application's RSA private
    key, authenticate the API caller and return a session token.  A HTTP 401
    Unauthorized error is returned on errors during authentication (e.g. invalid
    app, malformed authentication token, app's public key not imported in the
    pod, invalid token signature etc.).

    Args:
        authenticate_request:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/pubkey/app/authenticate`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 401 | Client is unauthorized to access this resource. |
    | 403 | Forbidden to access this endpoint . |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/pubkey/app/authenticate"  # noqa

    responses = {
        200: "OK.",  # noqa
        401: "Client is unauthorized to access this resource.",  # noqa
        403: "Forbidden to access this endpoint .",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "authenticate_request": authenticate_request,
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
async def post_pubkey_app_user_user_id_authenticate(
    session_token: str,
    user_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Authenticate an application in a delegated context to act on behalf of a user.

    Args:
        session_token:
            App Session authentication token.
        user_id:
            User id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/pubkey/app/user/{user_id}/authenticate`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 401 | Client is unauthorized to access this resource. |
    | 403 | Forbidden to access this endpoint . |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/pubkey/app/user/{user_id}/authenticate"  # noqa
    responses = {
        200: "OK.",  # noqa
        401: "Client is unauthorized to access this resource.",  # noqa
        403: "Forbidden to access this endpoint .",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "user_id": user_id,
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
async def post_pubkey_app_username_username_authenticate(
    session_token: str,
    username: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Authenticate an application in a delegated context to act on behalf of a user.

    Args:
        session_token:
            App Session authentication token.
        username:
            Username used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/pubkey/app/username/{username}/authenticate`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 401 | Client is unauthorized to access this resource. |
    | 403 | Forbidden to access this endpoint . |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/pubkey/app/username/{username}/authenticate"  # noqa
    responses = {
        200: "OK.",  # noqa
        401: "Client is unauthorized to access this resource.",  # noqa
        403: "Forbidden to access this endpoint .",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "username": username,
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
async def post_pubkey_authenticate(
    authenticate_request: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Based on an authentication request token signed by the caller's RSA private key,
    authenticate the API caller and return a session token.  A HTTP 401
    Unauthorized error is returned on errors during authentication (e.g. invalid
    user, malformed authentication token, user's public key not imported in the
    pod, invalid token signature etc.).

    Args:
        authenticate_request:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/pubkey/authenticate`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 401 | Client is unauthorized to access this resource. |
    | 403 | Forbidden to access this endpoint . |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/pubkey/authenticate"  # noqa

    responses = {
        200: "OK.",  # noqa
        401: "Client is unauthorized to access this resource.",  # noqa
        403: "Forbidden to access this endpoint .",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "authenticate_request": authenticate_request,
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
async def post_v1_pubkey_app_authenticate_extension_app(
    authenticate_request: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Based on an authentication request token signed by the caller's RSA private key,
    authenticate the API caller and return a session token.  A HTTP 401
    Unauthorized error is returned on errors during authentication (e.g. invalid
    user, malformed authentication token, user's public key not imported in the
    pod, invalid token signature etc.).

    Args:
        authenticate_request:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/pubkey/app/authenticate/extensionApp`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Request object is invalid. |
    | 401 | Client is unauthorized to access this resource. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/pubkey/app/authenticate/extensionApp"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Request object is invalid.",  # noqa
        401: "Client is unauthorized to access this resource.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "authenticate_request": authenticate_request,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.POST,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
