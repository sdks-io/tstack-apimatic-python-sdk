from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_iteration_end_event import V1IterationEndEvent, V1IterationEndEventDict


class V1ResearchEventIterationEnd(SdkBaseModel):
    """Envelope for the "iteration:end" event from /v1/research."""

    event: str
    data: V1IterationEndEvent


class V1ResearchEventIterationEndDict(TypedDict):
    event: str
    data: V1IterationEndEventDict
