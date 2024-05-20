import json
import asyncio
from PyCHZZK.api import Channels


if __name__ == "__main__":
    channel = Channels()
    res = asyncio.run(channel.search("녹두로"))
    print(json.dumps(res, indent=4, ensure_ascii=False))
