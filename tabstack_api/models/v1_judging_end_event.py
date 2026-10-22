from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1JudgingEndEvent(SdkBaseModel):
    approved: bool
    attempt: float
    feedback: Optional[str] = UNSET
    message: str
    score: float
    timestamp: float


class V1JudgingEndEventDict(TypedDict):
    approved: bool
    attempt: float
    feedback: NotRequired[str]
    message: str
    score: float
    timestamp: float
