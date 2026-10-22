from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_start_event import V1StartEvent, V1StartEventDict


class V1ResearchEventStart(SdkBaseModel):
    """Envelope for the "start" event from /v1/research."""

    event: str
    data: V1StartEvent
    """start - Research begins"""


class V1ResearchEventStartDict(TypedDict):
    event: str
    data: V1StartEventDict
