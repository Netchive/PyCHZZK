import pytest
from PyCHZZK.enums import Fields
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
