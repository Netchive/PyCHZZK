from .enums import Fields
from .utils import null_check
from ._http import HTTP
from .exceptions import OfflineException
from .exceptions import ChannelNotFound


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
    
    async def get_info(self, channel_id: str) -> dict:
        """Get channel info

        example:
            ```python
            import asyncio
            from PyCHHZK.api import Channels
            
            async def print_channel_info():
                channel = Channels()
                channel_info = await channel.get_info(channel_id)
                print(channel_info)
            
            asyncio.run(print_channel_info())
            ```

        Args:
            channel_id (str): Channel ID
        
        Returns:
            dict: Channel info
        """
        response = await self.fetch("GET", f"channels/{channel_id}")
        raw_data = response.json()
        content = null_check(raw_data.get("content"))
        
        def check_vaild_response(response: dict) -> bool:
            return not response["channelId"]
        check = check_vaild_response(content)
        if check:
            raise ChannelNotFound(channel_id)
        return content

    async def get_live_status(self, channel_id: str) -> dict:
        """Get channel live status

        example:
            ```python
            import asyncio
            from PyCHHZK.api import Channels
            
            async def print_live_status():
                channel = Channels()
                live_status = await channel.get_live_status(channel_id)
                print(live_status)
            
            asyncio.run(print_live_status())
            ```

        Args:
            channel_id (str): Channel ID
        
        Returns:
            dict: Channel live status
        """

        resp = await self.get_info(channel_id)
        live_status: bool = resp["openLive"]

        if live_status:
            self.temp_base_url = self.base_url
            self.base_url = "https://api.chzzk.naver.com/polling/v2/"
            response = await self.fetch("GET", f"channels/{channel_id}/live-status")
            self.base_url = self.temp_base_url
            del self.temp_base_url
            raw_data = response.json()
            content = null_check(raw_data.get("content"))
            return content
        else:
            raise OfflineException()
