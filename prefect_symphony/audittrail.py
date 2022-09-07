"""
This is a module containing tasks for interacting with:
Symphony audittrail
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: agent-api-public.yaml
# Updated at: 2022-09-07T03:10:44.714351

from typing import Any, Dict, List, Union  # noqa

from prefect import task

from prefect_symphony import SymphonyCredentials
from prefect_symphony.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def get_v1_audittrail_privilegeduser(
    session_token: str,
    key_manager_token: str,
    start_timestamp: int,
    symphony_credentials: "SymphonyCredentials",
    end_timestamp: int = None,
    before: str = None,
    after: str = None,
    limit: int = None,
    initiator_id: int = None,
    role: str = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Get a list of actions performed by a privileged account acting as privileged
    user given a period of time.

    Args:
        session_token:
            Session authentication token.
        key_manager_token:
            Key Manager authentication token.
        start_timestamp:
            Start timestamp in unix timestamp in millseconds.
        symphony_credentials:
            Credentials to use for authentication with Symphony.
        end_timestamp:
            End timestamp in unix timestamp in millseconds. If not specified, it
            assumes to be current time.
        before:
            Return results from an opaque “before” cursor value as presented via a
            response cursor.
        after:
            Return results from an opaque “after” cursor value as presented via a
            response cursor.
        limit:
            Max No. of violations to return. If no value is provided, 50 is the
            default. Some maximums for limit may be enforced for
            performance reasons. The maximum supported value is 500.
        initiator_id:
            If present, only the initiator with this initiator <user id> will be
            returned.
        role:
            If present, only the audit trail initiated by s user with privileged
            role acting as privileged user will be returned. Privileged
            eliglible roles: User Provisioning (USER_PROVISIONING),
            Content Management (CONTENT_MANAGEMENT), Expression Filter
            Policy Management (EF_POLICY_MANAGEMENT), SCO
            (SUPER_COMPLIANCE_OFFICER), CO (COMPLIANCE_OFFICER), Super
            admin (SUPER_ADMINISTRATOR), Admin (ADMINISTRATOR), L1
            (L1_SUPPORT), L2 (L2_SUPPORT), Scope Manager
            (SCOPE_MANAGEMENT).

    Returns:
        A dict of the response.

    <h4>API Endpoint:</h4>
    `/v1/audittrail/privilegeduser`

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
    endpoint = "/v1/audittrail/privilegeduser"  # noqa

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
        "start_timestamp": start_timestamp,
        "end_timestamp": end_timestamp,
        "before": before,
        "after": after,
        "limit": limit,
        "initiator_id": initiator_id,
        "role": role,
    }

    response = await execute_endpoint.fn(
        endpoint,
        symphony_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
