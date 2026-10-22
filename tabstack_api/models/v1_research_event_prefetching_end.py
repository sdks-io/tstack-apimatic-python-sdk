from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_prefetching_end_event import V1PrefetchingEndEvent, V1PrefetchingEndEventDict


class V1ResearchEventPrefetchingEnd(SdkBaseModel):
    """Envelope for the "prefetching:end" event from /v1/research."""

    event: str
    data: V1PrefetchingEndEvent


class V1ResearchEventPrefetchingEndDict(TypedDict):
    event: str
    data: V1PrefetchingEndEventDict
