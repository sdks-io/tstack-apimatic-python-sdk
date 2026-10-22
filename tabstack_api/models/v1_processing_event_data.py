from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1ProcessingEventData(SdkBaseModel):
    """Event data for when the agent is waiting for model generation"""

    has_screenshot: bool = Field(alias="hasScreenshot")
    iteration_id: str = Field(alias="iterationId")
    operation: str
    timestamp: float


class V1ProcessingEventDataDict(TypedDict):
    has_screenshot: bool
    iteration_id: str
    operation: str
    timestamp: float
