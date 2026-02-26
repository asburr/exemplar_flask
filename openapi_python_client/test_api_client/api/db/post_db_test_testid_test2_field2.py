from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.test_2_post_request_json import Test2PostRequestJson
from ...models.test_2_post_response import Test2PostResponse
from ...types import Response


def _get_kwargs(
    testid: str,
    field2: str,
    *,
    body: Test2PostRequestJson,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/db/test/{testid}/test2/{field2}".format(
            testid=quote(str(testid), safe=""),
            field2=quote(str(field2), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Test2PostResponse:
    if response.status_code == 200:
        response_200 = Test2PostResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Test2PostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    testid: str,
    field2: str,
    *,
    client: AuthenticatedClient | Client,
    body: Test2PostRequestJson,
) -> Response[Error | Test2PostResponse]:
    """Add row to test2 with foreign key to test.

    Args:
        testid (str):
        field2 (str):
        body (Test2PostRequestJson):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Test2PostResponse]
    """

    kwargs = _get_kwargs(
        testid=testid,
        field2=field2,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    testid: str,
    field2: str,
    *,
    client: AuthenticatedClient | Client,
    body: Test2PostRequestJson,
) -> Error | Test2PostResponse | None:
    """Add row to test2 with foreign key to test.

    Args:
        testid (str):
        field2 (str):
        body (Test2PostRequestJson):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Test2PostResponse
    """

    return sync_detailed(
        testid=testid,
        field2=field2,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    testid: str,
    field2: str,
    *,
    client: AuthenticatedClient | Client,
    body: Test2PostRequestJson,
) -> Response[Error | Test2PostResponse]:
    """Add row to test2 with foreign key to test.

    Args:
        testid (str):
        field2 (str):
        body (Test2PostRequestJson):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Test2PostResponse]
    """

    kwargs = _get_kwargs(
        testid=testid,
        field2=field2,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    testid: str,
    field2: str,
    *,
    client: AuthenticatedClient | Client,
    body: Test2PostRequestJson,
) -> Error | Test2PostResponse | None:
    """Add row to test2 with foreign key to test.

    Args:
        testid (str):
        field2 (str):
        body (Test2PostRequestJson):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Test2PostResponse
    """

    return (
        await asyncio_detailed(
            testid=testid,
            field2=field2,
            client=client,
            body=body,
        )
    ).parsed
