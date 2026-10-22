from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_writing_start_event import V1WritingStartEvent, V1WritingStartEventDict


class V1ResearchEventWritingStart(SdkBaseModel):
    """Envelope for the "writing:start" event from /v1/research."""

    event: str
    data: V1WritingStartEvent


class V1ResearchEventWritingStartDict(TypedDict):
    event: str
    data: V1WritingStartEventDict
