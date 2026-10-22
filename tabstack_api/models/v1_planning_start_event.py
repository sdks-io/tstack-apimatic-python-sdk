from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1PlanningStartEvent(SdkBaseModel):
    has_prefetched_context: bool = Field(alias="hasPrefetchedContext")
    """Whether prefetched user-provided URLs exist for context"""

    message: str
    timestamp: float


class V1PlanningStartEventDict(TypedDict):
    has_prefetched_context: bool
    message: str
    timestamp: float
