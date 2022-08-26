"""
This is a module containing tasks for interacting with:
Symphony file_ext
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: pod-api-public.yaml
# Updated at: 2022-08-26T18:55:04.205021

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def list_allowed_file_extensions(
    symphony_credentials: "SymphonyCredentials",
    limit: int = None,
    before: str = None,
    after: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Provides a RESTful API to iterate all file extensions configured by the tenant
    admin that are allowed for the upload.  Pagination of this list is managed
    through a combination of the optional request parameters and service-side
    managed maximums.  Pagination of the results is provided through the before
    or after input paramters and presented through the opaque cursor values
    provided as output from a previous response.  Only one of before or after or
    neither may be provided.  DO NOT store cursors. Cursors can quickly become
    invalid if items are added or deleted. Use them only during a short-period
    of time that you are traversing the list.

    Args:
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        limit:
            This is the maximum number of objects that may be returned. A query may
            return fewer than the value of limit due to filtering or
            service-side maximums. Do not depend on the number of
            results being fewer than the limit value to indicate your
            query reached the end of the list of data, use the absence
            of next instead as described below. For example, if you set
            limit to 10 and 9 results are returned, there may be more
            data available, but one item was removed due to privacy
            filtering. Some maximums for limit may be enforced for
            performance reasons. In all cases, the API returns the
            correct pagination links.
        before:
            Returns results from an opaque 'before' cursor value as presented via a
            response cursor.
        after:
            Returns results from an opaque 'after' cursor value as presented via a
            response cursor.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/file_ext/v1/allowed_extensions`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Requested sequence of file extensions object records with the page size limited    by the optional limit paramter or the service-specific maximum limit    offered. |
    | 400 | Invalid arguments were passed by the client. |
    | 401 | Authentication was not provided. |
    | 403 | Authorization is not provided to this request. |
    | 500 | Unexpected service error - a retry may work. |
    | 503 | Temporarily unable to handle request - could be due to service overload or    maintenance. |
    | 504 | Timeout waiting on response at gateway. |
    """  # noqa
    endpoint = "/file_ext/v1/allowed_extensions"  # noqa

    responses = {
        200: (  # noqa
            "Requested sequence of file extensions object records with the page size"
            " limited    by the optional limit paramter or the service-specific maximum"
            " limit    offered."
        ),
        400: "Invalid arguments were passed by the client.",  # noqa
        401: "Authentication was not provided.",  # noqa
        403: "Authorization is not provided to this request.",  # noqa
        500: "Unexpected service error - a retry may work.",  # noqa
        503: (  # noqa
            "Temporarily unable to handle request - could be due to service overload or"
            "    maintenance."
        ),
        504: "Timeout waiting on response at gateway.",  # noqa
    }

    params = {
        "limit": limit,
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
async def put_allowed_file_extension(
    session_token: str,
    extension: str,
    v3_file_extension: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Provides a method to create or replace a specific file extension configured for
    upload support via an admin. The API treats the file extension in the path
    case-insensitively by converting it to lowecase.

    Args:
        session_token:
            Session authentication token.
        extension:
            Extension used in formatting the endpoint URL.
        v3_file_extension:

        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/file_ext/v1/allowed_extensions/{extension}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | 200 response. |
    | 400 | Invalid arguments were passed by the client: the file extension object specified    the source as 'system' yet the file extension is not known to the system    (API cannot create system file extensions, only customer-defined file    extensions), the extension in the path doesn't match the extension in the    body, the length of the file extension exceeded the maximum length (64    characters). |
    | 403 | Authorization is not provided to this request. |
    | 500 | Unexpected service error - a retry may work. |
    """  # noqa
    endpoint = f"/file_ext/v1/allowed_extensions/{extension}"  # noqa
    responses = {
        200: "200 response.",  # noqa
        400: (  # noqa
            "Invalid arguments were passed by the client: the file extension object"
            " specified    the source as 'system' yet the file extension is not known"
            " to the system    (API cannot create system file extensions, only"
            " customer-defined file    extensions), the extension in the path doesn't"
            " match the extension in the    body, the length of the file extension"
            " exceeded the maximum length (64    characters)."
        ),
        403: "Authorization is not provided to this request.",  # noqa
        500: "Unexpected service error - a retry may work.",  # noqa
    }

    params = {
        "session_token": session_token,
        "extension": extension,
        "v3_file_extension": v3_file_extension,
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
async def delete_allowed_file_extension(
    session_token: str,
    extension: str,
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Provides a method to delete a specific file extension configured for upload
    support via an admin. The file extension identifying the resource is treated
    case-insensitively by the API.

    Args:
        session_token:
            Session authentication token.
        extension:
            Extension used in formatting the endpoint URL.
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/file_ext/v1/allowed_extensions/{extension}`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | 204 response. |
    | 400 | Invalid arguments were passed by the client. |
    | 403 | Authorization is not provided to this request. |
    | 500 | Unexpected service error - a retry may work. |
    """  # noqa
    endpoint = f"/file_ext/v1/allowed_extensions/{extension}"  # noqa
    responses = {
        204: "204 response.",  # noqa
        400: "Invalid arguments were passed by the client.",  # noqa
        403: "Authorization is not provided to this request.",  # noqa
        500: "Unexpected service error - a retry may work.",  # noqa
    }

    params = {
        "session_token": session_token,
        "extension": extension,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
