from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1JudgmentResult(SdkBaseModel):
    """Judgment result from research judge"""

    approved: bool
    feedback: Optional[str] = UNSET
    observation: str
    score: float


class V1JudgmentResultDict(TypedDict):
    approved: bool
    feedback: NotRequired[str]
    observation: str
    score: float
