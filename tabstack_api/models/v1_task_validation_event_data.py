from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.completion_quality import CompletionQualityOrStr


class V1TaskValidationEventData(SdkBaseModel):
    """Event data for task validation"""

    completion_quality: CompletionQualityOrStr = Field(alias="completionQuality")
    feedback: Optional[str] = UNSET
    final_answer: str = Field(alias="finalAnswer")
    iteration_id: str = Field(alias="iterationId")
    observation: str
    timestamp: float


class V1TaskValidationEventDataDict(TypedDict):
    completion_quality: CompletionQualityOrStr
    feedback: NotRequired[str]
    final_answer: str
    iteration_id: str
    observation: str
    timestamp: float
