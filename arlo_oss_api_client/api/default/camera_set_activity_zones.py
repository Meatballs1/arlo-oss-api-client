from typing import Any, Dict, List, Optional, Union, cast

import httpx
from attr import asdict

from ...client import AuthenticatedClient, Client
from ...types import Response




def _get_kwargs(
    *,
    client: Client,
    serial_number: str,

) -> Dict[str, Any]:
    url = "{}/camera/{serial_number}/activityzones".format(
        client.base_url,serial_number=serial_number)

    headers: Dict[str, Any] = client.get_headers()

    

    

    

    return {
        "url": url,
        "headers": headers,
        "cookies": client.get_cookies(),
        "timeout": client.get_timeout(),
    }




def _build_response(*, response: httpx.Response) -> Response[None]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    serial_number: str,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
serial_number=serial_number,

    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    serial_number: str,

) -> Response[None]:
    kwargs = _get_kwargs(
        client=client,
serial_number=serial_number,

    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(
            **kwargs
        )

    return _build_response(response=response)

