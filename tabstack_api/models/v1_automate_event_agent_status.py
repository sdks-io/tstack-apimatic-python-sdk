from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_status_message_event_data import V1StatusMessageEventData, V1StatusMessageEventDataDict


class V1AutomateEventAgentStatus(SdkBaseModel):
    """Envelope for the "agent:status" event from /v1/automate."""

    event: str
    data: V1StatusMessageEventData
    """Event data for status messages"""


class V1AutomateEventAgentStatusDict(TypedDict):
    event: str
    data: V1StatusMessageEventDataDict
