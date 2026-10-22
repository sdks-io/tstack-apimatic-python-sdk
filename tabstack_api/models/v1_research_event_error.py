from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_error_event import V1ErrorEvent, V1ErrorEventDict


class V1ResearchEventError(SdkBaseModel):
    """Envelope for the "error" event from /v1/research."""

    event: str
    data: V1ErrorEvent
    """error - Research failed"""


class V1ResearchEventErrorDict(TypedDict):
    event: str
    data: V1ErrorEventDict
