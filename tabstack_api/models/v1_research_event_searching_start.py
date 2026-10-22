from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_searching_start_event import V1SearchingStartEvent, V1SearchingStartEventDict


class V1ResearchEventSearchingStart(SdkBaseModel):
    """Envelope for the "searching:start" event from /v1/research."""

    event: str
    data: V1SearchingStartEvent


class V1ResearchEventSearchingStartDict(TypedDict):
    event: str
    data: V1SearchingStartEventDict
