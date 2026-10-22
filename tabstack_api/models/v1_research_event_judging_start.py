from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_judging_start_event import V1JudgingStartEvent, V1JudgingStartEventDict


class V1ResearchEventJudgingStart(SdkBaseModel):
    """Envelope for the "judging:start" event from /v1/research."""

    event: str
    data: V1JudgingStartEvent


class V1ResearchEventJudgingStartDict(TypedDict):
    event: str
    data: V1JudgingStartEventDict
