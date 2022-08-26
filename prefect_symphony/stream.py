"""
This is a module containing tasks for interacting with:
Symphony stream
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: agent-api-public.yaml
# Updated at: 2022-08-26T18:55:00.242184

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def get_v1_stream_sid_attachment(
    sid: str,
    file_id: str,
    message_id: str,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Downloads the attachment body by the attachment ID, stream ID, and message ID.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        file_id:
            The attachment ID (Base64-encoded).
        message_id:
            The ID of the message containing the attachment.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/stream/{sid}/attachment`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Attachment body as Base64 encoded string. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/stream/{sid}/attachment"  # noqa
    responses = {
        200: "Attachment body as Base64 encoded string.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "sid": sid,
        "file_id": file_id,
        "message_id": message_id,
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
async def post_v3_stream_sid_share(
    sid: str,
    session_token: str,
    share_content: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Given a 3rd party content (eg. news article), it can share to the given stream.
    The stream can be a chatroom, an IM or a multiparty IM.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        share_content:

        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/stream/{sid}/share`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v3/stream/{sid}/share"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "sid": sid,
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "share_content": share_content,
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
async def get_v4_stream_sid_message(
    sid: str,
    since: int,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    A caller can fetch all unseen messages by passing the timestamp of the last
    message seen as the since parameter and the number of messages with the same
    timestamp value already seen as the skip parameter. This means that every
    message will be seen exactly once even in the case that an additional
    message is processed with the same timestamp as the last message returned by
    the previous call, and the case where there are more than maxMessages with
    the same timestamp value.  This method is intended for historic queries and
    is generally reliable but if guaranteed delivery of every message in real
    time is required then the equivilent firehose method should be called.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        since:
            Timestamp of first required message.  This is a long integer value
            representing milliseconds since Jan 1 1970.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            No. of messages to skip.
        limit:
            Max No. of messages to return. If no value is provided, 50 is the
            default. The maximum supported value is 500.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v4/stream/{sid}/message`

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
    endpoint = f"/v4/stream/{sid}/message"  # noqa
    responses = {
        200: "OK.",  # noqa
        204: "No Messages.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "sid": sid,
        "since": since,
        "skip": skip,
        "limit": limit,
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
async def post_v4_stream_sid_message_create(
    sid: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
    message: str = None,
    data: str = None,
    version: str = None,
    attachment: str = None,
    preview: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Post a new message to the given stream. The stream can be a chatroom, an IM or a
    multiparty IM.  You may include an attachment on the message.  The message
    can be provided as MessageMLV2 or PresentationML. Both formats support
    Freemarker templates.  The optional parameter 'data' can be used to provide
    a JSON payload containing entity data. If the message contains explicit
    references to entity data (in 'data-entity-id' element attributes), this
    parameter is required.  If the message is in MessageML and fails schema
    validation a client error results  If the message is sent then 200 is
    returned.  Regarding authentication, you must either use the sessionToken
    which was created for delegated app access or both the sessionToken and
    keyManagerToken together.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        session_token:
            Authorization token used to make delegated calls.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.
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
    `/v4/stream/{sid}/message/create`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Message sent. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 451 | Compliance Issues found in message or file. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v4/stream/{sid}/message/create"  # noqa
    responses = {
        200: "Message sent.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        451: "Compliance Issues found in message or file.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "sid": sid,
        "session_token": session_token,
        "key_manager_token": key_manager_token,
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
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def post_v4_stream_sid_message_mid_update(
    sid: str,
    mid: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    key_manager_token: str = None,
    message: str = None,
    data: str = None,
    version: str = None,
    silent: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update an existing message. The existing message must be a valid social message,
    that has not been deleted.  The message can be provided as MessageMLV2 or
    PresentationML. Both formats support Freemarker templates.  The optional
    parameter 'data' can be used to provide a JSON payload containing entity
    data. If the message contains explicit references to entity data (in 'data-
    entity-id' element attributes), this parameter is required.  If the message
    is in MessageML and fails schema validation a client error results  If the
    message is updated then 200 is returned.  Regarding authentication, you must
    either use the sessionToken which was created for delegated app access or
    both the sessionToken and keyManagerToken together.

    Args:
        sid:
            Sid used in formatting the endpoint URL.
        mid:
            Mid used in formatting the endpoint URL.
        session_token:
            Authorization token used to make delegated calls.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        key_manager_token:
            Key Manager authentication token.
        message:
            The message payload in MessageML.
        data:
            Optional message data in EntityJSON.
        version:
            Optional message version in the format 'major.minor'. If empty, defaults
            to the latest supported version.
        silent:
            Optional boolean field that will determine if the user/s should receive
            the message as read or not (true by default). Since Agent
            20.14.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v4/stream/{sid}/message/{mid}/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Message sent. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 451 | Compliance Issues found in message or file. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v4/stream/{sid}/message/{mid}/update"  # noqa
    responses = {
        200: "Message sent.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        451: "Compliance Issues found in message or file.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "sid": sid,
        "mid": mid,
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "message": message,
        "data": data,
        "version": version,
        "silent": silent,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.POST,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
