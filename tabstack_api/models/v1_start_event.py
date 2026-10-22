from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1StartEvent(SdkBaseModel):
    """start - Research begins"""

    message: str
    timestamp: float


class V1StartEventDict(TypedDict):
    message: str
    timestamp: float
