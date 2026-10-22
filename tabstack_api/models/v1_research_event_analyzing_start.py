from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_analyzing_start_event import V1AnalyzingStartEvent, V1AnalyzingStartEventDict


class V1ResearchEventAnalyzingStart(SdkBaseModel):
    """Envelope for the "analyzing:start" event from /v1/research."""

    event: str
    data: V1AnalyzingStartEvent


class V1ResearchEventAnalyzingStartDict(TypedDict):
    event: str
    data: V1AnalyzingStartEventDict
