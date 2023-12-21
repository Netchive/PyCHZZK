from datetime import datetime, timedelta, timezone

kst = timezone(timedelta(hours=+9), 'Asia/Seoul')

def to_kst(time: datetime) -> datetime:
    return time.replace(tzinfo=kst)

__all__ = [
    to_kst
]
