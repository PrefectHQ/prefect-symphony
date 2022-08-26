"""
This is a module containing tasks for interacting with:
Symphony streams
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: pod-api-public.yaml
# Updated at: 2022-08-26T18:55:04.223885

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def post_v1_streams_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
    filter: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieve a list of all streams of which the requesting user is a member, sorted
    by creation date (ascending).

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            No. of results to skip.
        limit:
            Max no. of results to return. If no value is provided, 50 is the
            default.
        filter:
            Stream filtering criteria.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/streams/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 204 | Stream not found. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/streams/list"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "Stream not found.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "skip": skip,
        "limit": limit,
        "filter": filter,
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
async def get_v1_streams_sid_attachments(
    sid: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    since: int = None,
    to: int = None,
    limit: int = None,
    sort_dir: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get attachments in a particular stream.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        since:
            Timestamp of first required attachment. This is a long integer value
            representing milliseconds since Jan 1 1970.
        to:
            Timestamp of last required attachment. This is a long integer value
            representing milliseconds since Jan 1 1970.
        limit:
            Maximum number of attachments to return. Default is 50. Must be a
            positive integer and must not exceed 100.
        sort_dir:
            Attachment date sort direction : ASC or DESC (default to ASC).

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/streams/{sid}/attachments`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/streams/{sid}/attachments"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "sid": sid,
        "since": since,
        "to": to,
        "limit": limit,
        "sort_dir": sort_dir,
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
async def get_v2_streams_sid_info(
    sid: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get information about a partcular stream.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v2/streams/{sid}/info`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v2/streams/{sid}/info"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "sid": sid,
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
