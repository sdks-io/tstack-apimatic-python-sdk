from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_evaluating_end_event import V1EvaluatingEndEvent, V1EvaluatingEndEventDict


class V1ResearchEventEvaluatingEnd(SdkBaseModel):
    """Envelope for the "evaluating:end" event from /v1/research."""

    event: str
    data: V1EvaluatingEndEvent


class V1ResearchEventEvaluatingEndDict(TypedDict):
    event: str
    data: V1EvaluatingEndEventDict
