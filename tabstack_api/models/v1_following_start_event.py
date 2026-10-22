from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1FollowingStartEvent(SdkBaseModel):
    iteration: float
    link_count: float = Field(alias="linkCount")
    message: str
    timestamp: float


class V1FollowingStartEventDict(TypedDict):
    iteration: float
    link_count: float
    message: str
    timestamp: float
