from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.media_type import MediaTypeOrStr


class V1ScreenshotCapturedImageEventData(SdkBaseModel):
    """Event data for screenshot image capture with full image data This event contains the complete screenshot and can
    be very large"""

    image: str
    iteration_id: str = Field(alias="iterationId")
    media_type: MediaTypeOrStr = Field(alias="mediaType")
    timestamp: float


class V1ScreenshotCapturedImageEventDataDict(TypedDict):
    image: str
    iteration_id: str
    media_type: MediaTypeOrStr
    timestamp: float
