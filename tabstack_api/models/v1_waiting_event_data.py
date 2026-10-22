from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1WaitingEventData(SdkBaseModel):
    """Event data for waiting notifications"""

    iteration_id: str = Field(alias="iterationId")
    seconds: float
    timestamp: float


class V1WaitingEventDataDict(TypedDict):
    iteration_id: str
    seconds: float
    timestamp: float
