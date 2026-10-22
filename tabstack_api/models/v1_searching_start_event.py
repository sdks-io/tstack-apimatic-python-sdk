from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1SearchingStartEvent(SdkBaseModel):
    iteration: float
    message: str
    queries: list[str]
    timestamp: float


class V1SearchingStartEventDict(TypedDict):
    iteration: float
    message: str
    queries: list[str]
    timestamp: float
