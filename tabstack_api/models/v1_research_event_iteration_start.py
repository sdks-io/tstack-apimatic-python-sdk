from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_iteration_start_event import V1IterationStartEvent, V1IterationStartEventDict


class V1ResearchEventIterationStart(SdkBaseModel):
    """Envelope for the "iteration:start" event from /v1/research."""

    event: str
    data: V1IterationStartEvent


class V1ResearchEventIterationStartDict(TypedDict):
    event: str
    data: V1IterationStartEventDict
