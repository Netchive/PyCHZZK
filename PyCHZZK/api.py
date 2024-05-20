from .utils import null_check
from ._http import HTTP


class Channels(HTTP):
    def __init__(self):
        super().__init__(
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
            },
            base_url="https://api.chzzk.naver.com/service/v1/"
        )
    
    async def search(self, keyword: str) -> list[dict]:
        response = await self.fetch("GET", "search/channels", params={
            "keyword": keyword
        })
        raw_data = response.json()
        content = null_check(raw_data.get("content"))
        data = null_check(content.get("data"))
        return data