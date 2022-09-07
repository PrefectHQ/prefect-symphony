"""
This is a module containing tasks for interacting with:
Symphony events
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: agent-api-public.yaml
# Updated at: 2022-09-07T03:04:02.549803

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def read_events(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    type: str = None,
    tag: str = None,
    event_types: List[str] = None,
    ack_id: str = None,
    update_presence: bool = True,
) -> Dict[str, Any]:  # pragma: no cover
    """
    _Available on Agent 22.5.1 and above.This endpoint provides messages and events
    from all conversations that the user is in or events from the whole pod
    depending on the 'type' field value. When 'type':'fanout' is provided in the
    body, then only events from streams  the accountbelongs to are returned.
    Otherwise, if 'type': 'datahose' is provided in the body, then events
    returned are not limited to the streams user belongs to. In this case, at
    least one event type must be provided in the 'filters' field. In case you
    are using a datahose feed and retrieving SOCIALMESSAGE events, ceservice
    account must be properly configured in the Agent.The types of events
    returned can be found in the Real Time Events list (see definition on top of
    the file). The ackId sent as parameter can be empty for the first call. In
    the response an ackId will be sent back and it can be used for the next
    call: in this way you acknowledge that you have received the events that
    came with that ackId. If you have several instances of the same bot, they
    must share the same feed so  that events are spread across all bot
    instances. To do so, you must: share the same  service account provide the
    same 'tag' and same 'filters' values.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        type:
            Type of the feed. Allowed values are 'fanout' and 'datahose'.
        tag:
            A unique identifier to ensure uniqueness of the datafeed.
        event_types:
            At least one value is required if the type of feed is 'datahose'. Values
            must be a valid Real-Time Event type, i.e. one of: *
            MESSAGESENT * MESSAGESUPPRESSED * SYMPHONYELEMENTSACTION *
            SHAREDPOST * INSTANTMESSAGECREATED * ROOMCREATED *
            ROOMUPDATED * ROOMDEACTIVATED * ROOMREACTIVATED *
            USERREQUESTEDTOJOINROOM * USERJOINEDROOM * USERLEFTROOM *
            ROOMMEMBERPROMOTEDTOOWNER * ROOMMEMBERDEMOTEDFROMOWNER *
            CONNECTIONREQUESTED * CONNECTIONACCEPTED.
        ack_id:
            Should be empty for the first call, acknowledges that the current batch
            of messages have been successfully received by the client.
        update_presence:
            Whether to update the presence status of the account to AVAILABLE  when
            calling the endpoint. Default value is true.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v5/events/read`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Datafeed successfully read. |
    | 400 | Bad request. |
    | 401 | Unauthorized. |
    | 403 | Forbidden. |
    | 500 | Internal server error. |
    """  # noqa
    endpoint = "/v5/events/read"  # noqa

    responses = {
        200: "Datafeed successfully read.",  # noqa
        400: "Bad request.",  # noqa
        401: "Unauthorized.",  # noqa
        403: "Forbidden.",  # noqa
        500: "Internal server error.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    json_payload = {
        "type": type,
        "tag": tag,
        "event_types": event_types,
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