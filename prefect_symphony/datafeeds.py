"""
This is a module containing tasks for interacting with:
Symphony datafeeds
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: agent-api-public.yaml
# Updated at: 2022-09-07T03:04:02.548094

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def list_datafeed(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    tag: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    _Available on Agent 2.57.0 and above._  The datafeed provides messages and
    events from all conversations that the user is in. The types of events
    surfaced in the datafeed can be found in the [Real Time Events](./docs/real-
    time-events.md) list.  Returns the list of the datafeeds for the user. Any
    datafeed ID of the list can then be used as input to the Read
    Messages/Events Stream v4 endpoint.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        tag:
            A unique identifier to ensure uniqueness of the datafeed. Used to
            restrict search.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v5/datafeeds`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Datafeed sucessfully created. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 500 | Internal server error. |
    """  # noqa
    endpoint = "/v5/datafeeds"  # noqa

    responses = {
        200: "Datafeed sucessfully created.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
        500: "Internal server error.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "tag": tag,
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
async def create_datafeed(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    tag: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    _Available on Agent 2.57.0 and above._  The datafeed provides messages and
    events from all conversations that the user is in. The types of events
    surfaced in the datafeed can be found in the Real Time Events list. (see
    definition on top of the file)  Returns the ID of the datafeed that has just
    been created. This ID should then be used as input to the Read
    Messages/Events Stream v4 endpoint.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        tag:
            A unique identifier to ensure uniqueness of the datafeed.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v5/datafeeds`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Datafeed sucessfully created. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 500 | Internal server error. |
    """  # noqa
    endpoint = "/v5/datafeeds"  # noqa

    responses = {
        201: "Datafeed sucessfully created.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
        500: "Internal server error.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    json_payload = {
        "tag": tag,
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
async def delete_datafeed(
    datafeed_id: str,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    _Available on Agent 2.57.0 and above._  The datafeed provides messages and
    events from all conversations that the user is in. The types of events
    surfaced in the datafeed can be found in the Real Time Events list. (see
    definition on top of the file)  Delete the specified datafeed.

    Args:
        datafeed_id:
            Datafeed id used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v5/datafeeds/{datafeed_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | Datafeed successfully deleted. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 500 | Internal server error. |
    """  # noqa
    endpoint = f"/v5/datafeeds/{datafeed_id}"  # noqa
    responses = {
        204: "Datafeed successfully deleted.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
        500: "Internal server error.",  # noqa
    }

    params = {
        "datafeed_id": datafeed_id,
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def read_datafeed(
    datafeed_id: str,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    ack_id: str = None,
    update_presence: bool = True,
) -> Dict[str, Any]:  # pragma: no cover
    """
    _Available on Agent 2.57.0 and above._  The datafeed provides messages and
    events from all conversations that the user is in. The types of events
    surfaced in the datafeed can be found in the Real Time Events list. (see
    definition on top of the file)  Read the specified datafeed.  The ackId sent
    as parameter can be empty for the first call. In the response an ackId will
    be sent back and it can be used for the next call: in this way you
    acknowledge that you have received the events that came with that ackId;
    datafeed will remove the events associated with that ackId from your queue.

    Args:
        datafeed_id:
            Datafeed id used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        ack_id:
            A unique id for events that can be deleted from a client's. Empty for
            the first read. If set to null or missing, it will be
            considered empty feed.
        update_presence:
            Set to false to avoid updating the user's presence when reading events.
            Default is true.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v5/datafeeds/{datafeed_id}/read`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Datafeed successfully read. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 403 | Forbidden. |
    | 500 | Internal server error. |
    """  # noqa
    endpoint = f"/v5/datafeeds/{datafeed_id}/read"  # noqa
    responses = {
        200: "Datafeed successfully read.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
        403: "Forbidden.",  # noqa
        500: "Internal server error.",  # noqa
    }

    params = {
        "datafeed_id": datafeed_id,
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    json_payload = {
        "ack_id": ack_id,
        "update_presence": update_presence,
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
