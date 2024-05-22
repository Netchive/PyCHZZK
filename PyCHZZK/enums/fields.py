from enum import Enum


class Fields(Enum):
    description = "description"
    banners = "banners"
    topExposedVideos = "topExposedVideos"
    missionDonationChannelHomeExposure = "missionDonationChannelHomeExposure"
    all = "description,banners,topExposedVideos,missionDonationChannelHomeExposure"