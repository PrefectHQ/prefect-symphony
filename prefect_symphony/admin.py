"""
This is a module containing tasks for interacting with:
Symphony admin
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: pod-api-public.yaml
# Updated at: 2022-09-07T03:04:07.518722

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def post_v1_admin_app_create(
    session_token: str,
    application_detail: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Creates a new app.

    Args:
        session_token:
            Session authentication token.
        application_detail:
            Application detail to create the app with.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/app/create`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/app/create"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "application_detail": application_detail,
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
async def get_v1_admin_app_entitlement_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the list of application entitlements for the company.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/app/entitlement/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/app/entitlement/list"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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
async def post_v1_admin_app_entitlement_list(
    session_token: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the application entitlements for the company.

    Args:
        session_token:
            Session authentication token.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/app/entitlement/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/app/entitlement/list"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "payload": payload,
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
async def post_v1_admin_app_id_delete(
    session_token: str,
    id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deletes a app.

    Args:
        session_token:
            Session authentication token.
        id:
            Id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/app/{id}/delete`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/app/{id}/delete"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
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
async def get_v1_admin_app_id_get(
    session_token: str,
    id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Gets a app.

    Args:
        session_token:
            Session authentication token.
        id:
            Id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/app/{id}/get`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/app/{id}/get"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
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
async def post_v1_admin_app_id_update(
    session_token: str,
    id: str,
    application_detail: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Updates a app.

    Args:
        session_token:
            Session authentication token.
        id:
            Id used in formatting the endpoint URL.
        application_detail:
            Details to update the app with.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/app/{id}/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/app/{id}/update"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "id": id,
        "application_detail": application_detail,
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
async def get_v1_admin_disclaimer_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    List all disclaimers for the company (pod).

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/disclaimer/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/disclaimer/list"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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
async def get_v1_admin_disclaimer_did(
    session_token: str,
    did: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get a disclaimer by disclaimer id.

    Args:
        session_token:
            Session authentication token.
        did:
            Did used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/disclaimer/{did}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/disclaimer/{did}"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "did": did,
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
async def get_v1_admin_disclaimer_did_users(
    session_token: str,
    did: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    List all users assigned to this disclaimer.

    Args:
        session_token:
            Session authentication token.
        did:
            Did used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/disclaimer/{did}/users`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/disclaimer/{did}/users"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "did": did,
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
async def get_v1_admin_group_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get a list of all Information Barrier Groups.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/group/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/group/list"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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
async def post_v1_admin_group_gid_membership_add(
    gid: str,
    session_token: str,
    users: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add members to an Information Barrier group.

    Args:
        gid:
            Gid used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        users:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/group/{gid}/membership/add`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/group/{gid}/membership/add"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "gid": gid,
        "session_token": session_token,
        "users": users,
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
async def get_v1_admin_group_gid_membership_list(
    gid: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the list of userids in this Information Barrier Group.

    Args:
        gid:
            Gid used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            Number of records to skip. Must be a positive integer.
        limit:
            Max number of records to return. Default is 10000. Must be a positive
            integer and must not exceed 10000.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/group/{gid}/membership/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: Group cannot be found. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/group/{gid}/membership/list"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: Group cannot be found.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "gid": gid,
        "session_token": session_token,
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
async def post_v1_admin_group_gid_membership_remove(
    gid: str,
    session_token: str,
    users: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Remove members from an Information Barrier group.

    Args:
        gid:
            Gid used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        users:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/group/{gid}/membership/remove`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/group/{gid}/membership/remove"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "gid": gid,
        "session_token": session_token,
        "users": users,
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
async def post_v1_admin_im_create(
    uid_list: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    At least two user IDs must be provided or an error response will be sent.  The
    caller is not included in the members of the created chat.  Duplicate users
    will be included in the membership of the chat but the duplication will be
    silently ignored.  If there is an existing IM conversation with the same set
    of participants then the id of that existing stream will be returned.

    Args:
        uid_list:
            List of (integer) User IDs of participants.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/im/create`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/im/create"  # noqa

    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "uid_list": uid_list,
        "session_token": session_token,
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
async def post_v1_admin_messages(
    session_token: str,
    message_ids: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Fetch message details.

    Args:
        session_token:
            Session authentication token.
        message_ids:
            the ids of the messages to be fetched.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/messages`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not found: Message ID could not be found. |
    | 422 | Unprocessable entity: Invalid message type. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/messages"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not found: Message ID could not be found.",  # noqa
        422: "Unprocessable entity: Invalid message type.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "message_ids": message_ids,
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
async def get_v1_admin_messages_message_id_metadata_relationships(  # noqa
    session_token: str,
    user_agent: str,
    message_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the message metadata relationship.

    Args:
        session_token:
            Session authentication token.
        user_agent:
            Request user agent.
        message_id:
            Message id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/messages/{message_id}/metadata/relationships`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Successful Operation. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/messages/{message_id}/metadata/relationships"  # noqa
    responses = {
        200: "Successful Operation.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "user_agent": user_agent,
        "message_id": message_id,
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
async def get_v1_admin_messages_message_id_receipts(
    session_token: str,
    message_id: str,
    symphony_credentials: "SymphonyCredentials",
    before: str = None,
    after: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Fetch receipts details from a specific message.

    Args:
        session_token:
            Session authentication token.
        message_id:
            Message id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        before:
            Returns results from an opaque “before” cursor value as presented via a
            response cursor.
        after:
            Returns results from an opaque “after” cursor value as presented via a
            response cursor.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/messages/{message_id}/receipts`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: Message receipt details cannot be found. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/messages/{message_id}/receipts"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: Message receipt details cannot be found.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "message_id": message_id,
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
async def post_v1_admin_messagesuppression_id_suppress(
    id: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Suppress a message.

    Args:
        id:
            Id used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/messagesuppression/{id}/suppress`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/messagesuppression/{id}/suppress"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "id": id,
        "session_token": session_token,
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
async def get_v1_admin_policy_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get all Information Policies.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/policy/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/policy/list"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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
async def post_v1_admin_room_id_membership_add(
    id: str,
    payload: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add a member to an existing room.

    Args:
        id:
            Id used in formatting the endpoint URL.
        payload:

        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/room/{id}/membership/add`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/room/{id}/membership/add"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "id": id,
        "payload": payload,
        "session_token": session_token,
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
async def get_v1_admin_room_id_membership_list(
    id: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    include_past_members: bool = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Lists current and previous members of an existing room.

    Args:
        id:
            Id used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        include_past_members:
            If true, the membership list will include past members of the stream. If
            false, the listing will only incude current members. Default
            false.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/room/{id}/membership/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/room/{id}/membership/list"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "id": id,
        "session_token": session_token,
        "include_past_members": include_past_members,
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
async def post_v1_admin_room_id_membership_remove(
    id: str,
    payload: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Remove a member from a room.

    Args:
        id:
            Id used in formatting the endpoint URL.
        payload:

        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/room/{id}/membership/remove`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/room/{id}/membership/remove"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "id": id,
        "payload": payload,
        "session_token": session_token,
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
async def post_v1_admin_room_id_set_active(
    id: str,
    active: bool,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deactivate or reactivate a chatroom via AC Portal.

    Args:
        id:
            Id used in formatting the endpoint URL.
        active:

        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/room/{id}/setActive`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/room/{id}/setActive"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "id": id,
        "active": active,
        "session_token": session_token,
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
async def get_v1_admin_stream_id_membership_list(
    id: str,
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List the current members of an existing stream.  The stream can be of type IM,
    MIM, or ROOM.

    Args:
        id:
            Id used in formatting the endpoint URL.
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            Number of items to skip. Default is 0.
        limit:
            Maximum number of items to return. Default is 100 and not to exceed
            1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/stream/{id}/membership/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/stream/{id}/membership/list"  # noqa
    responses = {
        200: "OK.",  # noqa
        400: "Client error.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "id": id,
        "session_token": session_token,
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
async def get_v1_admin_system_features_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the full set of Symphony features available for this pod.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/system/features/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The list of valid feature entitlement names. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/system/features/list"  # noqa

    responses = {
        200: "The list of valid feature entitlement names.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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
async def post_v1_admin_system_protocols(
    session_token: str,
    protocol: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add an entry to URI protocols supported by the company (pod).

    Args:
        session_token:
            Session authentication token.
        protocol:
            the protocol to add.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/system/protocols`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/system/protocols"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "protocol": protocol,
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
async def get_v1_admin_system_protocols_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get a list of all URI protocols supported by the company (pod).

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/system/protocols/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/system/protocols/list"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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
async def delete_v1_admin_system_protocols_scheme(
    session_token: str,
    scheme: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Remove an entry from URI protocols supported by the company (pod).

    Args:
        session_token:
            Session authentication token.
        scheme:
            Scheme used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/system/protocols/{scheme}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | 204 response. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/system/protocols/{scheme}"  # noqa
    responses = {
        204: "204 response.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "scheme": scheme,
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
async def get_v1_admin_system_roles_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get a list of all roles available in the company (pod).

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/system/roles/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/system/roles/list"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
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
async def post_v1_admin_user_find(
    session_token: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Find a user based on attributes.

    Args:
        session_token:
            Session authentication token.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            Number of users to skip. Default is 0. Must be a integer equals or
            bigger than 0.
        limit:
            Maximum number of users to return. Default is 100. Must be a positive
            integer and must not exceed 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/find`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/admin/user/find"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "skip": skip,
        "limit": limit,
        "payload": payload,
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
async def get_v1_admin_user_uid_app_entitlement_list(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the list of application entitlements for this user.

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
    `/v1/admin/user/{uid}/app/entitlement/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/app/entitlement/list"  # noqa
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
async def post_v1_admin_user_uid_app_entitlement_list(
    session_token: str,
    uid: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the application entitlements for this user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/{uid}/app/entitlement/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/app/entitlement/list"  # noqa
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
        "payload": payload,
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
async def patch_v1_admin_user_uid_app_entitlement_list(
    session_token: str,
    uid: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update unique entitlement of an app for this user. Entitlement can be
    installation, visibility or product.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/{uid}/app/entitlement/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/app/entitlement/list"  # noqa
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
        "payload": payload,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.PATCH,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def get_v1_admin_user_uid_avatar(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the URL of the avatar of a particular user.

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
    `/v1/admin/user/{uid}/avatar`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/avatar"  # noqa
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
async def post_v1_admin_user_uid_avatar_update(
    session_token: str,
    uid: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the avatar of a particular user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/{uid}/avatar/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/avatar/update"  # noqa
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
        "payload": payload,
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
async def get_v1_admin_user_uid_delegates(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the delegates assigned to a user.

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
    `/v1/admin/user/{uid}/delegates`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The userid's of the delegates of this user. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/delegates"  # noqa
    responses = {
        200: "The userid's of the delegates of this user.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "uid": uid,
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
async def post_v1_admin_user_uid_delegates_update(
    session_token: str,
    uid: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the delegates assigned to a user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/{uid}/delegates/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Sucesss. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/delegates/update"  # noqa
    responses = {
        200: "Sucesss.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "uid": uid,
        "payload": payload,
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
async def get_v1_admin_user_uid_disclaimer(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the disclaimer assigned to a user.

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
    `/v1/admin/user/{uid}/disclaimer`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 204 | No content. User doesn't have an assigned disclaimer. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/disclaimer"  # noqa
    responses = {
        200: "Success.",  # noqa
        204: "No content. User doesn't have an assigned disclaimer.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "uid": uid,
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
async def delete_v1_admin_user_uid_disclaimer(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Unassign a disclaimer from a user.

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
    `/v1/admin/user/{uid}/disclaimer`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/disclaimer"  # noqa
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
async def post_v1_admin_user_uid_disclaimer_update(
    session_token: str,
    uid: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Assign a disclaimer to a user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/{uid}/disclaimer/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/disclaimer/update"  # noqa
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
        "payload": payload,
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
async def get_v1_admin_user_uid_features(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the list of Symphony feature entitlements enabled for a particular user.

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
    `/v1/admin/user/{uid}/features`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/features"  # noqa
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
async def post_v1_admin_user_uid_features_update(
    session_token: str,
    uid: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the list of Symphony feature entitlements for a particular user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/{uid}/features/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/features/update"  # noqa
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
        "payload": payload,
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
async def post_v1_admin_user_uid_roles_add(
    session_token: str,
    uid: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Add a role to a user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/{uid}/roles/add`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/roles/add"  # noqa
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
        "payload": payload,
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
async def post_v1_admin_user_uid_roles_remove(
    session_token: str,
    uid: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Remove a role from a user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/{uid}/roles/remove`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Not Found: User cannot be found. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/roles/remove"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Not Found: User cannot be found.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "uid": uid,
        "payload": payload,
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
async def get_v1_admin_user_uid_status(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get the status, active or inactive, for a particular user.

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
    `/v1/admin/user/{uid}/status`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/status"  # noqa
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
async def post_v1_admin_user_uid_status_update(
    session_token: str,
    uid: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the status of a particular user.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/{uid}/status/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{uid}/status/update"  # noqa
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
        "payload": payload,
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
async def put_v1_admin_user_user_id_suspension_update(
    session_token: str,
    user_id: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the status of suspension of a particular user.

    Args:
        session_token:
            Session authentication token.
        user_id:
            User id used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/admin/user/{user_id}/suspension/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/admin/user/{user_id}/suspension/update"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "user_id": user_id,
        "payload": payload,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.PUT,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def post_v2_admin_streams_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
    filter: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieve all the streams across the enterprise where the membership of the
    stream has been modified between a given time range.

    Args:
        session_token:
            Session authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            Number of items to skip. Default is 0.
        limit:
            Maximum number of items to return. Default is 50.  This value cannot
            exceed 100.
        filter:
            Stream filtering criteria.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v2/admin/streams/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | OK. |
    | 400 | Client error. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v2/admin/streams/list"  # noqa

    responses = {
        200: "OK.",  # noqa
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
async def post_v2_admin_user_create(
    session_token: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create a new V2 User.

    Args:
        session_token:
            Session authentication token.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v2/admin/user/create`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v2/admin/user/create"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "payload": payload,
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
async def get_v2_admin_user_list(
    session_token: str,
    symphony_credentials: "SymphonyCredentials",
    skip: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieve a list of all users in the company (pod).

    Args:
        session_token:
            Session Authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        skip:
            Number of users to skip. Default is 0. Must be a integer equals or
            bigger than 0.
        limit:
            Maximum number of users to return. Default is 100. Must be a positive
            integer and must not exceed 1000.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v2/admin/user/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v2/admin/user/list"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
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
async def get_v2_admin_user_uid(
    session_token: str,
    uid: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retreive V2 User details for a particular user.

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
    `/v2/admin/user/{uid}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v2/admin/user/{uid}"  # noqa
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
async def post_v2_admin_user_uid_update(
    session_token: str,
    uid: str,
    payload: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update an existing V2 User.

    Args:
        session_token:
            Session authentication token.
        uid:
            Uid used in formatting the endpoint URL.
        payload:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v2/admin/user/{uid}/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v2/admin/user/{uid}/update"  # noqa
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
        "payload": payload,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.POST,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
