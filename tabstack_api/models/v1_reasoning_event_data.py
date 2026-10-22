from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1ReasoningEventData(SdkBaseModel):
    """Event data for agent reasoning"""

    iteration_id: str = Field(alias="iterationId")
    reasoning: str
    timestamp: float


class V1ReasoningEventDataDict(TypedDict):
    iteration_id: str
    reasoning: str
    timestamp: float
