from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_screenshot_captured_event_data import V1ScreenshotCapturedEventData, V1ScreenshotCapturedEventDataDict


class V1AutomateEventBrowserScreenshotCaptured(SdkBaseModel):
    """Envelope for the "browser:screenshot_captured" event from /v1/automate."""

    event: str
    data: V1ScreenshotCapturedEventData
    """Event data for screenshot capture"""


class V1AutomateEventBrowserScreenshotCapturedDict(TypedDict):
    event: str
    data: V1ScreenshotCapturedEventDataDict
