from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class V1StatusMessageEventData(SdkBaseModel):
    """Event data for status messages"""

    iteration_id: str = Field(alias="iterationId")
    message: str
    timestamp: float


class V1StatusMessageEventDataDict(TypedDict):
    iteration_id: str
    message: str
    timestamp: float
