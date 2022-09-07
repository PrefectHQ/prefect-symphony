"""
This is a module containing tasks for interacting with:
Symphony channelco
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: community-connect-public-api.yaml
# Updated at: 2022-09-07T03:10:47.523727

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.models import channelco as models
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def get_user(
    user_id: str,
    company_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get channelco user by companyId and userId.

    Args:
        user_id:
            User id used in formatting the endpoint URL.
        company_id:
            Company id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/channelco/company/{company_id}/user/{user_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | body. |
    | 400 | Something was wrong about the request. |
    | 401 | Unauthorized request. |
    | 404 | The user do not exist. |
    """  # noqa
    endpoint = f"/v1/channelco/company/{company_id}/user/{user_id}"  # noqa
    responses = {
        200: "body.",  # noqa
        400: "Something was wrong about the request.",  # noqa
        401: "Unauthorized request.",  # noqa
        404: "The user do not exist.",  # noqa
    }

    params = {
        "user_id": user_id,
        "company_id": company_id,
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
async def update_user(
    user_id: str,
    company_id: str,
    symphony_credentials: "SymphonyCredentials",
    email: str = None,
    first_name: str = None,
    last_name: str = None,
    display_name: str = None,
    phone_number: str = None,
    department: str = None,
    title: str = None,
    location: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Update channelco user.

    Args:
        user_id:
            User id used in formatting the endpoint URL.
        company_id:
            Company id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        email:
            , e.g. `foo@example.com`.
        first_name:
            , e.g. `Paul`.
        last_name:
            , e.g. `Smith`.
        display_name:
            , e.g. `Paul Smith`.
        phone_number:
            , e.g. `33612345678`.
        department:
            , e.g. `Product Engineering`.
        title:
            , e.g. `Engineering manager`.
        location:
            country.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/channelco/company/{company_id}/user/{user_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | body. |
    | 400 | Something was wrong about the request. |
    | 401 | Unauthorized request. |
    | 404 | The user do not exist. |
    """  # noqa
    endpoint = f"/v1/channelco/company/{company_id}/user/{user_id}"  # noqa
    responses = {
        200: "body.",  # noqa
        400: "Something was wrong about the request.",  # noqa
        401: "Unauthorized request.",  # noqa
        404: "The user do not exist.",  # noqa
    }

    params = {
        "user_id": user_id,
        "company_id": company_id,
    }

    json_payload = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "display_name": display_name,
        "phone_number": phone_number,
        "department": department,
        "title": title,
        "location": location,
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
async def disable_user(
    user_id: str,
    company_id: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Disable channelco user.

    Args:
        user_id:
            User id used in formatting the endpoint URL.
        company_id:
            Company id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/channelco/company/{company_id}/user/{user_id}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | The user was disabled successfully. |
    | 400 | Something was wrong about the request. |
    | 401 | Unauthorized request. |
    | 404 | The user do not exist. |
    """  # noqa
    endpoint = f"/v1/channelco/company/{company_id}/user/{user_id}"  # noqa
    responses = {
        204: "The user was disabled successfully.",  # noqa
        400: "Something was wrong about the request.",  # noqa
        401: "Unauthorized request.",  # noqa
        404: "The user do not exist.",  # noqa
    }

    params = {
        "user_id": user_id,
        "company_id": company_id,
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
async def add_role(
    user_id: str,
    company_id: str,
    symphony_credentials: "SymphonyCredentials",
    id: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Adds a role to a channelco user's account.

    Args:
        user_id:
            User id used in formatting the endpoint URL.
        company_id:
            Company id used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        id:
            role Id, e.g. `COMPLIANCE_OFFICER`.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/channelco/company/{company_id}/user/{user_id}/roles/add`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | body. |
    | 400 | Something was wrong about the request. |
    | 401 | Unauthorized request. |
    | 404 | The user do not exist. |
    """  # noqa
    endpoint = f"/v1/channelco/company/{company_id}/user/{user_id}/roles/add"  # noqa
    responses = {
        200: "body.",  # noqa
        400: "Something was wrong about the request.",  # noqa
        401: "Unauthorized request.",  # noqa
        404: "The user do not exist.",  # noqa
    }

    params = {
        "user_id": user_id,
        "company_id": company_id,
    }

    json_payload = {
        "id": id,
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
async def search_user(
    email: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Search channelco user.

    Args:
        email:
            user's email, e.g. `user@comcocompany.com`.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/channelco/user`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | body. |
    | 400 | Something was wrong about the request. |
    | 401 | Unauthorized request. |
    | 404 | The user do not exist. |
    """  # noqa
    endpoint = "/v1/channelco/user"  # noqa

    responses = {
        200: "body.",  # noqa
        400: "Something was wrong about the request.",  # noqa
        401: "Unauthorized request.",  # noqa
        404: "The user do not exist.",  # noqa
    }

    params = {
        "email": email,
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
async def create_user(
    symphony_credentials: "SymphonyCredentials",
    company_name: str = None,
    users: List["models.ChannelCoUserRequest"] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create channelco user.

    Args:
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        company_name:
            This field is mandatory only if a company with same domain (taken from
            email) does not exist yet, e.g. `Symphony`.
        users:


    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/channelco/user`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | body. |
    | 400 | Something was wrong about the request. |
    | 401 | Unauthorized request. |
    """  # noqa
    endpoint = "/v1/channelco/user"  # noqa

    responses = {
        201: "body.",  # noqa
        400: "Something was wrong about the request.",  # noqa
        401: "Unauthorized request.",  # noqa
    }

    json_payload = {
        "company_name": company_name,
        "users": users,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.POST,
        json=json_payload,
    )

    contents = _unpack_contents(response, responses)
    return contents
