"""
This is a module containing tasks for interacting with:
Symphony signals
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: agent-api-public.yaml
# Updated at: 2022-09-07T03:04:01.826530

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def post_v1_signals_create(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
    name: str = None,
    query: str = None,
    visible_on_profile: bool = None,
    company_wide: bool = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create a signal.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.
        name:
            Signal name.
        query:
            The query used to define this signal. The query is defined as
            'field:value' pairs combined by the operators 'AND' or 'OR'.
            Supported fields are (case-insensitive): 'author', 'hashtag'
            and 'cashtag'. MUST contain at least one 'hashtag' or
            'cashtag' definition.
        visible_on_profile:
            Whether the signal is visible on its creator's profile.
        company_wide:
            Whether the signal is a push signal.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/signals/create`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Signal created. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 451 | Compliance Issues found in signal. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/signals/create"  # noqa

    responses = {
        200: "Signal created.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        451: "Compliance Issues found in signal.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    json_payload = {
        "name": name,
        "query": query,
        "visible_on_profile": visible_on_profile,
        "company_wide": company_wide,
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


@task
async def get_v1_signals_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
    skip: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List signals for the requesting user. This includes signals that the user has
    created and public signals to which they subscribed.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.
        skip:
            No. of signals to skip.
        limit:
            Max no. of signals to return. If no value is provided, 50 is the
            default. The maximum supported value is 500.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/signals/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | List of signals for the requesting user. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/signals/list"  # noqa

    responses = {
        200: "List of signals for the requesting user.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
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


@task
async def post_v1_signals_id_delete(
    session_token: str,
    id: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete a signal.

    Args:
        session_token:
            Session authentication token.
        id:
            Id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/signals/{id}/delete`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Signal deleted. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/signals/{id}/delete"  # noqa
    responses = {
        200: "Signal deleted.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "id": id,
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
async def get_v1_signals_id_get(
    session_token: str,
    id: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get details of the requested signal.

    Args:
        session_token:
            Session authentication token.
        id:
            Id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/signals/{id}/get`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | List of signals for the requesting user. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/signals/{id}/get"  # noqa
    responses = {
        200: "List of signals for the requesting user.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "id": id,
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
async def post_v1_signals_id_subscribe(
    session_token: str,
    id: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
    pushed: bool = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Subscribe to a Signal.

    Args:
        session_token:
            Session authentication token.
        id:
            Id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.
        pushed:
            Prevent the user to unsubscribe (only for bulk subscription).

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/signals/{id}/subscribe`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Signal subscribed. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/signals/{id}/subscribe"  # noqa
    responses = {
        200: "Signal subscribed.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "id": id,
        "pushed": pushed,
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
async def get_v1_signals_id_subscribers(
    session_token: str,
    id: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
    skip: int = 0,
    limit: int = 100,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the subscribers of a signal.

    Args:
        session_token:
            Session authentication token.
        id:
            Id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.
        skip:
            No. of results to skip.
        limit:
            Max No. of subscribers to return. If no value is provided, 100 is the
            default.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/signals/{id}/subscribers`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Signal Subscribers. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/signals/{id}/subscribers"  # noqa
    responses = {
        200: "Signal Subscribers.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "id": id,
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


@task
async def post_v1_signals_id_unsubscribe(
    session_token: str,
    id: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Unsubscribe to a Signal.

    Args:
        session_token:
            Session authentication token.
        id:
            Id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/signals/{id}/unsubscribe`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Signal unsubscribed. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/signals/{id}/unsubscribe"  # noqa
    responses = {
        200: "Signal unsubscribed.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "id": id,
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
async def post_v1_signals_id_update(
    session_token: str,
    id: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
    name: str = None,
    query: str = None,
    visible_on_profile: bool = None,
    company_wide: bool = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update a signal.

    Args:
        session_token:
            Session authentication token.
        id:
            Id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.
        name:
            Signal name.
        query:
            The query used to define this signal. The query is defined as
            'field:value' pairs combined by the operators 'AND' or 'OR'.
            Supported fields are (case-insensitive): 'author', 'hashtag'
            and 'cashtag'. MUST contain at least one 'hashtag' or
            'cashtag' definition.
        visible_on_profile:
            Whether the signal is visible on its creator's profile.
        company_wide:
            Whether the signal is a push signal.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/signals/{id}/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Signal updated. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 451 | Compliance Issues found in signal. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/signals/{id}/update"  # noqa
    responses = {
        200: "Signal updated.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        451: "Compliance Issues found in signal.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "id": id,
    }

    json_payload = {
        "name": name,
        "query": query,
        "visible_on_profile": visible_on_profile,
        "company_wide": company_wide,
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
