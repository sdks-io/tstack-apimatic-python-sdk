from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .v1_waiting_event_data import V1WaitingEventData, V1WaitingEventDataDict


class V1AutomateEventAgentWaiting(SdkBaseModel):
    """Envelope for the "agent:waiting" event from /v1/automate."""

    event: str
    data: V1WaitingEventData
    """Event data for waiting notifications"""


class V1AutomateEventAgentWaitingDict(TypedDict):
    event: str
    data: V1WaitingEventDataDict
