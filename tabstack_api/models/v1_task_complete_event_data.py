from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class V1TaskCompleteEventData(SdkBaseModel):
    """Event data when a task is completed"""

    final_answer: str | None = Field(alias="finalAnswer")
    iteration_id: str = Field(alias="iterationId")
    success: Optional[bool] = UNSET
    timestamp: float


class V1TaskCompleteEventDataDict(TypedDict):
    final_answer: str | None
    iteration_id: str
    success: NotRequired[bool]
    timestamp: float
