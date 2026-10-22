from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.format import FormatOrStr


class V1ScreenshotCapturedEventData(SdkBaseModel):
    """Event data for screenshot capture"""

    format: FormatOrStr
    iteration_id: str = Field(alias="iterationId")
    size: float
    timestamp: float


class V1ScreenshotCapturedEventDataDict(TypedDict):
    format: FormatOrStr
    iteration_id: str
    size: float
    timestamp: float
