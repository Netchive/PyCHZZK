from typing import Optional
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class RawModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        extra="forbid"
    )

class BaseResponse(RawModel):
    code: int
    message: str | None
    content: Optional[dict]


__all__ = [
    BaseResponse,
    RawModel
]