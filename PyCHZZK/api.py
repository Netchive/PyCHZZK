from .enums import Fields
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
        """Search channels

        example:
            ```python
            import asyncio
            from PyCHHZK.api import Channels

            async def print_search_channels():
                channel = Channels()
                channels = await channel.search("녹두로")
                print(channels)
            
            asyncio.run(print_search_channels())
            ```
        
        Args:
            keyword (str): Search keyword
        
        Returns:
            dict: Search result
        """
        response = await self.fetch("GET", "search/channels", params={
            "keyword": keyword
        })
        raw_data = response.json()
        content = null_check(raw_data.get("content"))
        data = null_check(content.get("data"))
        return data
    
    async def get_data(self, channel_id: str, fields: Fields) -> dict:
        """Get channel data

        example:
            ```python
            import asyncio
            from PyCHHZK.api import Channels
            from PyCHZZK.enums import Fields
            
            async def print_channel_data():
                channel = Channels()
                channel_data = await channel.get_data(channel_id, Fields.description)
                print(channel_data)
            
            asyncio.run(print_channel_data())
            ```

        Args:
            channel_id (str): Channel ID
            fields (Fields): Fields
        
        Returns:
            dict: Channel data
        """
        response = await self.fetch("GET", f"channels/{channel_id}/data", params={
            "fields": fields.value
        })
        raw_data = response.json()
        content = null_check(raw_data.get("content"))
        return content