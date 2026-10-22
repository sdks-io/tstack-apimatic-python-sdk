from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_outlining_end_event import V1OutliningEndEvent, V1OutliningEndEventDict


class V1ResearchEventOutliningEnd(SdkBaseModel):
    """Envelope for the "outlining:end" event from /v1/research."""

    event: str
    data: V1OutliningEndEvent


class V1ResearchEventOutliningEndDict(TypedDict):
    event: str
    data: V1OutliningEndEventDict
