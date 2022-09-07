"""
This is a module containing tasks for interacting with:
Symphony dlp
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: agent-api-public.yaml
# Updated at: 2022-09-07T03:04:01.819044

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.models import dlp as models
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def get_v1_dlp_dictionaries(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    page: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get all dictionary metadatas with the latest version. Each dictionary object
    will only contain meta data of the content.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        page:
            Optional parameter to specify which page to return (default is 0).
        limit:
            Optional parameter to specify the number of result to return per page,
            default is 50. Maximum is 50.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/dictionaries`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/dlp/dictionaries"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "page": page,
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
async def post_v1_dlp_dictionaries(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    name: str = None,
    type: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Creates a dictionary with basic metadata and no content. Only 'name' and 'type'
    field is used to create a new dictionary entry.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        name:
            The name of dictionary.
        type:
            The type of dictionary, which specify the content is a list of words or
            a list of regexes. By default set to 'Word' if not
            specified. Possible values - Word, Regex.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/dictionaries`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/dlp/dictionaries"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    json_payload = {
        "name": name,
        "type": type,
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
async def get_v1_dlp_dictionaries_dict_id(
    session_token: str,
    key_manager_token: str,
    dict_id: str,
    symphony_credentials: "SymphonyCredentials",
    dict_version: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get basic information for a dictionary.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        dict_id:
            Dict id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        dict_version:
            If set to be valid dictionary version number, will return dictionary
            metadata with specified version.  Otherwise, return the
            latest dictionary metadata.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/dictionaries/{dict_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/dlp/dictionaries/{dict_id}"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "dict_id": dict_id,
        "dict_version": dict_version,
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
async def put_v1_dlp_dictionaries_dict_id(
    session_token: str,
    key_manager_token: str,
    dict_id: str,
    symphony_credentials: "SymphonyCredentials",
    name: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Updates the dictionary's basic metadata without content. This API cannot be used
    for creating a new dictionary. In case of update only 'name' can be changed.
    Note: All related policies will also have versions updated.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        dict_id:
            Dict id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        name:
            The name of dictionary.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/dictionaries/{dict_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/dlp/dictionaries/{dict_id}"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "dict_id": dict_id,
    }

    json_payload = {
        "name": name,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.PUT,
        params=params,
        json=json_payload,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def delete_v1_dlp_dictionaries_dict_id(
    session_token: str,
    key_manager_token: str,
    dict_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deletes a dictionary. Note: All related policies will be affected.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        dict_id:
            Dict id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/dictionaries/{dict_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/dlp/dictionaries/{dict_id}"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "dict_id": dict_id,
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
async def get_v1_dlp_dictionaries_dict_id_data_download(
    session_token: str,
    key_manager_token: str,
    dict_id: str,
    symphony_credentials: "SymphonyCredentials",
    dict_version: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Downloads Base 64 encoded dictionary content.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        dict_id:
            Dict id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        dict_version:
            If set to be valid dictionary version number, will return dictionary
            with specified version.  Otherwise, return the latest
            dictionary.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/dictionaries/{dict_id}/data/download`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Attachment body as Base64 encoded string. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/dlp/dictionaries/{dict_id}/data/download"  # noqa
    responses = {
        200: "Attachment body as Base64 encoded string.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "dict_id": dict_id,
        "dict_version": dict_version,
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
async def post_v1_dlp_dictionaries_dict_id_data_upload(
    session_token: str,
    key_manager_token: str,
    dict_id: str,
    symphony_credentials: "SymphonyCredentials",
    data: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Override dictionary content with provided content.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        dict_id:
            Dict id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        data:


    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/dictionaries/{dict_id}/data/upload`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/dlp/dictionaries/{dict_id}/data/upload"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "dict_id": dict_id,
    }

    json_payload = {
        "data": data,
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
async def get_v1_dlp_policies(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    page: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get all policies.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        page:
            Optional parameter to specify which page to return (default is 0).
        limit:
            Optional parameter to specify the number of result to return per page,
            default is 50. Maximum is 50.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/policies`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/dlp/policies"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "page": page,
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
async def post_v1_dlp_policies(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    content_types: List[str] = None,
    dictionary_ids: List[str] = None,
    name: str = None,
    scopes: List[str] = None,
    type: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Creates a new policy with dictionary references.  At the time of policy
    creation, the caller should only provide - contentTypes, name, scopes and
    type. The rest of the information is populated automatically.  Note - You
    need to enable the policy after creation to start enforcing the policy.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        content_types:
            The list of content types that policy should apply to. Cannot be empty.
            Policy content types could be either of 'Messages',
            'RoomMeta', 'SignalMeta'. Default is set to ['Messages'] if
            not specified.
        dictionary_ids:
            List of dictionaries Ids for the policy.
        name:
            Unique name of a policy, max 30 characters. Cannot be empty. All the
            leading and trailing blank spaces are trimmed.
        scopes:
            List of communication scopes. Possible values are 'Internal' (for
            Internal conversations) or 'External' (for External
            conversations). You can apply both scopes if you set it to
            ['Internal', 'External'].
        type:
            Type of policy. Possible values 'Block' or 'Warn'.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/policies`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v1/dlp/policies"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    json_payload = {
        "content_types": content_types,
        "dictionary_ids": dictionary_ids,
        "name": name,
        "scopes": scopes,
        "type": type,
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
async def get_v1_dlp_policies_policy_id(
    session_token: str,
    key_manager_token: str,
    policy_id: str,
    symphony_credentials: "SymphonyCredentials",
    policy_version: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get a policy.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        policy_id:
            Policy id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        policy_version:
            Optional parameter, if set to be valid policy version number,  will
            return policy with specified policyVersion.  Otherwise,
            return the latest policy.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/policies/{policy_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/dlp/policies/{policy_id}"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "policy_id": policy_id,
        "policy_version": policy_version,
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
async def put_v1_dlp_policies_policy_id(
    session_token: str,
    key_manager_token: str,
    policy_id: str,
    symphony_credentials: "SymphonyCredentials",
    content_types: List[str] = None,
    dictionary_ids: List[str] = None,
    name: str = None,
    scopes: List[str] = None,
    type: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the policy (name, type, contentTypes, scopes) and also the dictionaries
    for a policy. Warning: If you send empty list of dictionaries during the
    update operation, then all the dictionaries for this policy are deleted and
    policy is automatically disabled. Note: The policy should already exist.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        policy_id:
            Policy id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        content_types:
            The list of content types that policy should apply to. Cannot be empty.
            Policy content types could be either of 'Messages',
            'RoomMeta', 'SignalMeta'. Default is set to ['Messages'] if
            not specified.
        dictionary_ids:
            List of dictionaries Ids for the policy.
        name:
            Unique name of a policy, max 30 characters. Cannot be empty. All the
            leading and trailing blank spaces are trimmed.
        scopes:
            List of communication scopes. Possible values are 'Internal' (for
            Internal conversations) or 'External' (for External
            conversations). You can apply both scopes if you set it to
            ['Internal', 'External'].
        type:
            Type of policy. Possible values 'Block' or 'Warn'.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/policies/{policy_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/dlp/policies/{policy_id}"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "policy_id": policy_id,
    }

    json_payload = {
        "content_types": content_types,
        "dictionary_ids": dictionary_ids,
        "name": name,
        "scopes": scopes,
        "type": type,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.PUT,
        params=params,
        json=json_payload,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def delete_v1_dlp_policies_policy_id(
    session_token: str,
    key_manager_token: str,
    policy_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete a policy. Note: Only disabled policy can be deleted.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        policy_id:
            Policy id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/policies/{policy_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/dlp/policies/{policy_id}"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "policy_id": policy_id,
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
async def post_v1_dlp_policies_policy_id_disable(
    session_token: str,
    key_manager_token: str,
    policy_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Disables a policy.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        policy_id:
            Policy id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/policies/{policy_id}/disable`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/dlp/policies/{policy_id}/disable"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "policy_id": policy_id,
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
async def post_v1_dlp_policies_policy_id_enable(
    session_token: str,
    key_manager_token: str,
    policy_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Enables a policy.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        policy_id:
            Policy id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/policies/{policy_id}/enable`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v1/dlp/policies/{policy_id}/enable"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "policy_id": policy_id,
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
async def get_v1_dlp_violations_message(
    start_time: int,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    end_time: int = None,
    next: str = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get violations as a result of policy enforcement on messages.

    Args:
        start_time:
            Timestamp of the first required violation. This is a long integer value
            representing milliseconds since Jan 1 1970.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        end_time:
            Timestamp of the last required violation. This is a long integer value
            representing milliseconds since Jan 1 1970 If unspecified,
            it will default to current time of the request.
        next:
            Offset of the next chunk of violations. Value is null for the first
            request.
        limit:
            Max No. of violations to return. If no value is provided, 50 is the
            default. The maximum supported value is 500.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/violations/message`

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
    endpoint = "/v1/dlp/violations/message"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "No Messages.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "next": next,
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
async def get_v1_dlp_violations_signal(
    start_time: int,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    end_time: int = None,
    next: str = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get violations as a result of policy enforcement on signals.

    Args:
        start_time:
            Timestamp of the first required violation. This is a long integer value
            representing milliseconds since Jan 1 1970.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        end_time:
            Timestamp of the last required violation. This is a long integer value
            representing milliseconds since Jan 1 1970 If unspecified,
            it will default to current time of the request.
        next:
            Offset of the next chunk of violations. Value is null for the first
            request.
        limit:
            Max No. of violations to return. If no value is provided, 50 is the
            default. The maximum supported value is 500.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/violations/signal`

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
    endpoint = "/v1/dlp/violations/signal"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "No Messages.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "next": next,
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
async def get_v1_dlp_violations_stream(
    start_time: int,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    end_time: int = None,
    next: str = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get violations as a result of policy enforcement on streams.

    Args:
        start_time:
            Timestamp of the first required violation. This is a long integer value
            representing milliseconds since Jan 1 1970.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        end_time:
            Timestamp of the last required violation. This is a long integer value
            representing milliseconds since Jan 1 1970 If unspecified,
            it will default to current time of the request.
        next:
            Offset of the next chunk of violations. Value is null for the first
            request.
        limit:
            Max No. of violations to return. If no value is provided, 50 is the
            default. The maximum supported value is 500.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/dlp/violations/stream`

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
    endpoint = "/v1/dlp/violations/stream"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "No Messages.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "next": next,
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
async def get_v3_dlp_policies(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    page: int = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get all policies.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        page:
            Optional parameter to specify which page to return (default is 0).
        limit:
            Optional parameter to specify the number of result to return per page,
            default is 50. Maximum is 50.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/policies`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v3/dlp/policies"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "page": page,
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
async def post_v3_dlp_policies(
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    name: str = None,
    scopes: List[str] = None,
    applies_to: List["models.V3DLPPolicyAppliesTo"] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Creates a new policy with dictionary references. At the time of policy creation,
    the caller should only provide - contentTypes, name, scopes and type. The
    rest of the information is populated automatically. Note - You need to
    enable the policy after creation to start enforcing the policy.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        name:
            Unique name of a policy, max 30 characters. Cannot be empty. All the
            leading and trailing blank spaces are trimmed.
        scopes:
            List of communication scopes. Possible values are 'Internal' (for
            Internal conversations) or 'External' (for External
            conversations). You can apply both scopes if you set it to
            ['Internal', 'External'].
        applies_to:


    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/policies`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v3/dlp/policies"  # noqa

    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
    }

    json_payload = {
        "name": name,
        "scopes": scopes,
        "applies_to": applies_to,
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
async def get_v3_dlp_policies_policy_id(
    session_token: str,
    key_manager_token: str,
    policy_id: str,
    symphony_credentials: "SymphonyCredentials",
    policy_version: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get a policy.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        policy_id:
            Policy id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        policy_version:
            Optional parameter, if set to be valid policy version number,  will
            return policy with specified policyVersion.  Otherwise,
            return the latest policy.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/policies/{policy_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v3/dlp/policies/{policy_id}"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "policy_id": policy_id,
        "policy_version": policy_version,
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
async def post_v3_dlp_policies_policy_id_delete(
    session_token: str,
    key_manager_token: str,
    policy_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Delete a policy. Note: Only disabled policy can be deleted.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        policy_id:
            Policy id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/policies/{policy_id}/delete`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v3/dlp/policies/{policy_id}/delete"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "policy_id": policy_id,
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
async def post_v3_dlp_policies_policy_id_disable(
    session_token: str,
    key_manager_token: str,
    policy_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Disables a policy.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        policy_id:
            Policy id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/policies/{policy_id}/disable`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v3/dlp/policies/{policy_id}/disable"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "policy_id": policy_id,
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
async def post_v3_dlp_policies_policy_id_enable(
    session_token: str,
    key_manager_token: str,
    policy_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Enables a policy.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        policy_id:
            Policy id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/policies/{policy_id}/enable`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v3/dlp/policies/{policy_id}/enable"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "policy_id": policy_id,
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
async def post_v3_dlp_policies_policy_id_update(
    session_token: str,
    key_manager_token: str,
    policy_id: str,
    symphony_credentials: "SymphonyCredentials",
    name: str = None,
    scopes: List[str] = None,
    applies_to: List["models.V3DLPPolicyAppliesTo"] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update the policy (name, type, contentTypes, scopes) and also the dictionaries
    for a policy. Warning: If you send empty list of dictionaries during the
    update operation, then all the dictionaries for this policy are deleted and
    policy is automatically disabled. Note: The policy should already exist.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        policy_id:
            Policy id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        name:
            Unique name of a policy, max 30 characters. Cannot be empty. All the
            leading and trailing blank spaces are trimmed.
        scopes:
            List of communication scopes. Possible values are 'Internal' (for
            Internal conversations) or 'External' (for External
            conversations). You can apply both scopes if you set it to
            ['Internal', 'External'].
        applies_to:


    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/policies/{policy_id}/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Success. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = f"/v3/dlp/policies/{policy_id}/update"  # noqa
    responses = {
        200: "Success.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "session_token": session_token,
        "key_manager_token": key_manager_token,
        "policy_id": policy_id,
    }

    json_payload = {
        "name": name,
        "scopes": scopes,
        "applies_to": applies_to,
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
async def get_v3_dlp_violation_attachment(
    file_id: str,
    violation_id: str,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieves attachments from related message violations as a base64 encoded
    String.

    Args:
        file_id:
            ID of attachment that will be downloaded.
        violation_id:
            ID of violation that corresponds to the flagged message that contains
            the attachment.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/violation/attachment`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Attachment body as Base64 encoded string. |
    | 400 | Client error, see response body for further details. |
    | 401 | Unauthorized: Session tokens invalid. |
    | 403 | Forbidden: Caller lacks necessary entitlement. |
    | 404 | Resource not found. |
    | 500 | Server error, see response body for further details. |
    """  # noqa
    endpoint = "/v3/dlp/violation/attachment"  # noqa

    responses = {
        200: "Attachment body as Base64 encoded string.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        404: "Resource not found.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "file_id": file_id,
        "violation_id": violation_id,
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
async def get_v3_dlp_violations_message(
    start_time: int,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    end_time: int = None,
    next: str = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieves DLP v3 message related violations for a given time range.

    Args:
        start_time:
            Timestamp of the first required violation. This is a long integer value
            representing milliseconds since Jan 1 1970.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        end_time:
            Timestamp of the last required violation. This is a long integer value
            representing milliseconds since Jan 1 1970 If unspecified,
            it will default to current time of the request.
        next:
            Offset of the next chunk of violations. Value is null for the first
            request.
        limit:
            Max No. of violations to return. If no value is provided, 50 is the
            default. The maximum supported value is 500.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/violations/message`

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
    endpoint = "/v3/dlp/violations/message"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "No Messages.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "next": next,
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
async def get_v3_dlp_violations_signal(
    start_time: int,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    end_time: int = None,
    next: str = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieves DLP v3 signal related violations for a given time range.

    Args:
        start_time:
            Timestamp of the first required violation. This is a long integer value
            representing milliseconds since Jan 1 1970.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        end_time:
            Timestamp of the last required violation. This is a long integer value
            representing milliseconds since Jan 1 1970 If unspecified,
            it will default to current time of the request.
        next:
            Offset of the next chunk of violations. Value is null for the first
            request.
        limit:
            Max No. of violations to return. If no value is provided, 50 is the
            default. The maximum supported value is 500.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/violations/signal`

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
    endpoint = "/v3/dlp/violations/signal"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "No Messages.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "next": next,
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
async def get_v3_dlp_violations_stream(
    start_time: int,
    session_token: str,
    key_manager_token: str,
    symphony_credentials: "SymphonyCredentials",
    end_time: int = None,
    next: str = None,
    limit: int = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieves DLP v3 signal related violations for a given time range.

    Args:
        start_time:
            Timestamp of the first required violation. This is a long integer value
            representing milliseconds since Jan 1 1970.
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        end_time:
            Timestamp of the last required violation. This is a long integer value
            representing milliseconds since Jan 1 1970 If unspecified,
            it will default to current time of the request.
        next:
            Offset of the next chunk of violations. Value is null for the first
            request.
        limit:
            Max No. of violations to return. If no value is provided, 50 is the
            default. The maximum supported value is 500.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/dlp/violations/stream`

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
    endpoint = "/v3/dlp/violations/stream"  # noqa

    responses = {
        200: "OK.",  # noqa
        204: "No Messages.",  # noqa
        400: "Client error, see response body for further details.",  # noqa
        401: "Unauthorized: Session tokens invalid.",  # noqa
        403: "Forbidden: Caller lacks necessary entitlement.",  # noqa
        500: "Server error, see response body for further details.",  # noqa
    }

    params = {
        "start_time": start_time,
        "end_time": end_time,
        "next": next,
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
