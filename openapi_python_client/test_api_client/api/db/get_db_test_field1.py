from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.test_get_response import TestGetResponse
from ...types import Response


def _get_kwargs(
    field1: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/db/test/{field1}".format(
            field1=quote(str(field1), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TestGetResponse:
    if response.status_code == 200:
        response_200 = TestGetResponse.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | TestGetResponse]:
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
) -> Response[Error | TestGetResponse]:
    """Get row from test.

    Args:
        field1 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TestGetResponse]
    """

    kwargs = _get_kwargs(
        field1=field1,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    field1: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | TestGetResponse | None:
    """Get row from test.

    Args:
        field1 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TestGetResponse
    """

    return sync_detailed(
        field1=field1,
        client=client,
    ).parsed


async def asyncio_detailed(
    field1: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | TestGetResponse]:
    """Get row from test.

    Args:
        field1 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TestGetResponse]
    """

    kwargs = _get_kwargs(
        field1=field1,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    field1: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | TestGetResponse | None:
    """Get row from test.

    Args:
        field1 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TestGetResponse
    """

    return (
        await asyncio_detailed(
            field1=field1,
            client=client,
        )
    ).parsed
