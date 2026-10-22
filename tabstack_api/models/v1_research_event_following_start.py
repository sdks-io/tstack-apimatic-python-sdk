from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_following_start_event import V1FollowingStartEvent, V1FollowingStartEventDict


class V1ResearchEventFollowingStart(SdkBaseModel):
    """Envelope for the "following:start" event from /v1/research."""

    event: str
    data: V1FollowingStartEvent


class V1ResearchEventFollowingStartDict(TypedDict):
    event: str
    data: V1FollowingStartEventDict
