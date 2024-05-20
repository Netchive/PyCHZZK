from httpx import AsyncClient
from httpx import Response

class HTTP(AsyncClient):
    def __init__(self, 
        base_url: str,
        headers: dict[str, str] | None = None,
    ):
        super().__init__(
            base_url=base_url,
            headers=headers,
        )
    
    async def fetch(self, method: str, url: str, params: dict[str, str] | None = None, json: dict | None = None) -> Response:
        match method.upper():
            case "GET":
                res = await self.get(
                    url=url,
                    params=params,
                )
                return res.raise_for_status()
            case "POST":
                res = await self.post(
                    url=url,
                    params=params,
                    json=json
                )
                return res.raise_for_status()
            case _:
                raise NotImplementedError(f"Method {method} is not implemented")