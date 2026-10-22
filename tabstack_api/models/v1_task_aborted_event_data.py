from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1TaskAbortedEventData(SdkBaseModel):
    """Event data when a task is aborted"""

    final_answer: str = Field(alias="finalAnswer")
    iteration_id: str = Field(alias="iterationId")
    reason: str
    timestamp: float


class V1TaskAbortedEventDataDict(TypedDict):
    final_answer: str
    iteration_id: str
    reason: str
    timestamp: float
