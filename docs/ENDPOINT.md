# Chzzk Endpoint

## V1

### **Service**

#### Home
> https://api.chzzk.naver.com/service/v1/home/recommendation-channels

    HTTP Method: GET
```json
{
    "code": 200,
    "message": null,
    "content": {
        "recommendationChannels": [
            {
                "channelId": "9381e7d6816e6d915a44a13c0195b202",
                "channel": {
                    "channelId": "9381e7d6816e6d915a44a13c0195b202",
                    "channelName": "치지직 e스포츠",
                    "channelImageUrl": "https://nng-phinf.pstatic.net/MjAyMzEyMThfNDcg/MDAxNzAyODg1MDgwNzY3.P5DJlXA88mUBbm4JrDJtlYYRgDx9Bz9XD_BJYwzDB44g.kw21eBBQ1vGkI6DMhytMky0p3K7XgZhDIugibfFNaKIg.PNG/%EC%B9%98%EC%A7%80%EC%A7%81.png",
                    "verifiedMark": false
                },
                "streamer": {
                    "openLive": true
                }
            },
        ]
    }
}
```

> https://api.chzzk.naver.com/service/v1/home/lives
    
    HTTP Method: GET
    Payload:
        includeLatestVideo: bool
```json
{
    "code": 200,
    "message": null,
    "content": {
        "topRecommendationLiveList": [
            {
                "liveId": 4145157,
                "liveTitle": "준비 아님말고",
                "status": "OPEN",
                "liveImageUrl": "https://livecloud-thumb.akamaized.net/chzzk/livecloud/KR/stream/26479964/live/4145157/record/24058209/thumbnail/image_{type}.jpg",
                "defaultThumbnailImageUrl": null,
                "concurrentUserCount": 369,
                "accumulateCount": 2221,
                "openDate": "2023-12-21 12:46:09",
                "closeDate": null,
                "chatChannelId": "N1384k",
                "categoryType": "GAME",
                "liveCategory": "Ready_or_Not",
                "liveCategoryValue": "레디 올 낫",
                "chatActive": true,
                "chatAvailableGroup": "ALL",
                "paidPromotion": false,
                "chatAvailableCondition": "NONE",
                "minFollowerMinute": 0,
                "livePlaybackJson": "{\"meta\":{\"videoId\":\"51E581A4A09BB86E75E620665E6F3FF842A6\",\"streamSeq\":26479964,\"liveId\":\"4145157\",\"paidLive\":false,\"cdnInfo\":{\"cdnType\":\"GCDN\",\"zeroRating\":false},\"p2p\":false},\"serviceMeta\":{\"contentType\":\"VIDEO\"},\"live\":{\"start\":\"2023-12-21T12:46:09\",\"open\":\"2023-12-21T12:46:09\",\"timeMachine\":false,\"status\":\"STARTED\"},\"api\":[{\"name\":\"p2p-config\",\"path\":\"https://apis.naver.com/livecloud/livecloud/xray/p2p/v1/config/chzzk\"},{\"name\":\"qoeConfig\",\"path\":\"https://apis.naver.com/policy/policy/policy\"}],\"media\":[{\"mediaId\":\"HLS\",\"protocol\":\"HLS\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr2/anmss0457/awh0oulvf0agfh32o7m2xlyaftlhn5adl7/hls_playlist.m3u8?hdnts=st=1703131188~exp=1703163598~acl=*/awh0oulvf0agfh32o7m2xlyaftlhn5adl7/*~hmac=c0116e8ee196247eb2f46466e446be937935b5c9d5f455c08047f8d10ea7fcd3\",\"encodingTrack\":[{\"encodingTrackId\":\"144p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":128000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":256,\"videoHeight\":144,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"360p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":800000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":640,\"videoHeight\":360,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"480p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":1500000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":852,\"videoHeight\":480,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"1080p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":8000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1920,\"videoHeight\":1080,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"720p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":5000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1280,\"videoHeight\":720,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"alow.stream\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr2/anmss0457/awh0oulvf0agfh32o7m2xlyaftlhn5adl7/afragalow.stream_hls_playlist.m3u8?hdnts=st=1703131188~exp=1703163598~acl=*/awh0oulvf0agfh32o7m2xlyaftlhn5adl7/*~hmac=c0116e8ee196247eb2f46466e446be937935b5c9d5f455c08047f8d10ea7fcd3\",\"audioCodec\":\"AAC\",\"audioBitRate\":64000,\"audioOnly\":true,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false}]},{\"mediaId\":\"LLHLS\",\"protocol\":\"HLS\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr2/anmss0457/awh0oulvf0agfh32o7m2xlyaftlhn5adl7/playlist.m3u8?hdnts=st=1703131188~exp=1703163598~acl=*/awh0oulvf0agfh32o7m2xlyaftlhn5adl7/*~hmac=c0116e8ee196247eb2f46466e446be937935b5c9d5f455c08047f8d10ea7fcd3\",\"latency\":\"lowLatency\",\"encodingTrack\":[{\"encodingTrackId\":\"144p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":128000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":256,\"videoHeight\":144,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"360p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":800000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":640,\"videoHeight\":360,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"480p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":1500000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":852,\"videoHeight\":480,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"1080p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":8000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1920,\"videoHeight\":1080,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"720p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":5000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1280,\"videoHeight\":720,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"alow.stream\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr2/anmss0457/awh0oulvf0agfh32o7m2xlyaftlhn5adl7/afragalow.stream_playlist.m3u8?hdnts=st=1703131188~exp=1703163598~acl=*/awh0oulvf0agfh32o7m2xlyaftlhn5adl7/*~hmac=c0116e8ee196247eb2f46466e446be937935b5c9d5f455c08047f8d10ea7fcd3\",\"audioCodec\":\"AAC\",\"audioBitRate\":64000,\"audioOnly\":true,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false}]}],\"thumbnail\":{\"snapshotThumbnailTemplate\":\"https://livecloud-thumb.akamaized.net/chzzk/livecloud/KR/stream/26479964/live/4145157/record/24058209/thumbnail/image_{type}.jpg\",\"types\":[\"1080\",\"720\",\"480\",\"360\",\"270\",\"144\"]},\"multiview\":[]}",
                "channel": {
                    "channelId": "bee4b42475b5937226b8b7ccbe2eb2dc",
                    "channelName": "칸데르니아",
                    "channelImageUrl": "https://nng-phinf.pstatic.net/MjAyMzEyMDZfMjc0/MDAxNzAxODI5NTAwMzQ1.tWiGOf27WjmRWaBfM24lGMX9Qz5CJzEuzU0wvTnL4KUg.8O9cCU8LcyqE4LgJVQxGQkCzogF8M3X67yHfXVxw0Jog.PNG/%EB%B9%BC%EA%BC%BC.png",
                    "verifiedMark": false
                },
                "livePollingStatusJson": "{\"status\": \"STARTED\", \"isPublishing\": true, \"playableStatus\": \"PLAYABLE\", \"trafficThrottling\": -1, \"callPeriodMilliSecond\": 10000}",
                "homeLiveType": "STREAMING",
                "gameId": null,
                "leagueId": null,
                "topLeagueId": null,
                "gameCode": null,
                "esportsLoungeId": null
            }
        ],
        "streamingLiveList": [
            {
                "liveId": 4145097,
                "liveTitle": "\uD83D\uDD25다주  여행때문에 못 본 로아 윈터 쇼케이스 시청",
                "liveImageUrl": "https://livecloud-thumb.akamaized.net/chzzk/livecloud/KR/stream/26479034/live/4145097/record/24058001/thumbnail/image_{type}.jpg",
                "defaultThumbnailImageUrl": null,
                "concurrentUserCount": 5629,
                "accumulateCount": 40284,
                "openDate": "2023-12-21 11:43:00",
                "categoryType": "ETC",
                "liveCategory": "talk",
                "liveCategoryValue": "talk",
                "channel": {
                    "channelId": "bdc57cc4217173f0e89f63fba2f1c6e5",
                    "channelName": "핫다주",
                    "channelImageUrl": "https://nng-phinf.pstatic.net/MjAyMzEyMjBfMTc1/MDAxNzAzMDUxOTY1OTU2.OgfgQCGfgriKJukj6nCvnXsUgpy6Rjq8ZIhhZQIakVMg.yF3CnqRLEFVUUupSDKvaICW8ZLCvgZ1cK6L7f1lnrzwg.JPEG/NNG-17030519634272930902637659552871.jpg",
                    "verifiedMark": false
                }
            },
        ],
        "esportsLiveList": [],
        "latestVideoList": [
            {
                "videoNo": 1989,
                "videoId": "AE40D93CB6C0215253E4D44641B376D7B315",
                "videoTitle": "준비 아님말고",
                "videoType": "REPLAY",
                "publishDate": "2023-12-21 12:46:07",
                "thumbnailImageUrl": "https://video-phinf.pstatic.net/20231221_30/17031303712063wT5N_JPEG/78cac131-9fb3-11ee-a2b6-b443264fff5e_03.jpg",
                "trailerUrl": null,
                "duration": 327,
                "readCount": 27,
                "publishDateAt": 1703130366847,
                "categoryType": "GAME",
                "videoCategory": "Ready_or_Not",
                "videoCategoryValue": "레디 올 낫",
                "exposure": false,
                "channel": {
                    "channelId": "bee4b42475b5937226b8b7ccbe2eb2dc",
                    "channelName": "칸데르니아",
                    "channelImageUrl": "https://nng-phinf.pstatic.net/MjAyMzEyMDZfMjc0/MDAxNzAxODI5NTAwMzQ1.tWiGOf27WjmRWaBfM24lGMX9Qz5CJzEuzU0wvTnL4KUg.8O9cCU8LcyqE4LgJVQxGQkCzogF8M3X67yHfXVxw0Jog.PNG/%EB%B9%BC%EA%BC%BC.png",
                    "verifiedMark": false
                }
            },
        ]
    }
}
```

### **comm-api**

#### User
* **Require authorized**
> https://comm-api.game.naver.com/nng_main/v1/user/getUserStatus
    
    HTTP Method: GET
```json
{
    "code": 200,
    "message": null,
    "content": {
        "hasProfile": true,
        "userIdHash": "<hashed user id>",
        "nickname": "zeroday0619",
        "profileImageUrl": "<URL>",
        "penalties": [],
        "officialNotiAgree": true,
        "officialNotiAgreeUpdatedDate": "2023-12-07T07:47:00.000+09",
        "verifiedMark": false,
        "loggedIn": true
    }
}
```

#### Search

> https://comm-api.game.naver.com/nng_main/v2/search/lounges/auto-complete

    HTTP Method: GET
    Payload:
        keyword: str
        limit: int
        offset: int

```json
{
    "code": 200,
    "message": null,
    "content": {
        "page": 1,
        "size": 10,
        "totalCount": 1,
        "totalPages": 1,
        "data": [
            "녹두로로"
        ]
    }
}
```

#### Search

> https://api.chzzk.naver.com/service/v1/search/channels

    HTTP Method: GET
    Payload:
        keyword: str
        offset: int
        size: int
        withFirstChannelContent: bool
```json
{
    "code": 200,
    "message": null,
    "content": {
        "size": 13,
        "page": {
            "next": {
                "offset": 13
            }
        },
        "data": [
            {
                "channel": {
                    "channelId": "6e06f5e1907f17eff543abd06cb62891",
                    "channelName": "녹두로로",
                    "channelImageUrl": "https://nng-phinf.pstatic.net/MjAyMzEyMTlfMTc2/MDAxNzAyOTc3NjA0NTc4.Vd9lD67bKMJbZS8aBvyX8KjDqKLCR9zCuhxGilqhSEQg.Pdsam1-hUc0QiCEjOmOm6-bbwHeLXBQ2W_udwZOzyskg.PNG/2.png",
                    "verifiedMark": false,
                    "channelDescription": "녹두로임",
                    "followerCount": 44284,
                    "openLive": false
                }
            }
        ]
    }
}
```

> https://api.chzzk.naver.com/service/v1/search/lives

    HTTP Method: GET
    Payload:
        keyword: str
        offset: int
        size: int
```json
{
    "code": 200,
    "message": null,
    "content": {
        "size": 12,
        "page": {
            "next": {
                "offset": 12
            }
        },
        "data": [
            {
                "live": {
                    "liveTitle": "치지직 세팅중",
                    "liveImageUrl": "https://livecloud-thumb.akamaized.net/chzzk/livecloud/KR/stream/26480057/live/4145166/record/24058238/thumbnail/image_{type}.jpg",
                    "defaultThumbnailImageUrl": null,
                    "concurrentUserCount": 190,
                    "accumulateCount": 1638,
                    "openDate": "2023-12-21 12:56:26",
                    "liveId": 4145166,
                    "chatChannelId": "N1384y",
                    "categoryType": "ETC",
                    "liveCategory": "talk",
                    "liveCategoryValue": "talk",
                    "channelId": "de27c33ee2364c4e5007867bb3b96001",
                    "livePlaybackJson": "{\"meta\":{\"videoId\":\"24A0CF6603A28A892E18C6C8BCBD22996D1D\",\"streamSeq\":26480057,\"liveId\":\"4145166\",\"paidLive\":false,\"cdnInfo\":{\"cdnType\":\"GCDN\",\"zeroRating\":false},\"p2p\":false},\"serviceMeta\":{\"contentType\":\"VIDEO\"},\"live\":{\"start\":\"2023-12-21T12:56:26\",\"open\":\"2023-12-21T12:59:24\",\"timeMachine\":false,\"status\":\"STARTED\"},\"api\":[{\"name\":\"p2p-config\",\"path\":\"https://apis.naver.com/livecloud/livecloud/xray/p2p/v1/config/chzzk\"},{\"name\":\"qoeConfig\",\"path\":\"https://apis.naver.com/policy/policy/policy\"}],\"media\":[{\"mediaId\":\"HLS\",\"protocol\":\"HLS\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr2/anmss1233/0oz6fell5pmgsydggx5yetma6wx4ezwh7n/hls_playlist.m3u8?hdnts=st=1703131642~exp=1703164052~acl=*/0oz6fell5pmgsydggx5yetma6wx4ezwh7n/*~hmac=64fb3fc6b0e18152008e9f202f8c0168e05ac20444855603aab5c23c23a01829\",\"encodingTrack\":[{\"encodingTrackId\":\"144p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":128000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":256,\"videoHeight\":144,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"360p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":800000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":640,\"videoHeight\":360,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"480p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":1500000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":852,\"videoHeight\":480,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"1080p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":8000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1920,\"videoHeight\":1080,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"720p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":5000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1280,\"videoHeight\":720,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"alow.stream\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr2/anmss1233/0oz6fell5pmgsydggx5yetma6wx4ezwh7n/afragalow.stream_hls_playlist.m3u8?hdnts=st=1703131642~exp=1703164052~acl=*/0oz6fell5pmgsydggx5yetma6wx4ezwh7n/*~hmac=64fb3fc6b0e18152008e9f202f8c0168e05ac20444855603aab5c23c23a01829\",\"audioCodec\":\"AAC\",\"audioBitRate\":64000,\"audioOnly\":true,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false}]},{\"mediaId\":\"LLHLS\",\"protocol\":\"HLS\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr2/anmss1233/0oz6fell5pmgsydggx5yetma6wx4ezwh7n/playlist.m3u8?hdnts=st=1703131642~exp=1703164052~acl=*/0oz6fell5pmgsydggx5yetma6wx4ezwh7n/*~hmac=64fb3fc6b0e18152008e9f202f8c0168e05ac20444855603aab5c23c23a01829\",\"latency\":\"lowLatency\",\"encodingTrack\":[{\"encodingTrackId\":\"144p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":128000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":256,\"videoHeight\":144,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"360p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":800000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":640,\"videoHeight\":360,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"480p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":1500000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":852,\"videoHeight\":480,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"1080p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":8000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1920,\"videoHeight\":1080,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"720p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":5000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1280,\"videoHeight\":720,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"alow.stream\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr2/anmss1233/0oz6fell5pmgsydggx5yetma6wx4ezwh7n/afragalow.stream_playlist.m3u8?hdnts=st=1703131642~exp=1703164052~acl=*/0oz6fell5pmgsydggx5yetma6wx4ezwh7n/*~hmac=64fb3fc6b0e18152008e9f202f8c0168e05ac20444855603aab5c23c23a01829\",\"audioCodec\":\"AAC\",\"audioBitRate\":64000,\"audioOnly\":true,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false}]}],\"thumbnail\":{\"snapshotThumbnailTemplate\":\"https://livecloud-thumb.akamaized.net/chzzk/livecloud/KR/stream/26480057/live/4145166/record/24058238/thumbnail/image_{type}.jpg\",\"types\":[\"1080\",\"720\",\"480\",\"360\",\"270\",\"144\"]},\"multiview\":[]}"
                },
                "channel": {
                    "channelId": "de27c33ee2364c4e5007867bb3b96001",
                    "channelName": "크랭크",
                    "channelImageUrl": "https://nng-phinf.pstatic.net/MjAyMzEyMjBfMTkx/MDAxNzAzMDQ4MDIxNzI2.gcnD3FQdL3ZqWYJH8vbVhsbrKDUZ4e9CVyPGnQZCUHgg.5eLpnI1nAj2QEE9aALDK1qjSqbeeL0KVbLiI1mI3SCkg.PNG/%EC%A0%9C%EB%AA%A9-%EC%97%86%EC%9D%8C-1.png",
                    "verifiedMark": false
                }
            },
        ]
    }
}
```

> https://api.chzzk.naver.com/service/v1/search/videos

    HTTP Method: GET
    Payload:
        keyword: str
        offset: int
        size: int
```json
{
    "code": 200,
    "message": null,
    "content": {
        "size": 12,
        "page": {
            "next": {
                "offset": 12
            }
        },
        "data": [
            {
                "video": {
                    "videoNo": 1789,
                    "videoId": "9DAB93D6F290574BE42B2CC7BD54EF6A3D2E",
                    "videoTitle": "녹두로로의 라이브 방송",
                    "videoType": "REPLAY",
                    "publishDate": "2023-12-19 20:13:56",
                    "thumbnailImageUrl": "https://video-phinf.pstatic.net/20231219_163/1702984440101BgRfw_JPEG/b31abe5e-9e5f-11ee-ac6a-a0369ffdb988_03.jpg",
                    "duration": 71,
                    "readCount": 4387,
                    "channelId": "6e06f5e1907f17eff543abd06cb62891",
                    "publishDateAt": 1702984435870,
                    "categoryType": null,
                    "videoCategory": null,
                    "videoCategoryValue": ""
                },
                "channel": {
                    "channelId": "6e06f5e1907f17eff543abd06cb62891",
                    "channelName": "녹두로로",
                    "channelImageUrl": "https://nng-phinf.pstatic.net/MjAyMzEyMTlfMTc2/MDAxNzAyOTc3NjA0NTc4.Vd9lD67bKMJbZS8aBvyX8KjDqKLCR9zCuhxGilqhSEQg.Pdsam1-hUc0QiCEjOmOm6-bbwHeLXBQ2W_udwZOzyskg.PNG/2.png",
                    "verifiedMark": false
                }
            },
        ]
    }
}
```

#### Channels

> https://api.chzzk.naver.com/service/v1/channels/[channelId]

    HTTP Method: GET

```json
{
    "code": 200,
    "message": null,
    "content": {
        "channelId": "9381e7d6816e6d915a44a13c0195b202",
        "channelName": "치지직 e스포츠",
        "channelImageUrl": "https://nng-phinf.pstatic.net/MjAyMzEyMThfNDcg/MDAxNzAyODg1MDgwNzY3.P5DJlXA88mUBbm4JrDJtlYYRgDx9Bz9XD_BJYwzDB44g.kw21eBBQ1vGkI6DMhytMky0p3K7XgZhDIugibfFNaKIg.PNG/%EC%B9%98%EC%A7%80%EC%A7%81.png",
        "verifiedMark": false,
        "channelType": "STREAMING",
        "channelDescription": "",
        "followerCount": 18897,
        "openLive": true
    }
}
```

> https://api.chzzk.naver.com/service/v1/channels/[channelId]/data

    HTTP Method: GET
    Payload:
        fields: [banners, topExposedVideos, description]

```json
{
    "code": 200,
    "message": null,
    "content": {
        "description": "녹두로임",
        "topExposedVideos": {
            "openLive": null,
            "fixedVideo": null,
            "latestVideo": {
                "videoNo": 1978,
                "videoId": "0EC7B9373DFE583702F42780974B2E7A6B6B",
                "videoTitle": "전문 림월드 방송 ㅇㅅㅇ;;",
                "videoType": "REPLAY",
                "publishDate": "2023-12-21 05:01:00",
                "thumbnailImageUrl": "https://video-phinf.pstatic.net/20231221_82/17031029538535ko0o_JPEG/7ec43525-9f72-11ee-becb-a0369ffac20c_03.jpg",
                "duration": 30493,
                "readCount": 1580,
                "channelId": "6e06f5e1907f17eff543abd06cb62891",
                "publishDateAt": 1703102459659,
                "categoryType": "GAME",
                "videoCategory": "Rimworld",
                "videoCategoryValue": "림월드"
            }
        }
    }
}
```

> https://api.chzzk.naver.com/service/v1/channels/[channelId]/videos

    HTTP Method: GET
    Payload:
        sortType: [LATEST]
        pagingType: [PAGE]
        page: int
        size: int
        publishDateAt: <Optional>
        videoType: <Optional>

```json
{
    "code": 200,
    "message": null,
    "content": {
        "page": 0,
        "size": 24,
        "totalCount": 8,
        "totalPages": 1,
        "data": [
            {
                "videoNo": 1978,
                "videoId": "0EC7B9373DFE583702F42780974B2E7A6B6B",
                "videoTitle": "전문 림월드 방송 ㅇㅅㅇ;;",
                "videoType": "REPLAY",
                "publishDate": "2023-12-21 05:01:00",
                "thumbnailImageUrl": "https://video-phinf.pstatic.net/20231221_82/17031029538535ko0o_JPEG/7ec43525-9f72-11ee-becb-a0369ffac20c_03.jpg",
                "trailerUrl": "https://a01-g-naver-vod.akamaized.net/glive/c/read/v2/VOD_ALPHA/glive_2023_12_21_2/54cd852f-9fa1-11ee-9f4a-80615f0bcc1e.mp4?__gda__=1703160548_458025af7261f9fa4a6abd02227e72ee",
                "duration": 30493,
                "readCount": 1574,
                "publishDateAt": 1703102459659,
                "categoryType": "GAME",
                "videoCategory": "Rimworld",
                "videoCategoryValue": "림월드",
                "exposure": false,
                "channel": {
                    "channelId": "6e06f5e1907f17eff543abd06cb62891",
                    "channelName": "녹두로로",
                    "channelImageUrl": "https://nng-phinf.pstatic.net/MjAyMzEyMTlfMTc2/MDAxNzAyOTc3NjA0NTc4.Vd9lD67bKMJbZS8aBvyX8KjDqKLCR9zCuhxGilqhSEQg.Pdsam1-hUc0QiCEjOmOm6-bbwHeLXBQ2W_udwZOzyskg.PNG/2.png",
                    "verifiedMark": false,
                    "personalData": {
                        "privateUserBlock": false
                    }
                }
            },
        ]
    }
}
```

> https://api.chzzk.naver.com/service/v1/channels/[channelId]/live-detail

    HTTP Method: GET
```json
{
    "code": 200,
    "message": null,
    "content": {
        "liveId": 4141748,
        "liveTitle": "V4를 향한 여정! 19-23 T1 전경기 다시보기",
        "status": "OPEN",
        "liveImageUrl": "https://livecloud-thumb.akamaized.net/chzzk/livecloud/KR/stream/26428721/live/4141748/record/24029941/thumbnail/image_{type}.jpg",
        "defaultThumbnailImageUrl": null,
        "concurrentUserCount": 853,
        "accumulateCount": 664011,
        "openDate": "2023-12-19 12:03:34",
        "closeDate": null,
        "chatChannelId": "N137Or",
        "categoryType": "GAME",
        "liveCategory": "League_of_Legends",
        "liveCategoryValue": "리그 오브 레전드",
        "chatActive": true,
        "chatAvailableGroup": "ALL",
        "paidPromotion": false,
        "chatAvailableCondition": "NONE",
        "minFollowerMinute": 0,
        "livePlaybackJson": "{\"meta\":{\"videoId\":\"0B7684D470F4204C4BDB36C0869B8B7C9C7E\",\"streamSeq\":26428721,\"liveId\":\"4141748\",\"paidLive\":false,\"cdnInfo\":{\"cdnType\":\"GCDN\",\"zeroRating\":false},\"p2p\":false},\"serviceMeta\":{\"contentType\":\"VIDEO\"},\"live\":{\"start\":\"2023-12-19T12:03:34\",\"open\":\"2023-12-19T14:14:19\",\"timeMachine\":false,\"status\":\"STARTED\"},\"api\":[{\"name\":\"p2p-config\",\"path\":\"https://apis.naver.com/livecloud/livecloud/xray/p2p/v1/config/chzzk\"},{\"name\":\"qoeConfig\",\"path\":\"https://apis.naver.com/policy/policy/policy\"}],\"media\":[{\"mediaId\":\"HLS\",\"protocol\":\"HLS\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr/pgsg1nmss1u0002/sj86jmgapzqozv4qs8xaevua56kg4wxe7q/hls_playlist.m3u8?hdnts=st=1703133025~exp=1703165435~acl=*/sj86jmgapzqozv4qs8xaevua56kg4wxe7q/*~hmac=eda5950838fd849afc57b2abeb392324c0a450300e47d161835270847bb12516\",\"encodingTrack\":[{\"encodingTrackId\":\"144p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":128000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":256,\"videoHeight\":144,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"360p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":800000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":640,\"videoHeight\":360,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"1080p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":8000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1920,\"videoHeight\":1080,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"480p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":1500000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":852,\"videoHeight\":480,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"720p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":5000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1280,\"videoHeight\":720,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"alow.stream\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr/pgsg1nmss1u0002/sj86jmgapzqozv4qs8xaevua56kg4wxe7q/afragalow.stream_hls_playlist.m3u8?hdnts=st=1703133025~exp=1703165435~acl=*/sj86jmgapzqozv4qs8xaevua56kg4wxe7q/*~hmac=eda5950838fd849afc57b2abeb392324c0a450300e47d161835270847bb12516\",\"audioCodec\":\"AAC\",\"audioBitRate\":64000,\"audioOnly\":true,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false}]},{\"mediaId\":\"LLHLS\",\"protocol\":\"HLS\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr/pgsg1nmss1u0002/sj86jmgapzqozv4qs8xaevua56kg4wxe7q/playlist.m3u8?hdnts=st=1703133025~exp=1703165435~acl=*/sj86jmgapzqozv4qs8xaevua56kg4wxe7q/*~hmac=eda5950838fd849afc57b2abeb392324c0a450300e47d161835270847bb12516\",\"latency\":\"lowLatency\",\"encodingTrack\":[{\"encodingTrackId\":\"144p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":128000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":256,\"videoHeight\":144,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"360p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":800000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":640,\"videoHeight\":360,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"1080p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":8000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1920,\"videoHeight\":1080,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"480p\",\"videoProfile\":\"main\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":1500000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":852,\"videoHeight\":480,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"720p\",\"videoProfile\":\"high\",\"audioProfile\":\"LC\",\"videoCodec\":\"H264\",\"videoBitRate\":5000000,\"audioBitRate\":192000,\"videoFrameRate\":\"30.0\",\"videoWidth\":1280,\"videoHeight\":720,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false,\"videoDynamicRange\":\"SDR\"},{\"encodingTrackId\":\"alow.stream\",\"path\":\"https://livecloud.akamaized.net/chzzk/lip2_kr/pgsg1nmss1u0002/sj86jmgapzqozv4qs8xaevua56kg4wxe7q/afragalow.stream_playlist.m3u8?hdnts=st=1703133025~exp=1703165435~acl=*/sj86jmgapzqozv4qs8xaevua56kg4wxe7q/*~hmac=eda5950838fd849afc57b2abeb392324c0a450300e47d161835270847bb12516\",\"audioCodec\":\"AAC\",\"audioBitRate\":64000,\"audioOnly\":true,\"audioSamplingRate\":48000,\"audioChannel\":2,\"avoidReencoding\":false}]}],\"thumbnail\":{\"snapshotThumbnailTemplate\":\"https://livecloud-thumb.akamaized.net/chzzk/livecloud/KR/stream/26428721/live/4141748/record/24029941/thumbnail/image_{type}.jpg\",\"types\":[\"1080\",\"720\",\"480\",\"360\",\"270\",\"144\"]},\"multiview\":[]}",
        "channel": {
            "channelId": "9381e7d6816e6d915a44a13c0195b202",
            "channelName": "치지직 e스포츠",
            "channelImageUrl": "https://nng-phinf.pstatic.net/MjAyMzEyMThfNDcg/MDAxNzAyODg1MDgwNzY3.P5DJlXA88mUBbm4JrDJtlYYRgDx9Bz9XD_BJYwzDB44g.kw21eBBQ1vGkI6DMhytMky0p3K7XgZhDIugibfFNaKIg.PNG/%EC%B9%98%EC%A7%80%EC%A7%81.png",
            "verifiedMark": false
        },
        "livePollingStatusJson": "{\"status\": \"STARTED\", \"isPublishing\": true, \"playableStatus\": \"PLAYABLE\", \"trafficThrottling\": -1, \"callPeriodMilliSecond\": 10000}"
    }
}
```

> https://api.chzzk.naver.com/service/v1/channels/[channelId]/chat-rules

    HTTP Method: GET
```json
{
    "code": 200,
    "message": null,
    "content": {
        "agree": false,
        "channelId": "9381e7d6816e6d915a44a13c0195b202",
        "rule": "클린한 e스포츠 문화를 위해 매너 채팅 부탁드립니다.",
        "updatedDate": "2023-12-19 11:25:49",
        "serviceAgree": false
    }
}
```
---
### **Polling**
#### channels
> https://api.chzzk.naver.com/polling/v1/channels/[channelId]/live-status

    HTTP Method: GET
```json
{
    "code": 200,
    "message": null,
    "content": {
        "liveTitle": "V4를 향한 여정! 19-23 T1 전경기 다시보기",
        "status": "OPEN",
        "concurrentUserCount": 853,
        "accumulateCount": 664011,
        "paidPromotion": false,
        "adult": false,
        "chatChannelId": "N137Or",
        "categoryType": "GAME",
        "liveCategory": "League_of_Legends",
        "liveCategoryValue": "리그 오브 레전드",
        "livePollingStatusJson": "{\"status\": \"STARTED\", \"isPublishing\": true, \"playableStatus\": \"PLAYABLE\", \"trafficThrottling\": -1, \"callPeriodMilliSecond\": 10000}",
        "faultStatus": null
    }
}
```