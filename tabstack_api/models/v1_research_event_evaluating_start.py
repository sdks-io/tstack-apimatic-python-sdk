from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_evaluating_start_event import V1EvaluatingStartEvent, V1EvaluatingStartEventDict


class V1ResearchEventEvaluatingStart(SdkBaseModel):
    """Envelope for the "evaluating:start" event from /v1/research."""

    event: str
    data: V1EvaluatingStartEvent


class V1ResearchEventEvaluatingStartDict(TypedDict):
    event: str
    data: V1EvaluatingStartEventDict
