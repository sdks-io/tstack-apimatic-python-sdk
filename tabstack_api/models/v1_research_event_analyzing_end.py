from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_analyzing_end_event import V1AnalyzingEndEvent, V1AnalyzingEndEventDict


class V1ResearchEventAnalyzingEnd(SdkBaseModel):
    """Envelope for the "analyzing:end" event from /v1/research."""

    event: str
    data: V1AnalyzingEndEvent


class V1ResearchEventAnalyzingEndDict(TypedDict):
    event: str
    data: V1AnalyzingEndEventDict
