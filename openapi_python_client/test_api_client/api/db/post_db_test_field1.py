from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.test_post_request_json import TestPostRequestJson
from ...models.test_post_response import TestPostResponse
from ...types import Response


def _get_kwargs(
    field1: str,
    *,
    body: TestPostRequestJson,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/db/test/{field1}".format(
            field1=quote(str(field1), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TestPostResponse:
    if response.status_code == 200:
        response_200 = TestPostResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | TestPostResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field1: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestPostRequestJson,
) -> Response[Error | TestPostResponse]:
    """Add row into test.

    Args:
        field1 (str):
        body (TestPostRequestJson):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TestPostResponse]
    """

    kwargs = _get_kwargs(
        field1=field1,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    field1: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestPostRequestJson,
) -> Error | TestPostResponse | None:
    """Add row into test.

    Args:
        field1 (str):
        body (TestPostRequestJson):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TestPostResponse
    """

    return sync_detailed(
        field1=field1,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    field1: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestPostRequestJson,
) -> Response[Error | TestPostResponse]:
    """Add row into test.

    Args:
        field1 (str):
        body (TestPostRequestJson):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TestPostResponse]
    """

    kwargs = _get_kwargs(
        field1=field1,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    field1: str,
    *,
    client: AuthenticatedClient | Client,
    body: TestPostRequestJson,
) -> Error | TestPostResponse | None:
    """Add row into test.

    Args:
        field1 (str):
        body (TestPostRequestJson):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TestPostResponse
    """

    return (
        await asyncio_detailed(
            field1=field1,
            client=client,
            body=body,
        )
    ).parsed
