import asyncio
import json
from pychzzk.chzzk import Chzzk

app = Chzzk()
if __name__ == "__main__":
    res =asyncio.run(app.search_channel(keyword="김용녀", offset=0, size=50))
    print(res)
    print(res[0].live.live_playback_json.media[0].model_dump_json(indent=4))