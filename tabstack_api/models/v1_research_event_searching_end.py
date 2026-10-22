from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_searching_end_event import V1SearchingEndEvent, V1SearchingEndEventDict


class V1ResearchEventSearchingEnd(SdkBaseModel):
    """Envelope for the "searching:end" event from /v1/research."""

    event: str
    data: V1SearchingEndEvent


class V1ResearchEventSearchingEndDict(TypedDict):
    event: str
    data: V1SearchingEndEventDict
