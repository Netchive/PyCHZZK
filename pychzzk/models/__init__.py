from datetime import datetime
from typing import Literal, Optional, Generic, TypeVar
from pydantic import BaseModel, HttpUrl, Field, AliasPath
from pychzzk.models.base import RawModel
from pychzzk.models.live_playback_json import livePlaybackJson


T = TypeVar("T", bound="SearchRecord")

class Resource(BaseModel):
    url: HttpUrl


class Profile(BaseModel):
    nickname: str
    image: Resource

class User(BaseModel):
    id: str
    profile: Profile
    logged_in: bool
    verified: bool

class Following(BaseModel):
    following: bool
    following_at: Optional[datetime] = None
    notification: bool

class Channel(BaseModel):
    id: str
    type: Optional[Literal["NORMAL", "STREAMING"]] = None
    name: str
    description: Optional[str] = None
    image: Optional[Resource] = None
    verfied: bool
    live: Optional[bool] = None
    followers_count: Optional[int] = None
    following: Optional[Following] = None
    blocked: Optional[bool] = None

class Video(BaseModel):
    id: str
    no: int
    tilte: str
    type: str
    status: Optional[str] = None
    thumbnail: Resource
    trailer: Optional[Resource] = None
    category_type: Optional[str] = None
    category: str
    published: Optional[bool] = None
    published_at: datetime
    stream_started_at: Optional[datetime] = None
    duration: int
    view_count: int
    is_paid_promotion: Optional[bool] = None
    channel: Optional[Channel] = None

class Videos(RawModel):
    video_no: int
    video_id: str
    video_title: str
    video_type: str
    publish_date: str
    thumbnail_image_url: HttpUrl
    duration: int
    read_count: int
    channel_id: str
    publish_date_at: int
    category_type: Optional[str]
    video_category: str | None
    video_category_value: str

class Live(BaseModel):
    live_title: str
    live_image_url: HttpUrl
    default_thumbnail_image_url: Optional[HttpUrl]
    concurrent_user_count: int
    accumulate_count: int
    open_date: str
    live_id: int | str
    chat_channel_id: str
    category_type: str
    live_category: str
    live_category_value: str
    channel_id: str
    live_playback_json: livePlaybackJson

class SearchRecord(RawModel):
    pass

class SearchCursor(RawModel, Generic[T]):
    size: int
    next: int = Field(alias=AliasPath("page", "next", "offset"))
    data: list[T]

class Content(RawModel):
    live: Optional[Live] = None
    videos: Optional[list[Videos]] = None
