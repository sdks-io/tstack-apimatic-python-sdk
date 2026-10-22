from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1WritingStartEvent(SdkBaseModel):
    attempt: float
    is_revision: bool = Field(alias="isRevision")
    """Whether this is a revision attempt (attempt > 1)"""

    max_attempts: float = Field(alias="maxAttempts")
    """Maximum attempts allowed (1 + maxRevisions)"""

    message: str
    previous_score: Optional[float] = Field(default=UNSET, alias="previousScore")
    """Previous judgment score if this is a revision"""

    timestamp: float


class V1WritingStartEventDict(TypedDict):
    attempt: float
    is_revision: bool
    max_attempts: float
    message: str
    previous_score: NotRequired[float]
    timestamp: float
