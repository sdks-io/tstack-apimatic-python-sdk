from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_page_navigation_event_data import V1PageNavigationEventData, V1PageNavigationEventDataDict


class V1AutomateEventBrowserNavigated(SdkBaseModel):
    """Envelope for the "browser:navigated" event from /v1/automate."""

    event: str
    data: V1PageNavigationEventData
    """Event data when navigating to a page"""


class V1AutomateEventBrowserNavigatedDict(TypedDict):
    event: str
    data: V1PageNavigationEventDataDict
