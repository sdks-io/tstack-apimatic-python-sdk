from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1JudgingStartEvent(SdkBaseModel):
    attempt: float
    max_attempts: float = Field(alias="maxAttempts")
    """Maximum attempts allowed (1 + maxRevisions)"""

    message: str
    timestamp: float


class V1JudgingStartEventDict(TypedDict):
    attempt: float
    max_attempts: float
    message: str
    timestamp: float
