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

## License
Licensed under the [MIT](./LICENSE)