from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_following_end_event import V1FollowingEndEvent, V1FollowingEndEventDict


class V1ResearchEventFollowingEnd(SdkBaseModel):
    """Envelope for the "following:end" event from /v1/research."""

    event: str
    data: V1FollowingEndEvent


class V1ResearchEventFollowingEndDict(TypedDict):
    event: str
    data: V1FollowingEndEventDict
