from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1WritingEndEvent(SdkBaseModel):
    attempt: float
    message: str
    timestamp: float


class V1WritingEndEventDict(TypedDict):
    attempt: float
    message: str
    timestamp: float
