from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.test_2_get_response import Test2GetResponse
from ...types import Response


def _get_kwargs(
    testid: str,
    field2: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/db/test/{testid}/test2/{field2}".format(
            testid=quote(str(testid), safe=""),
            field2=quote(str(field2), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Test2GetResponse:
    if response.status_code == 200:
        response_200 = Test2GetResponse.from_dict(response.json())

        return response_200

    response_default = Error.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | Test2GetResponse]:
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
) -> Response[Error | Test2GetResponse]:
    """Get row from test2.

    Args:
        testid (str):
        field2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Test2GetResponse]
    """

    kwargs = _get_kwargs(
        testid=testid,
        field2=field2,
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
) -> Error | Test2GetResponse | None:
    """Get row from test2.

    Args:
        testid (str):
        field2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Test2GetResponse
    """

    return sync_detailed(
        testid=testid,
        field2=field2,
        client=client,
    ).parsed


async def asyncio_detailed(
    testid: str,
    field2: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | Test2GetResponse]:
    """Get row from test2.

    Args:
        testid (str):
        field2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Test2GetResponse]
    """

    kwargs = _get_kwargs(
        testid=testid,
        field2=field2,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    testid: str,
    field2: str,
    *,
    client: AuthenticatedClient | Client,
) -> Error | Test2GetResponse | None:
    """Get row from test2.

    Args:
        testid (str):
        field2 (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Test2GetResponse
    """

    return (
        await asyncio_detailed(
            testid=testid,
            field2=field2,
            client=client,
        )
    ).parsed
