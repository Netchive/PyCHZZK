from typing import Optional
from pychzzk.client import ChzzkClient, GameClient, Credentials
from pychzzk.models import Channel, User, Video
from pychzzk.models import _model as m


class Chzzk:
    def __init__(self, credential: Optional[Credentials] = None):
        self._client = ChzzkClient(credential)
        self._game = Game(credential)
    
    async def me(self) -> User:
        return await self._game.me()
    
    async def search_channel(self, keyword: str, offset: int, size: int, withFirstChannelContent: bool = True) -> m.SearchChannel:
        """
            keyword: str
            offset: int
            size: int
            withFirstChannelContent: bool
        """
        response = await self._client.get("service/v1/search/channels", params={
            "keyword": keyword,
            "offset": offset,
            "size": size,
            "withFirstChannelContent": withFirstChannelContent
        })
        return m.SearchChannel(**response)
    async def channel(self, channel_id: int) -> Channel:
        response = await self._client.get(f"services/v1/channels/{channel_id}")
        return m.Channel(**response).warp()
    
    async def video(self, video_no: int) -> Video:
        response = await self._client.get(f"services/v1/videos/{video_no}")
        return m.Video(**response).warp()


class Game:
    def __init__(self, credential: Optional[Credentials] = None):
        self._client = GameClient(credential)
    
    async def me(self) -> User:
        response = await self._client.get("v1/user/getUserStatus")
        return m.User(**response).warp()