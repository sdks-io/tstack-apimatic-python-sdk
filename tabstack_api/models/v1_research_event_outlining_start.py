from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_outlining_start_event import V1OutliningStartEvent, V1OutliningStartEventDict


class V1ResearchEventOutliningStart(SdkBaseModel):
    """Envelope for the "outlining:start" event from /v1/research."""

    event: str
    data: V1OutliningStartEvent


class V1ResearchEventOutliningStartDict(TypedDict):
    event: str
    data: V1OutliningStartEventDict
