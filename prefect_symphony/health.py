"""
This is a module containing tasks for interacting with:
Symphony health
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: agent-api-public.yaml
# Updated at: 2022-09-07T03:04:02.203014

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def v3_health(
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    _Available on Agent 2.57.0 and above._  Returns the connectivity status of your
    Agent server. If your Agent server is started and running, the status value
    will be `UP`.

    Args:
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/health`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Agent application is alive. |
    """  # noqa
    endpoint = "/v3/health"  # noqa

    responses = {
        200: "Agent application is alive.",  # noqa
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.GET,
    )

    contents = _unpack_contents(response, responses)
    return contents


@task
async def v3_extended_health(
    symphony_credentials: "SymphonyCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    _Available on Agent 2.57.0 and above._  Returns the connectivity status of the
    Agent services (**pod**, **key manager** and **datafeed**) as well as users
    connectivity (**agentservice** and **ceservice**).  The global status will
    be set to `DOWN` if at least one of the sub-status is also `DOWN`.

    Args:
        symphony_credentials:
            Credentials to use for authentication with Symphony.

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v3/health/extended`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Agent is healthy, all components are `UP`. |
    | 503 | Agent is unhealthy, some components are `DOWN`. |
    """  # noqa
    endpoint = "/v3/health/extended"  # noqa

    responses = {
        200: "Agent is healthy, all components are `UP`.",  # noqa
        503: "Agent is unhealthy, some components are `DOWN`.",  # noqa
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.GET,
    )

    contents = _unpack_contents(response, responses)
    return contents
