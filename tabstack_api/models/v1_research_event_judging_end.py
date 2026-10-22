from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_judging_end_event import V1JudgingEndEvent, V1JudgingEndEventDict


class V1ResearchEventJudgingEnd(SdkBaseModel):
    """Envelope for the "judging:end" event from /v1/research."""

    event: str
    data: V1JudgingEndEvent


class V1ResearchEventJudgingEndDict(TypedDict):
    event: str
    data: V1JudgingEndEventDict
