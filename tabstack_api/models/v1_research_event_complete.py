from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_complete_event import V1CompleteEvent, V1CompleteEventDict


class V1ResearchEventComplete(SdkBaseModel):
    """Envelope for the "complete" event from /v1/research."""

    event: str
    data: V1CompleteEvent
    """complete - Research finished successfully"""


class V1ResearchEventCompleteDict(TypedDict):
    event: str
    data: V1CompleteEventDict
