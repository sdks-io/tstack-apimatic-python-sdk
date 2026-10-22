from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1PrefetchingEndEvent(SdkBaseModel):
    failed: float
    fetched: float
    message: str
    timestamp: float


class V1PrefetchingEndEventDict(TypedDict):
    failed: float
    fetched: float
    message: str
    timestamp: float
