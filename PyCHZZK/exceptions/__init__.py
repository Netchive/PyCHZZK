class PyCHHZKException(BaseException):
    pass


class OfflineException(PyCHHZKException):
    """Live status is offline"""

    def __init__(self):
        self.message = "Live status is offline"

    def __str__(self):
        return self.message


class ChannelNotFound(PyCHHZKException):
    """Live status is offline"""

    def __init__(self, channel_id: str):
        self.message = f"Channel {channel_id} is not found"

    def __str__(self):
        return self.message
