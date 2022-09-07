"""
This is a module containing tasks for interacting with:
Symphony message
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: agent-api-public.yaml
# Updated at: 2022-09-07T03:10:44.721892

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def get_v1_message_search(
    query: str,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
    scope: str = None,
    sort_dir: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Search messages according to the specified criteria. The 'query' parameter takes
    a search query defined as 'field:value' pairs combined by the operator 'AND'
    (e.g. 'text:foo AND autor:bar'). Supported fields are  (case-insensitive):
    'text', 'author', 'hashtag', 'cashtag', 'mention', 'signal', 'fromDate',
    'toDate',  'streamId', 'streamType'.  'text' search requires a 'streamId' to
    be specified.  'streamType' accepts one of the following values: 'chat' (IMs
    and MIMs), 'im', 'mim', 'chatroom', 'post'.  'signal' queries can only be
    combined with 'fromDate', 'toDate', 'skip' and 'limit' parameters.

    Args:
        query:
            The search query. See above for the query syntax.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            No. of results to skip.
        limit:
            Max no. of results to return. If no value is provided, 50 is the
            default.
        scope:
            Describes where content should be searched for that query. It can
            exclusively apply to Symphony content or to one Connector.
        sort_dir:
            Messages sort direction : ASC or DESC (default to DESC).

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/message/search`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 204 | No Messages. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/message/search"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "No Messages.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "query": query,
        "skip": skip,
        "limit": limit,
        "scope": scope,
        "sort_dir": sort_dir,
        "session_token": session_token,
        "key_manager_token": key_manager_token,
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
async def post_v1_message_search(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
    scope: str = None,
    sort_dir: str = None,
    text: str = None,
    stream_id: str = None,
    stream_type: str = None,
    author: int = None,
    hashtag: str = None,
    cashtag: str = None,
    mention: int = None,
    signal: str = None,
    from_date: int = None,
    to_date: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Search messages according to the specified criteria.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            No. of results to skip.
        limit:
            Max no. of results to return. If no value is provided, 50 is the
            default.
        scope:
            Describes where content should be searched for that query. It can
            exclusively apply to Symphony content or to one Connector.
        sort_dir:
            Messages sort direction : ASC or DESC (default to DESC).
        text:
            Search for messages containing this text. Requires streamId to be
            specified.
        stream_id:
            Search for messages sent to this stream.
        stream_type:
            Search for messages sent to this type of streams. Accepted values are
            CHAT, IM, MIM, ROOM, POST.
        author:
            Search for messages sent by this user ID.
        hashtag:
            Search for messages containing this hashtag.
        cashtag:
            Search for messages containing this cashtag.
        mention:
            Search for messages mentioning this user ID.
        signal:
            Search for messages matching this signal. Can only be combined with date
            filtering and paging parameters.
        from_date:
            Search for messages sent on or after this timestamp.
        to_date:
            Search for messages sent before this timestamp.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/message/search`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 204 | No Messages. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/message/search"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "No Messages.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "skip": skip,
        "limit": limit,
        "scope": scope,
        "sort_dir": sort_dir,
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    json_payload = {
        "text": text,
        "stream_id": stream_id,
        "stream_type": stream_type,
        "author": author,
        "hashtag": hashtag,
        "cashtag": cashtag,
        "mention": mention,
        "signal": signal,
        "from_date": from_date,
        "to_date": to_date,
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
async def get_v1_message_id(
    session_token: str,
    key_manager_token: str,
    id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get a message by ID.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        id:
            Id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/message/{id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 204 | No Messages. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/message/{id}"  # noqa
    responses = {
        200: "OK.",  # noqa
        204: "No Messages.",  # noqa
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
async def post_v4_message_blast(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
    sids: List[str] = None,
    message: str = None,
    data: str = None,
    version: str = None,
    attachment: str = None,
    preview: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Post a new message to the given list of streams. The stream can be a chatroom,
    an IM or a multiparty IM.  You may include an attachment on the message.
    The message can be provided as MessageMLV2 or PresentationML. Both formats
    support Freemarker templates.  The optional parameter 'data' can be used to
    provide a JSON payload containing entity data. If the message contains
    explicit references to entity data (in 'data-entity-id' element attributes),
    this parameter is required.  If the message is in MessageML and fails schema
    validation a client error results  This endpoint is idempotent, it means
    that a 200 response will be returned even if the message has not been
    delivered to some streams. Check the `errors` map from the response in order
    to see on which stream(s) the message has not been delivered.  The maximum
    number of streams where the message can be sent is limitted to 100.
    Regarding authentication, you must either use the sessionToken which was
    created for delegated app access or both the sessionToken and
    keyManagerToken together.

    Args:
        session_token:
            Authorization token used to make delegated calls.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.
        sids:
            A comma-separated list of Stream IDs.
        message:
            The message payload in MessageML.
        data:
            Optional message data in EntityJSON.
        version:
            Optional message version in the format 'major.minor'. If empty, defaults
            to the latest supported version.
        attachment:
            Optional file attachment.
        preview:
            Optional attachment preview.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v4/message/blast`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Blast message sent. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 451 | Compliance Issues found in message or file. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v4/message/blast"  # noqa

    responses = {
        200: "Blast message sent.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        451: "Compliance Issues found in message or file.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    json_payload = {
        "sids": sids,
        "message": message,
        "data": data,
        "version": version,
        "attachment": attachment,
        "preview": preview,
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
async def post_v4_message_import(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Sends a message to be imported into the system. Allows you to override the
    timestamp and author of the message with your desired values. The requesting
    user must have the Content Management role. The user that the message is
    intended to have come from must also be present in the conversation. The
    intended message timestamp must be a valid time from the past. It cannot be
    a future timestamp. Optionally the original message ID can be specified to
    identify the imported message for the purpose of repeat imports.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v4/message/import`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Message sent. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v4/message/import"  # noqa

    responses = {
        200: "Message sent.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
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
async def get_v1_message_mid_status(
    mid: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the read status of a particular message.

    Args:
        mid:
            Mid used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/message/{mid}/status`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not found: The informed Message ID does not exist. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/message/{mid}/status"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not found: The informed Message ID does not exist.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "mid": mid,
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
