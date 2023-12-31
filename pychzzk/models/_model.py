from __future__ import annotations
from typing import Optional, Literal, Any, TypeVar, Generic
from datetime import datetime
from pydantic import AliasPath, Field, HttpUrl, BaseModel
from pychzzk.models.base import RawModel
from pychzzk.utils import to_kst
from pychzzk import models as m
from pychzzk.models.live_playback_json import livePlaybackJson

import json


class Following(RawModel):
    following: bool
    notification: bool
    follow_date: Optional[datetime]

    def model_post_init(self, _: Any) -> None:
        if self.follow_date is not None:
            self.follow_date = to_kst(self.follow_date)

    def warp(self) -> m.Following:
        return m.Following(
            following=self.following,
            following_at=self.follow_date,
            notification=self.notification
        )


class PersonalData(RawModel):
    private_user_block: bool
    following: Optional[Following] = None


class User(RawModel):
    has_profile: bool
    user_id_hash: str
    nickname: str
    profile_image_url: HttpUrl
    penalties: list[Any]
    official_noti_agree: bool
    official_noti_agree_updated_date: Optional[datetime]
    verified_mark: bool
    logged_in: bool

    def warp(self) -> m.User:
        return m.User(
            id=self.user_id_hash,
            profile=m.Profile(
                nickname=self.nickname,
                image=m.Resource(url=self.profile_image_url)
            ),
            logged_in=self.logged_in,
            verified=self.verified_mark
        )


class Live(RawModel):
    live_title: str
    live_image_url: str
    default_thumbnail_image_url: Optional[HttpUrl]
    concurrent_user_count: int
    accumulate_count: int
    open_date: str
    live_id: str | int
    chat_channel_id: str
    category_type: str | None
    live_category: str | None
    live_category_value: str
    channel_id: str
    live_playback_json: str

    def warp(self) -> m.Live:
        return m.Live(
            live_title=self.live_title,
            live_image_url=self.live_image_url if self.live_image_url is not None else None,
            default_thumbnail_image_url=m.Resource(url=self.default_thumbnail_image_url) if self.default_thumbnail_image_url is not None else None,
            concurrent_user_count=self.concurrent_user_count,
            accumulate_count=self.accumulate_count,
            open_date=self.open_date,
            live_id=self.live_id,
            chat_channel_id=self.chat_channel_id,
            category_type=self.category_type,
            live_category=self.live_category,
            live_category_value=self.live_category_value,
            channel_id=self.channel_id,
            live_playback_json=livePlaybackJson(**json.loads(self.live_playback_json))
        )

class Content(RawModel):
    live: Optional[Live] = None
    videos: Optional[list[m.Videos]] = None

    def warp(self):
        if self.live:
            return m.Content(
                live=self.live.warp(),
                videos=self.videos
            )
        else:
            return m.Content(
                live=None,
                videos=self.videos
            )

class Channel(RawModel):
    channel_id: str
    channel_name: str
    channel_image_url: Optional[HttpUrl] = None
    verified_mark: bool
    channel_type: Optional[Literal["NORMAL", "STREAMING"]] = None
    channel_description: Optional[str] = None
    follower_count: Optional[int] = None
    open_live: Optional[bool] = None
    personal_data: Optional[PersonalData] = None
    def warp(self) -> m.Channel:
        following = None
        blocked = None
        if self.personal_data is not None:
            if self.personal_data.following is not None:
                following = self.personal_data.following.warp()
            blocked = self.personal_data.private_user_block
        
        return m.Channel(
            id=self.channel_id,
            type=self.channel_type,
            name=self.channel_name,
            description=self.channel_description,
            image=m.Resource(url=self.channel_image_url) if self.channel_image_url is not None else None,
            verfied=self.verified_mark,
            live=self.open_live,
            followers_count=self.follower_count,
            following=following,
            blocked=blocked
        )


class Video(RawModel):
    video_no: int
    video_id: str
    video_title: str
    video_type: str
    published_date: datetime
    thumbnail_image_url: HttpUrl
    trailer_url: Optional[HttpUrl] = None
    duration: int
    read_count: int
    channel_id: Optional[str] = None
    published_date_at: int
    category_type: Optional[str] = None
    video_category: str
    video_category_value: str
    exposure: Optional[bool] = None
    channel: Optional[Channel] = None
    paid_promotion: Optional[bool] = None
    in_key: Optional[str] = None
    live_open_date: Optional[datetime] = None
    vod_status: Optional[str] = None
    prev_video: Optional[Video] = None
    next_video: Optional[Video] = None

    def model_post_init(self, _: Any):
        self.published_date = to_kst(self.published_date)

        if self.live_open_date is not None:
            self.live_open_date = to_kst(self.live_open_date)

    def warp(self) -> m.Video:
        return m.Video(
            id=self.video_id,
            no=self.video_no,
            tilte=self.video_title,
            type=self.video_type,
            status=self.vod_status,
            thumbnail=m.Resource(url=self.thumbnail_image_url),
            trailer=m.Resource(url=self.trailer_url) if self.trailer_url is not None else None,
            category_type=self.category_type,
            category=self.video_category,
            published=self.exposure,
            published_at=self.published_date,
            stream_started_at=self.live_open_date,
            duration=self.duration,
            view_count=self.read_count,
            is_paid_promotion=self.paid_promotion,
            channel=self.channel.warp() if self.channel is not None else None,
        )


class VideoSearchRecord(m.SearchRecord):
    video: Video
    channel: Channel


class ChannelSearchRecord(m.SearchRecord):
    channel: Optional[Channel] = None
    content: Optional[Content] = None
    def model_post_init(self, _: Any) -> None:
        if self.content:
            self.content = self.content.warp()
        
class SearchChannel(m.SearchCursor):
    data: list[ChannelSearchRecord]


class SearchChannelsLiveInfo(BaseModel):
    """
    live = {
        "channel_name": channel.channel.channel_name,
        "live": channel.content.live
    }
    """
    channel_name: str
    live: m.Live