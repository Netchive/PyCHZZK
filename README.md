# PyCHZZK
NAVER CHZZK Python SDK


## Usage
```
pip install PyCHZZK
```

## Example
#### **PyCHZZK.api.Channels**
**channel.search**
```python
import asyncio
from PyCHHZK.api import Channels

async def print_search_channels():
    channel = Channels()
    channels = await channel.search("녹두로")
    print(channels)

asyncio.run(print_search_channels())
```
---
**channel.get_data**
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
---
**channel.get_info**
```python
import asyncio
from PyCHHZK.api import Channels

async def print_channel_info():
    channel = Channels()
    channel_info = await channel.get_info(channel_id)
    print(channel_info)

asyncio.run(print_channel_info())
```
---
**channel.get_live_status**
```python
import asyncio
from PyCHHZK.api import Channels

async def print_live_status():
    channel = Channels()
    live_status = await channel.get_live_status(channel_id)
    print(live_status)

asyncio.run(print_live_status())
```

## License
Licensed under the [MIT](./LICENSE)