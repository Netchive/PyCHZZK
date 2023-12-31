import httpx

from typing import Any, ClassVar, Mapping, Optional
from urllib.parse import urljoin
from pychzzk.models.credential import Credentials
from pychzzk.exceptions import PyChzzkHTTPException
from pychzzk.config import API_URL, GAME_API_URL


class HTTPClient:
    BASE_URL: ClassVar[str]

    def __init__(self, credential: Optional[Credentials] = None):
        assert self.BASE_URL.endswith("/")

        self._credential = credential
        self._client = httpx.AsyncClient()

        if self._credential is not None:
            self._client.cookies.update(self._credential.as_cookie())
    
    async def request(
            self,
            method: str,
            url: str,
            *,
            params: Optional[Mapping[str, Any]] = None,
            data: Optional[Mapping[str, Any]] = None,
            **kwargs
    ) -> Any:
        response = await self._client.request(
            method=method,
            url=urljoin(self.BASE_URL, url),
            params=params,
            data=data,
            **kwargs
        )

        if response.status_code != 200:
            raise PyChzzkHTTPException(message="HTTP request failed", code=response.status_code)
        
        resp = response.json()
        if resp["code"] != 200:
            raise PyChzzkHTTPException(message=resp["message"], code=resp["code"])
        
        return resp["content"]
    
    async def get(
            self,
            url: str,
            *,
            params: Optional[Mapping[str, Any]] = None,
            data: Optional[Mapping[str, Any]] = None,
            **kwargs
    ) -> Any:
        return await self.request("GET", url, params=params, data=data, **kwargs)
    
    async def post(
            self,
            url: str,
            *,
            params: Optional[Mapping[str, Any]] = None,
            data: Optional[Mapping[str, Any]] = None,
            **kwargs
    ) -> Any:
        return await self.request("POST", url, params=params, data=data, **kwargs)
    

class GameClient(HTTPClient):
    BASE_URL = GAME_API_URL

    def __init__(self, credential: Optional[Credentials]= None):
        super().__init__(credential)

class ChzzkClient(HTTPClient):
    BASE_URL = API_URL

    def __init__(self, credential: Optional[Credentials]= None):
        super().__init__(credential)

__all__ = [
    GameClient,
    ChzzkClient
]
