from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_prefetching_start_event import V1PrefetchingStartEvent, V1PrefetchingStartEventDict


class V1ResearchEventPrefetchingStart(SdkBaseModel):
    """Envelope for the "prefetching:start" event from /v1/research."""

    event: str
    data: V1PrefetchingStartEvent


class V1ResearchEventPrefetchingStartDict(TypedDict):
    event: str
    data: V1PrefetchingStartEventDict
