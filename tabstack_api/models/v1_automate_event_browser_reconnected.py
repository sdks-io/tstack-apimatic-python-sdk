from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_browser_reconnected_event_data import V1BrowserReconnectedEventData, V1BrowserReconnectedEventDataDict


class V1AutomateEventBrowserReconnected(SdkBaseModel):
    """Envelope for the "browser:reconnected" event from /v1/automate."""

    event: str
    data: V1BrowserReconnectedEventData
    """Event data when the browser reconnects after a mid-task disconnect"""


class V1AutomateEventBrowserReconnectedDict(TypedDict):
    event: str
    data: V1BrowserReconnectedEventDataDict
