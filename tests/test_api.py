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
    res = await channel.get_data(channel_id="1906dd57f578c255feca54700bcccfc9", fields=Fields.all)
    assert isinstance(res, dict)


@pytest.mark.asyncio
async def test_channel_info():
    channel = Channels()
    res = await channel.get_info(channel_id="1906dd57f578c255feca54700bcccfc9")
    assert isinstance(res, dict)


@pytest.mark.asyncio
async def test_channel_live_status():
    channel = Channels()
    res = await channel.get_live_status(channel_id="1906dd57f578c255feca54700bcccfc9")
    assert isinstance(res, dict)


@pytest.mark.asyncio
async def test_channel_vods():
    channel = Channels()
    res = await channel.get_videos(channel_id="1906dd57f578c255feca54700bcccfc9", sort_type=SortType.LATEST,
                                   paging_type=PagingType.PAGE, page=0, size=10)
    assert isinstance(res, list)
