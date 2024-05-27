import pytest
from PyCHZZK.enums import Fields
from PyCHZZK.enums import SortType
from PyCHZZK.enums import PagingType
from PyCHZZK.api import Channels

@pytest.mark.asyncio
async def test_channel_search():
    channel = Channels()
    res = await channel.search("녹두로")
    assert isinstance(res, list)

@pytest.mark.asyncio
async def test_channel_data():
    channel = Channels()
    res = await channel.get_data(channel_id="6e06f5e1907f17eff543abd06cb62891", fields=Fields.all)
    assert isinstance(res, dict)

@pytest.mark.asyncio
async def test_channel_info():
    channel = Channels()
    res = await channel.get_info(channel_id="6e06f5e1907f17eff543abd06cb62891")
    assert isinstance(res, dict)


@pytest.mark.asyncio
async def test_channel_live_status():
    channel = Channels()
    res = await channel.get_live_status(channel_id="6e06f5e1907f17eff543abd06cb62891")
    assert isinstance(res, dict)

@pytest.mark.asyncio
async def test_channel_vods():
    channel = Channels()
    res = await channel.get_videos(channel_id="6e06f5e1907f17eff543abd06cb62891", sort_type=SortType.LATEST, paging_type=PagingType.PAGE, page=0, size=10)
    assert isinstance(res, list)