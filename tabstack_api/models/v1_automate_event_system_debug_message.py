from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_messages_debug_event_data import V1MessagesDebugEventData, V1MessagesDebugEventDataDict


class V1AutomateEventSystemDebugMessage(SdkBaseModel):
    """Envelope for the "system:debug_message" event from /v1/automate."""

    event: str
    data: V1MessagesDebugEventData
    """Event data for message debug info"""


class V1AutomateEventSystemDebugMessageDict(TypedDict):
    event: str
    data: V1MessagesDebugEventDataDict
