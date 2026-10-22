from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_screenshot_captured_image_event_data import (
    V1ScreenshotCapturedImageEventData,
    V1ScreenshotCapturedImageEventDataDict,
)


class V1AutomateEventBrowserScreenshotCapturedImage(SdkBaseModel):
    """Envelope for the "browser:screenshot_captured_image" event from /v1/automate."""

    event: str
    data: V1ScreenshotCapturedImageEventData
    """Event data for screenshot image capture with full image data This event contains the complete screenshot and can
    be very large"""


class V1AutomateEventBrowserScreenshotCapturedImageDict(TypedDict):
    event: str
    data: V1ScreenshotCapturedImageEventDataDict
