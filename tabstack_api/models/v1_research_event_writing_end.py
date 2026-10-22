from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_writing_end_event import V1WritingEndEvent, V1WritingEndEventDict


class V1ResearchEventWritingEnd(SdkBaseModel):
    """Envelope for the "writing:end" event from /v1/research."""

    event: str
    data: V1WritingEndEvent


class V1ResearchEventWritingEndDict(TypedDict):
    event: str
    data: V1WritingEndEventDict
